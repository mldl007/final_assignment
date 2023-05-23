from utils.token_frequency import get_token_freq
from utils.tokenizer import get_tokens
import pandas as pd
import spacy
import os
import pytest


@pytest.fixture()
def nlp():
    nlp = spacy.load(os.path.join(".", "en_core_web_sm-3.4.1"))
    return nlp


def test_token_freq_valid_input(nlp):
    input_txt = 'hello world Hello'
    input_tokens = get_tokens(input_txt, nlp)
    actual = get_token_freq(input_tokens)
    expected = pd.Series({"hello": 2, "world": 1})
    assert actual.equals(expected)


def test_token_freq_empty_input(nlp):
    input_txt = ''
    input_tokens = get_tokens(input_txt, nlp)
    actual = get_token_freq(input_tokens)
    expected = None
    assert actual == expected


def test_token_freq_single_input(nlp):
    input_txt = 'Hello'
    input_tokens = get_tokens(input_txt, nlp)
    actual = get_token_freq(input_tokens)
    expected = pd.Series({"hello": 1})
    assert actual.equals(expected)
