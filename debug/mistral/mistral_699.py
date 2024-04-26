
import subprocess

# Boolean variable definition
is_run = True

if is_run:
    # Using subprocess to run batch file
    subprocess.call('path_to_your_batchfile.bat')
else:
    print("Batch file not executed")
