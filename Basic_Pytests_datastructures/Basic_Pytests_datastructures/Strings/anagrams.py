word_list = ["listen", "silent", "enlist", "eat", "tea", "ate"]

def group_anagrams(words):
    anagram_groups = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    return anagram_groups


anagram_groups = group_anagrams(word_list)

for group in anagram_groups.values():
    print(" ".join(group))
