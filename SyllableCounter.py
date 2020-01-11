import sys
from string import punctuation
import nltk
from nltk.corpus import cmudict
cmudict=cmudict.dict()

#Define the syllable calculation from the CMUDICT
def count_syllables(words):
    words=words.replace('-','')
    words=words.lower().split()
    num_sylls=0
    for word in words:
        word=word.strip(punctuation)
        if word.endswith("'s"):
            word=word[:-2]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_sylls+=1
    return num_sylls

#Define the main operation of asking user for word or sentence to count.
def main():
    while True:
        print("Syllable Counter")
        word=input("Enter word or phrase; else press Enter to exit")
        if word=='':
            sys.exit()
        try:
            num_syllables=count_syllables(word)
            print("number of syllables in {} is: {}".format(word,num_syllables))
            print()
        except KeyError:
            print("Word not found. Try again.", file=sys.stderr)

if __name__ == '__main__':
    main()
    
#NOTE-The CMUDICT does not contain every word in the English language and may return as an error if the word is not in the dictionary.
