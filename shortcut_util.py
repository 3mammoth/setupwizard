from subprocess import call
from program import *
import os


def backup_shortcuts(program):
    if not os.path.exists(program.get_app_directory()) and program.appName not in all_special_programs:
        print program.appName + " not installed!  Skipping it"
        return

    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    call(["cp", program.keyMapLocation, program.get_shortcut_backup_location()])


def restore_shortcuts(program):
    if (not os.path.exists(program.get_app_directory())) and program.appName not in all_special_programs:
        print program.appName + " not installed! Skipping it"
        return

    if not os.path.exists(program.get_shortcut_backup_location()):
        print ("Shortcut for %s doens't exist!" % program.appName)

    call(["sudo", "cp", program.get_shortcut_backup_location(), program.keyMapLocation])
