# Prog1-HW3

Write a program to tackle the following problem. All programming should use good function and variable names and sufficient comments for improved readability.

We want to leverage the computer to compute some large sums using loops. Your program should have at least three functions defined, as specified below. It will also use a menu, and require valid inputs at all times.

Required functions:
- A function taking 1 parameter $n$, and returning $1 + 2 + 3 + \cdots + n$
- A function taking 1 parameter $n$, and returning $1^2 + 2^2 + 3^2 + \cdots + n^2$
- A function taking 1 parameter $n$, and returning $1^3 + 2^3 + 3^3 + \cdots + n^3$

Optional functions:
- A function which takes no parameters and outputs the menu
- Any other tasks which would produce more readable code by encapsulating into a function



Your program should produce a visually pleasing menu with (at least) 4 options:
- Sum
- Sum of squares
- Sum of cubes
- Quit

Upon choosing one of the first three options, the user should then be prompted for a *nonnegative integer*. If the user inputs a negative integer, continue to prompt them to correct their mistake until they input a nonnegative integer. Once valid input has been given, plug the input into the corresponding function and print the result with a description (that is, do not print just a number, but use words that remind them what sum they actually computed alongside the result). Then return to the menu.

If the user chooses the quit option, print a nice exit message before the program ends.

If the user inputs an invalid menu choice, tell them so, reprint the menu, and have them try again.

***Bonus***

Add another option that computes $1^k + 2^k + 3^k + \cdots + n^k$ for any even integer $k$. Prompt the user for both $n$ and $k$, and only accept valid inputs. This sum computation should also be encapsulated in a function taking the 2 parameters $n$ and $k$.
