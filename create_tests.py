#create test programs from output
import os
import re

def create_mistral(content):
    save_path = os.getcwd() +"/mistral"

    pattern = "\d+\npython"

    program = re.split(pattern, content)

    i = 0
    for p in program:
        completeName = os.path.join(save_path, "mistral_" + str(i) + ".py")
        f = open(completeName, "w")
        f.write(p)
        f.close()
        i += 1


# def create_codellama(content):
#     save_path = "/home/k20054277/Documents/llm/LLM-for-better-Compilers/codellama"

#     l = len(content)-1
#     end_index = 0
#     i = 0

#     while (end_index<l):
#         start_index = content.find("```", end_index)
#         if start_index == -1:
#             return
#         end_index = content.find("```", start_index + len("```"))
#         if end_index == -1:
#             return
#         if (content[start_index:start_index+ len("python")] == "```python"):
#             start_index += len("python")

#         program = content[start_index+ len("```"):end_index].strip()

#         completeName = os.path.join(save_path, "codellama_" + str(i) + ".txt")

#         f = open(completeName, "w")
#         f.write(program)
#         f.close()

#         i +=1
#         end_index += 3

def create_codellama(content):
    save_path = os.getcwd() +"/codellama"

    pattern = "\d+\n```"

    program = re.split(pattern, content)

    i = 0
    for p in program:
        
        start_index = p.find("python")
        if start_index == 0:
            start_index = len("python")
        else:
            start_index = 0 
        end_index = p.find("```", start_index)
        if end_index == -1:
           end_index = len(p)-1

        new_p = p[start_index:end_index].strip()

        completeName = os.path.join(save_path, "codellama_" + str(i) + ".py")
        f = open(completeName, "w")
        f.write(new_p)
        f.close()
        i += 1


def create_gemma(content):
    save_path = os.getcwd() +"/gemma"

    pattern = "\d+\npython"

    program = re.split(pattern, content)

    i = 0
    for p in program:
        p.strip()
        completeName = os.path.join(save_path, "gemma_" + str(i) + ".py")
        f = open(completeName, "w")
        f.write(p)
        f.close()
        i += 1


def input_txt(model):

    if model == "codellama":
        txt_file = open("codellama_output.txt", 'r')
        content = txt_file.read() 
        create_codellama(content)
    elif model == "mistral":
        txt_file = open("mistral_output.txt", 'r')
        content = txt_file.read() 
        create_mistral(content)
    elif model == "gemma":
        txt_file = open("gemma_output.txt", 'r')
        content = txt_file.read() 
        create_gemma(content)

def main():
    model = input("Enter model: ") 
    input_txt(model)

if __name__ == "__main__":
    main()

