word=str(input("enter any alphabet:"))
change=word.upper().strip()
if (word=="A") or (word=="B") or (word=="C") or (word=="z"):
    print("it is an alphabet.")
else:
    print("it is not an alphabet")