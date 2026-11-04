# Cultural Roots Explorer - Backend API

This is the Flask REST API for the Cultural Roots Explorer. It serves dynamic, crowdsourced cultural narratives (food, history, and social norms) and generates geospatial map queries for the frontend client.

This guide covers everything needed to start the backend from scratch, including spinning up a local PostgreSQL database using Docker, seeding pilot data, and verifying the endpoints.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.10+
- Docker Desktop (make sure the Docker engine is currently running)

## 1. Environment Configuration

First, navigate to the backend directory and create your environment variables file.

```bash
cd backend
cp .env.example .env
```

Inside the .env, you will find the database URL line:

**`backend/.env`**

```env
DATABASE_URL=postgresql://postgres:password@localhost:5434/cultural_roots
```
**Replace the //{postgres:password} portion with your desired {user_name:password}**

## 2. Database Setup (Docker)

We use Docker to quickly spin up a PostgreSQL instance without needing to install the full database software on your host machine.

Run this single command in your terminal to download, configure, and start the database:

```bash
docker run --name cultural_roots_db \
  -e POSTGRES_USER={Your Username} \
  -e POSTGRES_PASSWORD={Your Password} \
  -e POSTGRES_DB=cultural_roots \
  -p 5434:5432 \
  -d postgres:latest
```

**To verify the database is running:** Run `docker ps`. You should see `cultural_roots_db` in the list of active containers.

## 3. Python Virtual Environment

Next, isolate your Python dependencies by creating and activating a virtual environment.

**For Mac / Linux / WSL:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

Once activated (you will see `(venv)` in your terminal prompt), install the required packages:

```bash
pip install -r requirements.txt
```

## 4. Initialize and Seed the Database

With the database running and dependencies installed, you need to create the SQL tables and populate them with the pilot data for Ethiopia and Kenya.

Run the seed script:

```bash
python seed_db.py
```

**Expected output:** `Pilot data seeded successfully.`

## 5. Run the Flask Server

Start the development server:

```bash
python run.py
```

The server will bind to port 5000 and print: `Running on http://127.0.0.1:5000`

## 6. Verify the API Works

Leave the server running and open your web browser (or use a tool like Postman or `curl` in a new terminal window) to test these endpoints:

### A. Health Check

- **URL:** http://localhost:5000/api/health
- **Expected response:**

```json
{
  "database": "PostgreSQL configured",
  "status": "healthy"
}
```

### B. Fetch Approved Countries (Public API)

- **URL:** http://localhost:5000/api/countries
- **Expected response:** You should see a JSON array containing the seeded data for Ethiopia and Kenya. Notice that the backend dynamically generates the `food_map_url`, `history_map_url`, and `culture_map_url` on the fly.

```json
[
  {
    "culture_map_url": "https://www.google.com/maps/search/?api=1&query=Ethiopian%20Orthodox%20Tewahedo%20Church",
    "culture_narrative": "The traditional coffee ceremony (Buna) is a cornerstone of our social life...",
    "culture_query": "Ethiopian Orthodox Tewahedo Church",
    "food_map_url": "https://www.google.com/maps/search/?api=1&query=Gursha%20Ethiopian%20Restaurant%2C%20Grand%20Rapids%2C%20MI",
    "id": 1,
    "name": "Ethiopia",
    "status": "Approved"
    ...
  }
]
```