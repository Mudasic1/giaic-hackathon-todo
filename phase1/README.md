# Phase 1: Todo In-Memory Python Console App

## 🚀 Overview
This project is a command-line Task Manager built using **Spec-Driven Development (SDD)**. It was developed entirely through AI agents (Claude Code) guided by rigorous specifications, with zero manual coding.

## 🛠 Tech Stack
* **Language:** Python 3.13+
* **Package Manager:** [uv](https://github.com/astral-sh/uv)
* **Agentic Workflow:** Claude Code + Spec-Kit Plus

## 📋 Features (Phase 1)
- **Add Tasks:** Create tasks with a title and description.
- **View List:** See all tasks with their current status (Pending/Completed).
- **Update:** Edit existing task details.
- **Toggle Status:** Mark tasks as complete or incomplete.
- **Delete:** Remove tasks by their unique ID.
- **In-Memory Storage:** Fast, session-based data management.

## 🏗 SDD Workflow
This project follows the **Hierarchy of Truth**:
1. `speckit.constitution` (Project Rules)
2. `specs/speckit.specify` (Requirements)
3. `specs/speckit.plan` (Architecture)
4. `specs/speckit.tasks` (Implementation Steps)





### Prerequisites
Ensure you have `uv` installed:
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh