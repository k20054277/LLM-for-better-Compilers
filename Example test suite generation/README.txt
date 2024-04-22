Dataset Cover Sheet
Project Title: Large Language Models For Better Compilers

Date: [25 APR 2024]

Author: [Jiaqi Xu]

The dataset files are structured as follows:

Initial Test Cases: Contains the original LLM-generated Python scripts. In folders: mistral, Gemma, and code llama

Fuzzed Outputs: Comprises the outputs from the AFL++ fuzzing process, including mutated test cases that triggered crashes or uncovered anomalies. There are two folders for each model, each containing a 24hr Python-afl output. In folders: mistral-afl, codellama-afl, gemma-afl.

Minimized Test Suite: (If applied) Provides a curated collection of test cases that have been minimized for efficiency without compromising the breadth of code coverage or the depth of testing using AFL++:afl-cmin.
In folders: mistral-cmin, codellama-cmin, gemma-cmin.

Usage of the Dataset
This dataset serves as a valuable resource for:

Compiler Developers: To verify and improve the robustness of compilers.
Research Community: To study the impact of combining AI-generated test cases with traditional fuzzing techniques.
Quality Assurance Teams: To enhance testing protocols and frameworks for software products.
Data Integrity and Reproducibility
To ensure the integrity and reproducibility of the dataset:

Access and Further Information
For access to the dataset or further details regarding its creation and applications, please contact xujackiei@gmail.com.
