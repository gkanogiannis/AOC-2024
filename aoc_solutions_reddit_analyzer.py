import praw
import re
import sys
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

def extract_languages(comments):
    language_pattern = re.compile(r"\[LANGUAGE:\s*(\w+)\]", re.IGNORECASE)
    languages = []
    for comment in comments:
        matches = language_pattern.findall(comment.body)
        languages.extend(matches)
    return languages

def plot_and_save_histogram(language_counts, text_file, pdf_file, day_number):
    sorted_languages = sorted(language_counts.items(), key=lambda x: (-x[1], x[0]))
    languages, counts = zip(*sorted_languages)
    
    with open(text_file, "w") as file:
        for language, count in sorted_languages:
            file.write(f"{language}: {count}\n")
    
    plt.figure(figsize=(12, 6))
    plt.bar(languages, counts)
    plt.xlabel('Programming Languages', fontsize=10)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Histogram of Programming Languages Used in day-%s' % (day_number), fontsize=14)
    plt.xticks(rotation=45, fontsize=6)
    plt.tight_layout()
    
    plt.savefig(pdf_file)
    plt.show()

def read_credentials(file_path):
    df = pd.read_csv(file_path, delim_whitespace=True)
    return df.iloc[0]['client_id'], df.iloc[0]['client_secret']

def main():
    if len(sys.argv) < 4:
        print("Usage: python aoc_language_histogram.py <reddit_thread_url> <day_number> <credentials_file>")
        return

    thread_url = sys.argv[1]
    day_number = sys.argv[2]
    credentials_file = sys.argv[3]

    client_id, client_secret = read_credentials(credentials_file)

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="AoC_Language_Analyzer",
    )

    submission = reddit.submission(url=thread_url)
    submission.comments.replace_more(limit=None)  # Ensure we fetch all comments

    comments = submission.comments.list()
    languages = extract_languages(comments)

    language_counts = Counter(languages)

    text_file = f"language_counts_day_{day_number}.txt"
    pdf_file = f"language_histogram_day_{day_number}.pdf"

    plot_and_save_histogram(language_counts, text_file, pdf_file, day_number)
    print(f"Results saved to {text_file} and {pdf_file}")

if __name__ == "__main__":
    main()