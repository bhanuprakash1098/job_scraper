# Job Scraper Project
# JobHarvest: Intelligent Job Scraper

## 📌 Overview
JobHarvest is an **automated job scraper** that extracts job postings from multiple job portals like **LinkedIn, Indeed, Monster, and Glassdoor** based on user-defined filters. It exports results into an easy-to-use **CSV file**.

---

## 🚀 Features
- **Multi-Portal Scraping** – Extract job postings from LinkedIn, Indeed, Monster, Glassdoor.
- **Advanced Filtering** – Filter by **location, job type, industry, experience level, salary**.
- **CSV Export** – Save job listings with title, company, location, and job link. .
- **Data Cleanup** – Removes duplicates and formats data.

---

## 🔧 Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/bhanuprakash1098/job_scraper.git
cd job_scraper
```

### **2. Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## ⚡ Usage
### **1. Provide Filters in the CSV File**
- Before running the scraper, ensure your filters are defined in filters.csv

### **2. Run the Scrapper**
```bash
python main.py
```
- This will read the filters from filters.csv, scrape jobs from multiple portals, and save the results.

### **3. View Scraped Data**
- Once the scraper runs successfully, the job listings are saved in CSV format.
- Open it using Excel, Google Sheets, or any CSV viewer.

---

## 🛠️ Technologies Used
- Python
- Selenium - For web scraping
- Pandas - CSV integration

## 🚨 Preventing Errors: Read Before You Start

Before entering experience levels in the CSV file, follow these important guidelines to avoid errors:

- **Use '|' as a separator** if selecting multiple experience levels.  
  📌 **Example:** `Internship | Entry level | Associate`  
- **Only use the following valid experience levels:**  
  - `Internship`
  - `Entry level`
  - `Associate`
  - `Mid-Senior level`
  - `Director`
  - `Executive`
- **Experience levels are case-sensitive**  
  - ✅ **Correct:** `Entry level`
  - ❌ **Incorrect:** `entry Level`, `ENTRY LEVEL`, `Entry-level`

Failure to follow these rules may cause the script to ignore or incorrectly process the filters.
