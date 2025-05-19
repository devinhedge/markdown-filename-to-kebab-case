--- START OF FILE prompt-rename-markdown-files.prompt.md ---

CONTEXT:
- You are a python programmer
- You have a bunch of horribly named markdown files in a directory
- Each markdown file has an h1 ("#") title in the first few lines
- The markdown file may or may not have frontmatter

GOAL: A directory who's markdown filenames are easily machine and human readable for wiki entries.

TASK: Create a python script named 'convert-to-kebab-case.py' that renames the markdown files in a directory.

## **PSEUDO CODE**:
// NOTE TO LLM: The following pseudocode outlines the core logic and flow.
// Please implement this logic by designing appropriate classes and methods,
// adhering to the principles and structure detailed in the
// "LLM Prompt Guidance: Python Script Generation" section.

// SCRIPT MAIN
  // // Purpose: Main execution flow of the script.

  // 1. Initialize variables.
  // validated_pathname = NULL
  // command_line_args = GET_COMMAND_LINE_ARGUMENTS()
  // initial_path_from_args = NULL

  // 2. Check if a path was provided as a command-line argument.
  // IF command_line_args CONTAINS a path argument THEN
  //   initial_path_from_args = EXTRACT_PATH_FROM_ARGS(command_line_args)
  // END IF

  // 3. Call the function to get a validated directory path from the user.
  //    Pass the initial path from args (which might be NULL).
  // PRINT "Starting directory path validation..."
  // validated_pathname = GET_VALID_DIRECTORY_PATH_FROM_USER(initial_path_from_args)

  // 4. Check the result from the path validation function.
  // IF validated_pathname IS NULL THEN
    // User chose to quit, or no valid path was provided.
    // PRINT "No valid directory path provided or user chose to quit. Exiting program."
    // EXIT_PROGRAM()
  // ELSE
    // A valid directory path was obtained.
    // PRINT "Using directory: '" + validated_pathname + "'"

    // 5. Store the path (Criterion 4 from original request for GET_VALID_DIRECTORY_PATH_FROM_USER)
    //    is implicitly handled as 'validated_pathname' now holds this value.

    // 6. "Reads the contents of the directory matching 'pathname'" (Criterion 5 & parts of 6)
    //    This step is now part of the RENAME_MARKDOWN_FILES_TO_KEBAB_CASE function or
    //    could be a separate check here if desired, though typically the processing function
    //    would handle listing directory contents.
    //    For now, assume RENAME_MARKDOWN_FILES_TO_KEBAB_CASE handles it.

    // 7. Proceed with the main task of the script (e.g., renaming files).
    // PRINT "Starting markdown file renaming process..."
    // CALL RENAME_MARKDOWN_FILES_TO_KEBAB_CASE(validated_pathname)
    //    // RENAME_MARKDOWN_FILES_TO_KEBAB_CASE will handle:
    //    //   - Reading the contents of 'validated_pathname'.
    //    //   - Iterating through files.
    //    //   - Identifying markdown files (.md, .mmd, .markdown).
    //    //   - Extracting H1 header or using filename.
    //    //   - Intelligent character conversion.
    //    //   - Invalid filename character removal.
    //    //   - Kebab-case conversion.
    //    //   - Extension handling (.md/.markdown to .md, .mmd preserved).
    //    //   - Idempotency check.
    //    //   - Conflict resolution (prompt user).
    //    //   - Performing rename with error handling.

    // PRINT "All operations completed."
  // END IF

// END SCRIPT MAIN

// --- Conceptual Helper Functions assumed by the system ---

// FUNCTION GET_COMMAND_LINE_ARGUMENTS ()
  // // Returns a representation of command line arguments.
// END FUNCTION

// FUNCTION EXTRACT_PATH_FROM_ARGS (arguments)
  // // Parses arguments to find and return a path string, if present. Returns NULL if not found.
// END FUNCTION

// FUNCTION PROMPT_USER_FOR_INPUT (message_string)
  // // Displays message_string to the user and returns their typed input as a string. Can return NULL or empty if user provides no input.
// END FUNCTION

// FUNCTION DOES_PATH_EXIST (path_string)
  // // Returns TRUE if path_string points to an existing file system object, FALSE otherwise.
// END FUNCTION

// FUNCTION IS_DIRECTORY (path_string)
  // // Returns TRUE if path_string points to an existing directory, FALSE otherwise.
// END FUNCTION

