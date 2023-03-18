"""
Lists all tracked files from the current git repository.

It shows the relative path to the repository.
"""
import git # pip install GitPython

# Raises an except if no git repo exists
repo = git.Repo('.')

# use f.fullpath to show the full path
files = [f.path for f in repo.commit().tree.traverse()]
