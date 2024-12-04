import re
import sys
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def load_language_reference(file_path):
    reference = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = [part.strip() for part in line.split(',')]
                primary_language = parts[0]
                synonyms = parts[1:]
                for synonym in synonyms:
                    reference[synonym.lower()] = primary_language
                reference[primary_language.lower()] = primary_language
        return reference
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def normalize_entry(entry):
    entry = re.sub(r'\(.*?\)', '', entry).strip()

    critical_symbols = {"+", "#", "-", "."}
    normalized = ''.join(char if char.isalnum() or char in critical_symbols else ' ' for char in entry)

    normalized = re.sub(r'\s+', ' ', normalized).strip()

    normalized = re.sub(r'\s+\d+$', '', normalized)

    return normalized

def preprocess_language(language):
    language = re.sub(r'(\+\+|\#|\b)[\d]+', r'\1', language).strip()
    
    language = re.sub(r'\s+', ' ', language)
    return language

def extract_languages_from_raw_html(html_file, language_reference, unknown_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        raw_text = file.read()

    language_pattern = re.compile(r"\[LANGUAGE:\s*([^\]]+)\]", re.IGNORECASE)
    languages = language_pattern.findall(raw_text)

    escaped_reference = {re.escape(key): value for key, value in language_reference.items()}

    normalized_languages = []
    unknown_languages = []

    for language in languages:
        match_found = False

        candidates = re.split(r'[\/,\-&\s]', language)
        for candidate in candidates:
            candidate = preprocess_language(candidate.strip())
            normalized_candidate = normalize_entry(candidate)

            for ref_language, primary in escaped_reference.items():
                if re.fullmatch(ref_language, normalized_candidate, re.IGNORECASE):
                    normalized_languages.append(primary)
                    match_found = True
                    break

        if not match_found:
            normalized_languages.append("Unknown")
            unknown_languages.append(language)

    with open(unknown_file, 'w', encoding='utf-8') as file:
        for unknown in set(unknown_languages):
            file.write(f"{unknown}\n")

    print(f"Saved {len(set(unknown_languages))} unknown entries to '{unknown_file}'.")

    return normalized_languages

def plot_and_save_histogram(language_counts, text_file, pdf_file, day_number):
    sorted_languages = sorted(language_counts.items(), key=lambda x: (-x[1], x[0]))
    languages, counts = zip(*sorted_languages)

    with open(text_file, "w") as file:
        for language, count in sorted_languages:
            file.write(f"{language}: {count}\n")

    num_bars = len(languages)
    colors = cm.coolwarm(np.linspace(0, 1, num_bars))[::-1]

    plt.figure(figsize=(16, 9))
    bars = plt.bar(languages, counts, color=colors, edgecolor='black', linewidth=0.7)

    for bar, count in zip(bars, counts):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(count),
            ha='center',
            va='bottom',
            fontsize=8,
            color='black'
        )

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.xticks(rotation=45, fontsize=8, ha='right')
    plt.yticks(fontsize=10)
    plt.xlabel("Programming Languages", fontsize=12, labelpad=10)
    plt.ylabel("Frequency", fontsize=12, labelpad=10)
    plt.title(f"Programming Languages Used (Day-{day_number})", fontsize=16, pad=20)

    plt.tight_layout()

    plt.savefig(pdf_file, dpi=600, bbox_inches='tight')
    plt.show()


def main():
    if len(sys.argv) < 4:
        print("Usage: python reddit_language_histogram_raw.py <html_file> <language_file> <day_number>")
        return

    html_file = sys.argv[1]
    language_file = sys.argv[2]
    day_number = sys.argv[3]

    language_reference = load_language_reference(language_file)

    unknown_file = f"unknown_languages_day_{day_number}.txt"

    languages = extract_languages_from_raw_html(html_file, language_reference, unknown_file)
    language_counts = Counter(languages)

    text_file = f"language_counts_day_{day_number}.txt"
    pdf_file = f"language_histogram_day_{day_number}.pdf"

    plot_and_save_histogram(language_counts, text_file, pdf_file, day_number)
    print(f"Results saved to {text_file} and {pdf_file}")


if __name__ == "__main__":
    main()