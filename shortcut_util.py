from subprocess import call

from program import *


def backup_shortcuts(program):
    if program.appName is not None and not os.path.exists(program.get_app_directory()):
        print program.appName + " not installed!  Skipping it"
        return

    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    call(["cp", program.keyMapLocation, program.get_shortcut_backup_location()])


def restore_shortcuts(program):
    if program.appName is not None and (not os.path.exists(program.get_app_directory())):
        print program.appName + " not installed! Skipping it"
        return

    if not os.path.exists(program.get_shortcut_backup_location()):
        print ("Shortcut for %s doens't exist!" % program.appName)
        return

    if not os.path.exists(os.path.dirname(program.keyMapLocation)):
        os.makedirs(os.path.dirname(program.keyMapLocation))

    call(["sudo", "cp", program.get_shortcut_backup_location(), program.keyMapLocation])
