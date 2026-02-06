# Authentication Feature

## Overview

Authentication is handled via **Better Auth** on the frontend. The backend (FastAPI) performs **stateless verification** of the JWT token.

## Mechanism

1.  **Frontend**:

    - Authenticates user via Better Auth.
    - Sends request with `Authorization: Bearer <token>` header.

2.  **Backend**:
    - Middleware/Dependency extracts token.
    - Verifies signature using `BETTER_AUTH_SECRET`.
    - extracts `user_id` from token payload.
    - Rejects invalid/expired tokens with `401 Unauthorized`.

## Environment Variables

- `BETTER_AUTH_SECRET`: Shared secret key used for HMAC SHA256 signature verification.

## Security Requirements

- All protected endpoints **MUST** verify the token.
- `user_id` from the token **MUST** be used to filter database queries (User Isolation).
- No sensitive user data (passwords) is stored in the FastAPI database.
