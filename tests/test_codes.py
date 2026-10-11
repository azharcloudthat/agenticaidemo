from app import describe_code


def test_describe_code_returns_overcast():
    assert describe_code(3) == "Overcast"
