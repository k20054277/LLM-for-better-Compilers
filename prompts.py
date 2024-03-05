import itertools
import subprocess
import time

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

def run_prompt(prompt, model):
    if model == "mistral":
        result = subprocess.run(
        "ollama run mistral:latest " + prompt +"",
        shell =True,
        capture_output = True, # Python >= 3.7 only
        text = True # Python >= 3.7 only
        )

    elif model == "magicoder":
        result = subprocess.run(
        "ollama run magicoder:latest " + prompt +"",
        shell =True,
        capture_output = True, # Python >= 3.7 only
        text = True # Python >= 3.7 only
        )
    out = result.stdout
    err = result.stderr
    return out

def read_file(file_name, model):
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
    
    # for line in Lines:
    #     out = run_prompt(line.strip('\n\r'), model)
    #     extract_code(out)

    for i in range(200):
        out = run_prompt(Lines[i].strip('\n\r'), model)
        extract_code(out)

def extract_code(output):

    start_index = output.find("```python")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        return

    program = output[start_index:end_index+ 3].strip()
    # print (program)

    f = open("output.txt", "a")
    f.write(program + "\n")
    f.close()

def save_time(time):

    f = open("output.txt", "a")
    f.write(time + "\n")
    f.close()

def main():
    prompts = generate_all_prompts()

    # Output the generated prompts
    # print("Generated Prompts:")
    # for idx, prompt in enumerate(prompts, start=1):
    #     print(f"{idx}. {prompt}")
    
        
    # # Optionally, you can save the prompts to a file
    # f = open("generated_prompts.txt", "w")
    # f.truncate(0)
    # for prompt in prompts:
    #     f.write(prompt + "\n")
    # f.close()

    read_file("generated_prompts.txt", "mistral")

if __name__ == "__main__":
    start_time = time.time()
    main()
    save_time("--- %s seconds ---" % round(time.time() - start_time, 2))


