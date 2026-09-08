# FastAPI Complete Learning Guide

A comprehensive, progressive tutorial series covering FastAPI from fundamentals to advanced production patterns. This repository contains 20 complete tutorial files with practical examples, building a complete understanding of modern Python web API development.

**Author:** rishabhriyal112  
**Repository:** https://github.com/rishabhriyal112/FastAPI  

---

## 📚 Table of Contents

1. [Project Overview](#project-overview)
2. [Installation & Setup](#installation--setup)
3. [Tutorial Progression](#tutorial-progression)
4. [Project Structure](#project-structure)
5. [Running the Examples](#running-the-examples)
6. [Key Concepts](#key-concepts)
7. [Dependencies](#dependencies)
8. [Learning Path](#learning-path)

---

## 🎯 Project Overview

This is a **complete FastAPI learning repository** with 20 progressive tutorial files that teach you how to build production-ready APIs. Each file focuses on a specific FastAPI feature or concept, building upon previous lessons.

**What You'll Learn:**
- ✅ RESTful API design and HTTP methods
- ✅ Request/response validation with Pydantic
- ✅ Database integration with SQLAlchemy
- ✅ Authentication & authorization (JWT + OAuth2)
- ✅ Error handling & exceptions
- ✅ Middleware & request processing
- ✅ File uploads & static file serving
- ✅ CORS & security configurations
- ✅ External API integration & web scraping
- ✅ Advanced patterns: pagination, caching, rate limiting

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+ (tested with Python 3.10)
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone git@github-account1:rishabhriyal112/FastAPI.git
cd FastAPI
```

### Step 2: Create Virtual Environment
```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install fastapi uvicorn pydantic sqlalchemy python-jose passlib[bcrypt] python-multipart requests beautifulsoup4 slowapi python-dotenv
```

### Step 4: Create Environment File (Optional)
```bash
cp .env.example .env
# Edit .env with your configuration
```

---

## 📖 Tutorial Progression

### **Phase 1: Fundamentals (Files 01-05)**
Master the basics of FastAPI routing, request handling, and data validation.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `01_main.py` | **Routing & Parameters** | GET/POST endpoints, path params, query params, request body |
| `02_schema_pydantic.py` | **Data Validation** | Pydantic BaseModel, nested schemas, type validation |
| `03_todo_crud.py` | **CRUD Operations** | Create, Read, Update, Delete patterns with in-memory storage |
| `04_path_query_bodycombo.py` | **Mixed Parameters** | Combining path, query, and body parameters in one endpoint |
| `05_response_model.py` | **Response Filtering** | Using `response_model` to filter/hide sensitive fields |

**Run Example:**
```bash
uvicorn 01_main:app --reload
# Visit: http://127.0.0.1:8000/docs
```

---

### **Phase 2: Error Handling & Security (Files 06-08)**
Handle errors gracefully and implement basic security with dependencies and tokens.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `06_status_code.py` | **HTTP Status Codes** | Using correct status codes (201, 404, etc.) with HTTPException |
| `07_exception_handling.py` | **Custom Exceptions** | Creating custom exception classes and handlers |
| `08_dependency_exception.py` | **Dependency Injection** | Using `Depends()` for token validation and reusable logic |

**Run Example:**
```bash
uvicorn 06_status_code:app --reload
```

---

### **Phase 3: Middleware & Infrastructure (Files 09-10)**
Intercept requests and responses for logging, timing, and other cross-cutting concerns.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `09_middleware.py` | **Middleware Basics** | Request/response interception, async middleware patterns |
| `10_middleware2.py` | **Request Logging** | Performance logging, timing calculations, enhanced middleware |

**Run Example:**
```bash
uvicorn 10_middleware2:app --reload
# Make requests and watch the terminal for detailed logs
```

**Test Endpoints:**
```bash
# Fast response
curl http://127.0.0.1:8000/

# Slow response (2 seconds)
curl http://127.0.0.1:8000/slow

# Very slow response (5 seconds)
curl http://127.0.0.1:8000/very-slow
```

---

### **Phase 4: Database Integration (Files 11-12)**
Connect to databases and perform complex operations using SQLAlchemy ORM.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `11_sqlite_db.py` | **SQLite Connection** | Direct SQLite connection, table creation, basic setup |
| `12_sql_alchemy.py` | **SQLAlchemy ORM** | ORM models, sessions, CRUD with ORM, relationship queries |

**Run Example:**
```bash
uvicorn 12_sql_alchemy:app --reload
# Visit: http://127.0.0.1:8000/docs for interactive API
```

**Database File:**
- Creates `test.db` automatically in the project root

---

### **Phase 5: Authentication & Security (File 13)**
Implement JWT-based authentication with OAuth2 and password hashing.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `13_auth.py` | **JWT Authentication** | Password hashing (bcrypt), JWT tokens, OAuth2 flow, protected routes |

**Run Example:**
```bash
uvicorn 13_auth:app --reload
```

**Test Authentication:**
1. Go to: http://127.0.0.1:8000/docs
2. Click **Authorize** button
3. Login with:
   - **Username:** `admin`
   - **Password:** `1234`
4. Copy the token you receive
5. Paste token in the **Authorize** dialog
6. Access `/protected` endpoint

**Key Files:**
- `13_auth.py` - Complete JWT authentication implementation

---

### **Phase 6: File & Configuration Management (Files 14-15)**
Handle file uploads, serve static files, and manage environment configuration.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `14_upload_files.py` | **File Handling** | File uploads, disk storage, static file serving with StaticFiles |
| `15_config.py` | **Configuration** | Environment variables, .env file loading, settings management |
| `15_CORS.py` | **CORS Setup** | Cross-Origin Resource Sharing for frontend-backend communication |

**Run Example:**
```bash
uvicorn 14_upload_files:app --reload
```

**Upload File:**
```bash
curl -F "file=@your-file.pdf" http://127.0.0.1:8000/upload
```

**Access Uploaded Files:**
- Navigate to: `http://127.0.0.1:8000/files/your-filename`
- Files stored in: `/uploads` directory

---

### **Phase 7: External Integration (Files 16-17)**
Consume external APIs and scrape web content.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `16_ext_api.py` | **External APIs** | Making HTTP requests with `requests`, error handling, JSON parsing |
| `17_web_crawling.py` | **Web Scraping** | BeautifulSoup for HTML parsing, CSS selectors, data extraction |

**Run Example:**
```bash
uvicorn 16_ext_api:app --reload
```

**Test External API:**
```bash
curl http://127.0.0.1:8000/posts
curl http://127.0.0.1:8000/posts/1
```

---

### **Phase 8: Advanced Features (Files 18-20)**
Master pagination, caching, and rate limiting for production-ready APIs.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `18_pagination.py` | **Pagination** | Query params for page/limit, offset calculation, large dataset handling |
| `19_caching.py` | **Response Caching** | Time-based cache invalidation, performance optimization, freshness control |
| `20_rate_limiting.py` | **Rate Limiting** | Request throttling with slowapi, IP-based limits, abuse prevention |

**Run Example:**
```bash
uvicorn 20_rate_limiting:app --reload
```

**Test Rate Limiting:**
```bash
# Make 6 requests rapidly - the 6th will be rate limited
for i in {1..6}; do curl http://127.0.0.1:8000/data; done
```

---

## 📁 Project Structure

```
FastAPI/
├── 01_main.py                    # Basic routing and parameters
├── 02_schema_pydantic.py         # Pydantic schema design
├── 03_todo_crud.py               # CRUD operations
├── 04_path_query_bodycombo.py    # Parameter combination
├── 05_response_model.py          # Response filtering
├── 06_status_code.py             # HTTP status codes
├── 07_exception_handling.py      # Custom exceptions
├── 08_dependency_exception.py    # Dependency injection
├── 09_middleware.py              # Middleware basics
├── 10_middleware2.py             # Request logging middleware ⭐ Enhanced
├── 11_sqlite_db.py               # SQLite connection
├── 12_sql_alchemy.py             # SQLAlchemy ORM
├── 13_auth.py                    # JWT authentication
├── 14_upload_files.py            # File uploads
├── 15_config.py                  # Configuration management
├── 15_CORS.py                    # CORS middleware
├── 16_ext_api.py                 # External API consumption
├── 17_web_crawling.py            # Web scraping
├── 18_pagination.py              # Pagination
├── 19_caching.py                 # Response caching
├── 20_rate_limiting.py           # Rate limiting
├── main.py                       # Main entry point
├── test_main.py                  # Test examples
├── test.db                       # SQLite database (auto-generated)
├── uploads/                      # Uploaded files directory
├── .env                          # Environment variables (create from .env.example)
├── .env.example                  # Environment template
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

---

## 🔧 Running the Examples

### Run Any Tutorial File

```bash
# Using uvicorn with reload (hot-reloading)
uvicorn 01_main:app --reload

# Using venv's uvicorn (recommended)
.\venv\Scripts\uvicorn.exe 01_main:app --reload

# Specify host and port
uvicorn 01_main:app --host 0.0.0.0 --port 8000 --reload
```

### Interactive API Documentation

After running any file:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **OpenAPI Schema:** http://127.0.0.1:8000/openapi.json

### Run Tests

```bash
pytest test_main.py -v
```

---

## 🔑 Key Concepts

### HTTP Methods
- **GET** - Retrieve data (safe, idempotent)
- **POST** - Create new resource
- **PUT** - Update entire resource
- **DELETE** - Remove resource

### Parameter Types

```python
# Path parameter - part of URL
@app.get("/users/{user_id}")

# Query parameter - URL query string
@app.get("/users?name=john&age=30")

# Request body - JSON in request body
@app.post("/users")
def create_user(user: UserModel):
    pass
```

### Data Validation

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True  # default value
```

### Exception Handling

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

### Dependency Injection

```python
from fastapi import Depends

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validate token and return user
    return user

@app.get("/protected")
def protected_route(user = Depends(get_current_user)):
    return {"user": user}
```

### Authentication with JWT

```python
# Login endpoint returns token
token = jwt.encode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)

# Protected endpoints verify token
def verify_token(token: str = Depends(oauth2_schema)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
```

---

## 📦 Dependencies

### Core FastAPI
```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
```

### Database
```
sqlalchemy==2.0.23
```

### Authentication
```
python-jose==3.3.0
passlib[bcrypt]==1.7.4
bcrypt==3.2.2           # ⚠️ Must be 3.2.2 (not 4.x) for passlib compatibility
python-multipart==0.0.9  # Required for OAuth2PasswordRequestForm
```

### External APIs & Web Scraping
```
requests==2.31.0
beautifulsoup4==4.12.2
```

### Advanced Features
```
slowapi==0.1.9          # Rate limiting
python-dotenv==1.0.0    # Environment variables
```

### Testing
```
pytest==7.4.3
httpx==0.25.1
```

---

## 🎓 Learning Path

### For Beginners
**Start here → Complete in order:**
1. `01_main.py` - Understand basic routing
2. `02_schema_pydantic.py` - Learn data validation
3. `03_todo_crud.py` - Practice CRUD operations
4. `05_response_model.py` - Filter sensitive data

### For Intermediate Developers
**After basics, jump to:**
1. `06_status_code.py` - Proper HTTP semantics
2. `07_exception_handling.py` - Error handling
3. `12_sql_alchemy.py` - Database operations
4. `13_auth.py` - Authentication

### For Advanced Development
**Production-ready patterns:**
1. `10_middleware2.py` - Request logging & monitoring
2. `15_CORS.py` - Frontend integration
3. `18_pagination.py` - Handle large datasets
4. `20_rate_limiting.py` - Prevent abuse

### For Full Mastery
**Complete all 20 files in order** to understand:
- Architecture patterns
- Security best practices
- Performance optimization
- Production deployment considerations

---

## ⚠️ Important Notes

### Version Compatibility
- **bcrypt version:** Must use `3.2.2` with `passlib 1.7.4`
  ```bash
  pip install bcrypt==3.2.2 passlib[bcrypt]==1.7.4
  ```
  This ensures JWT authentication works correctly (bcrypt 4.x has compatibility issues)

### Database
- SQLite database (`test.db`) is automatically created on first run
- Data persists between runs
- Good for learning; use PostgreSQL/MySQL for production

### Security
- The `SECRET_KEY` in `13_auth.py` should be a strong, random value in production
- Never commit `.env` files with real secrets to git
- Use environment variables for sensitive data

### File Uploads
- Uploaded files are stored in the `/uploads` directory
- Ensure proper permission for your OS
- Implement file size limits in production

---

## 🚀 Deployment Considerations

### Before Deploying:
1. Change `reload=False` in production
2. Use production ASGI server (Gunicorn + Uvicorn)
3. Add proper logging and monitoring
4. Implement proper error handling and validation
5. Use environment variables for secrets
6. Set up database migrations
7. Add request authentication & authorization
8. Implement rate limiting and CORS properly

### Example Production Deployment:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

---

## 📚 Additional Resources

- **Official Docs:** https://fastapi.tiangolo.com/
- **Pydantic:** https://docs.pydantic.dev/
- **SQLAlchemy:** https://docs.sqlalchemy.org/
- **Python-jose (JWT):** https://github.com/mpdavis/python-jose
- **Slowapi (Rate Limiting):** https://github.com/laurentS/slowapi

---

## 🤝 Contributing

Found issues or have improvements? Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📝 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Author

**Rishabh Riyal** (rishabhriyal112)  
GitHub: [@rishabhriyal112](https://github.com/rishabhriyal112)  
Email: riyalrishabh22@gmail.com

---

## 🎉 Start Learning!

**Pick a file based on your interest and run it:**

```bash
# For beginners
uvicorn 01_main:app --reload

# For understanding databases
uvicorn 12_sql_alchemy:app --reload

# For authentication
uvicorn 13_auth:app --reload

# For advanced features
uvicorn 20_rate_limiting:app --reload
```

Visit http://127.0.0.1:8000/docs to interact with any API using Swagger UI!

---

**Happy Learning! 🚀**
