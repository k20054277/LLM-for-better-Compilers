import subprocess
import time
import os

def save_time(time):
    #save time in time.txt
    f = open("time.txt", "a")
    f.write(time + "\n")
    f.close()

def run_prompt_mistral(prompt):
    #run ollama with mistral and prompt
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
    #run ollama with codeLlama and prompt
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
    #run ollama with gemma and prompt
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
    completeName = os.path.join(save_path, "mistral_" + str(index) + ".py")
    f = open(completeName, "w")
    
    #remove llm syntax
    #if syntax for python program not found then generate empty program
    start_index = output.find("```python")
    if start_index == -1:
        f.close()
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        f.close()
        return

    program = output[start_index + len("```python") :end_index].strip()
    # print (program)
    f.write(program)
    f.close()

def extract_code_codellama(output, index):
    save_path = os.getcwd() +"/codellama"
    completeName = os.path.join(save_path, "codellama_" + str(index) + ".py")
    f = open(completeName, "w")

    #remove llm syntax
    #if syntax for python program not found then generate empty program
    start_index = output.find("```")
    if start_index == -1:
        f.close()
        return
    end_index = output.find("```", start_index + len("```"))
    if end_index == -1:
        f.close()
        return

    program = output[start_index+len("```"):end_index].strip()
    # print (program)
    
    f.write(program)
    f.close()


def extract_code_gemma(output, index):
    save_path = os.getcwd() +"/gemma"
    completeName = os.path.join(save_path, "gemma_" + str(index) + ".py")
    f = open(completeName, "w")

    #remove llm syntax
    #if syntax for python program not found then generate empty program
    start_index = output.find("```python")
    if start_index == -1:
        f.close()
        return
    end_index = output.find("```", start_index + len("```python"))
    if end_index == -1:
        f.close()
        return

    program = output[start_index+len("```python") : end_index].strip()
    # print (program)

    f.write(program)
    f.close()

def read_file(model):

    #read past generated prompts
    file1 = open("prompts.txt", 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    if model == "Mistral": 
        save_time(model)
        dir_path = (os.getcwd() +"/mistral")
        #count number of test cases already generated
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        #only keep the prompts that havn't been used
        Lines = Lines[count:]
        print("Generating...")
        for i in range(len(Lines)):
            print("-Test "+ str(count))
            #use llm to generate test cases for each prompt
            out = run_prompt_mistral(Lines[i].strip('\n\r'))
            #extract program
            extract_code_mistral(out, count)
            count += 1
    elif model == "CodeLlama": 
        save_time(model)
        #count number of test cases already generated
        dir_path = (os.getcwd() +"/codellama")
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        #only keep the prompts that havn't been used
        Lines = Lines[count:]
        print("Generating...")
        for i in range(len(Lines)):
            print("-Test "+ str(count))
            #use llm to generate test cases for each prompt
            out = run_prompt_codellama(Lines[i].strip('\n\r'))
            #extract program
            extract_code_codellama(out, count)
            count += 1
    elif model == "Gemma": 
        save_time(model)
        #count number of test cases already generated
        dir_path = (os.getcwd() +"/gemma")
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        #only keep the prompts that havn't been used
        Lines = Lines[count:]
        print("Generating...")
        for i in range(len(Lines)):
            print("-Test "+ str(count))
            #use llm to generate test cases for each prompt
            out = run_prompt_gemma(Lines[i].strip('\n\r'))
            extract_code_gemma(out, count)
            #extract program
            count += 1
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


def main():
    #select models
    print("Large Language Model options: ")
    print("-------------------------------------")
    print("Mistral")
    print("CodeLlama")
    print("Gemma")

    print("-------------------------------------")

    model = input("Please select a model to start generating test cases: ")
    read_file(model)

if __name__ == "__main__":
    #time process
    start_time = time.time()
    main()
    save_time("--- %s seconds ---" % round(time.time() - start_time, 2))


