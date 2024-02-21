# Cybersecurity
## Ariel Attacking Tool
### Overview

Ariel Attacking Tool is a Python-based GUI application designed for educational purposes to demonstrate and simulate different types of network attacks. It integrates functionalities for launching HTTP Flood, SYN Flood, and UDP Flood attacks to specified IP addresses using a user-defined number of threads. The application is built using tkinter for the GUI component, threading for concurrent attacks, and socket programming for network communication.
Installation
Prerequisites

    Python 3.x
    tkinter (usually comes with Python)
    Access to command-line/terminal

Steps

    Clone the repository or download the source code:

bash

    git clone https://github.com/KuberCaptain/Cybersecurity/ari-bomber.py

    Ensure Python and tkinter are installed on your system. You can verify the installation of Python and tkinter by running:
bash

    python --version

    python -m tkinter

If tkinter is installed, a small window will appear. You can close it and proceed.
Usage

To run the Ariel Attacking Tool, navigate to the directory containing the script and execute:

bash

python attack_tool.py

This command will open the GUI of the Ariel Attacking Tool. Follow the steps below to use the application:

Enter the IP address of the target: Provide the IP address you wish to attack.
Enter the number of threads to use: Specify the number of concurrent threads for the attack.
Choose the attack type: Select the type of attack you want to launch from the dropdown menu (HTTP Flood, SYN Flood, UDP Flood).
Launch Attack: Click the "Launch Attack" button to start the attack.

### Features

Multiple Attack Types: Supports HTTP Flood, SYN Flood, and UDP Flood attacks.
Threaded Execution: Utilizes threading to execute multiple instances of the attack simultaneously.
Simple GUI: Easy-to-use graphical interface for setting up and launching attacks.

## Disclaimer

This tool is developed for educational and research purposes only. The developer is not responsible for any misuse or damage caused by this tool. Users should only use the Ariel Attacking Tool to perform tests on networks and systems they have explicit permission to analyze.

# File Encryption and Decryption Utility shifr2
## Overview

This Python script provides a simple yet powerful utility for encrypting and decrypting files on a computer. It automatically generates a random encryption key, saves it to a file, and uses it to encrypt or decrypt files. The script is designed to encrypt all files in specified directories, excluding the Windows system directory, and decrypt them using the same key.
Features

 Automatic encryption key generation.
 Key storage for subsequent decryption use.
 File and directory encryption excluding system directories.
 Full directory decryption capability.

### Installation
Prerequisites

 Python 3.x installed on your system.
 Basic understanding of command-line operations.

Setup

 Clone the repository or download the script directly:

bash

    git clone https://github.com/KuberCaptain/Cybersecurity/shifr2

#### No external Python packages are required. The script uses standard libraries os, shutil, sys, random, and string.

### Usage

## Important: Before using this script, be aware that it encrypts files irreversibly if the key is lost. It is strongly recommended to use this script in a controlled environment and not on personal or sensitive files unless you understand the risks.
Encrypting Files

Run the script to encrypt files:

bash

    python shifr2.py

The script generates an encryption key if it doesn't exist and saves it to C:\encryption_key.txt.
It encrypts all files in directories other than C:\Windows and stores them in their original location.

Decrypting Files

To decrypt your files, simply run the script again. It reads the existing key and decrypts any encrypted files.

### Key Management

    The encryption key is stored in C:\encryption_key.txt. Ensure the safety of this file for decryption.
    Warning: Losing this key means you cannot decrypt your files. Keep a backup of the key in a secure location.

### Notices

    This utility is for educational purposes. The creator is not responsible for data loss or damage.
    Ensure you have permission to encrypt and decrypt the directories and files.

### Contributing

Contributions are welcome. Please fork the repository and submit pull requests with your improvements.
