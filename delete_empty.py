import os 
import glob 
import sys
  
def delete_empty_files_using_glob(path): 

    total_size = 0
    no_of_files_deleted = 0

    for entry in os.scandir(path):
        if entry.is_file():
            size = entry.stat().st_size
            if size == 0:
                print("Deleting File >>>", entry.path.replace('\\', '/')) 
                # Delete the empty file 
                os.unlink(entry.path) 
                no_of_files_deleted += 1
            else:
                total_size += entry.stat().st_size
    return total_size, no_of_files_deleted


def read_folder(model):

    if model == "Mistral": 
        dir_path = (os.getcwd() +"/mistral")
    elif model == "CodeLlama": 
        dir_path = (os.getcwd() +"/codellama")
    elif model == "Gemma": 
        dir_path = (os.getcwd() +"/gemma")
    else:
        print("Large Language Model options: ")
        print("-------------------------------------")
        print("Mistral")
        print("CodeLlama")
        print("Gemma")
        print("-------------------------------------")
        print("Error! Please type your model of choice exactly as displayed on screen (case sensitive)")
        model = input("Please select a model to check LLM generation statistics and remove anomalies: ")
        read_folder(model)

    workdir=os.listdir(dir_path)
    if '.DS_Store' in workdir:
        workdir.remove('.DS_Store')
    total = len(os.listdir(dir_path))
    print("-------------------------------------")
    if total == 0:
        print(f"No files were found in the folder belonging to {model}, check files are correctly stored under {dir_path}!")
        sys.exit() 
    else:
        total_size, empty = delete_empty_files_using_glob(dir_path)
        gen = str(round(100 * (float(total)-float(empty))/float(total),2)) + "%"
        mean = round(total_size/(total-empty), 2)
        file = open(model+"_statistics", 'a')
        file.write(f"{model} generation statistics: \n")
        file.write(f"{str(empty)} anomalies were found out of {str(total)} programs\n")
        file.write(f"Percentage of successful generation: {gen}\n")
        file.write(f"Mean size of successful generation: {mean} Bytes\n\n")

        file.close()
        if empty == 0:
            print(f"No anomalies found, LLM generation statistics stored in {model}_statistics.txt")
        else:
            print("-------------------------------------")
            print(f"{empty} anomalies found, LLM generation statistics stored in {model}_statistics.txt")
        sys.exit()

def main():
    print("Large Language Model options: ")
    print("-------------------------------------")
    print("Mistral")
    print("CodeLlama")
    print("Gemma")

    print("-------------------------------------")

    model = input("Please select a model to check LLM generation statistics and remove anomalies: ")
    read_folder(model)

if __name__ == "__main__": 
    main()
