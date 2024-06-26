import shutil
import os

def copy(source, des):
	source = os.getcwd() + source
	des = os.getcwd() + des
	print("-------------------------------------")
	if (os.path.exists(source) and os.path.exists(des)):
		print(f"Moving from {source} to {des}")
		print("...")
		shutil.copytree(source, des, dirs_exist_ok=True)
		print("Done!")
	else:
		print(f"!!! Move from {source} to {des} could not be completed. Check if directory exsits !!!")
	print("-------------------------------------")
def move(model):
	paths1 = [["/mistral_out/default/queue/","/Python-3.12.3/debug/mistral-afl/"],["/mistral_out/default/queue/","/Python-3.13.0a5/debug/mistral-afl/"],
	["/gemma_out/default/queue/","/Python-3.12.3/debug/gemma-afl/"], ["/gemma_out/default/queue/","/Python-3.13.0a5/debug/mistral-afl/"],
	["/codellama_out/default/queue/","/Python-3.12.3/debug/codellama-afl/"], ["/codellama_out/default/queue/","/Python-3.13.0a5/debug/codellama-afl/"]]

	paths2 = [["/Python-3.12.3/output/","/compare/3.12/"],["/Python-3.13.0a5/output/","/compare/3.13/"]]

	if model == "1":
		for s,d in paths1:
                        copy(s,d)
	elif model == "2":
		for s,d in paths2:
                        copy(s,d)
	else:
		print("Error! please Indicate a number to run your test case of choice")
		print("For example: enter \"1\" to Move output queue from AFL directory to Compiler directory")
		print("Options")
		print("-------------------------------------")
		print("1: Move output queue from AFL directory to Compiler directory")
		print("1: Move Compiler results from Compiler directory to Compare directory")
		print("-------------------------------------")
		model = input("Please enter your test case selection: ")
		move(model)

def main():
	print("Options")
	print("-------------------------------------")
	print("1: Move output queue from AFL directory to Compiler directory")
	print("2: Move Compiler results from Compiler directory to Compare directory")
	print("-------------------------------------")
	model = input("please enter a number to move your choice: ")
	move(model);

if __name__ == "__main__":
    main()
