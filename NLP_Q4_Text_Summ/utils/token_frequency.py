import pandas as pd


def get_token_freq(tokens: list) -> pd.Series:
    """
    Returns counts of tokens from input token list.
    :param tokens: list, token list
    :return: pd.Series, token counts
    """
    freq = None
    if len(tokens) > 0:
        freq = pd.Series(tokens).value_counts()
    return freq
