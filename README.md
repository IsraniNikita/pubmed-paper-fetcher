# PubMed Paper Fetcher

## 📌 Project Overview
This project is a command-line tool that fetches research papers from the **PubMed API** based on a given query. It extracts key details and filters papers authored by individuals affiliated with pharmaceutical or biotech companies. The results are then saved in a CSV file.

## 📂 Project Structure
```
📦 pubmed_fetcher
 ┣ 📜 pubmed_fetcher.py  # Core script to fetch papers and process data
 ┣ 📜 README.md          # Documentation
 ┣ 📜 pyproject.toml     # Poetry dependency configuration
 ┗ 📜 papers.csv         # Sample output file (generated after running the script)
```

## ⚙️ Installation
### **1️⃣ Prerequisites**
Make sure you have **Python 3.x** and **Poetry** installed.
- [Download Python](https://www.python.org/downloads/)
- [Install Poetry](https://python-poetry.org/docs/#installation)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### **3️⃣ Install Dependencies**
```sh
poetry install
```

## 🚀 Usage
### **Basic Command**
```sh
python pubmed_fetcher.py "cancer research" -f results.csv
```
- Replace `"cancer research"` with your search query.
- Use `-f` to specify the output CSV filename.

### **Enable Debug Mode**
```sh
python pubmed_fetcher.py "cancer research" -f results.csv -d
```
- `-d` or `--debug` prints additional logs for debugging.

## 📜 Output Format
The script saves results as a CSV file with the following columns:
| PubmedID  | Title  | Publication Date | Non-academic Authors | Company Affiliations | Corresponding Author Email |
|-----------|--------|-----------------|----------------------|----------------------|---------------------------|
| 12345678  | Research on X | 2024-01-01 | John Doe | XYZ Pharma | john.doe@xyz.com |

## 🛠️ Tools & Technologies Used
- **Python 3.x** – Programming language
- **Requests** – For API calls
- **Pandas** – To process and save CSV files
- **Argparse** – Command-line argument handling
- **Regex** – To filter non-academic authors
- **Poetry** – Dependency management
- **Git & GitHub** – Version control
- **ChatGPT (LLM)** – Used for guidance in structuring the project

## 📄 References
- [PubMed API Docs](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- [Poetry Documentation](https://python-poetry.org/docs/)

---

## 🤝 Contribution & Support
If you encounter any issues or want to contribute, feel free to open an issue or submit a pull request on GitHub.

🚀 Happy Coding!

