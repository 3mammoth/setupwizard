# def installShellScripts():
#   echoPath = "export PATH=\"$PATH:~/Dropbox/Programming/scripts/\""
#   profileFile = open(os.path.expanduser("~") + "/.profile", "a+")
#   profileFileRead = open(os.path.expanduser("~") + "/.profile", "r")
#   if echoPath not in profileFileRead.read().rstrip('\n'):
#     profileFile.write("\n"+echoPath)

#   def _usrbinPath(scriptName):
#     return "/usr/bin/" + scriptName

#   def _dropboxPath(scriptName):
#     return os.path.expanduser("~") + "/Dropbox/Programming/scripts/" + scriptName

#   for scriptName in allShellScripts:
#     call(["chmod", "+x", _dropboxPath(scriptName)])
#     call(["sudo", "rm", "-r", _usrbinPath(scriptName)])
#     call(["sudo", "ln", "-s", _dropboxPath(scriptName), _usrbinPath(scriptName)])

# allShellScripts = ["fd", "grp"]
