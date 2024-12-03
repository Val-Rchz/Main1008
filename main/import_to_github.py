import os
import subprocess


repo_url = "https://github.com/Val-Rchz/Main1008/tree/main/main.git"  
file_to_add = "Test.json" 
commit_message = "Add example.json file" 

if not os.path.exists("Test"):
    subprocess.run(["git", "clone", repo_url])

os.chdir("Test")

subprocess.run(["git", "add", file_to_add])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])
