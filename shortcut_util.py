from subprocess import call
from program import *
import os


def backupShortcuts(program):
    if not os.path.exists(program.getAppDirectory()) and program.appName not in allSpecialPrograms:
        print program.appName + " not installed!  Skipping it"
        return

    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    call(["cp", program.keyMapLocation, program.getShortcutBackupLocation()])


def restoreShortcuts(program):
    if (not os.path.exists(program.getAppDirectory())) and program.appName not in allSpecialPrograms:
        print program.appName + " not installed! Skipping it"
        return

    if not os.path.exists(program.getShortcutBackupLocation()):
        print ("Shortcut for %s doens't exist!" % program.appName)

    call(["sudo", "cp", program.getShortcutBackupLocation(), program.keyMapLocation])
