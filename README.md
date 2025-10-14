# Lingos.pl Flashcard Automator

This Python script automates the process of solving flashcards on the lingos.pl website. It uses Selenium for web browser automation to read flashcards and provide answers based on a predefined vocabulary list.

## How It Works

The script launches a Chrome browser and navigates to the lingos.pl group page. After the user logs in manually and navigates to the flashcards section, the automation can be started.

The script reads the phrase displayed on the flashcard, looks for its translation in the `vocab.txt` file, and types the answer into the input field. It then submits the answer and proceeds to the next flashcard.

## Features

-   **Automated Answering:** Automatically fills in answers for flashcards.
-   **Vocabulary from File:** Loads vocabulary from a simple text file (`vocab.txt`).
-   **Interactive Controls:** Use keyboard hotkeys to control the script's execution:
    -   **F8:** Start the automation.
    -   **F9:** Pause or resume the automation.
    -   **F10:** Stop the script.

## Requirements

-   Python 3.x
-   Google Chrome browser
-   ChromeDriver that matches your version of Google Chrome.
-   The following Python packages:
    -   `selenium`
    -   `keyboard`

You can install the required packages using pip:

```bash
pip install selenium keyboard
```

## Setup

1.  **Install Dependencies:** Make sure you have Python and Google Chrome installed. Then, install the required Python packages as shown above.
2.  **ChromeDriver:** Download the appropriate version of ChromeDriver for your operating system and Chrome version from the [official site](https://chromedriver.chromium.org/downloads). Place the `chromedriver.exe` (or equivalent for your OS) in the same directory as the script, or in a directory included in your system's PATH.
3.  **Login Credentials:** Create a `login.txt` file in the same directory as the script. The first line should contain your email, and the second line should contain your password. For example:

    ```
    your_email@example.com
    your_password
    ```

4.  **Vocabulary File:** Populate the `vocab.txt` file with your vocabulary, it can be copied entirely by selecting the text on the `zestawy` page. The format is one word or phrase per line, with the English and Polish translations on alternating lines. For example:
    ```
    Hello
    Cześć
    Good morning
    Dzień dobry
    ```

## Usage

1.  **Run the script** from your terminal:
    ```bash
    python main.py
    ```
2.  The script will open a new Chrome window and navigate to `https://lingos.pl/student-confirmed/group`.
3.  **Log in manually** to your lingos.pl account.
4.  Navigate to the flashcard exercise you want to complete.
5.  Press **F8** to start the automation.
6.  The script will now read the flashcards and automatically enter the answers.
7.  You can press **F9** to pause and resume the script at any time, or **F10** to exit.

## File Descriptions

-   `main.py`: The main Python script that runs the automation.
-   `login.txt`: A text file containing your login credentials (email and password).
-   `vocab.txt`: A plain text file containing the vocabulary used by the script. Each line should contain a word or phrase, with translations on subsequent lines.
-   `README.md`: This file, providing information about the project.

## Disclaimer

This script is intended for educational purposes only. The user is responsible for any consequences of using this script. Please use it responsibly and in accordance with the terms of service of lingos.pl.
