# Week 2

## Notes
- The steps of how a C code is "compiled":
    - Preprocessing
        - `#` is called a preprocessor directive.
        - Lines of code with `#` (e.g. `#include <stdio.h>`) are preprocessed.
        - Essentially, it *includes* the functions that will be used in the source code indicated by the header file. So, instead of writing the `printf` function, since it's already part of the library, you just have to the stdio header into.
        - The header files only contain the *function prototypes*.
    - Compiling
        - Transforms the source code to assembly code
        - Assembly code differs depending on the target CPU architecture.
    - Assembling
        - Transforms the assembly code to machine code
        - Literally turns it to zeros and ones of which a computer can *execute*
    - Linking
        - "Links" or connects all the library machine code to the generated machine code from the source code.
        - The library source code is sourced based on the header files included in the code.

## References
