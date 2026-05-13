CREATE TABLE guests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE properties (
    id VARCHAR(100) PRIMARY KEY,
    property_name VARCHAR(255),
    location TEXT
);

CREATE TABLE reservations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_ref VARCHAR(100) UNIQUE NOT NULL,
    guest_id UUID REFERENCES guests(id),
    property_id VARCHAR(100) REFERENCES properties(id),
    check_in DATE,
    check_out DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    guest_id UUID REFERENCES guests(id),
    reservation_id UUID REFERENCES reservations(id),
    source VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID REFERENCES conversations(id),
    sender_type VARCHAR(50),
    message_text TEXT NOT NULL,
    query_type VARCHAR(100),
    confidence_score DECIMAL(3,2),
    ai_drafted BOOLEAN DEFAULT FALSE,
    agent_edited BOOLEAN DEFAULT FALSE,
    auto_sent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE escalation_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    message_id UUID REFERENCES messages(id),
    escalation_reason TEXT,
    escalated_to VARCHAR(255),
    status VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);