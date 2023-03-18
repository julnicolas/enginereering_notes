"""
Lists all tracked files from the current git repository.
"""
import git # pip install GitPython

# Raises an except if no git repo exists
repo = git.Repo('.') 
files = [f.name for f in repo.commit().tree.traverse()]
