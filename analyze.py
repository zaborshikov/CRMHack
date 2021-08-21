from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
def analyze(messages):
    tokenizer = RegexTokenizer()
    tokens = tokenizer.split('всё очень плохо')  # [('всё', None), ('очень', None), ('плохо', None)]

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    messages = []

    results = model.predict(messages, k=2)

    for message, sentiment in zip(messages, results):
        return(message, '->', sentiment)