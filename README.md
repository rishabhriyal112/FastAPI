# FastAPI 🚀

This repository contains my FastAPI learning series, covering concepts from the basics to advanced API development. Each file focuses on a specific concept with simple examples and practical implementations.

## 📚 Tutorials

| #  | File                         | Topic                                                 |
| -- | ---------------------------- | ----------------------------------------------------- |
| 01 | `01_main.py`                 | FastAPI basics, routing, parameters, and request body |
| 02 | `02_schema_pydantic.py`      | Pydantic schemas and data validation                  |
| 03 | `03_todo_crud.py`            | CRUD operations                                       |
| 04 | `04_path_query_bodycombo.py` | Combining path, query, and body parameters            |
| 05 | `05_response_model.py`       | Response models and filtering                         |
| 06 | `06_status_code.py`          | HTTP status codes                                     |
| 07 | `07_exception_handling.py`   | Exception handling                                    |
| 08 | `08_dependency_exception.py` | Dependency injection                                  |
| 09 | `09_middleware.py`           | Middleware basics                                     |
| 10 | `10_middleware2.py`          | Request logging middleware                            |
| 11 | `11_sqlite_db.py`            | SQLite database connection                            |
| 12 | `12_sql_alchemy.py`          | SQLAlchemy ORM                                        |
| 13 | `13_auth.py`                 | JWT authentication and OAuth2                         |
| 14 | `14_upload_files.py`         | File uploads                                          |
| 15 | `15_config.py`               | Environment configuration                             |
| 16 | `15_CORS.py`                 | CORS middleware                                       |
| 17 | `16_ext_api.py`              | Working with external APIs                            |
| 18 | `17_web_crawling.py`         | Web scraping                                          |
| 19 | `18_pagination.py`           | API pagination                                        |
| 20 | `19_caching.py`              | Response caching                                      |
| 21 | `20_rate_limiting.py`        | API rate limiting                                     |

## 🚀 How to Run

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Run any tutorial file using:

```bash
uvicorn 01_main:app --reload
```

Replace `01_main` with the filename you want to run.

For example:

```bash
uvicorn 13_auth:app --reload
```

Then open the API documentation at:

```text
http://127.0.0.1:8000/docs
```

> Make sure the file contains a FastAPI instance named `app`.

---

**Learning FastAPI one concept at a time. 🚀**
