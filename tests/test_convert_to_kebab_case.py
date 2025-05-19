import unittest
import tempfile
import shutil
import os
from pathlib import Path
from src import convert_to_kebab_case

class TestMarkdownRenamerHelpers(unittest.TestCase):
    def test_intelligently_convert_special_characters(self):
        convert = convert_to_kebab_case.MarkdownRenamer.intelligently_convert_special_characters
        self.assertEqual(convert('Café & Bar'), 'Cafe and Bar')
        self.assertEqual(convert('AT&T'), 'ATandT')
        self.assertEqual(convert('rock-n-roll'), 'rock-n-roll')
        self.assertEqual(convert('foo_bar'), 'foo_bar')

    def test_remove_invalid_filename_characters(self):
        remove = convert_to_kebab_case.MarkdownRenamer.remove_invalid_filename_characters
        self.assertEqual(remove('file:name*with?invalid|chars'), 'filenamewithinvalidchars')
        self.assertEqual(remove('good-file_name'), 'good-file_name')

    def test_convert_string_to_kebab_case(self):
        kebab = convert_to_kebab_case.MarkdownRenamer.convert_string_to_kebab_case
        self.assertEqual(kebab('Hello World!'), 'hello-world')
        self.assertEqual(kebab('  Multiple   Spaces  '), 'multiple-spaces')
        self.assertEqual(kebab('snake_case_name'), 'snake-case-name')
        self.assertEqual(kebab('Already-Kebab-Case'), 'already-kebab-case')
        self.assertEqual(kebab('UPPERCASE'), 'uppercase')
        self.assertEqual(kebab(''), '')

    def test_extract_first_h1_header_from_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / 'test.md'
            # With frontmatter and H1
            content = """---
title: Something
---
# My Title\nSome text\n"""
            file_path.write_text(content, encoding='utf-8')
            h1 = convert_to_kebab_case.MarkdownRenamer.extract_first_h1_header_from_file(str(file_path))
            self.assertEqual(h1, 'My Title')
            # No frontmatter, H1 present
            file_path.write_text("# Another Title\nBody", encoding='utf-8')
            h1 = convert_to_kebab_case.MarkdownRenamer.extract_first_h1_header_from_file(str(file_path))
            self.assertEqual(h1, 'Another Title')
            # No H1
            file_path.write_text("No header here", encoding='utf-8')
            h1 = convert_to_kebab_case.MarkdownRenamer.extract_first_h1_header_from_file(str(file_path))
            self.assertEqual(h1, '')

class TestDirectoryValidation(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
    def tearDown(self):
        shutil.rmtree(self.tmpdir)
    def test_valid_directory(self):
        # Simulate user confirmation 'Y' via monkeypatching input
        def fake_input(prompt):
            return 'Y'
        orig_input = convert_to_kebab_case.input
        convert_to_kebab_case.input = fake_input
        try:
            result = convert_to_kebab_case.get_valid_directory_path_from_user(self.tmpdir)
            self.assertEqual(result, self.tmpdir)
        finally:
            convert_to_kebab_case.input = orig_input
    def test_quit_on_prompt(self):
        def fake_input(prompt):
            return 'quit'
        orig_input = convert_to_kebab_case.input
        convert_to_kebab_case.input = fake_input
        try:
            result = convert_to_kebab_case.get_valid_directory_path_from_user(None)
            self.assertIsNone(result)
        finally:
            convert_to_kebab_case.input = orig_input

class TestMarkdownFileRenaming(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
    def tearDown(self):
        shutil.rmtree(self.tmpdir)
    def test_rename_markdown_files_to_kebab_case(self):
        # Create a markdown file with a bad name and H1
        bad_name = 'My File (Draft)!.md'
        good_h1 = '# This is a Test Title\nBody'
        file_path = Path(self.tmpdir) / bad_name
        file_path.write_text(good_h1, encoding='utf-8')
        # Simulate always overwrite
        def fake_prompt_user(msg, choices):
            return 'O'
        orig_prompt_user = convert_to_kebab_case.MarkdownRenamer.prompt_user
        convert_to_kebab_case.MarkdownRenamer.prompt_user = staticmethod(fake_prompt_user)
        try:
            renamer = convert_to_kebab_case.MarkdownRenamer(self.tmpdir)
            renamer.rename_markdown_files_to_kebab_case()
            expected = Path(self.tmpdir) / 'this-is-a-test-title.md'
            self.assertTrue(expected.exists())
            self.assertFalse(file_path.exists())
        finally:
            convert_to_kebab_case.MarkdownRenamer.prompt_user = orig_prompt_user

if __name__ == "__main__":
    unittest.main()
