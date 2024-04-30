alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ")

# Caesar Cipher Encrypt/Decrypt
def caesar(message,shift):
	new = ""
	for letter in message:
			new += alphabet[(alphabet.index(letter.lower())+shift) % 27]
	return new.upper()



#Vigenere Encrypt
def vigenere_encrypt(text,key):
	new = ""
	index = 0
	for letter in text:
		new += alphabet[(alphabet.index(letter.lower())+(alphabet.index(key[index].lower())))%27]
		index+=1
		index = index%len(key)
	return new.upper()

# Vigenere Decrypt
def vigenere_decrypt(text, key):
	new = ""
	index = 0
	for letter in text:
		new += alphabet[(alphabet.index(letter.lower())-(alphabet.index(key[index].lower())))%27]
		index+=1
		index = index%len(key)
	return new.upper()

