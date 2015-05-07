# Should only be called for a new laptop setup

from shortcut_util import *
from program import *


def setup_all_programs_and_shortcuts_for_new_laptop():
    # Download Dropbox, Chrome, iTerm, git, Sublime as well as optionally IntelliJ, PyCharm, and RubyMine first
    # Load iTerm profile
    # ln -s subl "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"
    # git config --global core.editor "subl -n -w" currently not needed since it's in Git config which we will restore
    # Set copy file path here http://www.cnet.com/how-to/how-to-copy-a-file-path-in-os-x/
    for program in all_programs:
        restore_shortcuts(program)
