with open ("file.txt",'r') as f:
    k=f.read()
count=0
vowels='aeiou'
for char in k.lower():
    if char in vowels:
        count+=1
print(f"vowels present in file {count}")