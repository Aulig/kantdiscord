from utils.text_utils import split_text


def test_basic():

    assert split_text("deez|nuts") == ("deez", "nuts")
    assert split_text("deez nuts") == ("deez", "nuts")

    assert split_text("i like deez nuts") == ("i like", "deez nuts")


def test_edge_cases():
    assert split_text("nospaceshere!") == ("nospaceshere!", "")
    assert split_text("abc|") == ("abc", "")
    assert split_text("|mongus") == ("", "mongus")


