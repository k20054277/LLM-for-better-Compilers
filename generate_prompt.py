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


def generate_prompt(keyword1, keyword2):
    prompt = f"Write a program in python that demonstrates the use of '{keyword1}' and '{keyword2}'."
    return prompt

def generate_all_prompts():
    prompts = []
    # Generate all possible pairs of keywords
    keyword_pairs = list(itertools.combinations(keywords, 2))
    # Generate prompt for each pair
    for pair in keyword_pairs:
        prompt = generate_prompt(pair[0], pair[1])
        prompts.append(prompt)
    return prompts

def main():
    prompts = generate_all_prompts()

    #Output the generated prompts
    print("Generated Prompts:")
    for idx, prompt in enumerate(prompts, start=1):
        print(f"{idx}. {prompt}")

    f = open("generated_prompts.txt", "w")
    f.truncate(0)
    for prompt in prompts:
        f.write(prompt + "\n")
    f.close()