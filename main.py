def count_words(text):
    new_list = text.split()
    return len(new_list)

def count_letters(text):
    new_text = text.lower()
    new_dict = {}
    for i in new_text:
        if i.isalpha():
            if i in new_dict: 
                new_dict[i] += 1
            else: 
                new_dict[i] = 1
    return sorted(new_dict.items())

def total_letter_count(text2):
    new_text2 = text2.lower()
    new_dict2 = {}
    for i in new_text2:
        if i.isalpha():
            if i in new_dict2: 
                new_dict2[i] += 1
            else: 
                new_dict2[i] = 1
    return sum(new_dict2.values())

with open('books/frankenstein.txt') as book:
    contents = book.read()

print(f"There are {count_words(contents)} words in this book.")
print(f"There are {total_letter_count(contents)} letters in this book.")
print("Here is how many of each letter in this book")
print (count_letters(contents))


