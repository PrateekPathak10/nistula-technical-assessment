from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class IncomingMessage(BaseModel):
    source: str
    guest_name: str
    message: str
    timestamp: datetime
    booking_ref: Optional[str] = None
    property_id: str


class UnifiedMessage(BaseModel):
    message_id: str
    source: str
    guest_name: str
    message_text: str
    timestamp: datetime
    booking_ref: Optional[str]
    property_id: str
    query_type: str