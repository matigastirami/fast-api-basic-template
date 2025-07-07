# Description
This is a basic template for developing FastAPI services on top of it.

# Included
* PostgreSQL connection via ORM
* Input validation example
* JWT auth already implemented
* Basic folders structure to have a good starting point
* Swagger docs in /docs route

# Run the service
```bash
# Create an env file by copying the example and replace with actual values
cp .env.example .env

# Create a virtual env and activate it
# MacOS:
python3 -m venv venv
source venv/bin/activate

# Install the deps
pip install -r requirements.txt

# Run the service in dev mode
fastapi dev main.py
```

>Navigate to `http:localhost:8000/docs` to see the swagger docs of your API!
