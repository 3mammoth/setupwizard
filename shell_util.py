import os


def install_shell_scripts():
    echo_path = "export PATH=\"$PATH:~/Dropbox/Programming/scripts/\""
    profile_file = open(os.path.expanduser("~") + "/.profile", "a+")
    profile_file_read = open(os.path.expanduser("~") + "/.profile", "r")
    if echo_path not in profile_file_read.read().rstrip('\n'):
        profile_file.write("\n" + echo_path)

# def _usrbinPath(scriptName):
#     return "/usr/bin/" + scriptName

#   def _dropboxPath(scriptName):
#     return os.path.expanduser("~") + "/Dropbox/Programming/scripts/" + scriptName

#   for scriptName in allShellScripts:
#     call(["chmod", "+x", _dropboxPath(scriptName)])
#     call(["sudo", "rm", "-r", _usrbinPath(scriptName)])
#     call(["sudo", "ln", "-s", _dropboxPath(scriptName), _usrbinPath(scriptName)])

# allShellScripts = ["fd", "grp"]
