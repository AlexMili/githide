# GitHide
GitHide is a simple tool allowing you to move away your ```.git/``` folder and restore it whenever you want.

## Installation
After cloning this repository simply run :
```bash
cd githide/
pip install -e .
```

## Usage
To "hide" a git repository :
```bash
cd my_repo_git/
githide
```
Output :
```
[INFO] Every .git/ folder are moved in /home/yourname/.local/share/githide/
[INFO] Found .git folder in /home/yourname/my_repo_git
[INFO] Preparing a comfy place...
[INFO] Moving .git/ to his new home...
```
To "show" the same git repository :
```bash
gitshow
```
Output :
```
[INFO] Every .git/ folder are moved in /home/yourname/.local/share/githide/
[INFO] Found a matching backup for my_repo_git
[INFO] Restauring .git/ backup...
```
