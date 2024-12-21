words =["apple", "banana", "cherry", "date", "eggplant"]
if not words:
    print("List is empty")
else:
    max_len=0
    longest_word=[]
    for word in words:
        if len(word)>max_len:
            max_len=len(word)
            longest_word=[word]
        elif len(word)==max_len: 
            longest_word.append(word)

    print("Longest words are:", longest_word)
