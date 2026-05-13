from fastapi import FastAPI, HTTPException
from uuid import uuid4

from app.schemas import IncomingMessage, UnifiedMessage
from app.classifier import classify_query
from app.prompts import build_prompt
from app.claude_service import generate_reply
from app.utils import determine_action

app = FastAPI(
    title="Nistula Guest Messaging System"
)


@app.post("/webhook/message")
async def handle_message(payload: IncomingMessage):
    try:
        query_type, confidence = classify_query(payload.message)

        unified_message = UnifiedMessage(
            message_id=str(uuid4()),
            source=payload.source,
            guest_name=payload.guest_name,
            message_text=payload.message,
            timestamp=payload.timestamp,
            booking_ref=payload.booking_ref,
            property_id=payload.property_id,
            query_type=query_type
        )

        prompt = build_prompt(
            guest_name=payload.guest_name,
            message=payload.message,
            query_type=query_type
        )

        drafted_reply = generate_reply(prompt)

        action = determine_action(query_type, confidence)

        return {
            "message_id": unified_message.message_id,
            "query_type": query_type,
            "drafted_reply": drafted_reply,
            "confidence_score": round(confidence, 2),
            "action": action
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )