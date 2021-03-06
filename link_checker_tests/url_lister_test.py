import os
from link_checker.UrlLister import UrlLister


test_data = "test_data"


def test_init():
    assert len(UrlLister().links) == 0


def test_parsing():
    test_parser = "valid_html.html"
    path = os.path.join(os.path.dirname(__file__), test_data, test_parser)
    with open(path) as f:
        html = f.read()
        parser = UrlLister()
        parser.parse(html)
        assert len(parser.links) == 5


def test_empty_link():
    html = r"<a><\a>"
    parser = UrlLister()
    parser.parse(html)
    assert len(parser.links) == 0