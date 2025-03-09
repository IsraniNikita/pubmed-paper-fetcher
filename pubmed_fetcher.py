import requests
import pandas as pd
import re
import argparse
import logging
from typing import List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO)

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query: str, debug: bool = False) -> List[str]:
    """Fetch research papers from PubMed based on a search query."""
    params = {"db": "pubmed", "term": query, "retmax": 5, "retmode": "json"}

    if debug:
        logging.debug(f"Querying PubMed with parameters: {params}")

    try:
        response = requests.get(PUBMED_API_URL, params=params)
        response.raise_for_status()
        return response.json().get("esearchresult", {}).get("idlist", [])
    except requests.RequestException as e:
        logging.error(f"Error fetching papers: {e}")
        return []

def fetch_paper_details(paper_ids: List[str], debug: bool = False) -> List[Dict]:
    """Retrieve details for given paper IDs."""
    if not paper_ids:
        return []

    params = {"db": "pubmed", "id": ",".join(paper_ids), "retmode": "json"}

    if debug:
        logging.debug(f"Fetching details for paper IDs: {paper_ids}")

    try:
        response = requests.get(DETAILS_API_URL, params=params)
        response.raise_for_status()
        papers = response.json().get("result", {})
        return extract_paper_info(papers, paper_ids)
    except requests.RequestException as e:
        logging.error(f"Error fetching details: {e}")
        return []

def extract_paper_info(papers: Dict, paper_ids: List[str]) -> List[Dict]:
    """Extract required details from PubMed API response."""
    extracted = []
    for paper_id in paper_ids:
        paper = papers.get(paper_id, {})
        title = paper.get("title", "N/A")
        pub_date = paper.get("pubdate", "N/A")
        authors = paper.get("authors", [])

        non_academic_authors, company_affiliations, corresponding_email = [], [], None

        for author in authors:
            name, affiliation = author.get("name", "Unknown"), author.get("affiliation", "")
            if affiliation and not re.search(r"(university|college|lab|institute)", affiliation, re.I):
                non_academic_authors.append(name)
                company_affiliations.append(affiliation)
            if "email" in author:
                corresponding_email = author["email"]

        extracted.append({
            "PubmedID": paper_id, "Title": title, "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors) or "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) or "N/A",
            "Corresponding Author Email": corresponding_email or "N/A"
        })
    return extracted

def save_to_csv(papers: List[Dict], filename: str = "papers.csv"):
    """Save extracted data to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    logging.info(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, default="papers.csv", help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    paper_ids = fetch_pubmed_papers(args.query, args.debug)
    paper_details = fetch_paper_details(paper_ids, args.debug)

    if paper_details:
        save_to_csv(paper_details, args.file)
    else:
        logging.warning("No papers found.")

if __name__ == "__main__":
    main()
