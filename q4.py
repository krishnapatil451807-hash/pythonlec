sentence = input("enter a sentence ")
word=[]
with open("file2.txt","r")as f:
    word=[]
    words=f.read().split()
print(f"total word : {len(word)}")
print("unique word : ",end=" ")
for word in words:
    if words.count(word)==1:
        print(word,end="")