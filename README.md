# Markdown Filename to Kebab Case

A Python script to intelligently rename markdown files in a directory to human- and machine-friendly kebab-case filenames, based on their H1 titles or original names.

## Features

- Processes `.md`, `.markdown`, and `.mmd` files.
- Extracts the first H1 header (`# ...`) from each file (skipping frontmatter if present) to use as the new filename.
- Converts special characters and symbols to filename-friendly equivalents.
- Removes invalid filename characters for cross-platform compatibility.
- Converts names to kebab-case (lowercase, hyphen-separated).
- Handles extension normalization (`.markdown` → `.md`, `.mmd` preserved).
- Idempotent: skips files already correctly named.
- Handles filename conflicts (prompting to overwrite, append a number, or skip).
- Interactive: prompts for directory selection and conflict resolution.

## Usage

1. Place `convert-to-kebab-case.py` in your target directory or ensure it is accessible in your PATH.
2. Run the script from the command line:

   ```sh
   python convert-to-kebab-case.py [optional/path/to/markdown/files]
   ```

   - If no path is provided, you will be prompted to enter one.
   - The script will validate the directory and ask for confirmation before proceeding.

3. Follow on-screen prompts to resolve any filename conflicts.

## Design Principles

- **Modular, Class-Based Design:** Logic is encapsulated in classes for maintainability and clarity.
- **PEP 8 & Clean Code:** Readable, well-documented, and follows Python best practices.
- **Robust Error Handling:** Gracefully handles invalid input, file system errors, and user cancellations.
- **Extensible:** Helper functions and clear structure make it easy to adapt or extend.

## Example

Before:
```
My Notes.md
2023-Project Plan.markdown
README.mmd
```

After running the script:
```
my-notes.md
project-plan-2023.md
readme.mmd
```

## License

MIT License
