import subprocess
fecha = subprocess.check_output(["date", "+%d-%m-%Y %H:%M:%S"]).decode("utf-8").strip()
# Replace the following variables with your own values
repository_url = "https://github.com/DWES-LE/repaso-tercer-trimestre-MohamedElderkaoui.git"
commit_message = "Guardado el " + fecha

# Initialize a new Git repository


# Add all files to the staging area
subprocess.run(["git", "add", "."])

# Commit the changes with a message
subprocess.run(["git", "commit", "-m", commit_message])



# Push the changes to the master branch
subprocess.run(["git", "push", "-u", "origin", "master"])
