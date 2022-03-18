# 2. bytes.fromhex() builtin function
#    In Python, the bytes.fromhex() function can be used to convert hex to bytes. 
#    The .hex() instance method can be called on byte strings to get the hex representation. 
#    setiap 2 angka = 1 huruf

hex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

print(bytes.fromhex(hex))
print("\n")