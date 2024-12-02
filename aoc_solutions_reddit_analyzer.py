import praw
import re
from collections import Counter
import matplotlib.pyplot as plt

# Function to extract languages from comments
def extract_languages(comments):
    language_pattern = re.compile(r"\[LANGUAGE:\s*(\w+)\]", re.IGNORECASE)
    languages = []
    for comment in comments:
        matches = language_pattern.findall(comment.body)
        languages.extend(matches)
    return languages

def plot_histogram(language_counts):
    # Plot histogram
    languages, counts = zip(*language_counts.items())
    plt.bar(languages, counts)
    plt.xlabel('Programming Languages')
    plt.ylabel('Frequency')
    plt.title('Histogram of Programming Languages Used')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Set up Reddit API
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",  # Replace with your Reddit API client ID
        client_secret="YOUR_CLIENT_SECRET",  # Replace with your Reddit API client secret
        user_agent="AoC_Language_Analyzer",
    )

    # Fetch Reddit thread
    url = "https://www.reddit.com/r/adventofcode/comments/1h3vp6n/2024_day_1_solutions/"
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=None)  # Ensure we fetch all comments

    # Extract languages from comments
    comments = submission.comments.list()
    languages = extract_languages(comments)

    # Count occurrences of each language
    language_counts = Counter(languages)

    # Print and plot histogram
    print("Language Frequency:", language_counts)
    plot_histogram(language_counts)

if __name__ == "__main__":
    main()