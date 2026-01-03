# Job Scraper Analyzer

## Overview
Python project that scrapes job listings from a public website, analyzes in-demand skills, and exposes the data via a Flask API.

---

## Features
- Scrapes jobs from https://realpython.github.io/fake-jobs/
- Tracks skills: Python, Java, SQL, JavaScript, React, Flask
- Counts occurrences of skills
- Saves job data to CSV
- Provides API endpoint:
  - `/jobs` → Returns jobs as JSON
- Logging and error handling

---

## Technologies
- Python
- Requests
- BeautifulSoup
- Flask
- CSV & Logging

---

## How to Run

1. Install dependencies:
   
pip install -r requirements.txt

3. Run scraper:

python scraper.py

3. Run Flask API:

python app.py

4. Open browser: http://127.0.0.1:5000/jobs

