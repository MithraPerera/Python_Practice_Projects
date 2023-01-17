alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_word, shift_amount):
    encrypted_text = ""
    for c in text_word:
        position = alphabet.index(c)
        #if the position + the shift amount is greater than the number of letters in the alphabet
        #then the remainder of the shift amount divided by 26 will give us a right shift within the index limit
        if position + shift_amount > len(alphabet):
            encrypted_index = position + shift_amount
            index_outbounds = encrypted_index % len(alphabet)
            encrypted_index = index_outbounds
        #otherwise we can just add it and see the new index
        else:
            encrypted_index = position + shift_amount
        encrypted_text += alphabet[encrypted_index]
    print(encrypted_text)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

#decrypting is just doing the opposite as encrypting
#We can have a negative index because to decode we are shifting back left after shifting right to encode
def decrypt(text_word, shift_amount):
    decrypted_text = ""
    for c in text_word:
        position = alphabet.index(c)
        #negative index will only work up to -25 so we must remove the redundant shifts by getting the remainder after dividing by 26
        if position - shift_amount < -(len(alphabet)):
            decrypted_index = position - shift_amount
            index_outbounds = (-1 * decrypted_index) % len(alphabet)
            decrypted_index = -index_outbounds
        else:
            decrypted_index = position - shift_amount
        decrypted_text += alphabet[decrypted_index]
    print(decrypted_text)


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Choose an invalid option.")