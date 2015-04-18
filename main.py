# Usage
# python setup.py backup [option, e.g. "-s"]
# python setup.py restore [option, e.g. "-s"]
# python setup.py fresh_install

import sys
import re
from program import *
from utils import USAGE_STRING
from shortcut_util import *
from shell_util import *
from freshinstall_util import *

def checkArgs(args):  
  if len(args) > 3 or len(args) < 2:
    print "Argument length too long or short"
    print USAGE_STRING
    return None

  type = args[1]
  if type != 'shell' and type != 'backup' and type != 'restore':
    print "Operation not valid"
    print USAGE_STRING
    return None

  if len(args) == 2:
    return (type, allPrograms)

  optionsPattern = re.compile("^\-[a-z]+$")
  if optionsPattern.match(args[2]) == None:
    print "Option format incorrect"
    print USAGE_STRING
    return None

  selectedPrograms = []
  for char in args[2][1:]:
    for program in allPrograms:
      if program.commandLineOption == char:
        selectedPrograms.append(program)

  if len(selectedPrograms) == 0:
    print "Program not recognized"
    print USAGE_STRING
    return None

  return (type, selectedPrograms)

def main():
  (type, selectedPrograms) = checkArgs(sys.argv)
  if type == 'shell':
    installShellScripts()
  elif type == 'fresh_install':
    setupAllProgramsAndShortcutsForNewLaptop()
  else:
    for program in selectedPrograms:
      if type == 'backup':
        backupShortcuts(program)
      elif type == 'restore':
        restoreShortcuts(program)

main()