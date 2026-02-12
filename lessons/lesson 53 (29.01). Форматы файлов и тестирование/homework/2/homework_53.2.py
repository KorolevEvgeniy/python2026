import pytest


def count_punct_marks(string: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Функция ожидает строку в качестве аргумента")

    text_lower = text.lower()
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = sum(1 for char in text_lower if char in vowels)
    
    return count

    total_count = 0
    for sym in "a, e, i, o. u":
        total_count += string.count(sym)
    return total_count


def test_empty_string():
   assert count_punct_marks("") == 0

def test_no_punctuation():
    assert count_punct_marks("Hello World") == 0

def test_single_punctuation():
    assert count_punct_marks("Hello World!") == 1

def test_multiple_punctuation():
    assert count_punct_marks("Hello, World! How are you?") == 3

def test_edge_case():
    assert count_punct_marks("!!!") == 3

def test_all_punctuation():
    assert count_punct_marks(".,:;!?") == 6