# REST API Endpoints

## Base URL

- Development: `http://localhost:8000/api`

## Authentication

- **All endpoints** require `Authorization: Bearer <token>` header.
- Token is verified against `BETTER_AUTH_SECRET`.

## Endpoints

### Tasks

#### GET `/api/tasks`

- **Auth**: Required
- **Scope**: Returns tasks belonging to `current_user.id` only.
- **Response**: List of [Task]

#### POST `/api/tasks`

- **Auth**: Required
- **Body**: `{ "title": "...", "description": "..." }`
- **Action**: Creates task with `user_id` = `current_user.id`.
- **Response**: Created [Task]

#### PATCH `/api/tasks/{id}`

- **Auth**: Required
- **Body**: `{ "completed": true, ... }`
- **Scope**: Can only update task where `task.user_id` == `current_user.id`.
- **Response**: Updated [Task]

#### DELETE `/api/tasks/{id}`

- **Auth**: Required
- **Scope**: Can only delete task where `task.user_id` == `current_user.id`.
- **Response**: `204 No Content`
