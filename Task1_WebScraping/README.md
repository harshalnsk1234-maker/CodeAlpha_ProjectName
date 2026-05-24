# 💬 Quotes to Scrape Automation

An automated web scraping project designed to extract motivational quotes, their authors, and associated tags into a structured Excel spreadsheet.

## 🚀 Overview & Automation Tool
This project uses **Octoparse** to automatically extract data without writing code or manual browser navigation. 

* **Scraper Type:** Desktop App Workflow
* **Frequency:** Run manually / On-demand
* **Target Website:** `https://toscrape.com`
* **Output Format:** Microsoft Excel (`.xlsx`)

## 📊 Extracted Data Fields
The Octoparse task is configured to capture the following columns for the Excel sheet:
- `Quote` (The text body of the quote)
- `Author` (The person who said it)
- `Tags` (Keywords/Categories associated with the quote)

## 🛠️ Configuration & Setup
To run or modify this scraping task locally on your machine:

1. Download and install **[Octoparse](https://octoparse.com)** (Desktop Version).
2. Clone or download this repository to your local computer.
3. Open Octoparse and click on **Import Task**.
4. Select the `.otd` configuration file included in this repository (e.g., `quotes_scraper.otd`).
5. Click **Start Extraction** and choose **Run on your device**.
6. Once the run finishes, click **Export Data** and select **Excel (.xlsx)**.

## 💾 Output Sample
The extracted data will populate an Excel sheet structured like this:


| Quote | Author | Tags |
| :--- | :--- | :--- |
| “The world as we have created it is a process of our thinking...” | Albert Einstein | change, deep-thoughts, thinking |
| “It is our choices, Harry, that show what we truly are...” | J.K. Rowling | abilities, choices |

## ⚖️ Compliance & Ethics
- **Target Policy:** This project targets `://toscrape.com`, which is a sandbox website explicitly built for practicing web scraping techniques.
- **Rate Limiting:** Execution settings in Octoparse include built-in random wait times between page loads to mimic human browsing behavior.
- **Disclaimer:** This project is strictly for educational and training purposes. 

## 📝 License
This project is licensed under the [MIT License](LICENSE).   

GITHUB repo... link 
https://github.com/harshalnsk1234-maker/CodeAlpha_ProjectName.git
