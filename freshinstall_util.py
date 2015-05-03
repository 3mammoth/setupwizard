# Should only be called for a new laptop setup

from shortcut_util import *
from program import *


def setupAllProgramsAndShortcutsForNewLaptop():
    # Download Dropbox, Chrome, iTerm, and Sublime first
    # Load iTerm profile
    # call(["ln", "-s", "subl", "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"])
    # ln -s subl "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"
    # git config --global core.editor "subl -n -w"
    # ln -s subl "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"
    # alias gs='git status '
    # alias ga='git add '
    # alias gb='git branch '
    # alias gc='git commit'
    # alias gd='git diff'
    # alias gsh='git stash'
    # alias gr='git rebase -i'
    for program in allPrograms:
        restoreShortcuts(program)
