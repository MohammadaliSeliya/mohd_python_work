'''Write a Python program to find the first appearance of the substring
   'not' and 'poor' from a given string, if 'not' follows the 'poor', replace
   the whole 'not'...'poor' substring with 'good'. Return the resulting string.'''



sentence = "The foden is not a poor"

not_ = sentence.find('not')
poor = sentence.find('poor')

if not_ != -1 and poor != -1 and not_ < poor:
    sentence1 = sentence.replace(sentence[not_:poor + 4],'good')
    
print(sentence1)    