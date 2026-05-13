# Question A — Immediate Response

Hi Rahul, I’m really sorry to hear about the hot water issue, especially with guests arriving in a few hours. I’ve marked this as urgent and alerted our on-ground support team immediately. Someone will contact you shortly to resolve this as quickly as possible.

Why:
The response acknowledges frustration, avoids defensiveness, and assures immediate action without making refund promises the AI cannot authorize.

---

# Question B — System Design

The system should:

1. Classify the message as a complaint with high severity.
2. Automatically escalate to the operations manager and caretaker.
3. Trigger WhatsApp, SMS, and email alerts.
4. Create an incident ticket in the internal dashboard.
5. Mark the conversation for priority human handling.
6. Start a 30-minute SLA timer.

If no human responds within 30 minutes:
- escalate to senior operations staff,
- notify the property owner,
- trigger repeated alerts until acknowledged.

All actions, timestamps, escalations, and responses should be logged for operational auditing and analytics.

---

# Question C — Learning

The system should identify recurring complaints using issue frequency tracking.

If the same issue appears repeatedly:
- generate a maintenance risk alert,
- notify operations leadership,
- recommend preventive maintenance,
- temporarily flag the property internally.

I would build a recurring issue detection system that tracks complaint categories per property and automatically predicts operational risks before they affect guests again.