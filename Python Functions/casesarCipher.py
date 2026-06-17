alphabets =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(orignalText, shiftAmount):
  cipherText = ""
  for letter in orignalText:
    shiftedPosition = alphabets.index(letter) + shiftAmount
    shiftedPosition %= len(alphabets)
    cipherText += alphabets[shiftedPosition]
  print(f"Here is the encoded result: {cipherText}")

# encrypt("hello", 2)

def decrypt(encodedText, shiftAmount):
  decodedText = ""
  for letter in encodedText:
    shiftedPosition = alphabets.index(letter) - shiftAmount
    shiftedPosition %= len(alphabets)
    decodedText += alphabets[shiftedPosition]
  print(f"Here is the decoded result: {decodedText}")

decrypt("jgnnq", 2)