value=input("enter a value")
word_count=0;digit=0
for each_char in value:
    if each_char.isdigit():
       digit+=1
    elif each_char.isalpha():
        word_count+=1
print(word_count,digit)

        
            
