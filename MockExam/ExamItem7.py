import string


class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = []
        for letter in keyword:
            self.keyword.append(self.convert_char(letter))
        self.alphabet = [letter for letter in string.ascii_uppercase]

    #This assumes that all the characters are upper case
    def convert_char(self, character):
        return ord(character) - 65

    def encrypt(self, string_to_encrypt):
        idx = 0
        encrypted_text = ""

        for letter in string_to_encrypt:
            letter_num = self.convert_char(letter)
            shifted_alphabet = self.alphabet[letter_num:] + self.alphabet[:letter_num]
            encrypted_text += shifted_alphabet[self.keyword[idx]]
            idx += 1
            if idx == len(self.keyword):
                idx = 0

        return encrypted_text

    def decrypt(self, string_to_decrypt):
        idx = 0
        decrypted_text = ""

        for letter in string_to_decrypt:
            shifted_alphabet = self.alphabet[self.keyword[idx]:] + self.alphabet[:self.keyword[idx]]
            decrypted_text += self.alphabet[shifted_alphabet.index(letter)]
            idx += 1
            if idx == len(self.keyword):
                idx = 0

        return decrypted_text


message = "ALLYOURBASEAREBELONGTOUS"
code_word = "ZEROWING"
cipher = VigenereCipher(code_word)
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print(f"Message: {message}  Key: {code_word}")
print(f"\nEncrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
assert(message == decrypted)
