from watch import parse


def test_multi_attribute_iframe():
    html = (
        "<iframe "
        'width="560" '
        'height="315" '
        'src="https://www.youtube.com/embed/xvFZjo5PgG0" '
        'title="YouTube video player" '
        'frameborder="0" '
        'allow="accelerometer; '
        "autoplay; "
        "clipboard-write; "
        "encrypted-media; "
        "gyroscope; "
        'picture-in-picture" '
        "allowfullscreen> "
        "</iframe> "
    )
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"


def test_single_attribute_iframe():
    html = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"


def test_single_attribute_iframe_no_www():
    html = '<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"


def test_invalid_url():
    html = "https://cs50.harvard.edu/python/2022/psets/7/watch/"
    assert parse(html) is None
