import asyncio
import os

from temporalio.client import Client
from temporalio.worker import Worker

from aikademiya.temporal_app.workflows import GenerateCourseWorkflow
from aikademiya.temporal_app.activities import ai_task, save_course_to_db


async def main() -> None:
    address = os.getenv("TEMPORAL_ADDRESS", "localhost:7233")
    client = await Client.connect(address)

    worker = Worker(
        client,
        task_queue="course-task-queue",
        workflows=[GenerateCourseWorkflow],
        activities=[ai_task, save_course_to_db],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
