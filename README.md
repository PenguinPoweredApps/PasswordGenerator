# Password Generator

![Password Generator](padlock.png)

Password Generator is a simple application written in Python TKinter that allows you to generate strong and secure passwords with customizable length and character options. With this application, you can quickly create passwords that meet your specific requirements and enhance your online security.

## Features

- Generate passwords with customizable length, up to 32 characters.
- Include lower and upper case letters, numbers, and ASCII characters in the generated passwords.
- Easy-to-use user interface for a seamless password generation experience.
- Copy generated password to clipboard for easy pasting into other applications.
- No password storage: Generated passwords are not saved to ensure maximum security.

## Requirements

- Python 3.6 or above

## Usage

1. Clone the repository to your local machine or download the ZIP file.

```shell
git clone https://github.com/PenguinPoweredApps/password-generator.git
```

2. Install the necessary dependencies using pip.

```shell
pip install -r requirements.txt
```

3. Run the application.

```shell
python password_generator.py
```

4. Specify the desired length for your password by entering a value in the "Password Length" field.

5. Choose the character options you want to include in your password by checking the corresponding checkboxes:
   - Lowercase letters (a-z)
   - Uppercase letters (A-Z)
   - Numbers (0-9)
   - ASCII characters (!@#$%^&*())

6. Click the "Generate Password" button to generate a strong and secure password based on your specifications.

7. The generated password will be displayed in the "Generated Password" field.

8. Click the "Copy to Clipboard" button to copy the generated password to your clipboard for easy pasting.

9. Repeat the steps above to generate additional passwords as needed.

10. Remember to use passwords of maximum length and include lower and upper case letters, numbers, and ASCII characters for the most secure passwords.

## Contributing

Contributions to the Password Generator project are welcome and encouraged. If you find any issues or have suggestions for improvement, please submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- The Password Generator application uses the [TKinter](https://docs.python.org/3/library/tkinter.html) library for the user interface.
- The [random](https://docs.python.org/3/library/random.html) module is used to generate random passwords.
- The [pyperclip](https://pypi.org/project/pyperclip/) library is used for copying the generated password to the clipboard.
