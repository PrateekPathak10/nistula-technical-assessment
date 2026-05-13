def classify_query(message: str):
    msg = message.lower()

    if any(word in msg for word in ["available", "availability", "dates"]):
        return "pre_sales_availability", 0.92

    if any(word in msg for word in ["rate", "price", "cost", "pricing"]):
        return "pre_sales_pricing", 0.90

    if any(word in msg for word in ["check in", "wifi", "check-out", "password"]):
        return "post_sales_checkin", 0.88

    if any(word in msg for word in ["early check-in", "airport transfer", "chef"]):
        return "special_request", 0.82

    if any(word in msg for word in [
        "refund",
        "unacceptable",
        "not happy",
        "bad",
        "complaint",
        "issue",
        "problem",
        "ac not working"
    ]):
        return "complaint", 0.55

    return "general_enquiry", 0.70