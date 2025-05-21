/* ALGORITHM: 

STEP 1: Padding: 

 Append a single '1' bit to the message. 

 Append '0' bits until the length of the padded message in bits is congruent to 448 

 mod 512. 

 Append the length of the original message in bits as a 64-bit big-endian integer. 

STEP 2: Message Parsing 

 Divide the padded message into blocks of 512 bits (64 bytes). 

STEP 3: Initialize Hash Values 

STEP 4: Concatenate the hash values to get the final SHA-1 hash value.

PROGRAM */

import hashlib 

def calculate_sha1(text): 

 sha1_hash = hashlib.sha1(text.encode()).hexdigest() 

 return sha1_hash 

def main():

text = input("Enter the text to calculate SHA-1 hash: ") 

 sha1_hash = calculate_sha1(text) 

print("SHA-1 hash of the text:", sha1_hash) 

if __name__ == "__main__": 

main() 

/*OUTPUT:
Enter the text to calculate SHA-1 hash: Hello, SHA-1!

SHA-1 hash of the text: 95e3e81b0d6f5a050bfaba65f7d8412c5042e7d2 */
