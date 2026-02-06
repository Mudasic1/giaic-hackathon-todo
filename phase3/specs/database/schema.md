# Database Schema

## Overview

The database uses Neon Serverless PostgreSQL with SQLModel/SQLAlchemy ORM.

## Tables

### `tasks`

| Column        | Type       | Constraints                   | Description                                 |
| :------------ | :--------- | :---------------------------- | :------------------------------------------ |
| `id`          | `int`      | `primary_key`, `default=None` | Unique identifier                           |
| `user_id`     | `str`      | `index=True`                  | Reference to external user ID (Better Auth) |
| `title`       | `str`      | `index=True`                  | Task title                                  |
| `description` | `str`      | `nullable`                    | Task details                                |
| `completed`   | `bool`     | `default=False`               | Completion status                           |
| `created_at`  | `datetime` | `default=now`                 | Creation timestamp                          |
| `updated_at`  | `datetime` | `default=now`                 | Last update timestamp                       |

### `users`

> **Note**: User management is handled by **Better Auth**. This table reference is logic-only for `user_id` association. We do not manage credentials in this database directly.

- The application uses `user_id` (string) extracted from the JWT to scope all data access.

---

## Phase 3: Chatbot Tables

### `conversations`

Stores metadata about chat conversations between user and AI assistant.

| Column         | Type       | Constraints                   | Description                        |
| :------------- | :--------- | :---------------------------- | :--------------------------------- |
| `id`           | `str`      | `primary_key`                 | UUID for conversation              |
| `user_id`      | `str`      | `index=True`                  | Owner of the conversation          |
| `title`        | `str`      | `nullable`                    | Auto-generated conversation title  |
| `created_at`   | `datetime` | `default=now`                 | When conversation started          |
| `updated_at`   | `datetime` | `default=now`                 | Last message timestamp             |

**Indexes**:
- `user_id` - For filtering user's conversations
- `created_at` - For sorting conversations

**Relationships**:
- One-to-many with `messages`

---

### `messages`

Stores individual messages within conversations.

| Column            | Type       | Constraints                   | Description                               |
| :---------------- | :--------- | :---------------------------- | :---------------------------------------- |
| `id`              | `int`      | `primary_key`, `autoincrement`| Unique message identifier                 |
| `conversation_id` | `str`      | `foreign_key`, `index=True`   | Reference to conversation                 |
| `role`            | `str`      | -                             | `"user"` or `"assistant"`                 |
| `content`         | `text`     | -                             | Message text content                      |
| `created_at`      | `datetime` | `default=now`                 | Message timestamp                         |

**Indexes**:
- `conversation_id` - For fetching conversation history
- `created_at` - For ordering messages chronologically

**Constraints**:
- `role` must be either `"user"` or `"assistant"`
- `conversation_id` references `conversations.id` with `ON DELETE CASCADE`

**Relationships**:
- Many-to-one with `conversations`

---

## SQLModel Models

### Conversation Model

```python
from datetime import datetime, timezone
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
import uuid

class Conversation(SQLModel, table=True):
    __tablename__ = "conversations"
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    user_id: str = Field(index=True)
    title: Optional[str] = Field(default=None, max_length=200)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # Relationship
    messages: List["Message"] = Relationship(back_populates="conversation")
```

### Message Model

```python
class Message(SQLModel, table=True):
    __tablename__ = "messages"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: str = Field(foreign_key="conversations.id", index=True)
    role: str = Field()  # "user" or "assistant"
    content: str = Field()
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # Relationship
    conversation: Optional[Conversation] = Relationship(back_populates="messages")
```

---

## Migration Strategy

### For Development

Since we're using SQLModel with `create_all()`, simply:
1. Add the new models to `backend/src/models.py`
2. Restart the FastAPI server
3. Tables will be created automatically

### For Production

Use Alembic migrations (recommended for Phase 4):
```bash
# Generate migration
alembic revision --autogenerate -m "Add conversation and message tables"

# Apply migration
alembic upgrade head
```

---

## Data Access Patterns

### Creating a New Conversation

```python
conversation = Conversation(user_id=current_user_id)
session.add(conversation)
session.commit()
```

### Storing Messages

```python
# User message
user_message = Message(
    conversation_id=conversation_id,
    role="user",
    content=user_input
)
session.add(user_message)

# Assistant response
assistant_message = Message(
    conversation_id=conversation_id,
    role="assistant",
    content=agent_response
)
session.add(assistant_message)
session.commit()
```

### Fetching Conversation History

```python
from sqlmodel import select

# Get conversation with messages
conversation = session.exec(
    select(Conversation)
    .where(
        Conversation.id == conversation_id,
        Conversation.user_id == user_id  # Security: user isolation
    )
).first()

# Get messages ordered chronologically
messages = session.exec(
    select(Message)
    .where(Message.conversation_id == conversation_id)
    .order_by(Message.created_at.asc())
).all()
```

### Limiting History (Performance)

```python
# Get last N messages
messages = session.exec(
    select(Message)
    .where(Message.conversation_id == conversation_id)
    .order_by(Message.created_at.desc())
    .limit(50)
).all()

# Reverse to chronological order
messages = list(reversed(messages))
```

---

## Security Considerations

> [!CAUTION]
> **User Isolation**: Always filter conversations and messages by `user_id` to prevent unauthorized access.

### Correct Pattern

```python
# ✅ Good: Filters by user_id
conversation = session.exec(
    select(Conversation).where(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user_id
    )
).first()
```

### Incorrect Pattern

```python
# ❌ Bad: No user_id filter - security vulnerability!
conversation = session.exec(
    select(Conversation).where(Conversation.id == conversation_id)
).first()
```
