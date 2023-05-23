import pytest
from utils.tokenizer import get_tokens
import spacy
import os


@pytest.fixture()
def nlp():
    nlp = spacy.load(os.path.join(".", "en_core_web_sm-3.4.1"))
    return nlp


def test_tokenizer_valid_input(nlp):
    input_str = "hello world"
    actual = get_tokens(input_str, nlp)
    expected = ['hello', 'world']
    assert actual == expected


def test_tokenizer_single_token(nlp):
    input_str = "hello"
    actual = get_tokens(input_str, nlp)
    expected = ['hello']
    assert actual == expected


def test_tokenizer_single_punct(nlp):
    input_str = "."
    actual = get_tokens(input_str, nlp)
    expected = ['.']
    assert actual == expected


def test_tokenizer_multiple_punct(nlp):
    input_str = ".,,."
    actual = get_tokens(input_str, nlp)
    expected = []
    assert actual == expected


def test_tokenizer_empty_input(nlp):
    input_str = ""
    actual = get_tokens(input_str, nlp)
    expected = []
    assert actual == expected
