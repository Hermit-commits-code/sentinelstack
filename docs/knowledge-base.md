
# Knowledge Base

---

## Python — Core Concepts

### Lists

- Ordered collection of values.
- Supports indexing.
- Allows duplicates.
- Mutable (can be changed).

---

### Dictionaries

- Store data as key/value pairs.
- Accessed by keys, not index.
- Useful for structured data.

---

### Sets

- Store unique values only.
- Unordered.
- No indexing.
- Useful for removing duplicates.

---

## Python — Files

### File Modes

- "r" → read
- "w" → write (overwrites)

---

### Why use `with open()`?

- Automatically closes file.
- Safer and standard practice.

---

## Python — Modules

### What is a module?

A Python file used to organize and reuse code.

---

### Import patterns

```python
import utils
utils.greet()

from utils import greet
greet()
```

## FastAPI — Core Concepts

### What is FastAPI?

A Python web framework for building APIs using routes and HTTP methods.

### What is app = FastAPI()?

Creates an instance of a FastAPI application.

### What does @app.get("/path") do?

Defines a route that handles HTTP GET requests at a specific path.

### What happens when returning a dictionary?

FastAPI converts Python dictionaries into JSON responses.

### What does uvicorn app.main:app mean?

- app → folder
- main → file
- app → FastAPI instance

Runs the FastAPI application.

## Script vs Server

- Script → defines logic
- Server → runs and exposes logic over HTTP

### Why is /health important?

Used to verify the service is running.
Critical for monitoring and infrastructure systems.

## GET vs POST

- GET → retrieve data
- POST → send and create data

## In-memory storage

- Data stored in variables (like lists)
- Temporary (resets when server restarts)
