#create test programs from output
import os, subprocess, time


def run_compiler(run_path):
    try:
        p = subprocess.Popen(
        run_path,
        stdout= subprocess.PIPE,
        stdin=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        # shell =True, 
        # text = True,
        )
        grep_stdout = p.communicate(timeout=500)
        # print("ppoll")
        # print(p.poll())
        if p.poll() == None :
            out, err = p.communicate()
            if err == None:
                isFinished = False
                while isFinished != True:
                    print("output" + out )
                    answer = input("input :")
                    grep_stdout = p.communicate(answer)
                    if p.poll() != None :
                        isFinished = True
                    elif grep_stdout[1] != None:
                        isFinished = True
                    else:
                        out = grep_stdout[0]
            else:
                grep_stdout = (out, err)
    except subprocess.TimeoutExpired: 
        return("","TimeoutExpired")

    return grep_stdout

def read_files(file_path, result_file, error_file):
    
    err_i = 0
    out_i = 0    
    for file in sorted(os.listdir(os.getcwd() + file_path)):
        print("--------")
        print(file)
        run_path = ["./python.exe", "."+file_path+"/"+file]
        result = run_compiler(run_path)
        if str(result[1]) == "b''":
            # print("pass " + str(out_i) +"\n")
            # print("out: ")
            # print(result[0])
            f = open(result_file, "a")
            f.write(str(out_i) +file)
            f.write("\n")
            f.write(str(result[0]))
            f.write("\n")
            f.write("\n")
            f.close()
            out_i = out_i + 1
        else:
            # print("fail " + str(err_i))
            # print("out: ")
            # print(result[0])
            # print("err: ")
            # print(result[1])
            f = open(error_file, "a")
            f.write(str(err_i) + file)
            f.write("\n")
            f.write(str(result[1]))
            f.write("\n")
            f.write("\n")
            f.close()
            err_i = err_i + 1

    print("total pass: " + str(out_i))
    print("total fail: " + str(err_i))

def main():
    crash_path = "/debug/crashes"
    gemma_hang_path = "/debug/hangs/gemma"
    codellama_hang_path = "/debug/hangs/codellama"
    # mistral_hang_path = "/debug/hangs/mistral"
    gemma_cmin_path = "/debug/gemma-cmin"
    mistral_cmin_path = "/debug/mistral-cmin"
    codellama_cmin = "/debug/codellama-cmin"
    # read_files(crash_path, "gemma_crash_re.txt", "gemma_crash_err.txt")
    # read_files(gemma_hang_path, "gemma_hang_re.txt", "gemma_hang_err.txt")
    # read_files(codellama_hang_path, "codellama_hang_re.txt", "codellama_hang_err.txt")
    # # read_files(mistral_hang_path, "mistral_hang_re.txt", "mistral_hang_err.txt")
    # read_files(gemma_cmin_path, "gemma_result.txt", "gemma_error.txt")
    # read_files(mistral_cmin_path, "mistral_result.txt", "mistral_error.txt")
    read_files(codellama_cmin, "codellama_result.txt", "codellama_error.txt")
    
if __name__ == "__main__":
    main()
   
