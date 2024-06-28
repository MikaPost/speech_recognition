"""
This file is for our new theme: speech_recognition
Created by: Miqayel Postoyan
Date: 28 June
"""
import speech_recognition as sr
import pyttsx3
import os
import platform

def listen(text):
    """
    Function: listen
    Brief: Captures and recognizes speech input from the user.
    Params: text (str) - The prompt text to speak to the user.
    Return: task (str) - The recognized speech as text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        start.say(text)
        print(text)
        start.runAndWait()

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            task = r.recognize_google(audio).lower()
            print(task)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            task = listen("I'm hearing you")
        return task

def open_google():
    """
    Function: open_google
    Brief: Opens the Google Chrome browser.
    """
    start.say("open the google")
    print("open the google")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('start chrome')
    elif os_name == "Darwin":
        os.system('open -a "Google Chrome"')
    elif os_name == "Linux":
        os.system('google-chrome')

def create_file():
    """
    Function: create_file
    Brief: Creates a new file with the specified name.
    """
    file_name = listen("name file")
    with open(file_name, 'w') as f:
        f.write("This is a new file.")
    text = f"File {file_name} created."
    start.say(text)
    start.runAndWait()

def delete_file():
    """
    Function: delete_file
    Brief: Deletes a file with the specified name.
    """
    file_name = listen("name file to delete")
    if os.path.exists(file_name):
        os.remove(file_name)
        text = f"File {file_name} deleted."
    else:
        text = f"File {file_name} does not exist."
    start.say(text)
    start.runAndWait()

def create_directory():
    """
    Function: create_directory
    Brief: Creates a new directory with the specified name.
    """
    dir_name = listen("name directory")
    os.makedirs(dir_name, exist_ok=True)
    text = f"Directory {dir_name} created."
    start.say(text)
    start.runAndWait()

def delete_directory():
    """
    Function: delete_directory
    Brief: Deletes a directory with the specified name.
    """
    dir_name = listen("name directory to delete")
    if os.path.exists(dir_name):
        os.rmdir(dir_name)
        text = f"Directory {dir_name} deleted."
    else:
        text = f"Directory {dir_name} does not exist."
    start.say(text)
    start.runAndWait()

def list_files():
    """
    Function: list_files
    Brief: Lists all files in the specified directory.
    """
    dir_name = listen("name directory to list files")
    files = os.listdir(dir_name)
    text = f"Files in {dir_name}: {', '.join(files)}"
    start.say(text)
    start.runAndWait()

def rename_file():
    """
    Function: rename_file
    Brief: Renames a file from an old name to a new name.
    """
    old_name = listen("name file to rename")
    new_name = listen("new name for file")
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        text = f"File {old_name} renamed to {new_name}."
    else:
        text = f"File {old_name} does not exist."
    start.say(text)
    start.runAndWait()

def open_text_editor():
    """
    Function: open_text_editor
    Brief: Opens the default text editor based on the OS.
    """
    start.say("open text editor")
    print("open text editor")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('notepad')
    elif os_name == "Darwin":
        os.system('open -a "TextEdit"')
    elif os_name == "Linux":
        os.system('gedit')

def shutdown_computer():
    """
    Function: shutdown_computer
    Brief: Shuts down the computer.
    """
    start.say("Shutting down the computer")
    print("Shutting down the computer")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('shutdown /s /t 1')
    elif os_name == "Darwin":
        os.system('sudo shutdown -h now')
    elif os_name == "Linux":
        os.system('shutdown -h now')

def restart_computer():
    """
    Function: restart_computer
    Brief: Restarts the computer.
    """
    start.say("Restarting the computer")
    print("Restarting the computer")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('shutdown /r /t 1')
    elif os_name == "Darwin":
        os.system('sudo shutdown -r now')
    elif os_name == "Linux":
        os.system('shutdown -r now')

def sleep_computer():
    """
    Function: sleep_computer
    Brief: Puts the computer to sleep.
    """
    start.say("Putting the computer to sleep")
    print("Putting the computer to sleep")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    elif os_name == "Darwin":  # macOS
        os.system('pmset sleepnow')
    elif os_name == "Linux":
        os.system('systemctl suspend')
    else:
        text = f"Unsupported OS: {os_name}"
        start.say(text)
        start.runAndWait()

def hibernate_computer():
    """
    Function: hibernate_computer
    Brief: Hibernates the computer.
    """
    start.say("Hibernating the computer")
    print("Hibernating the computer")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('shutdown /h')
    elif os_name == "Darwin":  # macOS
        os.system('pmset hibernatemode 25')
    elif os_name == "Linux":
        os.system('systemctl hibernate')
    else:
        text = f"Unsupported OS: {os_name}"
        start.say(text)
        start.runAndWait()

def logoff_user():
    """
    Function: logoff_user
    Brief: Logs off the current user.
    """
    start.say("Logging off the user")
    print("Logging off the user")
    start.runAndWait()

    os_name = platform.system()
    if os_name == "Windows":
        os.system('shutdown /l')
    elif os_name == "Darwin":  # macOS
        os.system('osascript -e \'tell application "System Events" to log out\'')
    elif os_name == "Linux":
        os.system('gnome-session-quit --logout --no-prompt')
    else:
        text = f"Unsupported OS: {os_name}"
        start.say(text)
        start.runAndWait()

def request(task):
    """
    Function: request
    Brief: Maps the recognized task to the corresponding function.
    Params: task (str) - The task to be performed.
    """
    if "google" in task.lower():
        open_google()
    elif "create file" in task.lower():
        create_file()
    elif "delete file" in task.lower():
        delete_file()
    elif "create directory" in task.lower():
        create_directory()
    elif "delete directory" in task.lower():
        delete_directory()
    elif "list files" in task.lower():
        list_files()
    elif "rename file" in task.lower():
        rename_file()
    elif "open text editor" in task.lower():
        open_text_editor()
    elif "shutdown the computer" in task.lower():
        shutdown_computer()
    elif "restart the computer" in task.lower():
        restart_computer()
    elif "sleep" in task.lower():
        sleep_computer()
    elif "hibernate" in task.lower():
        hibernate_computer()
    elif "log off" in task.lower():
        logoff_user()

def main():
    """
    Function: main
    Brief: Entry point of the program.
    """
    global start
    start = pyttsx3.init()

    while True:
        request(listen("I'm hearing you"))

if __name__ == "__main__":
    main()
