import os
import sys
import shutil

moveDir = os.path.expanduser("~")+"/.local/share/githide/"
verbose = True

def verbose(msg):
	if verbose:
		print(msg)

def init():
	verbose("[INFO] Every .git/ folder are moved in "+moveDir)

	if not os.path.isdir(moveDir) and not os.path.exists(moveDir):
		verbose("[INFO] "+moveDir+" doesn't exists. Creating it...")
		os.makedirs(moveDir)

def githide():
	src = os.getcwd()+"/.git/"
	dst = moveDir+"/"+os.path.basename(os.getcwd())

	init()
	
	if os.path.isdir(src) and os.path.exists(src):
		print("[INFO] Found .git folder in "+os.getcwd())

		if not os.path.isdir(dst) and not os.path.exists(dst):
			verbose("[INFO] Preparing a comfy place...")
			os.makedirs(dst)
		
		verbose("[INFO] Moving .git/ to his new home...")
		
		shutil.move(src,dst)
	else:
		verbose("[ERROR] Couldn't find a .git folder. Are you sure to be in the root of your git repository ?")

def gitshow():
	dst = os.getcwd()
	src = moveDir+"/"+os.path.basename(os.getcwd())+"/.git/"

	init()

	if os.path.isdir(src) and os.path.exists(src):
		print("[INFO] Found a matching backup for "+os.path.basename(os.getcwd()))

		if os.path.isdir(dst+"/.git/") and os.path.exists(dst+"/.git/"):
			verbose("[ERROR] A .git/ golder is already in place in this folder. Interrupting operations !")
		else:
			verbose("[INFO] Restauring .git/ backup...")
			shutil.move(src,dst)
	else:
		verbose("[ERROR] Couldn't find the backup of your .git folder. Are you sure to be in the root of your git repository ?")