// FUNCTION PROMPT_USER_FOR_CHOICE (message_string, array_of_valid_choices)
  // // Displays message_string, expects input matching one of the valid_choices (case-insensitive).
  // // Returns the user's choice (e.g., "Y", "1", "Q") or a default/NULL if input is invalid or doesn't match.
// END FUNCTION

// FUNCTION TO_LOWERCASE (input_string)
// END FUNCTION

// FUNCTION TO_UPPERCASE (input_string)
// END FUNCTION

// PROCEDURE EXIT_PROGRAM ()
  // // Terminates the execution of the script/program.
// END PROCEDURE

// FUNCTION RENAME_MARKDOWN_FILES_TO_KEBAB_CASE (directory_path)
  // // (As defined in previous interactions - this is the core file processing logic)
// END FUNCTION

--- Conceptual Directory Validation Function (Comments on their purpose) ---
 
// FUNCTION GET_VALID_DIRECTORY_PATH_FROM_USER (command_line_path_argument)
   // // Purpose: To obtain a valid and user-confirmed directory path.
   // // It optionally takes a path from command line. If no path is provided or if subsequent paths are invalid,
   // // it prompts the user until a valid path is entered and confirmed, or the user chooses to quit.
   // // Returns the validated path string, or NULL if the user quits or fails to provide a valid path.

   // Initialize a variable to hold the path being evaluated.
   // potential_pathname = command_line_path_argument // Use supplied argument, or it will be NULL/empty

   // Start a loop that continues until a valid path is returned or the user opts out.
   // LOOP

     // 1. If no path is currently set (either not provided via command line, or a previous attempt failed/was rejected),
     //    prompt the user to enter one.
     // IF potential_pathname IS NULL OR potential_pathname IS EMPTY OR potential_pathname IS BLANK THEN
     //   potential_pathname = PROMPT_USER_FOR_INPUT("Please enter the target directory path (or type 'quit' to exit): ")
     //   IF TO_LOWERCASE(potential_pathname) EQUALS "quit" THEN
     //       RETURN NULL // User explicitly wants to quit
     //   END IF
     //   IF potential_pathname IS NULL OR potential_pathname IS EMPTY OR potential_pathname IS BLANK THEN
     //       PRINT "No path entered. Please try again or type 'quit' to exit."
     //       CONTINUE LOOP // Go to the next iteration to re-prompt.
     //   END IF
     // END IF

     // 2. Check if the path exists and is a directory.
     // IF DOES_PATH_EXIST(potential_pathname) AND IS_DIRECTORY(potential_pathname) THEN
       // Path seems valid.

       // 3. Confirm the pathname is correct with the user.
       // user_confirmation_choice = PROMPT_USER_FOR_CHOICE("Use directory: '" + potential_pathname + "'? (Y)es, (N)o, (Q)uit: ", ["Y", "N", "Q"])

       // IF TO_UPPERCASE(user_confirmation_choice) EQUALS "Y" THEN
         // Path is valid and confirmed by the user.
         // RETURN potential_pathname // This is the valid 'pathname' to be used.
       // ELSE IF TO_UPPERCASE(user_confirmation_choice) EQUALS "Q" THEN
         // User chose to quit at confirmation.
         // RETURN NULL
       // ELSE // User answered "N" (No) or gave invalid input at confirmation.
         // PRINT "Directory not confirmed. Please specify a different path."
         // potential_pathname = NULL // Clear the path to trigger prompt in the next loop iteration.
         // CONTINUE LOOP
       // END IF
     // ELSE // Path does not exist, or it exists but is not a directory.
       // PRINT "Error: The path '" + potential_pathname + "' either does not exist or is not a directory."

       // 4. Prompt the user if they want to 1) enter a different path, 2) quit.
       // user_choice_on_error = PROMPT_USER_FOR_CHOICE("Options: (1) Enter a different path, (2) Quit program: ", ["1", "2"])

       // IF user_choice_on_error IS "2" THEN
         // User chose to quit.
         // RETURN NULL
       // ELSE // User chose "1" (enter a different path) or provided invalid input (default to trying again).
         // potential_pathname = NULL // Clear the path to trigger prompt in the next loop iteration.
         // CONTINUE LOOP
       // END IF
     // END IF
   // END LOOP // End of the main validation and prompting loop.

 // END FUNCTION

--- Conceptual File Renaming Function (Comments on their purpose) ---

