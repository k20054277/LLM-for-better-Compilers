words = ['apple', 'banana', 'cherry']
for word in words:
    if word == 'banana':
        del words[1]
        print(f"Deleting {word} from the list.")
    else:
        print(f"Skipping {word}.")
print(words)