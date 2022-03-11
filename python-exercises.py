#!/usr/bin/env python
# coding: utf-8
1.Write a function that will take in a string parameter and return a string in its equivalent Morse code.
# In[2]:


dict1={'a':'.-'  ,'b':'-...','c':'-.-.','d':'-..'  ,'e':'.',
       'f':'..-.','g':'--.' ,'h':'....','i':'..'  ,'j':'.---',
       'k':'-.-' ,'l':'.-..','m':'--'  ,'n':'-.'  ,'o':'---' ,
       'p':'.--.','q':'--.-','r':'.-.' ,'s':'...' ,'t':'-'   ,
       'u':'..-' ,'v':'...-','w':'.--' ,'x':'-..-','y':'-.--','z':'--..',
       '0':'-----' ,'1':'.----' ,'2':'..---' ,'3': '...--','4': '....-' ,
       '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.' } # dictionary of word to morse


# In[3]:


def morse_code():
    words = input("Input the words that you want to turn into Morse code:")
    words = str.lower(words)
    for letter in words:
        if letter == ' ':
            print('/', end='')
           
        else:
            
            print(dict1[letter], sep='\t', end='')  


# In[4]:


morse_code()

2.Write a function that takes in a string parameter and returns a list and a count of the unique letters in the string.
# In[14]:


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def unique_letters (words) :
    words = words.upper()
    words_list = []
    counter = 0
    for letter in words:
        if letter not in words_list and letter in alphabet:
            counter = counter + 1 
            words_list.append(letter)
    return words_list,counter

print(unique_letters("Hello World"))

3.Write a function that accepts a string and prints to screen the number of uppercase letters and lowercase letters.
# In[11]:


case_count=input("Enter string:")
count1=0
count2=0
for i in case_count:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)


# In[1]:


def case_count(a):
    b={"Upper_case":0, "Lower_case":0}
    for i in a:
        if i.isupper():
           b["Upper_case"]+=1
        elif i.islower():
           b["Lower_case"]+=1
        else:
           pass
    print ("Uppercase: ", b["Upper_case"])
    print ("Lowercase: ", b["Lower_case"])
case_count('HelLo WorlD')

