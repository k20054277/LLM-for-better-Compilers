import subprocess
import time

def run_prompt_mistral(prompt):
    result = subprocess.run(
    "ollama run mistral:latest " + prompt +"",
    shell =True,
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
    )
    out = result.stdout
    err = result.stderr
    return out

def run_prompt_codellama(prompt):
    result = subprocess.run(
    "ollama run codellama:latest " + prompt +"",
    shell =True,
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
    )
    out = result.stdout
    err = result.stderr
    return out

def run_prompt_gemma(prompt):
    result = subprocess.run(
    "ollama run gemma:latest " + prompt +"",
    shell =True,
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
    )
    out = result.stdout
    err = result.stderr
    return out

def read_file(model):
    n = 1000
    # for line in Lines:
    #     out = run_prompt(line.strip('\n\r'), model)
    #     extract_code(out)
    if model == "mistral": 
        file1 = open("mistral_prompts.txt", 'r')
        Lines = file1.readlines()
        for i in range(n):
            out = run_prompt_mistral(Lines[i].strip('\n\r'))
            extract_code_mistral(out, i)
    elif model == "codellama": 
        file1 = open("Codellama_prompts.txt", 'r')
        Lines = file1.readlines()
        for i in range(n):
            out = run_prompt_codellama(Lines[i].strip('\n\r'))
            extract_code_codellama(out, i)
    elif model == "gemma": 
        file1 = open("gemma_prompts.txt", 'r')
        Lines = file1.readlines()
        for i in range(n):
            out = run_prompt_gemma(Lines[i].strip('\n\r'))
            extract_code_gemma(out, i)

def extract_code_mistral(output, index):

    start_index = output.find("```python")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        return

    program = output[start_index+3:end_index].strip()
    # print (program)

    f = open("mistral_output.txt", "a")
    f.write(str(index) + "\n")
    f.write(program + "\n")
    f.close()

def extract_code_codellama(output, index):

    start_index = output.find("```")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```"))
    if end_index == -1:
        return

    program = output[start_index:end_index+3].strip()
    # print (program)

    f = open("codellama_output.txt", "a")
    f.write(str(index) + "\n")
    f.write(program + "\n")
    f.close()

def extract_code_gemma(output, index):

    start_index = output.find("```python")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        return

    program = output[start_index+3:end_index].strip()
    # print (program)

    f = open("gemma_output.txt", "a")
    f.write(str(index) + "\n")
    f.write(program + "\n")
    f.close()

def save_time(time):

    f = open("time.txt", "a")
    f.write(time + "\n")
    f.close()

def main():
    model = input("Enter model: ") 
    f = open("time.txt", "a")
    f.write(model + "\n")
    f.close()
    read_file(model)

if __name__ == "__main__":
    start_time = time.time()
    main()
    save_time("--- %s seconds ---" % round(time.time() - start_time, 2))


