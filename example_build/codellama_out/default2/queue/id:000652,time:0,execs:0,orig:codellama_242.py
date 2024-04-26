import subprocess

# create a new process using the 'ping' command
proc = subprocess.Popen(['ping', '-c 2', 'example.com'], stdout=subprocess.PIPE)

# wait for the process to finish and get its return code
output, error = proc.communicate()
return_code = proc.wait()

if return_code == False:
    print("Ping was successful")
else:
    print("Ping failed")