#!/usr/bin/python3

def foo():
    print("Hello from foo")

def bar():
    print("Hello from bar")

# This will run foo() twice
for i in range(2):
    foo()

# This will run bar() once
bar()