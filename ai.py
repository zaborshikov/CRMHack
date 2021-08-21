from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import dotn
def analyze(messages):
    tokenizer = RegexTokenizer()

    sentiments = []

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(messages, k=1)

    for message, sentiment in zip(messages, results):
        sentiments.append(sentiment)
    try:
        pos = sentiments[0]['positive']
        self.db.setPos(nnID, pos)
    except Exception as e:
        print(e, 22)
        pos = 0
        self.db.setPos(nnID, pos)
    try:
        neg = sentiments[0]['negative']
        self.db.setNegative(nnID, neg)
    except Exception as e:
        print(e, 29)
        neg = 0
        self.db.setNegative(nnID, neg)