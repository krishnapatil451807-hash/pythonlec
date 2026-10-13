with open ("file.txt","r") as f:
    sa=f.readlines()
    print ("total number of line : ",len(sa))
    print("2nd line of file ",sa[1])
    print("4th line of file ",sa[3])
