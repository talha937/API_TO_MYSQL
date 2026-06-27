# API to MySQL

Fetches user data from the [ReqRes API](https://reqres.in) and stores it in a MySQL database. Handles pagination automatically.

## Tech Stack
- Python
- MySQL
- `requests`, `mysql-connector-python`, `python-dotenv`

## Setup
1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file based on `.env.example`
5. Run: `python main.py`