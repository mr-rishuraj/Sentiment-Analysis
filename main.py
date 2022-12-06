from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

vs = SentimentIntensityAnalyzer()

text = input("Enter you text: ")
print(vs.polarity_scores(text))
