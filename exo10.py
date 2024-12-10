word=str(input("type a word: "))
palindrome = False

if(len(word) % 2 !=0):
    hlen=int(len(word)/2)
    half1=word[:hlen]
    half2=word[hlen+1:][::-1] #reverse the word
    print(half1,half2)
    if(half1 == half2):
        palindrome = True
if(palindrome==True):
    print("the word is planidrome")
else:
    print("the word isnt planidrome")
