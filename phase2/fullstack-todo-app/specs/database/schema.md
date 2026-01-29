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
