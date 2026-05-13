def determine_action(query_type: str, confidence: float):
    if query_type == "complaint":
        return "escalate"

    if confidence > 0.85:
        return "auto_send"

    if confidence >= 0.60:
        return "agent_review"

    return "escalate"