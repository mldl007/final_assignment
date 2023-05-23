
def get_sents(doc: str, nlp) -> list:
    """
    Returns a ist of sentences form input doc/text.
    :param doc: str, document
    :param nlp: Spacy NLP object
    :return: list, sentences
    """
    nlp_doc = nlp(doc)
    sents = []
    if len(nlp_doc) > 0:
        sents = [str(s) for s in nlp_doc.sents]
    return sents
