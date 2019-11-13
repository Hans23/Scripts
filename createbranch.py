#########################################
#Description: This script creates a branch based off a tag in a git repository.
#             The repository needs to be cloned before using this script.
#             This script uses three parameters. 1. Path to repo 2. git Tag 3. New branch name.
########################################
import os
import sys
import subprocess
import re

def exec_cmd(cmd):
    print("Executing: "+cmd)
    res = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    stdout,stderr = res.communicate()
    if stderr:
        if (re.search('^Note: ',stderr.decode('utf-8')) or re.search('^Switched to ',stderr.decode('utf-8')) or re.search('^To ',stderr.decode('utf-8'))):
            pass
        else:
            print("Error: "+stderr.decode('utf-8'))
            exit()
    #Check to see if the cmd is git tag -l to check the output and see if more than one tags were returned. If so, error out.
    if re.search("\stag\s",cmd) :
        if len(stdout) == 0:
            print("The supplied tag %s did not match any existing tags.\n Please correct the tag name and re-run the script." %tag)
            exit()
        elif len(stdout.split()) > 1:
            #print("There are more than one match for the tag %s.\n Please correct tag name and re-run the script.\n Number of matching tags found are: %d \n" %( tag, len(stdout)))
            print("There are more than one match for the tag %s.\n Please correct tag name and re-run the script.\n Number of matching tags found are: %d \nand they are %s" %( tag, len(stdout),stdout))
            exit()
    
    
# Function to validate supplied args  
def check_args(self,*argv):
    global path, tag, branch
    # check the number of arguments passed to script
    if len(sys.argv) < 4:
        print("This script expects 3 arguments: \n1. The absolute path of repo (Ex:/home/<user>/ws/i<repo>)\n2. Tag name (Ex: Release_1.0)\n3. Branch name (Ex:Release_1.0_R1)")
        print("Only %s supplied" % str(len(sys.argv) - 1))
        exit()
    else:
        path, tag, branch = sys.argv[1], sys.argv[2], sys.argv[3]

#Validate the supplied args
def validate_args():
    print("cwd  = "+os.getcwd())
    print("path = "+path + "\n")
    #validate the path
    if os.path.exists(path) == False:
        print("The supplied path %s does not exist. \nPlease provide a valid path" %path)
        exit()
    else:
        exec_cmd('git fetch --all')
        exec_cmd('git tag -l | grep -x '+str(tag))

def create_branch():
    #os.chdir(path)
    exec_cmd('git checkout tags/'+ str(tag))
    exec_cmd('git checkout -b '+ str(branch))
    exec_cmd('git push origin '+str(branch))
    
    
check_args(sys.argv)
print("\n1. Path provided: " + path + " \n2. tag: " + tag + "\n3. branch: " + branch + "\n")
validate_args()
create_branch()
print("\nCreated the branch %s based off of tag %s \n"%(branch,tag))
