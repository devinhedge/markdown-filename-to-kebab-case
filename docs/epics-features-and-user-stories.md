# Numbered List of Epics, Features, and User Stories

## 1 - Automate the renaming of markdown files to human- and machine-friendly kebab-case filenames

### 1.1 - Select and validate the target directory
- 1.1.1 - Provide a directory path (via command-line or prompt) so that the script can process my markdown files

### 1.2 - Identify and process all relevant markdown files
- 1.2.1 - Find all `.md`, `.markdown`, and `.mmd` files in the directory so that all my markdown files are considered

### 1.3 - Generate new filenames based on the H1 header or fallback to the original filename
- 1.3.1 - Extract the first H1 header (skipping frontmatter) to use as the new filename so that the filename matches the document title

### 1.4 - Intelligently convert and clean filenames
- 1.4.1 - Special characters and symbols in the filename are converted to readable equivalents
- 1.4.2 - Invalid filename characters are removed so that the filename is valid on all major operating systems
- 1.4.3 - The filename is converted to kebab-case so that it is consistent and easy to use

### 1.5 - Handle file extensions and conflicts
- 1.5.1 - `.md` and `.markdown` files are renamed with a `.md` extension, and `.mmd` files keep their extension
- 1.5.2 - The script skips files that are already correctly named
- 1.5.3 - Prompt to resolve filename conflicts (overwrite, append a number, or skip)

### 1.6 - Be robust, interactive, and Pythonic
- 1.6.1 - The script handles errors gracefully and provides clear messages
- 1.6.2 - The script is modular, class-based, and follows Python best practices