# Telegram bot that tags all members of a group 👥

## Setup 🛠️
### Using Docker 🐋

1. Create `.env` file
    ```bash
    cp .env.example .env
    ```
2. Change credentials in [`.env` file](./.env) accordingly

3. Launch app ⚛️
    * Development mode (fast-refresh)
        ```bash
        docker compose watch
        ```

    * Production mode
        ```bash
        docker compose up --build -d
        ```

### Pure Python 🐍
1. Create virtual environment
    ```bash  
    python -m venv venv  
    ```

2. Activate it
    * On Windows:
        ```bash
        venv\Scripts\activate
        ```

   * On MacOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. Install dependencies 🛠️
    ```bash
    pip install -r requirements.txt
    ```

4. Create `.env` file
    ```bash
    cp .env.example .env
    ```
5. Change credentials in [`.env` file](./.env) accordingly

6. Launch app ⚛️
    * On Windows:
        ```bash
        python main.py
        ```

   * On MacOS/Linux:
        ```bash
        python3 main.py
        ```
