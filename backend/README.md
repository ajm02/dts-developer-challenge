# Backend (FastAPI)

## Setup

You will need to create a Python venv:

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

## Tests
Run
```
pytest -q
```
