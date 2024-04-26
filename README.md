# User Guide

Date: 25 APR 2024

Author: Jiaqi Xu

The implementation is a critical component in my project to enhance compiler testing techniques by integrating the innovative capabilities of LLMs with the robustness of fuzzing methodologies. This document will provide a step-by-step guide to building my proposed compiler testing process. 

    Environment requirements: The testing framework encompasses a series of tools that need to be built locally, including LLMs Mistral 7B, Codellama 7B, and Gemma 7B. These processes will require a large portion of memory. It is recommended that you have at least 100GB of storage available on your device before building the project.

# Installation Steps

1. Install Required Software:

Please first make sure Docker and Python3 are installed on your device.

Install Docker: 

   run this command to uninstall all conflicting packages.

    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

 If you are installing Docker for the first time on a new host machine, you need to set up the Docker repository. Afterwards, you can install and update Docker from the repository. Visit https://docs.docker.com/engine/install/ubuntu/ for more details.

Then install the Docker packages:

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Use this command to verify your installation:

    sudo docker run hello-world

This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

Docker install complete.

Install Python using the following: 

    sudo apt install python3 python3-pip

Install Ollama:

Ollama can be easily installed with the following command:

    curl -fsSL https://ollama.com/install.sh | sh

once installed, The models Mistral, Gemma, and CodelLama can be pulled using Ollama with the following command:

    ollama pull mistral
    ollama pull gemma
    ollama pull codellama

you will now see a status bar showing the progress of your install. To verify the install, run: 

    ollama list

If correctly installed, an interface should display all three models 

Installation complete
   
Using the Framework

Generate Test Cases:
 -
 Navigate into the root directory. Run generate_prompts.py with the following command to create prompts based on python features identified by GPT-4r.

    python3 generate_prompts.py
This program will ask for the number of features you would like to test in one prompt. For reference, the results generated in the evaluation of the project have been tested with 2 features per prompt.
The generated prompts will be stored in `prompts.txt`.

Run LLMs to Generate Test Cases:
- 
   - See the installation section to ensure Ollama and all three models are correctly installed.

   Run `run_prompts.py` to generate test cases using the prompt:
   - Test cases will be generated in directories named after each model (mistral, codellama, gemma). Please insure these directories are in the root folder before running `run_prompts.py`
  
    python3 run_prompts.py
   
   This will ask for a model to run the prompt with.

   The generation process may take a long time. It is possible to stop and restart the process by running the same command.

Prepare for Fuzzing:
-
   
   Use `delete_empty.py` to remove any ineffective test cases:
   - please note this script should only be run once generation from the model of choice is complete. The statistics generated will only display accurate information for the first time.  
```bash
python delete_empty.py
```

Fuzzing with AFL:
- 

    
We will be using Docker to set up and run the Fuzzing environment. You should be able to find a `dockerfile` in the root directory of your project.

- Please ensure docker has been set up by following the installation information in the first section of the user instructions.

Build the Docker image by running the following command:

    docker build -t dockerfile .

This will build a local image with the  successful indication: 
`Successfully tagged dockerfile:latest`

We can now build the container and navigate to the directory containing the test cases with the command:

    docker run -it --privileged dockerfile:latest

you will now see the host information in terminal change to follow the container id. For example: `root@c8a9ac2fd739:/home/debian# `

Begin fuzzing using Python-AFL:
- 

Ensure you are in the directory /home/debian inside the container. You will see the following selected directories:

    - AFLplusplus
    - Python-3.12.3
    - Python-3.13.0a5
    - codellama
    - codellama_out
    - mistral 
    - mistral_out
    - gemma
    - gemma_out
    - compare

and the following scripts:

    move_all.py
    compare.py

This means that the container has been correctly set up.

You can now run the following script to start fuzzing your llm generated programs, which are stored in their respective directories: gemma, mistral, and codellama.

- If running the container for the first time or restarting after a crash. you may need to follow the on-screen command to modify `/proc/sys/kernel/core_pattern` with the command `echo core >/proc/sys/kernel/core_pattern`

```bash
py-afl-fuzz -m 80000 -t1000000 -i mistral/ -o mistral_out/ -- Python-3.13.0a5/python @@
```
   - You can monitor the fuzzing process and manage any crashes as documented with the interface that will be generated once all the input test cases have been processed. 

The tag -i and -o are required tags denoting the input directory with test cases and the output directory for fuzzer findings. The tag -m denotes the memory limit for child process in MB with no limit as the default option. The tag -t denotes the timeout limit for each run with a default of 1000 ms. The final tag @@ is used to instruct that when child processes requires inputs, AFL generated inputs will be used.

During the fuzzing process, it is possible for Python-AFL to crash unexpectedly due to it's manipulation of memory processes. In this situation, Python-AFL can be resumed with the tag: AFL\_AUTORESUME, and setting the output directory to the same directory as the previous run.

A sample command to resume Py-afl from /home/debian is as follows: 

    py-afl-fuzz AFL\_AUTORESUME -m 80000 -t1000000 -i- -o mistral\_out/ -- Python-3.13.0a5/python @@

Optional Minimisation:
-
After fuzzing the test cases, you may run an option minimisation algorithm called afl-cmin. This process tries to find the smallest subset of files in the input directory that still triggers the full range of instrumentation data points seen in the starting corpus. The command to run cmin is as follows: 

    afl-cmin -i mistral\_out/default/queue -o Python-3.13.0a5/debug/mistral-cmin -- Python-3.13.0a5/python @@

Conduct Differential Testing:
-
After you have finished the fuzzing session. You can use the script `move_all.py` to move all the fuzzing output from the respective directories(mistral_out/, gemma_out/, codellama_out/) to the compiler libraries in Python-3.12.3/ and Python-3.13.0a5/. The compiler library is also where we will run the next script, `run_cpython_3.12.py` and `run_cpython_3.13.py` 

   - Use `run_cpython_3.12.py` and `run_cpython_3.13.py` to execute the test cases across different Python versions. You must first be in the Python directory before running the scripts:
     ```bash
     python3 run_cpython_3.12.py
     python3 run_cpython_3.13.py
     ```
    
This will run the compiler to generate error files and result files, ready for comparing outputs to identify discrepancies.

After running the test suite, the script `move_all.py` can be used again to move the results from the Python directories to the folder /home/debian/compare/

Evaluate Results:
-
 Review the data collected from the testing phases. Assess code coverage, crash data, and execution efficiency.

 The script `compare.py` can be run from /home/debian to compare the outputs between compiler versions for a selected model. As this script is mainly processed by human knowledge, however, this script only provides limited support.

Troubleshooting and Tips
- Handling Crashes: If Python-AFL crashes, resume the session using AFL_AUTORESUME.
- Optimization: If the test generation or fuzzing process is slow, consider adjusting the `-m` and `-t` parameters in the fuzzing command.

- Data Review: Regularly check the `fuzzer-stats` and `plot_data` for insights into the fuzzing process.


Footnote

This user guide is designed to help you effectively navigate and utilize the compiler testing framework. By following these instructions, users can harness the power of LLMs and AFL++ to enhance the robustness and reliability of compilers through comprehensive testing.
