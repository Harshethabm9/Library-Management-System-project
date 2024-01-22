## Metric

### Metric 1: Cyclomatic Complexity

**Objective: Measure the complexity of the code by assessing the number of independent paths through the program.**

    Calculation:
         - Use a code analysis tool, such as radon or McCabe complexity checker, to calculate the cyclomatic complexity.
         - The metric is typically represented as a single numeric value.

    Interpretation:
         - A lower cyclomatic complexity indicates simpler and more maintainable code.
         - Higher values suggest more complex code that may be harder to understand and maintain.
         
### Metric 2: Maintainability Index
**Objective: Provide an overall indication of how maintainable the code is based on various factors.**

        Calculation:
            - Use a code analysis tool, such as radon or other static code analyzers, to calculate the maintainability index.
            - The maintainability index is often presented as a score on a scale (e.g., 0 to 100).
            
         Interpretation:
             - Higher maintainability index values indicate more maintainable code.
             - Lower values suggest code that may be challenging to maintain.
             
#### Implementation:
For the code provided, you can use tools like radon to calculate these metrics.

    1. Cyclomatic Complexity:
        Tools:
            radon (installable via pip: pip install radon).
            Calculation Example:
            Run radon cc -s library_management_system.py to get cyclomatic complexity values.
     2. Maintainability Index:
         Tools:
            radon (installable via pip: pip install radon).
             
Benefits:
These metrics help gauge the complexity and maintainability of the code.
They provide insights into potential areas for refactoring or improvement.
