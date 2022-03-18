# 1. chr() builtin function
#   In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).
  
numbers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
  
for number in numbers:
      
    # Convert ASCII-based number to character.
    letter = chr(number)
    print(letter)
    
print("\n")