#1/usr/bin.python:w!
#########################################
#Description: This script commits the files in your worksapce 
########################################
import os
import sys
import subprocess

file_list = ""
branch = ""
path = ""
path = os.getcwd()
print("Current Workspace is  = "+path)

def exec_cmd(cmd):
    print("\nExecuting: "+cmd)
    res = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    stdout,stderr = res.communicate()
    if stderr:
       print("error: "+stderr.decode('utf-8'))
       exit()  
    return(stdout.decode('utf-8').split())

def validate_repo():
    global branch
    if os.path.exists(path+"/.git") == False:
        print("Current working folder does not seem to be a git repo. \nPlease execute this tool from the root of a repo")
        exit()
   
    branch = exec_cmd('git branch | grep \"*\"')
    branch = branch[-1] 
    print("Current branch is  " +branch)
    cont = input("Is this correct ? (y/n) : ")
    if cont.lower().strip() not in ['y','Y']:
       exit()

def collect_changes():
    global file_list
    # Check for newly added files or untracked files
    untracked_files = exec_cmd('git ls-files --others --exclude-standard')
    print("\nFollowing are untracked files.\nPlease add them if you want to commit and push them. ")
    for uf in list(untracked_files):
        print(uf)
    files = exec_cmd('git ls-files -m')
    if len(list(files)) ==0 :
        print("There are no changes to be committed:")
        exit()
    print("List of files to be committed :")
    for file in list(files):
       print(file)
       file_list += file+' '

def commit_changes():
    commit_message = input("Enter the commit message : ")
     
    if commit_message == "":
        print("No cimmit message entered. Exiting...")
        exit()
    else:
        res = exec_cmd('git commit -m \"'+commit_message+'\" '+file_list)
    
    if "error: " in res:
        s = " ".join(res)
        print("There was an error in commiting a file(s):\n %s" %s)
        exit()
    
def push_changes():
    res = exec_cmd('git push origin '+str(branch))
    if "error: " in res:
        s = " ".join(res)
        print("There was an error in pushing the file(s):\n %s" %s)
        exit()
    
validate_repo()
collect_changes()
commit_changes()
push_changes()
print("\nCommitted and pushed files to %s \n"%(branch))
