#!/usr/bin/env python
# coding: utf-8

# In[4]:


####task1
from functools import reduce
 
def  sum(x, y): 
    return x + y

print(reduce(sum, [10,40,30]))


# In[8]:


marks = [20,12,15,15,13,15,7,8,12,13,15]


def myFunc(x):
  if x < 13:
    return False
  else:
    return True

passed = filter(myFunc, marks)

for x in passed:
  print(x)


# In[9]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))


# In[12]:


input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


# In[14]:


input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))


# In[1]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


# In[2]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


# In[3]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[4]:


#### task2


def longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(longest_word(["python", "pearl", "anaconda"]))


# In[3]:


a=5
b=7
c=9
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# In[6]:


def long_words(n, str):  
    word_len = []  
    txt = str.split(" ")  
    for x in txt:  
        if len(x) > n:  
            word_len.append(x)  
    return word_len   
print(long_words(3, "can i have a cup of tea please")) 


# In[7]:


wordlist = ["can","you","please","sit","for","a","while"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))


# In[12]:


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))


# In[ ]:




