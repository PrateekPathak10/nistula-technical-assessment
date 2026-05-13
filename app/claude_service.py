from anthropic import Anthropic
from app.config import CLAUDE_API_KEY

client = Anthropic(api_key=CLAUDE_API_KEY)


def generate_reply(prompt: str):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        temperature=0.3,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text