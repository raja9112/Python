from collections import Counter

def check_anagram(str1, str2):
    #if (sorted(str1)== sorted(str2)):
    if (Counter(str1)== Counter(str2)):        #we can use either sorted nor Counter
        print("The given words are anagram.")
    else:
        print("The given words are not anagram.")

check_anagram("listen", "silent")
