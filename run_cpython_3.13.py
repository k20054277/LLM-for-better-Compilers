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
    result_file = "./output/" + result_file
    error_file = "./output/" + error_file

    err_i = 0
    out_i = 0
    f = open(result_file, "w").close
    f = open(error_file, "w").close
    print("Running...")  
    for file in sorted(os.listdir(os.getcwd() + file_path)):
        print("--------")
        print(file)
        run_path = ["./python", "."+file_path+"/"+file]
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
    print("your results are stored in : " + result_file +" and " +error_file)

def run_test(model):
    crash_path = "/debug/crashes"
    gemma_hang_path = "/debug/hangs/gemma"
    codellama_hang_path = "/debug/hangs/codellama"
    mistral_hang_path = "/debug/hangs/mistral"
    gemma_cmin_path = "/debug/cmin"
    mistral_cmin_path = "/debug/mistral-cmin2"
    codellama_cmin_path = "/debug/codellama-cmin2"
    gemma_path = "/debug/queue"
    mistral_path = "/debug/mistral"
    codellama_path = "/debug/codellama-queue1"

    match model:
        case "1":
            read_files(crash_path, "gemma_crash_re.txt", "gemma_crash_err.txt")
        case "2":
            read_files(gemma_hang_path, "gemma_hang_re.txt", "gemma_hang_err.txt")
        case "3":
            read_files(codellama_hang_path, "codellama_hang_re.txt", "codellama_hang_err.txt")
        case "4":
            read_files(mistral_hang_path, "mistral_hang_re.txt", "mistral_hang_err.txt")
        case "5":
            read_files(gemma_cmin_path, "gemma_mini_result2.txt", "gemma_mini_error2.txt")
        case "6":
            read_files(codellama_cmin_path, "codellama_mini_result.txt", "codellama_mini_error.txt")
        case "7":
            read_files(mistral_cmin_path, "mistral_mini_result.txt", "mistral_mini_error.txt")
        case "8":
            read_files(gemma_path, "gemma_result2.txt", "gemma_error2.txt")
        case "9":
            read_files(codellama_path, "codellama_result1.txt", "codellama_error1.txt")
        case "10":
            read_files(mistral_path, "mistral_result0.txt", "mistral_error0.txt")
        case _:
            print("test options: ")
            print("-------------------------------------")
            print("1: afl indicated crashes")
            print("2: afl indicated gemma hangs")
            print("3: afl indicated codellama hangs")
            print("4: afl indicated mistral hangs")

            print("5: afl fuzzed minimised gemma test suite")
            print("6: afl fuzzed minimised codellama test suite")
            print("7: afl fuzzed minimised mistral test suite")

            print("8: afl fuzzed gemma test suite")
            print("9: afl fuzzed codellama test suite")
            print("10: afl fuzzed mistral test suite")

            print("-------------------------------------")

            print("Error! please Indicate a number to run your test case of choice")
            print("For example: enter \"1\" to run afl indicated crashes ")
            model = input("Please enter your test case selection: ")
            run_test(model);
    
def main():
    print("test options: ")
    print("-------------------------------------")
    print("1: afl indicated crashes")
    print("2: afl indicated gemma hangs")
    print("3: afl indicated codellama hangs")
    print("4: afl indicated mistral hangs")

    print("5: afl fuzzed minimised gemma test suite")
    print("6: afl fuzzed minimised codellama test suite")
    print("7: afl fuzzed minimised mistral test suite")

    print("8: afl fuzzed gemma test suite")
    print("9: afl fuzzed codellama test suite")
    print("10: afl fuzzed mistral test suite")

    print("-------------------------------------")

    model = input("please enter a number to run your test case of choice: ")
    run_test(model);

if __name__ == "__main__":
    main()
