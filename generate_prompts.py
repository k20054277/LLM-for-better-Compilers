import itertools

# Predefined list of keywords
keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await", 
    "break", "class", "continue", "def", "del", "elif", "else", "except", 
    "finally", "for", "from", "global", "if", "import", "in", "is", 
    "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", 
    "while", "with", "yield",
    
    # Built-in functions
    "abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes", 
    "callable", "chr", "classmethod", "compile", "complex", "delattr", 
    "dict", "dir", "divmod", "enumerate", "eval", "exec", "filter", "float", 
    "format", "frozenset", "getattr", "globals", "hasattr", "hash", "help", 
    "hex", "id", "input", "int", "isinstance", "issubclass", "iter", "len", 
    "list", "locals", "map", "max", "memoryview", "min", "next", "object", 
    "oct", "open", "ord", "pow", "print", "property", "range", "repr", 
    "reversed", "round", "set", "setattr", "slice", "sorted", "staticmethod", 
    "str", "sum", "super", "tuple", "type", "vars", "zip",
    
    # Commonly used module names
    "os", "sys", "math", "random", "datetime", "time", "json", "csv", "sqlite3", 
    "re", "requests", "urllib", "pickle", "subprocess", "argparse", "logging",
    "flask", "django", "numpy", "pandas", "matplotlib", "seaborn", "tensorflow", 
    "keras", "scikit_learn", "beautifulsoup", "selenium", "pytorch", "sqlalchemy", 
    "pytest", "unittest", "pytest", "asyncio", "multiprocessing", "threading", 
    "socket", "tkinter", "pygame", "pyqt", "wxpython",
    
    # Other programming concepts and terms
    "algorithm", "datastructure", "oop", "inheritance", "polymorphism", "encapsulation", 
    "abstraction", "recursion", "iteration", "function", "method", "variable", "constant", 
    "parameter", "argument", "returnvalue", "conditional", "loop", "statement", "expression", 
    "comment", "indentation", "module", "package", "library", "namespace", "interpreter", 
    "compiler", "syntax", "semantics", "debugging", "testing", "documentation", "versioncontrol",
    "exception", "error", "tryexcept", "logging", "assertion", "refactoring", "optimization",
    "performance", "profiling", "deployment", "virtualenvironment", "dependency", "package manager",
    "pip", "conda", "virtualenv", "venv", "requirements.txt", "setup.py", "conda.yml", "environment variable",
    "shell", "scripting", "cron", "batch", "parallel", "concurrency", "thread", "process", "race condition",
    "deadlock", "resource", "lock", "mutex", "semaphore", "context manager", "garbagecollection", "memorymanagement"

    # symbols
    "+", "-", "*", "/", "//", "%", "**", "=", "==", "!=", "<", ">", "<=", ">=",
    "+=", "-=", "*=", "/=", "//=", "%=", "**=", "&", "|", "^", "~", "<<", ">>",
    "and", "or", "not", "in", "is", ":", ",", ".", "()", "[]", "{}", ":", ";"
]


def generate_prompt(keywords):
    prompt = f"Write a program in python that demonstrates the use of "
    for i in range(len(keywords)):
        if i == (len(keywords)-1):
            prompt = prompt + "'" + keywords[i] + "'."
        else:
            prompt = prompt + "'" + keywords[i] + "' and "
    return prompt

def generate_all_prompts(n):
    prompts = []
    # Generate all possible pairs of keywords
    keyword_pairs = list(itertools.combinations(keywords, n))
    # Generate prompt for each pair
    for pair in keyword_pairs:
        prompt = generate_prompt(pair)
        prompts.append(prompt)
    return prompts

def main():

    print("-------------------------------------")
    print("This is a tool to generate prompts targeting Python for use with Large Language Models")

    n = input("Please enter how many features you'd like to include in each prompt: ")
    print("Generating Prompts...")
    prompts = generate_all_prompts(int(n))

    #Store the generated prompts
    f = open("prompts.txt", "w")
    f.truncate(0)
    for prompt in prompts:
        f.write(prompt + "\n")
    f.close()
    print(str(len(prompts)) + " prompts generated")
    print("Done! View the generated prompts in <prompts.txt>")
    print("-------------------------------------")
if __name__ == "__main__":
    main()