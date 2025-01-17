from markdownify import MarkdownConverter
from bs4 import BeautifulSoup


class UnitTestConverter(MarkdownConverter):
    """
    Create a custom MarkdownConverter for unit tests
    """
    def convert_img(self, el, text, convert_as_inline):
        """Add two newlines after an image"""
        return super().convert_img(el, text, convert_as_inline) + '\n\n'

    def convert_custom_tag(self, el, text, convert_as_inline):
        """Ensure conversion function is found for tags with special characters in name"""
        return "FUNCTION USED: %s" % text


def test_custom_conversion_functions():
    # Create shorthand method for conversion
    def md(html, **options):
        return UnitTestConverter(**options).convert(html)

    assert md('<img src="/path/to/img.jpg" alt="Alt text" title="Optional title" />') == '![Alt text](/path/to/img.jpg "Optional title")\n\n'
    assert md('<img src="/path/to/img.jpg" alt="Alt text" />') == '![Alt text](/path/to/img.jpg)\n\n'

    assert md("<custom-tag>text</custom-tag>") == "FUNCTION USED: text"


def test_soup():
    html = '<b>test</b>'
    soup = BeautifulSoup(html, 'html.parser')
    assert MarkdownConverter().convert_soup(soup) == '**test**'
