# Task 4.2 — Compiler and interpreter comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates source code before the program is run. | Reads and executes source instructions while the program runs. |
| Typical output | Often produces machine code or an intermediate executable form. | Usually produces the program's runtime output directly. |
| One example | C or C++ are commonly compiled with tools such as GCC. | Python is commonly run through an interpreter. |
| One advantage | Translation is completed before execution, so repeated runs can be faster. | Changes can be tested quickly without a separate compile step. |

A compiler translates a program into another form before execution, while an interpreter carries out instructions at runtime. Python implementations commonly compile source into bytecode and then execute it through a runtime, so the distinction is not always absolute. In this mission, `python3 hello.py` invoked Python to interpret and execute the one-line program.
