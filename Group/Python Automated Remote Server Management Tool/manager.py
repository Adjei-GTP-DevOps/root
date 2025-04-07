import getpass
# import rc
import paramiko
import subprocess
import json
from datetime import datetime




with open("config.json", "r") as file:
    config = json.load(file)

host = config["server"]["host"]
username = config["server"]["username"]
local_commands = config["local_commands"]
remote_commands = config["remote_commands"]

user_password = getpass.getpass(f"Please enter your secret password for {username}@{host}:")

results = {"timestamp": str(datetime.now()), "local": {}, "remote": {}}

print("\n Executing local commands ... \n")
for cmd in local_commands:
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        results["local"][cmd] = {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
        print(f"SUCCESS - {cmd} -> {result.stdout.strip()}")
    except Exception as e:
        results["local"][cmd] = str(e)
        print(f"FAILED - {cmd} -> {e}")


print("\n Connecting to remote server ... \n")
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=user_password)

    for cmd in remote_commands:
        stdin, stdout, stderr = client.exec_command(cmd)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        results["remote"][cmd] = {
            "stdout": output,
            "stderr": error
        }
        print(f"SUCCESS - {cmd} -> {output}")

    client.close()

except Exception as e:
    print(f"SSH connection failed: {e}")
    results["remote"]["error"] = str(e)


# save results to file
log_filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(log_filename, "w") as log_file:
    json.dump(results, log_file, indent=4)

print(f"\n Results saved to {log_filename}")