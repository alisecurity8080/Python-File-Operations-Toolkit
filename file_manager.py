import os

# 1. Receipt and Transaction Logging
def create_receipt(item_name, item_price, balance):
    if balance >= item_price:
        remaining_balance = balance - item_price
        with open("receipt.txt", "w") as f:
            f.write(f"Item Price: {item_price}\n")
            f.write(f"{item_name} Purchased\n")
            f.write(f"Remaining Balance: {remaining_balance}\n")
        print(f"[+] Transaction complete. Remaining balance: {remaining_balance}")
    else:
        print("[-] Insufficient balance.")

# 2. Change/Replace Word in File
def change_word(filename, old_word, new_word):
    if not os.path.exists(filename):
        print(f"[-] File '{filename}' nahi mili.")
        return

    with open(filename, "r") as f:
        data = f.read()

    new_data = data.replace(old_word, new_word)

    with open(filename, "w") as f:
        f.write(new_data)
    print(f"[+] Replaced '{old_word}' with '{new_word}'.")

# 3. Check Word in File
def check_word(filename, word):
    if not os.path.exists(filename):
        print(f"[-] File '{filename}' nahi mili.")
        return

    with open(filename, "r") as f:
        data = f.read().lower()

    if word.lower() in data:
        print(f"[+] '{word}' file mein majood hai.")
    else:
        print(f"[-] '{word}' file mein nahi mila.")

# 4. Check Word with Line Number (Log Scanning)
def check_line(filename, word):
    if not os.path.exists(filename):
        print(f"[-] File '{filename}' nahi mili.")
        return

    word = word.lower()
    found = False
    line_no = 1

    with open(filename, "r") as f:
        for line in f:
            if word in line.lower():
                print(f"[+] Line {line_no} par word mila: {line.strip()}")
                found = True
            line_no += 1

    if not found:
        print(f"[-] Word '{word}' kisi line mein nahi mila.")

# 5. Daily Diary Logger
def add_diary_entry(date, note):
    with open("my_diary.txt", "a") as f:
        f.write(f"Date: {date}\n")
        f.write(f"Note: {note}\n")
        f.write("-" * 20 + "\n")
    print("[+] Entry diary mein save ho gayi.")


# --- MAIN EXECUTION ---
print("--- RUNNING FILE UTILITIES ---")

# Receipt generate karna
create_receipt("Laptop", 5000, 10000)

# Line-by-line word dhoondna
check_line("receipt.txt", "Remaining")

# Diary entry add karna
add_diary_entry("2026-09-30", "File I/O functions practice completed.")
