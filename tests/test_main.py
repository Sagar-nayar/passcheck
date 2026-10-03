from passcheck.main import get_feedback, get_rating, score_password


def test_empty_password_scores_zero():
    assert score_password("") == 0


def test_only_lowercase():
    assert score_password("abc") == 1


def test_length_8_lowercase_digit():
    assert score_password("abcdefg1") == 3


def test_everything():
    assert score_password("Abcdefghij1!") == 6


def test_ratings():
    assert get_rating(0) == "Weak"
    assert get_rating(2) == "Weak"
    assert get_rating(3) == "Medium"
    assert get_rating(4) == "Medium"
    assert get_rating(5) == "Strong"
    assert get_rating(6) == "Strong"


def test_strong_password_has_no_feedback():
    assert get_feedback("Abcdefghij1!") == []


def test_weak_password_gets_feedback():
    assert len(get_feedback("abc")) > 0
