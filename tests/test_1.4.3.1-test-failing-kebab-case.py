# ...existing code from 1.4.3.1-test-failing-kebab-case.py...
"""
Test for kebab-case conversion function.

Covers:
- Lowercasing
- Replacing spaces, underscores, and non-alphanumeric characters with hyphens
- Collapsing multiple hyphens
- Trimming leading/trailing hyphens
- Edge cases (empty string, already kebab-case, strings with only invalid characters)
"""

from src import convert_to_kebab_case

def test_basic_conversion():
    kebab = convert_to_kebab_case.MarkdownRenamer.convert_string_to_kebab_case
    assert kebab('Hello World!') == 'hello-world'
    assert kebab('snake_case_name') == 'snake-case-name'
    assert kebab('Already-Kebab-Case') == 'already-kebab-case'
    assert kebab('  Multiple   Spaces  ') == 'multiple-spaces'
    assert kebab('UPPERCASE') == 'uppercase'

def test_edge_cases():
    kebab = convert_to_kebab_case.MarkdownRenamer.convert_string_to_kebab_case
    assert kebab('') == ''
    assert kebab('---') == ''
    assert kebab('___') == ''
    assert kebab('   ') == ''
    assert kebab('foo--bar') == 'foo-bar'
    assert kebab('foo__bar') == 'foo-bar'
    assert kebab('foo   bar') == 'foo-bar'
    assert kebab('foo_bar-baz') == 'foo-bar-baz'

def test_only_invalid_characters():
    kebab = convert_to_kebab_case.MarkdownRenamer.convert_string_to_kebab_case
    assert kebab('***') == ''
