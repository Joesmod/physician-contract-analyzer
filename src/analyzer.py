import json, os
from openai import AsyncOpenAI
from models import AnalysisResponse
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

_client: AsyncOpenAI | None = None

def _get_client() -> AsyncOpenAI:
    global _client
    if _client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable is not set")
        _client = AsyncOpenAI(api_key=api_key)
    return _client

MAX_CONTRACT_CHARS = 100_000

async def analyze_contract(contract_text: str) -> AnalysisResponse:
    if len(contract_text) > MAX_CONTRACT_CHARS:
        contract_text = contract_text[:MAX_CONTRACT_CHARS] + "\n\n[TEXT TRUNCATED]"
    client = _get_client()
    response = await client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(contract_text=contract_text)},
        ],
    )
    raw = response.choices[0].message.content
    return AnalysisResponse(**json.loads(raw))
