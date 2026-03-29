import pytest
from Translator_Test import translate

def test_returns_string():
    result = translate("Hello", "French")
    assert isinstance(result, str)

def test_not_empty():
    result = translate("Hello", "French")
    assert len(result) > 0

def test_not_same_as_input():
    result = translate("Hello", "French")
    assert result.lower() != "hello"