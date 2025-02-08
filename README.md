# Job Scraper Project

# JobHarvest: Intelligent Job Scraper

## 📌 Overview

JobHarvest is an **automated job scraper** that extracts job postings from multiple job portals like **LinkedIn, Indeed,
Monster, and Glassdoor** based on user-defined filters. It exports results into an easy-to-use **CSV file**.

---

## 🚀 Features

- **Multi-Portal Scraping** – Extract job postings from LinkedIn, Indeed, Monster, Glassdoor.
- **Advanced Filtering** – Filter by **location, job type, industry, experience level, salary**.
- **CSV Export** – Save job listings with title, company, location, and job link. .
- **Data Cleanup** – Removes duplicates and formats data.

---

## 🔧 Installation

### **1️⃣. Clone the Repository**

```bash
git clone https://github.com/bhanuprakash1098/job_scraper.git
cd job_scraper
```

### **2️⃣. Set Up a Virtual Environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣3️. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣. Add `config.ini` File (Required for Authentication)**

For security reasons, the `config.ini` file, which stores login credentials for job portals (**LinkedIn, Indeed,
Handshake, Glassdoor**), is **not included in this repository**. You must **manually create** this file inside the
`resources` folder.

#### **Example `config.ini` Structure**

```ini
[LinkedIn]
username = ****your username****
password = ****your password****

[Handshake]
username = ****your username****
password = ****your password****

[Indeed]
username = ****your username****
password = ****your password****

[Glassdoor]
username = ****your username****
password = ****your password****
```

---

## ⚡ Usage

### **1️⃣. Provide Filters in the CSV File**

- Before running the scraper, ensure your filters are defined in filters.csv

### **2️⃣. Run the Scrapper**

```bash
python main.py
```

- This will read the filters from filters.csv, scrape jobs from multiple portals, and save the results.

### **3️⃣. View Scraped Data**

- Once the scraper runs successfully, the job listings are saved in CSV format.
- Open it using Excel, Google Sheets, or any CSV viewer.

---

## 🛠️ Technologies Used

- Python
- Selenium - For web scraping
- Pandas - CSV integration

---

## 🚨 Preventing Errors: Read Before You Start

Before entering filters in the CSV file, follow these important guidelines to avoid errors.

### **General Guidelines**

- **For multiple selections (Experience Level, Job Type, Remote options), enter multiple values in the same column**.
- **Ensure correct spelling and capitalization** as inputs are case-sensitive.

### **Filter-Specific Guidelines**

#### **1️⃣ Platform**

- Specify which job platform(s) to automate.
- Options:
    - `LinkedIn`
    - `Indeed`
    - `Handshake`
    - `Glassdoor`
- 📌 **Example:** `LinkedIn`

#### **2️⃣ Job Title**

- Enter the job title you are searching for.
- 📌 **Example:** `Software Engineer`

#### **3️⃣ Location**

- Enter the desired location for the job search.
- 📌 **Example:** `New York, NY` or `Remote`

#### **4️⃣ Sort By**

- Options: `Most recent`, `Most relevant`
- ⚠️ **Case-sensitive** – enter exactly as shown.
- 📌 **Example:** `Most recent`

#### **5️⃣ Date Posted**

- Options:
    - `Any time`
    - `Past month`
    - `Past week`
    - `Past 24 hours`
- ⚠️ **Case-sensitive** – enter exactly as shown.
- 📌 **Example:** `Past week`

#### **6️⃣ Experience Level**

- Options:
    - `Internship`
    - `Entry level`
    - `Associate`
    - `Mid-Senior level`
    - `Director`
    - `Executive`
- **Multiple selections allowed**.

#### **7️⃣ Job Type**

- Options:
    - `Full-time`
    - `Part-time`
    - `Contract`
    - `Temporary`
    - `Volunteer`
    - `Internship`
    - `Other`
- **Multiple selections allowed**.

#### **8️⃣ Remote Work**

- Options:
    - `Remote`
    - `On-site`
    - `Hybrid`
- **Multiple selections allowed**.

Failure to follow these rules may cause the script to ignore or incorrectly process the filters.
