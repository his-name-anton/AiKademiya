"""Helpers for calling OpenAI models."""

from __future__ import annotations

from typing import Any, Dict

import openai

from .models import AIModel


async def call_openai(model: AIModel, prompt: str) -> str:
    """Send a prompt to OpenAI and return the raw response text."""

    client = openai.AsyncOpenAI(api_key=model.api_key, base_url=model.endpoint_url or None)
    response = await client.chat.completions.create(
        model=model.name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=model.max_tokens,
    )
    return response.choices[0].message.content.strip()


def render_template(template: str, context: Dict[str, Any]) -> str:
    """Simple template rendering using ``str.format``."""

    return template.format(**context)

