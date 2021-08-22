from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import db
def analyze(messages, id):
    tokenizer = RegexTokenizer()

    sentiments = []

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(messages, k=1)

    for messages, sentiment in zip(messages, results):
        sentiments.append(sentiment)
    # try:
    if 'negative' not in sentiments[0]:
        if 'positive' in sentiments[0]:
            # print(sentiments)
            pos = sentiments[0]['positive']
            db.Database.setPos(id, pos, messages)
            # except Exception as e:
            #     print(e)
            #     pos = 0
            #     db.Database.setPos(id, pos)
            # try:
        else:
            if 'speech' in sentiments[0]:
                neutral = sentiments[0]['speech']
            else:
                neutral = sentiments[0]['neutral']
            db.Database.setNeutral(id, neutral, messages)
    else:
        neg = sentiments[0]['negative']
        db.Database.setNeg(id, neg, messages)
        # except Exception as e:
        #     print(e)
        #     neg = 0
        #     db.Database.setNeg(id, neg)
    return sentiments
if __name__ == "__main__":
    analyze(['вау'], -182637)