num = int(input("inserte el ancho de la piramide: "))
if num <= 8:
    if num >= 8:
        print ("inserte un numero menor que 8")
        pass
for i in range(num):
  print(' ' * (num - i - 1) + "#" * (2 * i + 1))
 
  
  
