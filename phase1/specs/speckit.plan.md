# Technical Plan: Phase 1

## Architecture
- **Data Model**: A `Task` class with fields: `id` (int), `title` (str), `description` (str), and `is_completed` (bool).
- **Controller**: A `TaskManager` class to handle the list of tasks and CRUD logic.
- **View**: A simple CLI loop using `input()` and `print()` statements.

## Logic Flow
1. Initialize an empty list `tasks`.
2. Enter a `while True` loop.
3. Display menu options.
4. Route user input to the appropriate `TaskManager` method.
5. Exit loop on 'Exit' command.