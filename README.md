# GeoSeer — AI-Powered Site Discovery Platform

Built by Sumit Ingole · April 2026

## Deploy to Render (same as InvoiceIQ)

1. Push this folder to a GitHub repo called `geoseer`
2. Go to render.com → New → Web Service
3. Connect your GitHub repo
4. Set these values:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment: Python 3
5. Click Deploy

Your live URL will be: `https://geoseer.onrender.com`

## Local development

```bash
pip install flask
python app.py
```

Open http://localhost:5000

## Pages

- `/` — Landing page with demo analyzer
- `/research` — Konkan Coast full research report
- `/api/sites` — JSON of all 7 excavation candidates
- `/api/analyze` — POST endpoint for region analysis
