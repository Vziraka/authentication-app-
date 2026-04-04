-- Enable UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- used as a saftey net if the uuid is not generated

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), 
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('supplier', 'restaurant')), -- check means the role can only be supplier or resturants 
    email_verified BOOLEAN NOT NULL DEFAULT FALSE, -- boolean means like true or false 
    created_at TIMESTAMP NOT NULL DEFAULT NOW() 
);

-- Verification codes table
CREATE TABLE verification_codes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- references means the code is related to the user and if the user is deleted the code is deleted too 
    code VARCHAR(6) NOT NULL,
    purpose VARCHAR(10) NOT NULL CHECK (purpose IN ('signup', 'login')),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    attempts INTEGER NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    used BOOLEAN NOT NULL DEFAULT FALSE
);

-- Indexes for fast lookups 
CREATE INDEX idx_users_username ON users(username);-- find by username fast
CREATE INDEX idx_users_email ON users(email); -- find by email fast 
CREATE INDEX idx_verification_codes_user_id ON verification_codes(user_id); -- finds codes by user id fast 
CREATE INDEX idx_verification_codes_active ON verification_codes(user_id, purpose, is_active); -- finds active code by user id, ahd purpose fast 