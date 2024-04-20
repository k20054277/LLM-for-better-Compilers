import subprocess
import time
import os

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

def extract_code_mistral(output, index):
    save_path = os.getcwd() +"/mistral"

    start_index = output.find("```python")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        return

    program = output[start_index + len("```python") :end_index].strip()
    # print (program)

    completeName = os.path.join(save_path, "mistral_" + str(index) + ".py")
    f = open(completeName, "w")
    f.write(program)
    f.close()

def extract_code_codellama(output, index):
    save_path = os.getcwd() +"/codellama"

    start_index = output.find("```")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```"))
    if end_index == -1:
        return

    program = output[start_index+len("```"):end_index].strip()
    # print (program)

    completeName = os.path.join(save_path, "codellama_" + str(index) + ".py")
    f = open(completeName, "w")
    f.write(program)
    f.close()


def extract_code_gemma(output, index):
    save_path = os.getcwd() +"/gemma"

    start_index = output.find("```python")
    if start_index == -1:
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        return

    program = output[start_index+len("```python") : end_index].strip()
    # print (program)

    completeName = os.path.join(save_path, "gemma_" + str(index) + ".py")
    f = open(completeName, "w")
    f.write(program)
    f.close()

def read_file(model):

    file1 = open("generated_prompts.txt", 'r')
    Lines = file1.readlines()

    if model == "Mistral": 
        print("Generating...")
        for i in range(len(Lines)):
            print("-Test "+ str(i))
            out = run_prompt_mistral(Lines[i].strip('\n\r'))
            extract_code_mistral(out, i)
    elif model == "CodeLlama": 
        print("Generating...")
        for i in range(len(Lines)):
            print("-Test "+ str(i))
            out = run_prompt_codellama(Lines[i].strip('\n\r'))
            extract_code_codellama(out, i)
    elif model == "Gemma": 
        print("Generating...")
        for i in range(len(Lines)):
            print("-Test "+ str(i))
            out = run_prompt_gemma(Lines[i].strip('\n\r'))
            extract_code_gemma(out, i)
    else:
        print("Large Language Model options: ")
        print("-------------------------------------")
        print("Mistral")
        print("CodeLlama")
        print("Gemma")
        print("-------------------------------------")
        print("Error! Please type your model of choice exactly as displayed on screen (case sensitive)")
        model = input("Please select a model to start generating test cases: ")
        read_file(model)


def save_time(time):

    f = open("time.txt", "a")
    f.write(time + "\n")
    f.close()

def main():
    print("Large Language Model options: ")
    print("-------------------------------------")
    print("Mistral")
    print("CodeLlama")
    print("Gemma")

    print("-------------------------------------")

    model = input("Please select a model to start generating test cases: ")
    read_file(model)

if __name__ == "__main__":
    start_time = time.time()
    main()
    save_time("--- %s seconds ---" % round(time.time() - start_time, 2))


