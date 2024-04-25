#create test programs from output
import os
import re
import shutil

def compare_each(E1, E2):
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
    err_file1 = open(path+ "-312-err.txt", "r")
    err_file2 = open(path+ "-313-err.txt", "r")
    out_file1 = open(path+ "-312-res.txt", "r")
    out_file2 = open(path+ "-313-res.txt", "r")
    files = [err_file1.read(),err_file2.read(),out_file1.read(),out_file2.read()]
    outputs =[[],[],[],[]]
    pattern = "\\d+id:.+\nb'"
    i =0
    for file in files:
        output = re.split(pattern, file)
        for o in output:
            outputs[i].append(o)
        i = i+1

    compare_each(outputs[0], outputs[1])
    compare_each(outputs[2], outputs[3])

def input_txt(model):

    if model == "minimised Codellama":
        dir_path = (os.getcwd() +"/compare/codellama-mini")
        compare(dir_path)
    elif model == "minimised Mistral":
        dir_path = (os.getcwd() +"/compare/mistral-mini")
        compare(dir_path)
    elif model == "minimised Gemma":
        dir_path = (os.getcwd() +"/compare/gemma-mini")
        compare(dir_path)
    elif model == "Mistral": 
        dir_path = (os.getcwd() +"/compare/mistral")
        compare(dir_path)
    elif model == "CodeLlama": 
        dir_path = (os.getcwd() +"/compare/codellama")
        compare(dir_path)
    elif model == "Gemma": 
        dir_path = (os.getcwd() +"/compare/gemma")
        compare(dir_path)
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


def main():
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

