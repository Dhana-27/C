def encrypt_column_major(text, key):
    cols = (len(text) + key - 1) // key
    matrix = [['' for _ in range(cols)] for _ in range(key)]
    idx = 0
    for col in range(cols):
        for row in range(key):
            if idx < len(text):
                matrix[row][col] = text[idx]
                idx += 1
    return ''.join(''.join(row) for row in matrix)

def decrypt_column_major(cipher, key):
    cols = (len(cipher) + key - 1) // key
    matrix = [['' for _ in range(cols)] for _ in range(key)]
    idx = 0
    for row in range(key):
        for col in range(cols):
            if idx < len(cipher):
                matrix[row][col] = cipher[idx]
                idx += 1
    return ''.join(matrix[row][col] for col in range(cols) for row in range(key) if matrix[row][col])

# Example usage
plain = input("Enter plain text: ")
key = int(input("Enter key (number of rows): "))

cipher = encrypt_column_major(plain, key)
print("Encrypted:", cipher)

original = decrypt_column_major(cipher, key)
print("Decrypted:", original)

/* Enter the plain text: Hello World!

Enter the key (number of rails): 3

Encrypted text: HorelWdlo!l

Decrypted text: Hello World! */
