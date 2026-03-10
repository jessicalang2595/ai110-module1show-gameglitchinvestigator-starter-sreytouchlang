from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


def test_get_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_get_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_valid():
    ok, value, err = parse_guess("25")
    assert ok is True
    assert value == 25
    assert err is None


def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a valid whole number."


def test_check_guess_win():
    outcome, message = check_guess(10, 10)
    assert outcome == "Win"
    assert "Correct" in message


def test_check_guess_high():
    outcome, message = check_guess(15, 10)
    assert outcome == "Too High"
    assert "lower" in message.lower()


def test_check_guess_low():
    outcome, message = check_guess(5, 10)
    assert outcome == "Too Low"
    assert "higher" in message.lower()


def test_update_score_win():
    assert update_score(0, "Win", 1) == 100


def test_update_score_wrong_guess():
    assert update_score(20, "Too Low", 2) == 15