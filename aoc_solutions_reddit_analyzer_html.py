import re
import sys
from collections import Counter
import matplotlib.pyplot as plt
from adjustText import adjust_text

def extract_languages_from_raw_html(html_file):
    """
    Extract programming languages directly from raw HTML text.
    """
    # Read the raw HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        raw_text = file.read()

    # Regex pattern to find [LANGUAGE: something]
    language_pattern = re.compile(r"\[LANGUAGE:\s*([^<^\]]+)\]", re.IGNORECASE)
    languages = language_pattern.findall(raw_text)

    # Normalize languages: convert to lowercase and extract the base name
    normalized_languages = []
    for language in languages:
        # Convert to lowercase and keep only the first word (base name)
        base_language = language.strip().lower().split()[0]
        normalized_languages.append(base_language)

    return normalized_languages

def plot_and_save_histogram(language_counts, text_file, pdf_file, day_number):
    """
    Plot and save the language frequency histogram with adjusted x-axis labels.
    """
    sorted_languages = sorted(language_counts.items(), key=lambda x: (-x[1], x[0]))
    languages, counts = zip(*sorted_languages)

    with open(text_file, "w") as file:
        for language, count in sorted_languages:
            file.write(f"{language}: {count}\n")

    plt.figure(figsize=(15, 8))
    bars = plt.bar(languages, counts)

    # Add and adjust count labels using adjustText
    texts = []
    for bar, count in zip(bars, counts):
        text = plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(count),
            ha='center',
            va='bottom',
            fontsize=8
        )
        texts.append(text)

    #adjust_text(texts, arrowprops=dict(arrowstyle="->", color='red'))

    plt.xticks(rotation=45, fontsize=8, ha='right')
    plt.xlabel("Programming Languages", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.title(f"Histogram of Programming Languages Used in Day-{day_number}", fontsize=16)
    plt.tight_layout()
    plt.savefig(pdf_file)
    plt.show()

def main():
    if len(sys.argv) < 3:
        print("Usage: python reddit_language_histogram_raw.py <html_file> <day_number>")
        return

    html_file = sys.argv[1]
    day_number = sys.argv[2]

    # Extract languages from raw HTML
    languages = extract_languages_from_raw_html(html_file)
    language_counts = Counter(languages)

    # Save results and plot the histogram
    text_file = f"language_counts_day_{day_number}.txt"
    pdf_file = f"language_histogram_day_{day_number}.pdf"

    plot_and_save_histogram(language_counts, text_file, pdf_file, day_number)
    print(f"Results saved to {text_file} and {pdf_file}")

if __name__ == "__main__":
    main()