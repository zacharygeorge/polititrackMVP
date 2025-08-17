from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Example headline or article text
text = "President Trump on Saturday split from Ukraine and key European allies after his summit with President Vladimir V. Putin of Russia, backing Mr. Putin’s plan for a sweeping peace agreement based on Ukraine ceding territory it controls to Russia, instead of the urgent cease-fire Mr. Trump had said he wanted before the meeting. Skipping cease-fire discussions would give Russia an advantage in the talks, which are expected to continue on Monday when President Volodymyr Zelensky of Ukraine visits Mr. Trump at the White House. It breaks from a strategy Mr. Trump and European allies, as well as Mr. Zelensky, had agreed to before the U.S.-Russia summit in Alaska."

# TEXTBLOB Analysis
blob = TextBlob(text)
print("TextBlob Analysis:")
print(f" - Subjectivity: {blob.sentiment.subjectivity:.2f}")  # 0.0 (objective) to 1.0 (subjective)
print(f" - Polarity: {blob.sentiment.polarity:.2f}")          # -1.0 (negative) to 1.0 (positive)

# VADER Analysis
analyzer = SentimentIntensityAnalyzer()
vader_scores = analyzer.polarity_scores(text)
print("\nVADER Analysis:")
print(f" - Compound Score: {vader_scores['compound']:.2f}")    # -1.0 to 1.0
print(f" - Pos: {vader_scores['pos']:.2f}, Neu: {vader_scores['neu']:.2f}, Neg: {vader_scores['neg']:.2f}")