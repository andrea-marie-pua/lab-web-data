# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt

tweets = []

for year in range(2009, 2019):
    filename = f"master_{year}.json"

    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
        tweets.extend(data)

total = len(tweets)

print("Total tweets:", total)


phrases = [
    "obama",
    "trump",
    "mexico",
    "russia",
    "fake news",
    "wall",
    "freedom",
    "maga"
]

counts = {}

for phrase in phrases:
    count = 0

    for tweet in tweets:
        message = tweet.get("full_text") or tweet.get("text") or ""
        message = message.lower()

        if phrase.lower() in message:
            count += 1

    counts[phrase] = count

for phrase in phrases:
    print(phrase, counts[phrase])

percentages = {}

for phrase in phrases:
    percentages[phrase] = counts[phrase] / total * 100

for phrase in phrases:
    print(phrase, f"{percentages[phrase]:.2f}%")

print()
print("| phrase            | percent of tweets |")
print("| ----------------- | ----------------- |")

for phrase in sorted(phrases):
    percentage = percentages[phrase]
    print(f"| {phrase:>17} | {percentage:05.2f}             |")

plt.figure(figsize=(10, 6))

chart_phrases = sorted(phrases)
chart_counts = [counts[phrase] for phrase in chart_phrases]

plt.barh(chart_phrases, chart_counts, color="lightpink")

plt.xlabel("Number of Tweets")
plt.ylabel("Phrase")
plt.title("Phrase Frequency in Trump's Tweets (2009–2018)")

plt.tight_layout()
plt.savefig("tweets.png")
plt.close()