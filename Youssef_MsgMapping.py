"""
Name: Youssef Omer
Course: CmpSc472 Lab
Description: Stores messages efficiently by mapping unique words and reconstructing messages.
"""

def main():
    # Ask for file name
    filename = input("Enter message file name: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except:
        print("Error opening file.")
        return

    # Data structures
    unique_words = []              # stores unique words
    word_index_map = {}            # word -> index
    messages = []                  # list of lists (word indices)

    # -------------------------
    # Part 1: Read + Store
    # -------------------------
    for line in lines:
        words = line.strip().split()
        message_indices = []

        for word in words:
            word = word.lower()

            if word not in word_index_map:
                word_index_map[word] = len(unique_words)
                unique_words.append(word)

            message_indices.append(word_index_map[word])

        messages.append(message_indices)

    # Display results
    print("\n--- Part 1 Results ---")
    print("Total messages:", len(messages))
    print("Unique words count:", len(unique_words))

    print("\nUnique words:")
    for i, word in enumerate(unique_words):
        print(f"{i}: {word}")

    # -------------------------
    # Part 2: Retrieve Messages
    # -------------------------
    while True:
        user_input = input("\nEnter message number to retrieve (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        if not user_input.isdigit():
            print("Invalid input.")
            continue

        msg_num = int(user_input)

        if msg_num < 1 or msg_num > len(messages):
            print("Out of range.")
            continue

        # reconstruct message
        indices = messages[msg_num - 1]
        reconstructed = [unique_words[i] for i in indices]

        print("Message:", " ".join(reconstructed))


if __name__ == "__main__":
    main()