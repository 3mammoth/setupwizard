from utils import *


class Program():
    def __init__(self, command_line_option, app_name, key_map_location):
        self.commandLineOption = command_line_option
        # which package should in ~/Library/Appliation Support we look into?
        self.appName = app_name
        # where is the key mapping file
        self.keyMapLocation = key_map_location

    def get_app_directory(self):
        return "/Applications/" + self.appName + ".app"

    def get_shortcut_backup_location(self):
        return BACKUP_FOLDER + "/" + self.appName


Sublime_Key = Program("s", "Sublime Text 2", os.path.expanduser(
    "~") + "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap")

# TODO
# Sublime_Setting = Program("s", "Sublime Text 2", \
# os.path.expanduser("~") + \
#   "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap")

# iTerm currently dysfunctional
# http://apple.stackexchange.com/questions/111534/iterm2-doesnt-read-com-googlecode-iterm2-plist
# iTerm = Program("t", "iTerm", os.path.expanduser("~") + "/Library/Preferences/com.googlecode.iterm2.plist")

# Mac
# https://discussions.apple.com/thread/2216176
# http://apple.stackexchange.com/questions/87619/where-are-keyboard-shortcuts-stored-for-backup-and-sync-purposes

Xcode = Program("x", "Xcode",
                os.path.expanduser("~") + "/Library/Developer/Xcode/UserData/KeyBindings/Ray.idekeybindings")
IntelliJ = Program("i", "IntelliJ IDEA 14 CE",
                   os.path.expanduser("~") + "/Library/Preferences/IdeaIC14/keymaps/Ray.xml")
RubyMine = Program("r", "RubyMine", os.path.expanduser("~") + "/Library/Preferences/RubyMine70/keymaps/Ray.xml")
PyCharm = Program("p", "PyCharm CE", os.path.expanduser("~") + "/Library/Preferences/PyCharm40/keymaps/Ray.xml")
Bash = Program("b", "Bash", os.path.expanduser("~") + "/.bash_profile")

all_programs = [Sublime_Key, Xcode, IntelliJ, RubyMine, Bash, PyCharm]

# Applications not listed under the /Applications folder
all_special_programs = [Bash.appName]
