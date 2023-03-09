# Dev Setup

1. Create virtual environment
2. Install prefect - `pip install prefect`
3. Set sqlite database path
    - `prefect config set PREFECT_API_DATABASE_CONNECTION_URL="sqlite+aiosqlite://///Users/ritabratamoitra/.prefect/prefect.db"`
4. Run required flow - `python3 hello_world_flow.py`