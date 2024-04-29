import os
import re
import shutil

def compare_each(E1, E2):
    #compare each testcase 
    i = 0
    div = []
    print(str(len(E1)))
    print(str(len(E2)))
    if len(E1) > len(E2):
        for output in E2:
            if output == E1[i]:
                pass
            else:
                div.append(i)
                
            i+= 1
    elif len(E1) < len(E2):
        for output in E1:
            if output == E2[i]:
                pass
            else:
                div.append(i)
                
            i+= 1

    print(f"diviation at {div}")

def compare(path):
    #fetch error and results files for selected directory
    err_file1 = open(path+ "_error.txt", "r")
    out_file1 = open(path+ "_result.txt", "r")
    files = [err_file1.read(),out_file1.read()]
    err_file1.close()
    out_file1.close()
    outputs1 =[[],[]]
    pattern = "\\d+id:.+\nb'"
    i =0
    #seperate error and results files into each test case
    for file in files:
        output = re.split(pattern, file)
        for o in output:
            outputs1[i].append(o)
        i = i+1

    return outputs1

def input_txt(model):
    #fetch error and results files for both versions of Cpython
    if model == "minimised Codellama":
        dir_path1 = (os.getcwd() +"/compare/3.12/codellama_mini")
        dir_path2 = (os.getcwd() +"/compare/3.13/codellama_mini")
 
    elif model == "minimised Mistral":
        dir_path1 = (os.getcwd() +"/compare/3.12/mistral_mini")
        dir_path2 = (os.getcwd() +"/compare/3.13/mistral_mini")
    elif model == "minimised Gemma":
        dir_path1 = (os.getcwd() +"/compare/3.12/gemma_mini")
        dir_path2 = (os.getcwd() +"/compare/3.13/gemma_mini")

    elif model == "Mistral": 
        dir_path1 = (os.getcwd() +"/compare/3.12/mistral")
        dir_path2 = (os.getcwd() +"/compare/3.13/mistral")

    elif model == "CodeLlama": 
        dir_path1 = (os.getcwd() +"/compare/3.12/codellama")
        dir_path2 = (os.getcwd() +"/compare/3.13/codellama")

    elif model == "Gemma": 
        dir_path1 = (os.getcwd() +"/compare/3.12/gemma")
        dir_path2 = (os.getcwd() +"/compare/3.13/gemma")

    else:
        print("Large Language Model options: ")
        print("-------------------------------------")
        print("Mistral")
        print("CodeLlama")
        print("Gemma")
        print("minimised Mistral")
        print("minimised CodeLlama")
        print("minimised Gemma")
        print("-------------------------------------")
        print("Error! Please type your model of choice exactly as displayed on screen (case sensitive)")
        model = input("Please select a model to check LLM generation statistics and remove anomalies: ")
        input_txt(model)

    #compare error and results files
    err1, out1 = compare(dir_path1)
    err2, out2 = compare(dir_path2)
    compare_each(err1, err2)
    compare_each(out1, out2)

def main():
    #Model selection
    print("Large Language Model options: ")
    print("-------------------------------------")
    print("Mistral")
    print("CodeLlama")
    print("Gemma")

    print("minimised Mistral")
    print("minimised CodeLlama")
    print("minimised Gemma")
    print("-------------------------------------")
    model = input("Please select a model to Compare results: ") 
    input_txt(model)

if __name__ == "__main__":
    main()

