from utils.tokenizer import get_tokens
from utils.token_frequency import get_token_freq
from utils.sentences import get_sents


def get_sent_dict(doc: str, nlp) -> dict:
    """
    Returns dictionary of sentences with the cumulative frequency of tokens as values
    :param doc: string, input doc/text
    :param nlp: Spacy NLP object
    :return: dict, dictionary of sentences with the cumulative frequency of tokens as values
    """
    sents = get_sents(doc, nlp=nlp)
    sent_dict = dict()
    if len(sents) > 0:
        tokens = get_tokens(doc, nlp=nlp)
        token_freq = get_token_freq(tokens)
        sent_dict = {}
        for sent in sents:
            for token, freq in token_freq.items():
                if sent.lower().find(token.lower()) != -1:
                    if sent_dict.get(sent) is not None:
                        sent_dict[sent] += freq
                    else:
                        sent_dict[sent] = freq
    return sent_dict
