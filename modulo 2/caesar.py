import string
abecedario = string.ascii_uppercase
k = 13
plaintext = "be sure to drink your Ovaltine"
ciphertext = ""
for l in plaintext:
    if l.upper() not in abecedario:
        ciphertext = ciphertext + l
        continue
        
    c = (abecedario.find(l.upper()) + k) %26
    
    
    if l.isupper():
          x = abecedario[c]
    else:
        x = abecedario[c].lower()
    
    ciphertext = ciphertext + x
    
print(ciphertext)