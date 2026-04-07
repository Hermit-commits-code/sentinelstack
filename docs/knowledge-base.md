
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

## FastAPI — Retention Notes

### What happens when the FastAPI server restarts?

- In development, `--reload` detects code changes and restarts the server.
- In-memory data such as `users = []` is reset on restart.
- This means all temporary user data is lost.

---

### Why is storing data in a Python list not enough for real applications?

- Data is lost when the server restarts.
- Data is not persistent.
- Multiple server instances would not share the same list.
- Lists do not provide database-level querying, constraints, or durability.

---

### Behavior difference between GET and POST

- `GET /users` reads and returns existing data.
- `POST /users` accepts incoming data and changes application state by creating new data.

---

### What format does FastAPI expect in a POST request body?

FastAPI expects JSON request body data, which it parses into Python data structures.

---

### What is the problem with `user: dict`?

Using `user: dict` accepts any dictionary structure without validation.

Problems:

- required fields are not enforced
- field names are not enforced
- data types are not enforced
- malformed input can be accepted

This is why structured validation with Pydantic is important.

---

## Pydantic — Core Concepts

### What is Pydantic?

A library used to validate and enforce data structure in Python applications.

---

### What is a BaseModel?

A class that defines the expected structure and types of data.

---

### Why use Pydantic instead of dict?

- Enforces required fields
- Enforces data types
- Prevents invalid input
- Provides automatic error responses

---

### What happens on invalid input?

FastAPI returns a structured validation error response automatically.

---

### Pydantic v2 change

- `.dict()` is deprecated
- Use `.model_dump()` instead

---

### What does `user: User` do?

- Parses incoming JSON
- Validates it against the model
- Rejects invalid data before your function runs

---

## Pydantic — Validation Behavior

### What happens if a required field is missing?

FastAPI returns a 422 validation error.
The route function is never executed.

---

### What happens if a type is incorrect?

FastAPI returns a 422 validation error due to type mismatch.

---

### Why is `user: dict` dangerous?

- Accepts any structure
- Does not enforce required fields
- Does not enforce types
- Allows invalid or unexpected data

---

### What does `user.model_dump()` do?

Converts a Pydantic model into a Python dictionary.

---

### Where does validation happen?

Validation happens BEFORE the route function runs.

Flow:

1. Request received
2. Data validated by Pydantic
3. If invalid → error returned
4. If valid → function executes

---

## FastAPI — In-Memory State

### What does `users = []` represent?

It creates temporary in-memory storage for user data while the server process is running.

---

### Why do users disappear after a reload?

The server process restarts during reload, so in-memory data is reset.

---

### What does `--reload` do?

It watches project files for changes and automatically restarts the development server.

---

### Why use in-memory storage first?

It allows route behavior and request flow to be tested before adding persistence.

---

### What is the next step after in-memory storage?

Use a database or other persistent storage so data survives restarts.

---

## FastAPI — Query Parameters

### What is a query parameter?

A value passed in the URL after `?` used to filter or modify responses.

Example:
`/users?name=Joseph`

---

### Why use `name: str = None`?

Makes the parameter optional.
If not provided, it defaults to None.

---

### Where do query parameters come from?

They come from the URL, not from request body or models.

---

### What happens if no data matches?

Returns an empty list, not an error.

---

## FastAPI — Path Parameters

### What is a path parameter?

A dynamic part of a URL used to identify a specific resource.

Example:
`/users/{index}`

---

### What does FastAPI do with path parameters?

- Parses them from the URL
- Converts them to the specified type
- Passes them into the function

---

### Why validate path parameters?

To prevent crashes and ensure safe responses.

---

## FastAPI — Model Design

### Why separate input and output models?

Using one model for everything can expose fields that should not be controlled by the client.

Example problem:

- Client can send their own `id`
- Leads to invalid or conflicting data

---

### What is `UserCreate`?

Represents incoming request data.

Used for:

- POST requests
- client input

---

### What is `User`?

Represents stored and returned data.

Includes:

- system-generated fields (like `id`)

---

### Why generate IDs in the backend?

- ensures uniqueness
- prevents collisions
- prevents client manipulation
- standard practice in APIs

---

### Why are UUIDs used?

- globally unique
- safe across distributed systems
- do not rely on ordering

---

### Why not use list index?

- unstable if list changes
- not unique
- not scalable
- breaks with persistence
