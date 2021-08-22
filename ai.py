from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import db
def analyze(messages, id):
    tokenizer = RegexTokenizer()

    sentiments = []

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(messages, k=1)

    for message, sentiment in zip(messages, results):
        sentiments.append(sentiment)
    try:
        pos = sentiments[0]['positive']
        db.Database.setPos(id, pos)
    except Exception as e:
        print(e)
        pos = 0
        db.Database.setPos(id, pos)
    try:
        neg = sentiments[0]['negative']
        db.Database.setNeg(id, neg)
    except Exception as e:
        print(e)
        neg = 0
        db.Database.setNeg(id, neg)