# Should only be called for a new laptop setup

from shortcut_util import * 
from program import *
from subprocess import call

def setupAllProgramsAndShortcutsForNewLaptop():
  # Download Dropbox, Chrome, iTerm, and Sublime first
  # Load iTerm profile
  # call(["ln", "-s", "subl", "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"])
  # ln -s subl "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" 
  # git config --global core.editor "subl -n -w"
  # git config --global alias.co checkout
  for program in allPrograms:
  	restoreShortcuts(program)
