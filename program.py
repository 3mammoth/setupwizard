import os
from utils import *

class Program():
   def __init__(self, commandLineOption, appName, keyMapLocation):
      self.commandLineOption = commandLineOption 
      # which package should in ~/Library/Appliation Support we look into?
      self.appName = appName
      # where is the key mapping file
      self.keyMapLocation = keyMapLocation

   def getAppDirectory(self):
      return "/Applications/" + self.appName + ".app"

   def getShortcutBackupLocation(self):
      return BACKUP_FOLDER + "/" + self.appName

Sublime_Key = Program("s", "Sublime Text 2", os.path.expanduser("~") + "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap")

#  TODO
# Sublime_Setting = Program("s", "Sublime Text 2", \
#   os.path.expanduser("~") + \
#   "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap")

# iTerm currently dysfunctional
# http://apple.stackexchange.com/questions/111534/iterm2-doesnt-read-com-googlecode-iterm2-plist
# iTerm = Program("t", "iTerm", os.path.expanduser("~") + "/Library/Preferences/com.googlecode.iterm2.plist")

# Mac
# https://discussions.apple.com/thread/2216176
# http://apple.stackexchange.com/questions/87619/where-are-keyboard-shortcuts-stored-for-backup-and-sync-purposes

Xcode = Program("x", "Xcode", os.path.expanduser("~") + "/Library/Developer/Xcode/UserData/KeyBindings/Ray.idekeybindings")
IntelliJ = Program("i", "IntelliJ IDEA 13", os.path.expanduser("~") + "/Library/Preferences/IntelliJIdea13/keymaps/Ray.xml")
RubyMine = Program("r", "RubyMine", os.path.expanduser("~") + "/Library/Preferences/RubyMine70/keymaps/Ray.xml")
Bash = Program("b", "Bash", os.path.expanduser("~") + "/.bash_profile")

allPrograms = [Sublime_Key, Xcode, IntelliJ, RubyMine, Bash]

# Appliations not listed under the /Applications folder
allSpecialPrograms = [Bash.appName]
