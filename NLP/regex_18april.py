# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 08:35:31 2025

@author: Vaishnavi
"""

import re
#1. .(dot)-matches any character except newline.
print(re.findall(r"a.c","abc ac aac acc adc a-c" ))
#['abc', 'aac', 'acc', 'adc', 'a-c']
'''
a->matches the letter 'a'
.->matches any one character (except newline \n)
c->matches the letter 'c'
So overall,its looking for three-character strings 
The first letter is 'a'
The 2nd letter is 'c'
The middle can be any character 
abc (a+any character +c )
aac (a +any character +c)
acc (a +any character +c)
adc (a +any character +c)
a-c (a +any character +c)

Use Case:
    suppose swiggy wants to find out which are is more foody
    
so it would be storing the name,address,area,phonenumber,etc 
for eg,A apartment A-colony-2.....986890
so from this we want the colony which is having more number of orders
for that we would be finding out the colony extracting only the colony
here,a datascientist would approach to increase the number of delievery people
so to have a better profits.
'''
#2. ^(caret)-matches start of string
print(re.findall(r"^Hello","Hello World\nHello Python"))
'''
^->This is the caret ,and it means:
"Matches the following pattern only if it appears at the start"
"Hello"->This is the actual text you're trying to match.
So ^Hello means:
    "MAtchthe word 'Hello' only if  it is at the very start of the string"
input:"Hello World\nHello Python"
"Hello WOrld"
"Hello python"->on a next line which 2nd string not the start of string
but since the ^anchor only applies to the beginning of the whole string.it will only match the first 
"Hello",not the second one.
output:['Hello']

'''
print(re.findall(r"^Hello","Hello World,Hello Python"))
#['Hello']
#3. $(dollar)-matches end of the string
print(re.findall(r"Python$","Hello Python"))
#['Python']
'''
Python->This is the text you're trying to match
$->this means:
"Match this **only if it appears at the end of the string"
so Python$ means:
"Match the word 'Python' only if its st the very end of the string."
'''
print(re.findall(r"Python$","Hello Python Developers"))
#[]
#4. *(asterisk)-0 or more of the preceding character
print(re.findall(r"ab*c","ac abc abbc abbbc"))
#['ac', 'abc', 'abbc', 'abbbc']
'''
PAttern:ab*c
This pattern uses the asterisk *,which is one of the mostly
Breakdown:
a->Match the character 'a'
b* ->matches zero or more 'b' characters
c->Match the character 'c'
Word    Matches ab*c    Why?
ac          Yes         'b' appears zero times
abc         Yes         'b' appears once
abbc        Yes         'b' appears twice
abbbc       Yes         'b' appears three times
'''
#5. +(plus)-1 or more of the preceding character
print(re.findall(r"ab+c","ac abc abbc abbc"))
#['abc', 'abbc', 'abbc']
'''
ab+c
this pattern uses the + plus quantifier,
which is closely related to the *we disccused before
Breakdown:
 a->matches the character 'a'
b->matches 1 or more character 'b'
c->matches the character 'c'
so the full pattern matches:
'a' followed by at least one 'b' ,followed by 'c'
lets check each word:
    
"ac"
No 'b' between 'a' and 'c'.'b+'requires at least one 
"abc" 
one 'b'->matches ab+c
"abbc"
two 'b'->matches ab+c
"abbbc"
3 'b'->matches ab+c   
   '''
   
#6. ?(question)-0 or 1 of the preceding character
print(re.findall(r"ab?c","ac abc abbc abbbc"))
#['ac', 'abc']
'''
PAttern:ab?c
Breakdown:
a->Match the character 'a'
b?->MAtch the zero or one character 'b'
c->match the character 'c'
so this pattern matches:
'a' followed by  at most 'b',followed by 'c'
Word        matches ab?c    Why
ac              Yes         'b' appears 0 times (allowed)
abc             Yes         'b' appears 1 time(allowed)
abbc            No          'b' appear 2 or more times (not allowed)
abbbc           No          'b' appear 2 or more times (not allowed)
'''
#7. {} (curly braces)-exact or range of repetitions
print(re.findall(r"ab{2}c","abc abbc abbbc abbbbc" ))
#['abbc']
'''
pattern: ab{2}c
breakdown:
a->matches the character 'a'
b{2}->matchs the character 'b' exactly 2 times
c->matches the character 'c'
so this regex will only match:
'a' followd by exactly 2 'b's,followed by 'c'
ie., the string "abbc"

'''
#8.[](square brackets)-either b or c character set
print(re.findall(r"a[bc]d","abd acd aad aed abcd"))
#['abd', 'acd']
'''
Pattern:a[bc]d
breakdown:
    a->matches character 'a'
    [bc]->matches exactly one character,and it must be either 'b' or 'c'
d->matches character 'd'
so,this pattern matches:
The string 'a' followed by either b or c ,followed by d
'''