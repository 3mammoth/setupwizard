# Usage
# python setup.py backup [option, e.g. "-s"]
# python setup.py restore [option, e.g. "-s"]
# python setup.py fresh_install

import sys
import re

from freshinstall_util import *
from shell_util import install_shell_scripts


def check_args(args):
    if len(args) > 3 or len(args) < 2:
        print "Argument length too long or short"
        print USAGE_STRING
        return None

    program_type = args[1]
    if program_type != 'shell' and program_type != 'backup' and program_type != 'restore':
        print "Operation not valid"
        print USAGE_STRING
        return None

    if len(args) == 2:
        return program_type, all_programs

    options_pattern = re.compile("^\-[a-z0-9]+$")
    if options_pattern.match(args[2]) is None:
        print "Option format incorrect"
        print USAGE_STRING
        return None

    selected_program = None
    for program in all_programs:
        if program.commandLineOption == args[2][1:]:
            selected_program = program

    if selected_program is None:
        print "Program not recognized"
        print USAGE_STRING
        return None

    return program_type, selected_program


def main():
    (program_type, program) = check_args(sys.argv)
    if program_type == 'shell':
        install_shell_scripts()
    elif program_type == 'fresh_install':
        setup_all_programs_and_shortcuts_for_new_laptop()
    elif program_type == 'backup':
        backup_shortcuts(program)
    elif program_type == 'restore':
        restore_shortcuts(program)


main()