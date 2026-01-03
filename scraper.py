from collections import Counter
import requests
from bs4 import BeautifulSoup
import csv
import logging

# Logging setup
logging.basicConfig(filename="logs.txt", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Skills to track
skills = ["python", "java", "sql", "javascript", "react", "flask"]
counter = Counter()

# Job site URL
URL = "https://realpython.github.io/fake-jobs/"

# Fetch page
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logging.error(f"Job request failed: {e}")
    print("Request failed:", e)
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.find_all("div", class_="card-content")

# Extract jobs and count skills
job_list = []
for job in jobs:
    title = job.find("h2", class_="title").get_text(strip=True)
    company = job.find("h3", class_="company").get_text(strip=True)
    location = job.find("p", class_="location").get_text(strip=True)
    description = job.get_text(strip=True).lower()

    # Count skills
    for skill in skills:
        if skill in description:
            counter[skill] += 1

    job_list.append([title, company, location])

# Save jobs to CSV
with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company", "Location"])
    writer.writerows(job_list)

logging.info("Job scraping completed successfully")
print("Job scraping done:", counter)
