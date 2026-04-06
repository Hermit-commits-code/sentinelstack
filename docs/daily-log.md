# Daily Log

## Day 0 — Environment

### Learned
- Structured dev environments reduce friction.
- Profiles and folders should reflect task boundaries.

### Built
- Repo structure
- VSCode profiles
- Ubuntu dev environment
- Initial project scaffolding

### Broke
- Kitty install path
- GNOME shell theming
- VSCode profile automation assumptions

### Fixed
- Clarified manual profile setup
- Continued GNOME extension configuration
- Standardized workspace layout

### Questions
- Best order for Day 1 learning flow
- Final Kitty/default terminal setup

## Day 1 — Python Phase 0
**Focus Area:** Python (Learning)
**Date:** 2026-04-05

### Learned
- Python code runs file by file.
- `print()` outputs text or values to the terminal.
- Variables store values.
- Strings and integers are different data types.

### Built
- A first Python file named `hello.py`
- Variables for name, age, and personal information

### Broke
- Tried to add a string and an integer:
  `"thirty" + 10`

### Fixed
- Separated text values from numeric values
- Re-ran the script successfully

### Questions
-

## Day 2 — Python Phase 0 (Control Flow)
**Date:** 2026-04-05
**Focus Area:** Python (Learning)

### Learned
- Python uses `if`, `elif`, and `else` to control program flow.
- Conditions evaluate to `True` or `False`.
- Comparison operators like `>=`, `<`, and `==` determine logic paths.
- Python is strict about data types when comparing values.

### Built
- Conditional logic to classify age groups (minor, adult, senior).
- A temperature-based decision system (cold, nice, hot).

### Broke
- Attempted to compare a string to an integer:
  ```python
  age = "twenty"
  if age >= 18:
  ```
### Fixed
- Replaced string value with an integer:
  ```python
    age = 20
  ```
- Understood that comparisons require compatible data types.
### Questions
- How does Python internally evaluate conditions?
- What other comparison operators exist beyond the ones used today?

## Day 3 — Python Phase 0 (Loops)
**Date:** 2026-04-05
**Focus Area:** Python (Learning)

### Learned
- A `for` loop repeats code over a sequence, such as a range or a list.
- `range(5)` produces values from `0` through `4`.
- A `while` loop repeats as long as its condition stays `True`.
- Loop control must be handled carefully to avoid infinite loops.

### Built
- A `for` loop that printed numbers from `0` to `4`.
- A loop that iterated through a list of names.
- A `while` loop that counted upward and stopped at a defined limit.

### Broke
- Created an infinite loop with:
  `while True:`
- The script kept running until it was manually interrupted.

### Fixed
- Stopped the program with `Ctrl + C`.
- Replaced the infinite loop with a bounded condition:
  `while count < 3:`
- Added `count += 1` so the loop could make progress and terminate.

### Questions
- When should I prefer a `for` loop over a `while` loop?
- What are `break` and `continue`, and when should they be used?

## Day 4 — Python Phase 0 (Functions)
**Date:** 2026-04-05
**Focus Area:** Python (Learning)

### Learned
- Functions let me group reusable logic into named blocks.
- `def` defines a function.
- Parameters let a function receive input.
- `return` sends a value back to the caller.

### Built
- A basic `greet()` function.
- A `greet(name)` function that accepted a parameter.
- An `add(a, b)` function that returned the sum of two values.
- A `describe_person(name, age)` function for formatted output.

### Broke
- Passed incompatible types into a function:
  `add("2", 3)`
- This caused a type error because Python cannot add a string and an integer directly.

### Fixed
- Passed matching numeric types instead:
  `add(2, 3)`
- Confirmed that function inputs matter just as much as function logic.

### Questions
- When should a function `print()` something versus `return` a value?
- How many parameters should a beginner function usually have before it becomes too much?


## Day 5 — Python Phase 1 (Lists)
**Date:** 2026-04-05
**Focus Area:** Python (Learning)

