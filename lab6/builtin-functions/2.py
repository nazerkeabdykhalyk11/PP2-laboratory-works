def count_letters(letter):
    upper=0
    lower=0
    for i in letter:
        if i>="A" and i<="Z":
            upper+=1
        elif i>="a" and i<="z":
            lower+=1
    print("sum upper case:", upper)
    print("sum lower case:", lower)
            
        

sentence=str(input("enter sentence:"))
count_letters(sentence)