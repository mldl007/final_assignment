from utils.sentence_dictionary import get_sent_dict
import numpy as np


def summarize_text(doc: str, nlp, factor: float = 1.2) -> str:
    """
    Returns summarized doc/text.
    :param doc: str, text to be summarized.
    :param factor: float, a multiple that controls the length of summarized text.
                   Higher the value shorter the text and inverse holds true.
    :param nlp: Spacy nlp object.
    :return: str, summarized text
    """
    sent_dict = get_sent_dict(doc, nlp=nlp)
    mean_sent_scores = np.mean([*sent_dict.values()])
    summarized_txt = " ".join([sent for sent, freq in sent_dict.items() if freq > (factor * mean_sent_scores)])
    summarized_txt = summarized_txt.replace("\n", "")
    summarized_txt = summarized_txt.replace("\t", "")
    summarized_txt = summarized_txt.replace("\r", "")
    return summarized_txt
