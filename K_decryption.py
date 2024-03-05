import string


class decryptor:
    def __init__(self, glossary_and_code: str) -> None:
        """Gets a string that has two parts: a glossary of words seperated by a space,
        ending with a hash ('#'), and an encrypted message.

        Args:
            glossary_and_code (str): the input stated above, which looks like this 
            "word1 word2 ...#wordsEncryptedWithhKEncryption".
        """
        self.glossary, self.encrypted_message = glossary_and_code.split('#')
        self.alphabet = [' '] + list(string.ascii_uppercase)
        self.glossary = self.separate_into_words(self.glossary, ' ')


    def separate_into_words(self, sentence:str, sep:str) -> list:
        return sentence.split(sep)


    def decrypt_word(self, word:str, K:int) -> str:
        alphabet = self.alphabet
        decrypted_word = ''
        for letter in word:
            OG_index = abs(alphabet.index(letter) - K)
            OG_letter = alphabet[OG_index]
            decrypted_word += OG_letter

        return decrypted_word
    
    
    def decrypt_sentence(self, sentence:str, K:int) -> list:
        """Gets an encrypted sentence and a shift and returns a list
        of decrypted words.

        Args:
            sentence (str): Encrypted sentence.
            K (int): Shift in K encryption.

        Returns:
            list: A list of decrypted words in the order of appearance
            in the sentence.
        """
        decrypted_words = []
        encrypted_space = self.alphabet[K]
        encrypted_words = self.separate_into_words(sentence, encrypted_space)
        for word in encrypted_words:
            decrypted_words += [self.decrypt_word(word, K)]

        return decrypted_words
    
    
    def find_best_K(self) -> int:
        best_k = 0
        best_score = 0
        for k in range(27): # 26 letters in English alphabet + ' '(index of it is 0) = 27.
            score = 0
            decrypted_words = self.decrypt_sentence(self.encrypted_message, k)
            for word in decrypted_words:
                if word in self.glossary:
                    score += 1
            if score > best_score:
                best_k = k
        
        return best_k


            
            
            
if __name__ == "__main__":
    message = "MAN AIR WE ATTACK DARK#XFABUUBDLAEBSL"
    my_decryptor = decryptor(message)
    bestK = my_decryptor.find_best_K()
    print(bestK)

            
            
            
            
            
