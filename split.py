sen=input("enter the sentence ")
word=[]
longest_word=""
for word in sen.split():
    word.append(word)
    if len(word)>len(longest_word):
        longest_word=word
print(f"longest word:{longest_word}",)