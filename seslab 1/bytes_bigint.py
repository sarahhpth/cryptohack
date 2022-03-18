# 4. Crypto.Util.number.bytes_to_long() and Crypto.Util.number.long_to_bytes()
#    Python's PyCryptodome library implements this with the methods Crypto.Util.number.bytes_to_long() and Crypto.Util.number.long_to_bytes(). 
#    You may first have to install PyCryptodome and import it with from Crypto.Util.number import *. 

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

data = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

print(long_to_bytes(data))