### Learned
- Lists store multiple values in an ordered structure.
- Indexing starts at 0, not 1.
- Accessing an invalid index causes an IndexError.
- Lists are mutable, meaning values can be changed after creation.
- `.append()` adds new elements to the end of a list.
- Lists can contain mixed data types, which can lead to runtime errors.

### Built
- Created lists of numbers and names.
- Accessed elements using indexing.
- Modified list values using assignment.
- Appended new elements to existing lists.
- Iterated over lists using a `for` loop.
- Combined loops with conditional logic to filter values.

### Broke
- Attempted to access an index that did not exist:
  `numbers[3]`
- Mixed data types in a list and tried to perform arithmetic:
  `num + 1` on a string value.

### Fixed
- Corrected index usage based on list length.
- Ensured consistent data types before performing operations.
- Understood that Python allows mixed types but does not handle them automatically.

### Questions
- When should lists contain mixed types versus a single type?
- What other operations can be performed on lists besides append?


## Day 6 — Python Phase 1 (Dictionaries)
**Date:** 2026-04-06
**Focus Area:** Python (Learning)

### Learned
- Dictionaries store data as key/value pairs instead of ordered positions.
- Keys are used to access values instead of numeric indexes.
- Accessing a missing key causes an error.
- Dictionaries are mutable and can be updated or extended after creation.
- Looping through a dictionary iterates over its keys by default.
- Values can be accessed inside a loop using the key.

### Built
- Created dictionaries to represent structured data (person, book).
- Accessed values using keys such as "name" and "age".
- Updated existing values in a dictionary.
- Added new key/value pairs dynamically.
- Iterated over dictionary keys and printed both keys and values.

### Broke
- Attempted to access a key that did not exist:
  `person["city"]`
- This caused a runtime error.

### Fixed
- Ensured the key existed before accessing it.
- Added the missing key to the dictionary before using it.
- Reinforced that dictionary access requires valid keys.

### Questions
- What is the best way to safely access keys that may not exist?
- Can dictionaries be nested, and how complex can they become?


## Day 7 — Python Phase 1 (Sets)
**Date:** 2026-04-06
**Focus Area:** Python (Learning)

### Learned
- Sets store unique values and automatically remove duplicates.
- Sets are unordered, meaning they do not maintain position like lists.
- Sets do not support indexing because they are not ordered.
- The `.add()` method is used to insert new values into a set.
- Sets are useful for filtering duplicates and validating uniqueness.

### Built
- Created sets with duplicate values and observed automatic deduplication.
- Added new elements to sets using `.add()`.
- Iterated over sets using a `for` loop.
- Converted lists into sets to remove duplicate entries.

### Broke
- Attempted to access a set using an index:
  `nums[0]`
- This caused an error because sets are unordered and do not support indexing.

### Fixed
- Used iteration (`for` loop) instead of indexing to access values.
- Reinforced that sets must be accessed through traversal, not position.

### Questions
- When should I use a set instead of a list in real applications?
  - you need unique values
  - you want to remove duplicates
  - you want to check membership quickly
- Are sets faster than lists for checking if a value exists?


## Day 8 — Python Phase 1 (Files + Modules)
**Date:** 2026-04-06
**Focus Area:** Python (Learning)

### Learned
- Files allow programs to persist data outside of memory.
- Opening a file with `"w"` writes to it and overwrites existing content.
- Opening a file with `"r"` reads existing content.
- Attempting to read a non-existent file results in an error.
- The `with open()` pattern is safer because it automatically closes the file.
- Python modules allow code to be split into multiple files for better organization.
- The `import` statement loads functions or variables from another file.
- Module names must match file names for imports to work correctly.

### Built
- Created and wrote data to a file using `open()` and `"w"` mode.
- Read data from a file and printed its contents.
- Rewrote file handling using `with open()` for safer execution.
- Created a separate module file (`utils.py`) containing reusable functions.
- Imported functions from another file and executed them.
- Created a `math_utils.py` module and used it in a main file.

### Broke
- Attempted to read a file that did not exist.
- Renamed a module file and attempted to import using the old name.
- Both cases caused runtime errors.