FUNCTION rename_markdown_files_to_kebab_case (directory_path)
    // Note: Input directory_path is assumed to be valid and exist, as per prior function handling.

   // 1. Get a list of all items (files and subdirectories) in the given directory_path.
   //   items_in_directory = GET_ALL_ITEMS_IN_DIRECTORY(directory_path)

   // 2. Iterate through each item in the directory.
   //   FOR EACH item_name IN items_in_directory
   //     current_full_path =  // Path Manipulation: COMBINE_PATH(directory_path, item_name) to form the full current path.

   //     3. Check if the item is a file.
   //     IF IS_FILE(current_full_path) THEN
   //       original_filename_without_extension, original_file_extension = SPLIT_FILENAME_AND_EXTENSION(item_name)
   //       LOWERCASE_original_file_extension = TO_LOWERCASE(original_file_extension)

   //        // File Identification: Determine the target extension and if this file is a markdown variant we want to process.
   //       target_extension = ""
   //       is_target_markdown_type = FALSE
   //       IF LOWERCASE_original_file_extension IS ".md" OR LOWERCASE_original_file_extension IS ".markdown" THEN
   //         target_extension = ".md"  // Extension Handling: Standardize .markdown to .md
   //         is_target_markdown_type = TRUE
   //       ELSE IF LOWERCASE_original_file_extension IS ".mmd" THEN
   //         target_extension = ".mmd"  // Extension Handling: Preserve .mmd extension
   //         is_target_markdown_type = TRUE
   //       END IF

   //       IF is_target_markdown_type THEN
   //          // This is a markdown file type we want to process.

   //         4. Extract the first H1 header from the markdown file content.
   //         // This involves reading the file (using UTF-8 encoding).
   //         // It should first attempt to identify and skip any YAML frontmatter
   //         // (typically enclosed by '---' or '+++' at the very beginning of the file).
   //         // After skipping frontmatter (if any), it finds the first subsequent line
   //         // that starts with "# " (H1 markdown header) and extracts the title text.
   //         h1_title_text = EXTRACT_FIRST_H1_HEADER_FROM_FILE(current_full_path)

   //         5. Determine the base name for the new file.
   //         IF h1_title_text IS NOT EMPTY AND h1_title_text IS NOT NULL THEN
   //           base_name_for_processing = h1_title_text
   //            // PRINT a message indicating H1 title is being used.
   //         ELSE
   //            // PRINT a warning that no H1 header was found.
   //           base_name_for_processing = original_filename_without_extension  // Fallback to original filename without extension.
   //         END IF

   //         6. Perform intelligent conversion of special characters in the base name.
   //          // This step aims to replace common symbols with their textual or URL-friendly equivalents.
   //         processed_base_name = INTELLIGENTLY_CONVERT_SPECIAL_CHARACTERS(base_name_for_processing)

   //         7. Remove any characters from processed_base_name that are invalid for filenames on common operating systems (Windows, Linux, MacOS).
   //         cleaned_base_name = REMOVE_INVALID_FILENAME_CHARACTERS(processed_base_name)

   //         8. Generate the new kebab-case filename (without extension) from the cleaned_base_name.
   //          // Kebab-Case Conversion Logic: This step is crucial and often complex enough for a helper function.
   //         new_base_filename_kebab = CONVERT_STRING_TO_KEBAB_CASE(cleaned_base_name)

   //         9. Handle cases where the resulting kebab-case name is empty.
   //         IF new_base_filename_kebab IS EMPTY THEN
   //              // PRINT a warning and skip this file.
   //             CONTINUE TO NEXT item_name
   //         END IF

   //         10. Construct the new full filename using the new_base_filename_kebab and the determined target_extension.
   //         new_filename_with_extension = new_base_filename_kebab + target_extension

   //         11. Idempotency Check: Check if a rename is actually needed.
   //         IF new_filename_with_extension EQUALS item_name THEN
   //            // PRINT a message that the file is already correctly named and skip.
   //           CONTINUE TO NEXT item_name
   //         END IF

   //         12. Construct the new full path for the renamed file.
   //         new_full_path_candidate =  // Path Manipulation: COMBINE_PATH(directory_path, new_filename_with_extension)

   //         13. Conflict Resolution: Check if the target filename already exists.
   //         actual_new_full_path = new_full_path_candidate
   //         perform_rename = TRUE

   //         IF FILE_EXISTS(actual_new_full_path) THEN
   //            // PRINT a message about the conflict.
   //           user_choice = PROMPT_USER("File 'new_filename_with_extension' already exists. (O)verwrite, (A)ppend number, or (S)kip?", ["O", "A", "S"])
   //           CASE user_choice OF
   //             "O":  // Overwrite
   //                // PRINT "User chose to overwrite."
   //               perform_rename = TRUE
   //             "A":  // Append number
   //                // PRINT "User chose to append a number."
   //               counter = 1
   //               LOOP
   //                 temp_base_name_numbered = new_base_filename_kebab + "-" + TO_STRING(counter)
   //                 temp_new_filename_numbered = temp_base_name_numbered + target_extension
   //                 temp_new_full_path_numbered =  // Path Manipulation: COMBINE_PATH(directory_path, temp_new_filename_numbered)
   //                 IF NOT FILE_EXISTS(temp_new_full_path_numbered) THEN
   //                   actual_new_full_path = temp_new_full_path_numbered
   //                    // PRINT "Found non-conflicting name: 'temp_new_filename_numbered'."
   //                   perform_rename = TRUE
   //                   BREAK LOOP
   //                 END IF
   //                 counter = counter + 1
   //                  // Optional: Add a safety break if counter gets too high.
   //               END LOOP
   //             "S":  // Skip
   //                // PRINT "User chose to skip 'item_name'."
   //               perform_rename = FALSE
   //             DEFAULT:  // Invalid input or no choice
   //                // PRINT "Invalid choice or no choice made. Skipping 'item_name'."
   //               perform_rename = FALSE
   //           END CASE
   //         END IF

   //         IF perform_rename THEN
   //            // 14. Perform the rename operation.
   //            // Error Handling: Use TRY-CATCH to handle potential issues during the file system operation.
   //           TRY
   //             RENAME_FILE(current_full_path, actual_new_full_path)
   //              // PRINT a success message: "Renamed 'item_name' to 'FILENAME_FROM_PATH(actual_new_full_path)'."
   //           CATCH RENAME_ERROR
   //              // PRINT an error message if renaming fails: "Error renaming 'item_name': " + RENAME_ERROR_MESSAGE
   //           END TRY
   //         ELSE
   //              // Message for skipping due to conflict resolution (if not already printed).
   //             IF NOT (user_choice EQUALS "S" OR user_choice EQUALS DEFAULT) THEN
   //                 // PRINT "Skipping rename of 'item_name' due to conflict and no resolution path taken."
   //             END IF
   //         END IF
   //       END IF  // End target_markdown_type check.
   //     END IF  // End is_file check.
   //   END FOR  // End loop through directory items.

   //  // PRINT a final message indicating the process is complete.
   //  // Clarity: Throughout the function, descriptive variable and conceptual function names are used.

 // END FUNCTION

 --- Conceptual Helper Functions (Comments on their purpose) ---

 // FUNCTION EXTRACT_FIRST_H1_HEADER_FROM_FILE (file_path)
 //    Reads the specified file (using UTF-8 encoding) line by line.
 //    If YAML frontmatter (e.g., enclosed by '---' lines or '+++' lines at the beginning)
 //    is detected, it should be correctly skipped.
 //    After any frontmatter, it finds and returns the trimmed text of the first
 //    H1 markdown header (e.g., text after "# ").
 //    Returns an empty string or null if no H1 is found, or on error.
 // END FUNCTION

 // FUNCTION INTELLIGENTLY_CONVERT_SPECIAL_CHARACTERS (input_string)
 //    Converts common symbols and accented characters to more filename-friendly equivalents (e.g., '&' to 'and', 'é' to 'e').
 // END FUNCTION

 // FUNCTION REMOVE_INVALID_FILENAME_CHARACTERS (input_string)
 //    Removes characters that are explicitly forbidden in filenames on major OSes (e.g., / \ : * ? " < > |).
 // END FUNCTION

 // FUNCTION CONVERT_STRING_TO_KEBAB_CASE (input_string)
 //    Kebab-Case Conversion Logic: Converts a string to kebab-case.
 //    This typically involves:
 //    1. Lowercasing.
 //    2. Replacing various separators (spaces, underscores, etc.) and non-alphanumeric characters with hyphens.
 //    3. Collapsing multiple hyphens into a single hyphen.
 //    4. Trimming leading/trailing hyphens.
 //    Assumes input has already had invalid filename characters removed and intelligent conversions applied.
 // END FUNCTION

 // FUNCTION PROMPT_USER (message, valid_choices_array)
 //    Displays a message to the user and waits for input.
 //    Validates the input against valid_choices_array (case-insensitively).
 //    Returns the uppercase valid choice, or a default/empty value if input is invalid or user cancels.
 // END FUNCTION
