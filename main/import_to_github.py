import os
import subprocess

# Configuration
repo_url = "https://github.com/TON-UTILISATEUR/TON-DÉPÔT.git"  # Remplace par ton URL GitHub
file_to_add = "Test.json" 
commit_message = "Add example.json file"  # Message du commit

# Clone le dépôt si nécessaire
if not os.path.exists("TON-DÉPÔT"):
    subprocess.run(["git", "clone", repo_url])

# Se déplacer dans le dossier du dépôt
os.chdir("TON-DÉPÔT")

# Ajouter le fichier au dépôt
subprocess.run(["git", "add", file_to_add])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])
