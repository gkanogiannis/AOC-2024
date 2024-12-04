import requests
from bs4 import BeautifulSoup
import re

def scrape_languages():
    urls = [
        "https://en.wikipedia.org/wiki/List_of_programming_languages"
    ]
    
    all_languages = set()

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            if "wikipedia.org" in url:
                list_items = soup.select(".div-col ul li a")
                for item in list_items:
                    language = item.text.strip()
                    if language:
                        all_languages.add(language)
            
            elif "wikibooks.org" in url:
                list_items = soup.select("#mw-content-text ul li a")
                for item in list_items:
                    language = item.text.strip()
                    if language:
                        all_languages.add(language)
            
            elif "rosettacode.org" in url:
                list_items = soup.select(".mw-category li a")
                for item in list_items:
                    language = item.text.strip()
                    if language:
                        all_languages.add(language)
        else:
            print(f"Failed to fetch data from {url}")

    return all_languages

def remove_nested_parentheses(text):
    while "(" in text and ")" in text:
        text = re.sub(r'\([^()]*\)', '', text)

def consolidate_languages(languages):
    redundancy_phrases = [
        "programming", "language", "cookbook", "from scratch",
        "development", "foundation", "tutorial", "toolkit",
        "guide", "framework", "reference", "manual", "introduction", "intro", "introducing"
    ]

    normalized = {}
    for lang in languages:
        base = remove_nested_parentheses(lang)

        for phrase in redundancy_phrases:
            base = re.sub(rf"\b{phrase}\b", "", base, flags=re.IGNORECASE)

        base = re.sub(r"\s+", " ", base).strip()

        if base not in normalized or len(lang) < len(normalized[base]):
            normalized[base] = lang

    return sorted(normalized.keys())

if __name__ == "__main__":
    raw_languages = scrape_languages()
    print(f"Extracted {len(raw_languages)} raw programming language entries.")

    consolidated_languages = consolidate_languages(raw_languages)
    print(f"Consolidated to {len(consolidated_languages)} unique programming languages.")

    with open("languages_consolidated.txt", "w", encoding="utf-8") as file:
        for lang in consolidated_languages:
            file.write(lang + "\n")
    
    print("Consolidated languages saved to 'languages_consolidated.txt'.")