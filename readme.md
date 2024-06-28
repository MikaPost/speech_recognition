# Speech Recognition Command Executor

This project allows you to execute various operating system commands based on spoken input using speech recognition and text-to-speech functionality.

## Introduction

The Speech Recognition Command Executor is a Python application that listens to voice commands and performs corresponding actions on your computer, such as opening Google Chrome, creating and deleting files and directories, shutting down or restarting the computer, and more.

## Features

- **Voice Commands**: Execute OS commands through voice input.
- **Text-to-Speech Feedback**: Receive audible feedback for actions performed.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## Files

- `main.py`: The main script containing the implementation of the voice command functions.


## Setup and Usage

### Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- Microphone for voice input



### Running the Application

1. Connect a microphone to your computer.
2. Run the `main.py` script:
    ```sh
    python main.py
    ```
3. The application will prompt you to say a command. Speak clearly into the microphone.
4. The recognized command will be executed, and you will receive audible feedback.

## Available Commands

- **Open Google**: Opens Google Chrome.
- **Create File**: Creates a new file with the specified name.
- **Delete File**: Deletes the specified file.
- **Create Directory**: Creates a new directory with the specified name.
- **Delete Directory**: Deletes the specified directory.
- **List Files**: Lists all files in the specified directory.
- **Rename File**: Renames a file from an old name to a new name.
- **Open Text Editor**: Opens the default text editor based on the OS.
- **Shutdown the Computer**: Shuts down the computer.
- **Restart the Computer**: Restarts the computer.
- **Sleep**: Puts the computer to sleep.
- **Hibernate**: Hibernates the computer.
- **Log Off**: Logs off the current user.

## Author

- **Miqayel Postoyan**
- **Created**: 28 June
