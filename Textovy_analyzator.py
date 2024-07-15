"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Přemysl Pleva
email: premyslpleva75@gmail.com
discord: premeq#5714
"""

from texts import TEXTS
from users import USERS
import sys
import re

un = input("username: ")
pw = input("password: ")

# Checking database of registered users - if not registered, program terminates
#
#
if (un, pw) not in list(USERS.items()):
    sys.exit("unregistered user, terminating the program...")

# Registered user - program greets them
#
#
print(
    "-" * 41,
    f"Welcome to the app, {un}",
    f"We have {len(TEXTS)} texts to be analyzed.",
    "-" * 41,
    sep="\n"
)

# User's choice of text
#
#
text_num = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print("-" * 41)

# If the input is not a number or is out of the given range, then the program terminates
#
#
if not text_num.isnumeric():
    sys.exit("Invalid entry. Terminating the program...")
elif int(text_num) not in range(1, len(TEXTS)):
    sys.exit("Invalid entry. Terminating the program...")

# Removing all "," and "." and "\n" from the chosen text and then splitting it into individual words
# "," and "." must be deleted - hence substituting for None
# "\n" must be replaced by empty space (it surprised me that .split() 'translates' new line as a string "\n")
#
#
# chosen_text_split = re.sub("[,.]", "", TEXTS[int(text_num) - 1]).replace("\n", " ").split(" ")

# chosen_text_final = [word for word in chosen_text_split if word != ""]

# chosen_text_final = ''.join(letter for letter in TEXTS[int(text_num) - 1] if letter.isalnum())


# Můj myšlenkový pochod na odstranění nežádoucích symbolů - teček a čárek v tomto případě:
# 1.) na konci potřebuju list s jednotlivými slovy
#
# 2.) připravím si prázdný list a v následném for-cyklu si odfiltruju všechny znaky,
# které nejsou alphanumerické nebo mezera či nový řádek
# v zápětí si nový řádek nahradím mezerou (upřímně si nejsem jist, jestli to funguje
# protože vzniklý text se pak vypisuje do odstavečku...
# na závěr si vyhovující znaky přidávám do připraveného listu
#
# 3.) z listu jednotlivých symbolů vytvořím string pomocí .join a hned jej splitnu pomocí .split
#
# 4.) voila, mám list jednotlivých slov

chosen_text = []

for i in TEXTS[int(text_num) - 1]:
    if i.isalnum() or i == " " or i == "\n":
        i.replace("\n", " ")
        chosen_text.append(i)

chosen_text_final = ''.join(i for i in chosen_text).split()
#
#
# Variables for desired information
#
#
total_words = len(chosen_text_final)
total_titlecase = len([word for word in chosen_text_final if word[0].isupper()])
total_upper = len([word for word in chosen_text_final if word.isupper() & word.isalpha()])
total_lower = len([word for word in chosen_text_final if word.islower() & word.isalpha()])
total_numeric = len([word for word in chosen_text_final if word.isnumeric()])
sum_numeric = sum([int(word) for word in chosen_text_final if word.isnumeric()])


print(
    f"There are {total_words} words in the selected text.",
    f"There are {total_titlecase} titlecase words.",
    f"There are {total_upper} uppercase words.",
    f"There are {total_lower} lowercase words.",
    f"There are {total_numeric} numeric strings.",
    f"The sum of all numbers is {sum_numeric}",
    sep="\n"
)

print("-" * 41)

# Finding and storing lengths of individual words in a chosen text
#
#
words_lengths = [len(word) for word in chosen_text_final]

# Ascending order
#
#
words_lengths.sort()

# Hlavička tabulky
#
#
print("LEN".rjust(5, " "), "OCCURENCES".center(20, " "), "NR.".ljust(5, " "), sep="|")

print("-" * 41)

# Final table of frequencies
#
#
for i in set(words_lengths):
    # Count frequency of given length
    #
    #
    frequency = words_lengths.count(i)
    print(str(i).rjust(5, " "), ("*" * frequency).ljust(20, " "), str(frequency).ljust(5, " "), sep="|")
