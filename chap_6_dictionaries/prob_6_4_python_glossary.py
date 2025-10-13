python_keywords = {
    "def": "Defines a function.",
    "class": "Defines a class.",
    "if": "Starts a conditional block.",
    "elif": "Else if; checks another condition in an if chain.",
    "else": "Specifies a block to run if conditions are false.",
    "for": "Iterates over a sequence.",
    "while": "Loops while a condition is true.",
    "break": "Exits the nearest loop immediately.",
    "continue": "Skips the rest of the current loop iteration.",
    "return": "Exits a function and optionally returns a value.",
    "import": "Brings modules into the current namespace.",
    "from": "Imports specific parts of a module.",
    "as": "Gives an alias name to a module or variable.",
    "try": "Starts a block that may raise exceptions.",
    "except": "Handles exceptions raised in the try block.",
    "finally": "Runs code after try/except, regardless of outcome.",
    "with": "Simplifies resource management using context managers.",
    "lambda": "Creates an anonymous (inline) function.",
    "yield": "Pauses a function and returns a generator value.",
    "global": "Declares a variable as global within a function."
}

for key, value in python_keywords.items():
    print(f"{key} => {value}")