
def get_tokens(doc: str, nlp) -> list:
    """
    Returns a list of tokens from a given doc/text.
    :param doc: str, document
    :param nlp: Spacy NLP object
    :return: list, tokens
    """
    tokens = []
    nlp_doc = nlp(doc)
    if len(nlp_doc) > 1:
        for i in nlp_doc:
            if (not i.is_stop) and (not i.is_bracket) and (not i.is_currency) and (not i.is_digit) and \
                    (not i.is_punct) and (not i.is_quote):
                tokens.append(i.text.lower().strip())
    elif len(nlp_doc) == 1:
        tokens = [doc.lower()]
    else:
        pass
    return tokens