### Fixed
- Ensured files exist before reading them.
- Matched import statements to the correct file names.
- Understood that Python resolves imports based on file/module names.

### Questions
- How are modules organized in larger applications with many files?
- What happens if two modules have the same name in different locations?


## Day 9 — Python Phase 1 (Project Structure + Virtual Environments)
**Date:** 2026-04-06
**Focus Area:** Python (Learning)

### Learned
- Real applications are structured across multiple files and directories.
- Separating logic into modules improves organization and maintainability.
- A virtual environment isolates project dependencies from the system Python.
- The `venv` module creates a local Python environment for a project.
- Activating a virtual environment ensures installed packages are scoped to that project.
- VSCode must be explicitly configured to use the correct Python interpreter.
- Terminal Python and VSCode Python can differ if the interpreter is not aligned.

### Built
- Created a structured Python project with an `app/` directory.
- Split logic into `main.py` and `utils.py`.
- Imported functions between modules successfully.
- Created a virtual environment using `python -m venv`.
- Activated the environment and installed the `requests` package.
- Configured VSCode to use the project's virtual environment interpreter.

### Broke
- Created the virtual environment inside the wrong directory (`app/venv`).
- VSCode failed to recognize installed packages due to incorrect interpreter selection.
- Encountered import errors for installed packages.

### Fixed
- Recreated the virtual environment at the correct project root (`project/venv`).
- Reinstalled dependencies within the correct environment.
- Selected the proper interpreter in VSCode to match the active virtual environment.
- Verified package availability and resolved import errors.

### Questions
- How are dependencies managed and tracked across larger projects?
- What is the standard way to recreate environments across machines?


## Day 10 — FastAPI Phase 0 (Backend Initialization)
**Date:** 2026-04-05
**Focus Area:** Backend (FastAPI)

### Learned
- FastAPI is a Python web framework used to build APIs.
- A FastAPI app is created using `FastAPI()`.
- Routes are defined using decorators like `@app.get()`.
- Each route maps a URL path to a Python function.
- FastAPI automatically converts Python dictionaries into JSON responses.
- Uvicorn is an ASGI server used to run FastAPI applications.
- The `--reload` flag enables automatic server reload during development.
- FastAPI automatically generates interactive API documentation at `/docs`.

### Built
- Created a backend project structure inside SentinelStack.
- Set up a virtual environment for the backend.
- Installed FastAPI and Uvicorn.
- Created `app/main.py` as the application entry point.
- Implemented a root endpoint (`/`) returning a JSON message.
- Implemented a health check endpoint (`/health`).
- Successfully ran the backend server locally.
- Verified endpoints through browser and interactive API docs.

### Broke
- No major issues encountered during setup.
- Verified correct environment usage before running server.

### Fixed
- Ensured backend virtual environment was active before installing dependencies.
- Confirmed VSCode interpreter matched backend environment.

### Questions
- How are routes organized across multiple files in larger applications?
- How do we start handling real data instead of static responses?


## Day 11 — FastAPI Phase 1 (POST + State)
**Date:** 2026-04-05
**Focus Area:** Backend (FastAPI)

### Learned
- APIs can accept incoming data using HTTP POST requests.
- FastAPI automatically parses incoming JSON into Python data structures.
- Request bodies can be defined as function parameters.
- Data can be stored in memory using Python data structures like lists.
- GET and POST routes work together to retrieve and modify application state.

### Built
- Implemented a POST `/users` endpoint to accept incoming user data.
- Stored user data in an in-memory list.
- Verified that POST requests modify application state.
- Retrieved stored users using the GET `/users` endpoint.
- Used FastAPI interactive docs to test API endpoints.

### Broke
- No major issues encountered during implementation.
- Verified correct request format via `/docs`.

### Fixed
- Ensured request body was valid JSON.
- Confirmed correct route usage (GET vs POST).

### Questions
- How do we validate incoming data instead of accepting any structure?
- How do we persist data beyond memory (database)?

