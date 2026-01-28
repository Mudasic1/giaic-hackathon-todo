# Specification: Phase 1 Todo App

## Project Goal
Build a Python CLI application to manage tasks in-memory.

## Functional Requirements
- **REQ-01: Add Task** - User can provide a title and description.
- **REQ-02: View Tasks** - Display a numbered list of all tasks with status.
- **REQ-03: Update Task** - Edit the title or description of an existing task ID.
- **REQ-04: Mark Complete** - Toggle a task between 'Pending' and 'Completed'.
- **REQ-05: Delete Task** - Remove a task from the session by ID.

## Acceptance Criteria
- The app must run via `python src/main.py`.
- Data does not need to persist after the program exits.
- Invalid IDs must be handled gracefully with an error message.