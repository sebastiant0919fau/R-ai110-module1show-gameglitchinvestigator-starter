from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_messages_point_toward_secret():
    # A guess above the secret should tell the player to go lower, and vice versa
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_numeric_comparison_not_string():
    # 9 < 10 numerically even though "9" > "10" as strings
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_parse_guess_valid_and_invalid():
    assert parse_guess("42") == (True, 42, None)
    assert parse_guess(" 7 ") == (True, 7, None)
    assert parse_guess("")[0] is False
    assert parse_guess("abc")[0] is False
    assert parse_guess("3.5")[0] is False

def test_first_try_win_scores_100():
    assert update_score(0, "Win", 1) == 100

def test_wrong_guess_always_costs_points():
    assert update_score(20, "Too High", 2) == 15
    assert update_score(20, "Too Low", 3) == 15
