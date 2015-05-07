from utils import *


class Program():
    def __init__(self, command_line_option, key_map_location, app_name=None, backup_file_name=None):
        if app_name is None and backup_file_name is None:
            raise Exception('At least one of app name and backup file name should be specified')
        self.commandLineOption = command_line_option
        self.appName = app_name
        self.keyMapLocation = key_map_location
        self.backUpDestination = backup_file_name
        if backup_file_name is None:
            self.backUpDestination = app_name

    def get_app_directory(self):
        return "/Applications/" + self.appName + ".app"

    def get_shortcut_backup_location(self):
        return BACKUP_FOLDER + "/" + self.backUpDestination

# iTerm currently dysfunctional
# http://apple.stackexchange.com/questions/111534/iterm2-doesnt-read-com-googlecode-iterm2-plist
# iTerm = Program("t", "iTerm", os.path.expanduser("~") + "/Library/Preferences/com.googlecode.iterm2.plist")

# Mac
# https://discussions.apple.com/thread/2216176
# http://apple.stackexchange.com/questions/87619/where-are-keyboard-shortcuts-stored-for-backup-and-sync-purposes
# http://superuser.com/questions/670584/how-can-i-migrate-all-keyboard-shortcuts-from-one-mac-to-another
# http://stackoverflow.com/questions/823705/programatically-get-set-mac-osx-default-system-keyboard-shortcut

# ~/Library/Preferences/.GlobalPreferences.plist
# ~/Library/Preferences/com.apple.finder.plist
# ~/Library/Preferences/com.apple.symbolichotkeys.plist

all_programs = [
    Program("m", os.path.expanduser("~") + "/Library/Preferences/.GlobalPreferences.plist",
            backup_file_name="Mac Global Preferences"),
    Program("m2", os.path.expanduser("~") + "/Library/Preferences/com.apple.symbolichotkeys.plist",
            backup_file_name="Mac Symbolic Hot Keys"),
    Program("f", os.path.expanduser("~") + "/Library/Preferences/com.apple.finder.plist",
            backup_file_name="Finder"),
    Program("x", os.path.expanduser("~") + "/Library/Developer/Xcode/UserData/KeyBindings/Ray.idekeybindings",
            app_name="Xcode"),
    Program("i", os.path.expanduser("~") + "/Library/Preferences/IdeaIC14/keymaps/Ray.xml",
            app_name="IntelliJ IDEA 14 CE"),
    Program("r", os.path.expanduser("~") + "/Library/Preferences/RubyMine70/keymaps/Ray.xml",
            app_name="RubyMine"),
    Program("p", os.path.expanduser("~") + "/Library/Preferences/PyCharm40/keymaps/Ray.xml",
            app_name="PyCharm CE"),
    Program("b", os.path.expanduser("~") + "/.bash_profile", backup_file_name="Bash"),
    Program("g", os.path.expanduser("~") + "/.gitconfig", backup_file_name="GitConfig"),
    Program("s", os.path.expanduser(
            "~") + "/Library/Application Support/Sublime Text 2/Packages/User/Default (OSX).sublime-keymap",
            app_name="Sublime Text 2", backup_file_name="Sublime_Key"),
    Program("s2", os.path.expanduser(
            "~") + "/Library/Application Support/Sublime Text 2/Packages/User/Preferences.sublime-settings",
            app_name="Sublime Text 2", backup_file_name="Sublime_Setting")
]
