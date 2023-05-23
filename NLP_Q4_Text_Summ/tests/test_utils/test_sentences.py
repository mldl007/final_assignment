import pytest
from utils.sentences import get_sents
import spacy
import os


@pytest.fixture()
def nlp():
    nlp = spacy.load(os.path.join(".", "en_core_web_sm-3.4.1"))
    return nlp


def test_tokenizer_valid_input(nlp):
    input_str = "hello world. How are you?"
    actual = get_sents(input_str, nlp)
    expected = ['hello world.', 'How are you?']
    assert actual == expected


def test_tokenizer_single_sent(nlp):
    input_str = "hello world."
    actual = get_sents(input_str, nlp)
    expected = ['hello world.']
    assert actual == expected


def test_tokenizer_single_punct(nlp):
    input_str = "."
    actual = get_sents(input_str, nlp)
    expected = ['.']
    assert actual == expected


def test_tokenizer_multiple_punct(nlp):
    input_str = ".,,."
    actual = get_sents(input_str, nlp)
    expected = [".,,."]
    assert actual == expected


def test_tokenizer_empty_input(nlp):
    input_str = ""
    actual = get_sents(input_str, nlp)
    expected = []
    assert actual == expected