---

**LLM Prompt Guidance: Python Script Generation**

When generating Python scripts, please adhere to the following guidelines to ensure the code is well-structured, readable, maintainable, and follows best practices:

**I. Overall Structure and Design:**

*   **Modularity with Classes:**
    *   Prioritize the use of classes to encapsulate related data and functionality.
    *   The main script should primarily orchestrate the instantiation and interaction of these classes, rather than containing the bulk of the logic.
    *   Each class should have a single, well-defined responsibility (Single Responsibility Principle).
*   **Main Script (`if __name__ == "__main__":`)**
    *   The primary execution logic should be contained within a `if __name__ == "__main__":` block.
    *   This block should be responsible for creating instances of your defined classes and calling their methods to achieve the script's overall goal.

**II. Pythonic Form:**

*   **Readability Counts:** Write code for humans first, machines second. Prioritize clarity and simplicity over overly complex or "clever" solutions.
*   **PEP 8 Compliance:** Follow the PEP 8 style guide for Python code. This includes conventions for naming, comments, layout, and more. Consider using linters/formatters like Black or Pylint to help enforce this.
*   **Naming Conventions:**
    *   Use meaningful and descriptive names for variables, functions, methods, and classes that clearly reflect their purpose.
    *   Follow standard Python naming conventions (e.g., `snake_case` for functions and variables, `CapWords` or `CamelCase` for classes).
