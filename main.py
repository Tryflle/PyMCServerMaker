import os
import urllib.request
import time

filepath = os.path.expanduser("~\\Documents\\PythonServer")
jarfilepath = os.path.expanduser("~\\Documents\\PythonServer\\paper.jar")
print("Target directory is " + filepath)
file_check = os.path.exists(filepath)
jarfile_check = os.path.isfile(jarfilepath)
if file_check:
    print("Directory already exists at " + filepath)
    print("Proceeding without creating directory.")
else:
    print("Making directory at " + filepath)
    os.mkdir(filepath)


def v1_8():
    if not jarfile_check:
        print("Downloading Paper 1.8.9 to " + jarfilepath)
        urllib.request.urlretrieve(
            "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar",
            jarfilepath)
        return True
    else:
        print("A server jar already exists here, delete it to continue! The file is located inside " + filepath)
        selectmenu()
        return False


def v1_12():
    if not jarfile_check:
        print("Downloading Paper 1.12.2 to " + jarfilepath)
        urllib.request.urlretrieve(
            "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
            jarfilepath)
    else:
        print("A server jar already exists here, delete it to continue! The file is located inside " + filepath)
        selectmenu()


def v1_16():
    if not jarfile_check:
        print("Downloading Paper 1.16.5 to " + jarfilepath)
        urllib.request.urlretrieve(
            "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
            jarfilepath)
    else:
        print("A server jar already exists here, delete it to continue! The file is located inside " + filepath)
        selectmenu()


def v1_19():
    if not jarfile_check:
        print("Downloading Paper 1.19.4 to " + jarfilepath)
        urllib.request.urlretrieve(
            "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
            jarfilepath)
    else:
        print("A server jar already exists here, delete it to continue! The file is located inside " + filepath)
        selectmenu()


def v1_20():
    if not jarfile_check:
        print("Downloading Paper 1.20.1 to " + jarfilepath)
        urllib.request.urlretrieve(
            "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/45/downloads/paper-1.20.1-45.jar",
            jarfilepath)
    else:
        print("A server jar already exists here, delete it to continue! The file is located inside " + filepath)
        selectmenu()


def vlist():
    print("What version would you like to install")
    print("Options:")
    print("1. 1.8.9")
    print("2. 1.12.2")
    print("3. 1.16.5")
    print("4. 1.19.4")
    print("5. 1.20.1")


def selectmenu():
    while True:
        user_input = input("Input your selection (1-5) ")
        if user_input == "1":
            v1_8()
            break
        if user_input == "2":
            v1_12()
            break
        if user_input == "3":
            v1_16()
            break
        if user_input == "4":
            v1_19()
            break
        if user_input == "5":
            v1_20()
            break
        else:
            print("Invalid selection, try again.")
            selectmenu()


print("Welcome to ServerStarter.py!")
vlist()
selectmenu()
ramone = """java -Xmx1024M -Xms1024M -jar paper.jar nogui
PAUSE
"""
ramtwo = """java -Xmx2048M -Xms2048M -jar paper.jar nogui
PAUSE
"""
ramthree = """java -Xmx3072M -Xms3072M -jar paper.jar nogui
PAUSE"""
ramfour = """java -Xmx4096M -Xms4096M -jar paper.jar nogui
PAUSE"""


def create_batch_file(ram_content, batch_file_path):
    with open(batch_file_path, "w") as batch_file:
        batch_file.write(ram_content)


create_batch_file(ramone, filepath + "\\run_1024M.bat")
create_batch_file(ramtwo, filepath + "\\run_2048M.bat")
create_batch_file(ramthree, filepath + "\\run_3072M.bat")
create_batch_file(ramfour, filepath + "\\run_4096M.bat")
print("Wrote .bat start files with various different ram configurations.")
print("If you need to specify the use of a different Java Runtime you can:")
print("Set your JAVA_HOME to the bin file of your updated java runtime")
print("OR")
print("Replace java in the batch file with the path to the proper JDK's java.exe")
time.sleep(2)


def accept_eula(content, file_path):
    with open(file_path, "w") as text_file:
        text_file.write(content)


eula = "eula = true"


def legalities_hehe():
    while True:
        print("Yes = 1")
        print("No = 2")
        user_input = input("Do you accept Mojang's EULA? ")
        if user_input == "1":
            accept_eula(eula, filepath + "\\eula.txt")
            print("Eula set to true.")
            break
        if user_input == "2":
            print("Well, unless you change that response, you aren't running a server.")
            print("Goodbye lol!")
            time.sleep(3)
            exit(code=2)
            break
        else:
            print("Invalid answer. Please try again.")
            legalities_hehe()


legalities_hehe()


def open_explorer_window(folder_path):
    try:
        os.startfile(folder_path)
    except Exception as e:
        print(f"Error opening Explorer window: {e}")


open_explorer_window(filepath)
print("Try run.bat with the amount of ram you want to use to start it.")
print("Thanks for using my tool!")
print("Exiting in 5 seconds.")
time.sleep(5)
exit(code=1)