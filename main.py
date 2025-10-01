import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

VOCAB_FILE = "vocab.txt"

def load_vocab(filename):
    vocab = {}
    with open(filename, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        for i in range(0, len(lines), 2):
            eng = lines[i]
            pl = lines[i+1]
            vocab[eng] = pl
            vocab[pl] = eng
    return vocab

def main():
    vocab = load_vocab(VOCAB_FILE)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://lingos.pl/student-confirmed/group")

    print("👉 Log in manually and go to the flashcards page.")
    print("👉 Press F8 to start, F9 to pause/resume, F10 to quit.")

    keyboard.wait("F8")
    print("🚀 Automation started!")

    paused = False

    while True:
        if keyboard.is_pressed("F10"):
            print("🛑 Exiting...")
            break

        if keyboard.is_pressed("F9"):
            paused = not paused
            print("⏸ Paused" if paused else "▶️ Resumed")
            time.sleep(1)

        if paused:
            time.sleep(1)
            continue

        time.sleep(1.5)
        try:
            phrase_el = driver.find_element(By.ID, "flashcard_main_text")
            phrase = phrase_el.text.strip()
            print("Phrase:", phrase)

            if phrase in vocab:
                answer = vocab[phrase]
                print("Answer:", answer)

                input_el = driver.find_element(By.ID, "flashcard_answer_input")
                input_el.clear()
                input_el.send_keys(answer)

                driver.find_element(By.ID, "enterBtn").click()
            else:
                print("⚠️ Not in vocab:", phrase)

        except Exception as e:
            try:
                btn = driver.find_element(By.ID, "enterBtn")
                btn.click()
                print("Clicked next page button")
            except:
                print("Error:", e)

if __name__ == "__main__":
    main()
