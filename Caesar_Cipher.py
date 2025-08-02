logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''def encrypt (original_text ,shift_amount):
    encoded_text = ""
    for letter in original_text:
        i = alphabet.index(letter) + shift_amount
        i %= len(alphabet)
        encoded_text += alphabet[i]
    print(f"Here is the encoded result: {encoded_text}")

def decrypt (original_text , shift_amount):
    decoded_text = ""
    for letter in original_text:
        i = alphabet.index(letter) - shift_amount
        i %= len(alphabet)
        decoded_text += alphabet[i]
    print(f"Here is the decoded result: {decoded_text}")'''


def caesar (original_text,shift_amount,direction_text):
    output_text=""
    if direction_text == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            i = alphabet.index(letter) + shift_amount
            i %= len(alphabet)
            output_text += alphabet[i]
        else:
            output_text += letter
    print(f"Here is the {direction_text} result: {output_text}")


loop = True

while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, direction_text=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n")
    if restart == "yes":
        loop = True
    else:
        loop = False
        print("GOOD BYE!")





















