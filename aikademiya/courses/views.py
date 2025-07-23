import asyncio
import json
import os
from uuid import uuid4

from django.http import JsonResponse, HttpResponseNotAllowed

from temporalio.client import Client
from temporalio.service import RPCError, RPCStatusCode

from aikademiya.temporal_app.workflows import GenerateCourseWorkflow


async def _start_workflow(topic: str) -> str:
    client = await Client.connect(os.getenv("TEMPORAL_ADDRESS", "temporal:7233"))
    handle = await client.start_workflow(
        GenerateCourseWorkflow.run,
        topic,
        id=f"course-{uuid4()}",
        task_queue="course-task-queue",
    )
    return handle.id


async def _signal_workflow(workflow_id: str, signal: str, payload) -> None:
    client = await Client.connect(os.getenv("TEMPORAL_ADDRESS", "localhost:7233"))
    handle = client.get_workflow_handle(workflow_id)
    await handle.signal(signal, payload)


async def _workflow_status(workflow_id: str):
    client = await Client.connect(os.getenv("TEMPORAL_ADDRESS", "localhost:7233"))
    handle = client.get_workflow_handle(workflow_id)
    try:
        info = await handle.query("get_state")
    except RPCError as err:
        if err.status == RPCStatusCode.DEADLINE_EXCEEDED:
            return {"error": "timeout"}
        raise

    if info.get("status") == "completed":
        result = await handle.result()
        info["result"] = result
    return info


def create_course(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    data = json.loads(request.body or "{}")
    topic = data.get("topic")
    if not topic:
        return JsonResponse({"error": "topic required"}, status=400)
    workflow_id = asyncio.run(_start_workflow(topic))
    return JsonResponse({"workflow_id": workflow_id})


def course_status(request, workflow_id: str):
    info = asyncio.run(_workflow_status(workflow_id))
    if isinstance(info, dict) and info.get("error") == "timeout":
        return JsonResponse(info, status=504)
    return JsonResponse(info)


def confirm_course(request, workflow_id: str):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    asyncio.run(_signal_workflow(workflow_id, "confirm", True))
    return JsonResponse({"status": "ok"})


def next_chapter(request, workflow_id: str):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    asyncio.run(_signal_workflow(workflow_id, "next_chapter", None))
    return JsonResponse({"status": "ok"})
