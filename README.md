# HMCTS Task System

This is the HMCTS Developer Task. Make sure you have the following installed:

- Python 3.12
- Node v20

## Backend

### Setup

First, navigate to the backend folder:

```
cd backend
```

You will then need to create a Python venv:

```
python -m venv .venv
```

Then you will need to activate it.
For Unix based systems:

```
source .venv/Scripts/activate
```

For Windows based systems:

```
 .venv\Scripts\activate
```

And then run

```
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

To view the interactive documentation,
visit: http://localhost:8000/docs

### Tests

Run

```
pytest -q
```

## Frontend

First navigate to the frontend folder:

```
cd frontend
```

Then run these commands:

```
npm install --legacy-peer-deps
npm run dev
```

View the application at http://localhost:5173
