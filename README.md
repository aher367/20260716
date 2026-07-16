# FastAPI Hello API for Render

A minimalist, highly performant FastAPI application designed to return a `"Hello"` JSON response, pre-configured for automatic deployment on [Render](https://render.com).

## 🚀 Local Development

To run this application locally, follow these steps:

### 1. Clone the repository and navigate to it:
```bash
cd render_test
```

### 2. Create and activate a Python virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI development server:
```bash
uvicorn main:app --reload
```

Open your browser and navigate to `http://127.0.0.1:8000/`. You should see:
```json
{
  "message": "Hello"
}
```

Interactive API documentation will be available at:
* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🌐 Deploying to Render

This project is pre-configured with a Render Blueprint configuration (`render.yaml`).

### Option A: Deploy via Blueprint (Recommended)
1. Push this project to your GitHub, GitLab, or Bitbucket repository.
2. Go to the [Render Dashboard](https://dashboard.render.com/).
3. Click **New** (top right) and select **Blueprint**.
4. Connect your Git repository.
5. Render will automatically parse `render.yaml` and set up the Web Service with the correct build and start commands.

### Option B: Manual Web Service Setup
If you prefer to configure it manually on Render:
1. Click **New > Web Service**.
2. Connect your Git repository.
3. Configure the following fields:
   * **Language**: `Python`
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Click **Deploy Web Service**.
