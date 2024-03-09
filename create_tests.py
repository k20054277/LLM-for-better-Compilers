#create test programs from output
import os.path

def create_mistral(content):
    save_path = "/home/k20054277/Documents/llm/LLM-for-better-Compilers/mistral"

    # for i in range (1000):
    #     start_index = content.find("python")
    #     if start_index == -1:
    #         return
    #     end_index = content.find("python", start_index + len("python"))
    #     if end_index == -1:
    #         return

    #     program = content[start_index+ len("python"):end_index].strip()
    #     # print (program)

    #     f = open("output.txt", "a")
    #     f.write(str(index) + "\n")
    #     f.write(program + "\n")
    #     f.close()

def create_codellama(content):
    save_path = "/home/k20054277/Documents/llm/LLM-for-better-Compilers/codellama"

    l = len(content)-1
    end_index = 0
    i = 0

    while (end_index<l):
        start_index = content.find("```", end_index)
        if start_index == -1:
            return
        end_index = content.find("```", start_index + len("```"))
        if end_index == -1:
            return
        if (content[start_index:start_index+ len("python")] == "```python"):
            start_index += len("python")

        program = content[start_index+ len("```"):end_index].strip()

        completeName = os.path.join(save_path, "gemma_" + str(i) + ".txt")

        f = open(completeName, "w")
        f.write(program)
        f.close()

        i +=1
        end_index += 3

        

def create_gemma(content):
    save_path = "/home/k20054277/Documents/llm/LLM-for-better-Compilers/gemma"

    # start_index = output.find("```python")
    # if start_index == -1:
    #     return
    # end_index = output.find("```", start_index + len("```python"))
    # if end_index == -1:
    #     return

    # program = output[start_index+3:end_index].strip()
    # # print (program)

    # f = open("gemma_output.txt", "a")
    # f.write(str(index) + "\n")
    # f.write(program + "\n")
    # f.close()


def input_txt(model):

    if model == "codellama":
        txt_file = open("codellama_output.txt", 'r')
        content = txt_file.read() 
        create_codellama(content)

def main():
    model = input("Enter model: ") 
    input_txt(model)

if __name__ == "__main__":
    main()

