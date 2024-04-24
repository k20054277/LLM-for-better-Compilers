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

def main():
	paths = [["/mistral_out/default/queue/","/Python-3.12.3/debug/mistral-queue/"],["/mistral_out/default/queue/","/Python-3.13.0a5/debug/mistral-queue/"],
	["/gemma_out/default/queue/","/Python-3.12.3/debug/gemma-queue/"], ["/gemma_out/default/queue/","/Python-3.13.0a5/debug/mistral-queue/"],
	["/codellama_out/default/queue/","/Python-3.12.3/debug/codellama-queue/"], ["/codellama_out/default/queue/","/Python-3.13.0a5/debug/codellama-queue/"]]

	for s,d in paths:
		copy(s,d)

if __name__ == "__main__":
    main()