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

# Packages/User/Preferences.sublime-settings
Sublime_Key = Program("s", "Sublime Text 2", os.path.expanduser("~") + "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap")

# Sublime_Setting = Program("s", "Sublime Text 2", \
#   os.path.expanduser("~") + \
#   "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap")

# iTerm currently dysfunctional
# iTerm = Program("t", "iTerm", os.path.expanduser("~") + "/Library/Preferences/com.googlecode.iterm2.plist")
Xcode = Program("x", "Xcode", os.path.expanduser("~") + "/Library/Developer/Xcode/UserData/KeyBindings/Ray.idekeybindings")
IntelliJ = Program("i", "IntelliJ IDEA 13", os.path.expanduser("~") + "/Library/Preferences/IntelliJIdea13/keymaps/Ray.xml")
RubyMine = Program("r", "RubyMine", os.path.expanduser("~") + "/Library/Preferences/RubyMine70/keymaps/Ray.xml")
Bash = Program("b", "Bash", os.path.expanduser("~") + "/.bash_profile")

allPrograms = [Sublime_Key, Xcode, IntelliJ, RubyMine, Bash]
allSpecialPrograms = [Bash.appName]
