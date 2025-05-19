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