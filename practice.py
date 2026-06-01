def clear_text(text):
    text = text.lower()
    chars = ".,!?:;\"'()[]{}"
    for char in chars:
        text = text.replace(char, "")
    return text

def count_words(text):
    text = clear_text(text)
    if not text.strip():
        return {}
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

print("Super Word Counter 3000")
user_input = input("Please type in your text: ").strip()

if not user_input:
    print("Error: No text was entered.")
else:
    result = count_words(user_input)
    if result:
        print("Word Count:")
        for word, amount in result.items():
            print(f"{word}: {amount}")
    else:
        print("No valid words were found.")