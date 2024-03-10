import regex as re
""" Question
Given a paragraph and a list of banned words, return the most frequent 
word that is not in the list of banned words. It is guaranteed there is 
at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of 
punctuation. Words in the paragraph are not case sensitive. 
The answer is in lowercase.
```
Example:
 Input: 
 paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
 banned = ["hit"]
 Output: "ball"
 Explanation: 
 "hit" occurs 3 times, but it is a banned word.
 "ball" occurs twice (and no other word does), so it is the most 
 frequent non-banned word in the paragraph. 
 Note that words in the paragraph are not case sensitive,
 that punctuation is ignored (even if adjacent to words, such as 
 "ball,"), 
 and that "hit" isn't the answer even though it occurs more because it 
 is banned.
```
"""
""" Solution
def get_most_freq_word(paragraph, banned_words):
    if paragraph is None:
        return ''
    if banned_words is None:
        banned_words = list()
    tokens = paragraph.split()
    tokens = sanitize(tokens)
    banned_words_set = set(banned_words)
    word_to_occur_pos_hash = create_occur_pos_hash(tokens, 
                                                    banned_words_set)
    return find_most_freq_word_in(word_to_occur_pos_hash)

def sanitize(tokens):
    result = list()
    for token in tokens:
        full_word = list()
        for letter in token:
            letter = letter.lower()
            if letter.isalpha():
                full_word.append(letter)
        if len(full_word) > 0:
            full_word = ''.join(full_word)
            result.append(full_word)
    return result

def create_occur_pos_hash(tokens, banned_words_set):
    result = dict()
    for pos, word in enumerate(tokens):
        if word not in banned_words_set:
            if word not in result:
                result[word] = (0,0)
            occurance = result[word][0]
            result[word] = (occurance+1, pos)
    return result

def find_most_freq_word_in(wtop_hash):
    result, global_occurance, global_position = '', -1, -1
    for word, value in wtop_hash.items():
        local_occurance = value[0]
        local_position = value[1]
        if local_occurance >= global_occurance:
            if local_position > global_position:
                result = word
                global_occurance = local_occurance
                global_position = local_position
    return result

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
assert(get_most_freq_word(paragraph, banned) == 'ball')

paragraph = "    a1 b# 0 $ a b c (    "
banned = ["b"]
assert(get_most_freq_word(paragraph, banned) == 'a')

paragraph = "    a1 b# 0 $ a b c (    "
banned = [""]
assert(get_most_freq_word(paragraph, banned) == 'b')

paragraph = ""
banned = ["b"]
assert(get_most_freq_word(paragraph, banned) == '')

paragraph = None
banned = ["b"]
assert(get_most_freq_word(paragraph, banned) == '')

paragraph = "a b a b"
banned = None
assert(get_most_freq_word(paragraph, banned) == 'b')
"""

class repCounter:
    def __init__(self, sentence:str, banned_words:list[str]) -> None:
        if sentence != None:
            self.sentence = sentence.lower()
            self.words = re.findall('[a-z]+', 
                                    self.sentence, overlapped=False)
        else:
            self.sentence = ""
            self.words = []
        if banned_words != None:
            self.banned_words = set(banned_words)
        else:
            self.banned_words = []

    def __filter_banned_words(self) -> list[str]:
        filtered_words = self.words
        for word in self.words:
            if word in self.banned_words:
               filtered_words.remove(word) 

        return filtered_words

    def calc_freq(self) -> dict[str:int]:
        filtered_words = self.__filter_banned_words()
        freq_dict = {word:0 for word in filtered_words}
        for word in filtered_words:
            freq_dict[word] += 1
        
        return freq_dict

    def most_frequent_word(self) -> str:
        max_freq = 0
        chosen_word = ''
        freq_dict = self.calc_freq()
        for word, freq in freq_dict.items():
            if freq_dict[word] >= max_freq:
                max_freq = freq
                chosen_word = word
            
        return chosen_word
            

def main() -> None:
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    my_counter = repCounter(paragraph, banned)
    assert(my_counter.most_frequent_word() == 'ball')

    paragraph = "    a1 b# 0 $ a b c (    "
    banned = ["b"]
    my_counter = repCounter(paragraph, banned)
    assert(my_counter.most_frequent_word() == 'a')

    paragraph = "    a1 b# 0 $ a b c (    "
    banned = [""]
    my_counter = repCounter(paragraph, banned)
    assert(my_counter.most_frequent_word() == 'b')

    paragraph = ""
    banned = ["b"]
    my_counter = repCounter(paragraph, banned)
    assert(my_counter.most_frequent_word() == '')

    paragraph = None
    banned = ["b"]
    my_counter = repCounter(paragraph, banned)
    assert(my_counter.most_frequent_word() == '')

    paragraph = "a b a b"
    banned = None
    my_counter = repCounter(paragraph, banned)
    assert(my_counter.most_frequent_word() == 'b')



            
if __name__ == "__main__":
    main()
            
            
            
            
            
            
            
            
            
            
