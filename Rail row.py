def rail_fence_encrypt_row_major(plain_text, key):
    # Fill the matrix row by row
    matrix = [['' for _ in range((len(plain_text) + key - 1) // key)] for _ in range(key)]
    index = 0
    for col in range(len(matrix[0])):
        for row in range(key):
            if index < len(plain_text):
                matrix[row][col] = plain_text[index]
                index += 1
    # Read the matrix row-wise
    return ''.join(''.join(row) for row in matrix)

def rail_fence_decrypt_row_major(cipher_text, key):
    cols = (len(cipher_text) + key - 1) // key
    matrix = [['' for _ in range(cols)] for _ in range(key)]
    index = 0
    # Fill the matrix row-wise
    for row in range(key):
        for col in range(cols):
            if index < len(cipher_text):
                matrix[row][col] = cipher_text[index]
                index += 1
    # Read the matrix column-wise
    decrypted = ''
    for col in range(cols):
        for row in range(key):
            if matrix[row][col]:
                decrypted += matrix[row][col]
    return decrypted

# Example usage
plain = input("Enter plain text: ")
k = int(input("Enter key (number of rows): "))

cipher = rail_fence_encrypt_row_major(plain, k)
print("Encrypted:", cipher)

original = rail_fence_decrypt_row_major(cipher, k)
print("Decrypted:", original)
