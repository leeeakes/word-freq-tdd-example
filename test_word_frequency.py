import word_frequency as wfreq

def test_empty_string():
    assert wfreq.word_frequency("") == {}

def test_one_word_string():
    assert wfreq.word_frequency("booth") == {"booth": 1}

def test_multiple_word_string():
    assert wfreq.word_frequency("booth is a booth") == {"booth": 2,
                                                        "is": 1,
                                                        "a": 1}

def test_string_with_capitalization():
    text = "Doctor Moreau made a beagle"
    expected = {"doctor": 1,
                "moreau": 1,
                "made": 1,
                "a": 1,
                "beagle": 1}
    assert wfreq.word_frequency(text) == expected

def test_string_with_simple_punctuation():
    text = "Doctor Moreau made a beagle, but not before he made a man."
    freq = wfreq.word_frequency(text)

    assert freq.get("man") == 1
    assert freq.get("beagle") == 1
