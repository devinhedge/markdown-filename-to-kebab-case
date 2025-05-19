"""
Test for converting special characters and symbols in a string to readable, ASCII-safe equivalents for use in filenames.
"""

from src import convert_to_kebab_case

def test_ampersand_to_and():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('AT&T') == 'ATandT'
    assert convert('R&D') == 'RandD'
    assert convert('Fish & Chips') == 'Fish and Chips'

def test_accented_characters():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('Café') == 'Cafe'
    assert convert('naïve') == 'naive'
    assert convert('façade') == 'facade'
    assert convert('résumé') == 'resume'

def test_mixed_special_characters():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('Café & Bar') == 'Cafe and Bar'
    assert convert('Crème brûlée & Co.') == 'Creme brulee and Co.'

def test_no_special_characters():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('simplefilename') == 'simplefilename'
    assert convert('foo_bar') == 'foo_bar'
"""
Test for converting special characters and symbols in a string to readable, ASCII-safe equivalents for use in filenames.
"""

from src import convert_to_kebab_case

def test_ampersand_to_and():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('AT&T') == 'ATandT'
    assert convert('R&D') == 'RandD'
    assert convert('Fish & Chips') == 'Fish and Chips'

def test_accented_characters():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('Café') == 'Cafe'
    assert convert('naïve') == 'naive'
    assert convert('façade') == 'facade'
    assert convert('résumé') == 'resume'

def test_mixed_special_characters():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('Café & Bar') == 'Cafe and Bar'
    assert convert('Crème brûlée & Co.') == 'Creme brulee and Co.'

def test_no_special_characters():
    convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
    assert convert('simplefilename') == 'simplefilename'
    assert convert('foo_bar') == 'foo_bar'
