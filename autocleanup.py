import os
import datetime

current_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
dir_sub_path = "_old"
now = datetime.datetime.now()

#Get the current date and format it
today = now.strftime("%Y%m%d")
directory_name = today + dir_sub_path


try:
    os.chdir("C:\\Users\\cho50\\Downloads")
    cwd = os.getcwd()
    print("change current directory to: " + cwd)
except WindowsError:
    print("cannot change to directory")


if not os.path.exists(directory_name):
    print("Creating directory: " + directory_name)
    os.makedirs(directory_name)


with os.scandir(cwd) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print("*" + entry.name)