from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
def analyze(messages):
    tokenizer = RegexTokenizer()

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(messages, k=1)

    for message, sentiment in zip(messages, results):
        return(message, '->', sentiment)