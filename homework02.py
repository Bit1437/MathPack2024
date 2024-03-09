import random
import string
import unittest

import caesar


class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("PYTHON", 3, "SBWKRQ"),
            ("python", 3, "sbwkrq"),
            ("Python", 3, "Sbwkrq"),
            ("Python3.6", 3, "Sbwkrq3.6"),
        ]

        for i, (plaintext, shift, chiphertext) in enumerate(cases):
            with self.subTest(case=i, plaintext=plaintext, chiphertext=chiphertext):
                self.assertEqual(chiphertext, caesar.encrypt_caesar(plaintext, shift=shift))

    def test_decrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("SBWKRQ", 3, "PYTHON"),
            ("sbwkrq", 3, "python"),
            ("Sbwkrq", 3, "Python"),
            ("Sbwkrq3.6", 3, "Python3.6"),
        ]

        for i, (chiphertext, shift, plaintext) in enumerate(cases):
            with self.subTest(case=i, chiphertext=chiphertext, plaintext=plaintext):
                self.assertEqual(plaintext, caesar.decrypt_caesar(chiphertext, shift=shift))

    def test_randomized(self):
        shift = random.randint(8, 24)
        plaintext = "".join(random.choice(string.ascii_letters + " -,") for _ in range(64))
        ciphertext = caesar.encrypt_caesar(plaintext, shift=shift)
        unittest.TestCase().assertEqual(
            plaintext,
            caesar.decrypt_caesar(ciphertext, shift=shift),
            msg=f"shift={shift}, ciphertext={ciphertext}",
        )


# Пример использования
if __name__ == "__main__":
    # Пример шифрования и дешифрования
    plaintext_example = "Hello, World!"
    shift_example = 5

    encrypted_example = caesar.encrypt_caesar(plaintext_example, shift_example)
    print(f"Пример шифрования: {encrypted_example}")

    decrypted_example = caesar.decrypt_caesar(encrypted_example, shift_example)
    print(f"Пример дешифрования: {decrypted_example}")

    # Пример взлома шифра Цезаря
    dictionary_example = {"hello", "world", "python"}
    encrypted_text_example = caesar.encrypt_caesar("python", shift_example)

    cracked_shift = caesar.caesar_breaker_brute_force(encrypted_text_example, dictionary_example)
    print(f"Найденный сдвиг для взлома: {cracked_shift}")
    print(f"Расшифрованный текст: {caesar.decrypt_caesar(encrypted_text_example, cracked_shift)}")
