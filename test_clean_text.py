from word_frequency import clean_text

def test_empty_string():
    assert clean_text("") == ""

def test_clean_string_is_unchanged():
    text = "i am a clean string"
    assert clean_text(text) == text

def test_text_is_lowercased():
    text = "Why Hello THERE"
    assert clean_text(text) == text.lower()

def test_simple_punctuation_is_removed():
    text = "Doctor Moreau made a beagle, but not before he made a man."
    expected = "doctor moreau made a beagle but not before he made a man"

    assert clean_text(text) == expected
