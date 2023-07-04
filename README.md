# Password Security Checker & Generator
This is a simple yet effective password security checker and generator built using Python. It offers a basic graphical user interface (GUI) for users to interact with. The GUI is constructed using the Tkinter library in Python, with some additional customizations provided by the CustomTkinter package.

## Features
**1.  Password Security Check:** Users can enter their passwords and have them checked for strength and security. This includes checks for password length, the presence of lowercase and uppercase characters, numerals, and special characters. The tool also checks whether the password has been exposed in a data breach using the 'Have I Been Pwned' API.

**2.  Password Generation:** The application can also generate secure passwords that are guaranteed to pass the security checks. These generated passwords contain a mix of letters (both upper and lower case), digits, and special characters and are not found in the list of breached passwords.

**3.  Copy to Clipboard:** Users can copy the generated password to their clipboard for convenience.

## Dependencies
To run this application, you need the following Python packages:

-  tkinter
-  customtkinter
-  requests
-  hashlib
-  re
-  string
-  random
-  pyperclip

## Running the Application
The application is a standalone Python script and can be run as follows:

`python Password_Security_Checker.py`

### Contributions
This project is open-source, and contributions are welcome. If you find a bug or think of a new feature, please open an issue or submit a pull request.
