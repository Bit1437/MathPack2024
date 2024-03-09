def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Шифрует текст с использованием шифра Цезаря.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - start + shift) % 26 + start)
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Дешифрует текст, закодированный шифром Цезаря.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - start - shift) % 26 + start)
        else:
            plaintext += char
    return plaintext


import typing as tp


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Полный перебор для взлома шифра Цезаря.

    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker_brute_force("python", d)
    0
    >>> caesar_breaker_brute_force("sbwkrq", d)
    3
    """
    best_shift = 0
    max_matches = 0

    for shift in range(26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        matches = sum(word.lower() in dictionary for word in decrypted_text.split())

        if matches > max_matches:
            max_matches = matches
            best_shift = shift

    return best_shift


# Пример использования
if __name__ == "__main__":
    # Пример шифрования и дешифрования
    plaintext_example = "Hello, World!"
    shift_example = 5

    encrypted_example = encrypt_caesar(plaintext_example, shift_example)
    print(f"Пример шифрования: {encrypted_example}")

    decrypted_example = decrypt_caesar(encrypted_example, shift_example)
    print(f"Пример дешифрования: {decrypted_example}")

    # Пример взлома шифра Цезаря
    dictionary_example = {"hello", "world", "python"}
    encrypted_text_example = encrypt_caesar("python", shift_example)

    cracked_shift = caesar_breaker_brute_force(encrypted_text_example, dictionary_example)
    print(f"Найденный сдвиг для взлома: {cracked_shift}")
    print(f"Расшифрованный текст: {decrypt_caesar(encrypted_text_example, cracked_shift)}")