# -*- coding: utf-8 -*-
"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.
"""

# step 1 consists in splitting the input sentence into words
# then, each word gets checked for incoherences
# note - no lowercase/uppercase checks are used, since it is assumed sentences only contain lowercase letters
# this check should be added otherwise

def countValidWords(sentence):
    
    validWords = []
    validPunct = ['!', '.', ',']
    
    # 1 - split sentence into words
    words = sentence.split()
    
    # 2 - loop on words
    for word in words:
        
        # 3 - loop on characters        
        # a one-character word is ok if it is alpha or punctuation
        if (len(word) == 1) and (word[0] in validPunct or word[0].isalpha()):
            validWords.append(word)
            
        # else, the first character must be alpha
        elif word[0].isalpha():
            
            # init hyphen marker
            hyphen = False
            
            # init valid marker
            valid = True
            
            # loop on the remaining characters
            for i in range (1, len(word)):
                
                # digit check
                if word[i].isdigit():
                    valid = False
                    break
                
                # hyphen check
                elif word[i] == '-':
                    # second hyphen
                    if hyphen:
                        valid = False
                        break
                    hyphen = True
                    # also check the next character, which has to be alpha
                    if i == len(word)-1:
                        valid = False
                        break
                    elif not word[i+1].isalpha():
                        valid = False
                        break
                    
                # punctuation check
                elif word[i] in validPunct:
                    # has to be the final character
                    if i != len(word)-1:
                        valid = False
                        break
                    # if conditions not merged for overall clarity
                
                # could add a failsafe mechanism breaking on any other non alpha (also merge the digit check here)
                # not needed if it is assumed input sentences are in the correct format
                
                # if alpha, no action to take
                
            # end of the word has been reached without incoherences
            if valid:
                validWords.append(word)
    
    return validWords


print(countValidWords("cat and  dog"))

print(countValidWords("!this  1-s b8d!"))

print(countValidWords("alice and  bob are playing stone-game10"))