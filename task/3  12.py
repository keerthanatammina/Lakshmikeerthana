def vow(a):
    b={'vowels':0,'consonants':0}
    for i in a:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            b['vowels']+=1
        else:
            b['consonants']+=1
    print(b)
    print(f"vowels are",b['vowels'],b['consonants'])
vow("entertainment")
