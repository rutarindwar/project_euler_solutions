# proj euler prob 43
import itertools
word = '0123456789'
l = [0]*3628800
for anagram in set(itertools.permutations(word, len(word))): 
    l.append(''.join(anagram))
    print ''.join(anagram)
