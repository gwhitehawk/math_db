# Math Problems REST API

This is a Python Flask REST API with SQLite backend.

## Endpoints
- `/list`: Lists all math problems (id and title)
- `/<problem_id>`: Loads a problem statement by id

## Setup
1. Create the database and sample data:
   ```bash
   python init_db.py
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```

## Requirements
- Python 3.x
- Flask

Install Flask:
```bash
pip install flask
```
