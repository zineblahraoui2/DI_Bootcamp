Longest_word = input("Write the longuest word without A")
while  "a"  not in Longest_word.lower():
    sentence_1 = input("Write the longuest word without A")
    if len(sentence_1) > len(Longest_word):
        Longest_word = sentence_1
        print("congratulation ")
    else:
        print("Try again") 
print(f"You entered a word with 'A'. The longest word without 'A' was {Longest_word}")        
 