*   **Explicit is Better than Implicit:** Code should be clear and its intentions obvious.
*   **Don't Repeat Yourself (DRY):** Avoid duplicating code or logic. Encapsulate reusable logic into functions or methods.
*   **List Comprehensions and Generators:** Use list comprehensions for concise creation of lists and generators for memory-efficient iteration over large datasets where appropriate.
*   **F-strings:** Prefer f-strings for string formatting (for Python 3.6+).
*   **Comments:**
    *   Use comments sparingly and ensure they are meaningful, explaining *why* something is done, rather than *what* is being done if the code is already clear.
    *   Write docstrings for all public modules, functions, classes, and methods, following PEP 257 conventions.
*   **Error Handling:** Implement robust error handling using try-except blocks, especially when dealing with external dependencies or operations that might fail.
*   **Type Hinting:** Use type hints for function arguments and return values to improve code clarity and allow for static analysis.

**III. Clean Code Principles (Inspired by "Clean Code"):**

*   **Meaningful Names:** As mentioned in Pythonic Form, choose names that reveal intent.
*   **Small Functions/Methods:** Functions and methods should be small and do one thing well. If a function is doing too much, break it down.
*   **Avoid Side Effects:** Functions should ideally not have hidden side effects (i.e., modifying state outside their scope unexpectedly). If they do, make it clear.
*   **Minimal Arguments:** Aim for fewer arguments in functions/methods.
*   **Encapsulation:** Hide internal implementation details of classes and expose a clear public interface. Use private/protected members (by convention using leading underscores) where appropriate.
*   **Keep it Simple, Stupid (KISS):** Strive for simplicity in design and implementation. Avoid unnecessary complexity.
*   **Composition Over Inheritance (where appropriate):** Favor creating complex objects by combining simpler ones (composition) over creating complex inheritance hierarchies, though inheritance has its place.
*   **Testability:** Write code in a way that is easy to test. This often goes hand-in-hand with small, focused functions/methods and clear interfaces.
*   **Refactor Continuously:** Don't be afraid to improve the design of existing code as you understand the problem better or as requirements change.

**IV. Class Creation and Usage Specifics:**

*   **Constructor (`__init__`):** Use the `__init__` method to initialize the state of new objects.
*   **Instance Methods:** Define methods within classes to operate on the instance's data (the first argument should be `self`).
*   **Class Attributes vs. Instance Attributes:** Understand and use class attributes (shared among all instances) and instance attributes (specific to each instance) appropriately.
*   **`@property` Decorator:** Consider using the `@property` decorator for getter and setter methods to manage attribute access if needed, providing a more Pythonic way to control attribute interactions.
*   **String Representation (`__str__`, `__repr__`):** Implement `__str__` for a user-friendly string representation of your objects and `__repr__` for an unambiguous developer-friendly representation.
*   **Avoid Hard-Coding:** Use constants or configuration for values that might change, rather than hard-coding them directly in the script. Define constants at the module level, typically in all caps.