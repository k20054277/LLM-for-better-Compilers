import os 
import glob 
  
  
def delete_empty_files_using_glob(pathname: str): 

    no_of_files_deleted = 0
    total_size = 0
  
    # Get the path that are matching with the pattern 
    files = glob.glob(pathname) 
  
    for path in files: 
        size = os.path.getsize(path)
        # Check if the path is a file and empty (size = 0) 
        if os.path.isfile(path):
            if size == 0: 
                # Print the path of the file that will be deleted 
                print("Deleting File >>>", path.replace('\\', '/')) 
                # Delete the empty file 
                os.remove(path) 
      
                no_of_files_deleted += 1
            else:
                total_size += size
    
    return no_of_files_deleted, total_size
  
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

    if '.DS_Store' in dir_path:
        dir_path.remove('.DS_Store')
    total = len(os.listdir(dir_path))
    print("-------------------------------------")
    if total == 0:
        print(f"No files were found in the folder belonging to {model}, check files are correctly stored under {dir_path}!")
        sys.exit() 
    else:
        empty, total_size = delete_empty_files_using_glob(dir_path)
        gen = str(round((100 * float(empty)/float(total_size)),2)) + "%"
        mean = round(total_size/(total-empty), 2)
        file = open(model+"_statistics", 'a')
        file.write(f"{model} generation statistics: ")
        file.write(f"{str(empty)} anomalies were found out of {str(total)} programs")
        file.write(f"Percentage of succesfull generation: {gen}")
        file.write(f"Mean size of succesfull generations: {mean} Bytes")

        file1.close()
        if empty == 0:
            print(f"No anomalies found, LLM generation statistics stored in {model}_statistics.txt")
        else:
            print("-------------------------------------")
            print(f"{empty} anomalies found, LLM generation statistics stored in {model}_statistics.txt")
        

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
