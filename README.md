# FastAPI Learning Project

This repository contains small, focused FastAPI examples.  
Each Python file is a standalone app that demonstrates a specific FastAPI concept.

## Project Structure

- `/home/runner/work/FastAPI/FastAPI/01_main.py`  
  Basic routes, query parameters, and simple request body usage with Pydantic.

- `/home/runner/work/FastAPI/FastAPI/02_schema_pydantic.py`  
  Pydantic schemas with nested models (`User` containing an `Address`).

- `/home/runner/work/FastAPI/FastAPI/03_todo_crud.py`  
  In-memory Todo CRUD API (`create`, `read all`, `read one`, `update`, `delete`).

- `/home/runner/work/FastAPI/FastAPI/04_path_query_bodycombo.py`  
  Combined usage of path params, query params, and request body in one flow.

- `/home/runner/work/FastAPI/FastAPI/05_response_model.py`  
  `response_model` filtering to hide sensitive fields (e.g., password).

- `/home/runner/work/FastAPI/FastAPI/06_status_code.py`  
  Custom status codes and `HTTPException` for error responses.

- `/home/runner/work/FastAPI/FastAPI/07_exception_handling.py`  
  Custom exception class and global exception handler with JSON responses.

- `/home/runner/work/FastAPI/FastAPI/08_dependency_exception.py`  
  Dependency injection for token validation using headers.

- `/home/runner/work/FastAPI/FastAPI/09_middleware.py`  
  Middleware that logs request path and processing time.

- `/home/runner/work/FastAPI/FastAPI/10_middleware2.py`  
  Middleware flow example showing pre-request and post-response hooks.

## Prerequisites

- Python 3.9+
- `pip`

## Setup

From `/home/runner/work/FastAPI/FastAPI`:

```bash
pip install fastapi uvicorn pydantic
```

## Run Any Example

Each file defines `app = FastAPI()`.  
Run one file at a time with uvicorn:

```bash
uvicorn 01_main:app --reload
```

Replace `01_main` with any other filename (without `.py`), for example:

```bash
uvicorn 03_todo_crud:app --reload
```

## Notes

- Data in Todo/User examples is stored in memory (lists), so it resets when the server restarts.
- Some files use `@app.get(...)` for learning demonstrations where `POST` is more typical in production.
