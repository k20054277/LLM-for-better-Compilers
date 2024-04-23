#!/usr/bin/env python3

import subprocess

def main():
    # Assert that the input file exists
    assert 'input_file.txt' in subprocess.listdir(), "Input file not found"

    # Assert that the output file does not exist
    assert 'output_file.txt' not in subprocess.listdir(), "Output file already exists"

    # Run the command to convert the input file to the output file
    subprocess.run(['convert', 'input_file.txt', 'output_file.txt'])