def base64_encode(data):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    byte_array = bytearray(data, 'utf-8')
    binary_string = ''.join(format(byte, '08b') for byte in byte_array)
    
    while len(binary_string) % 6 != 0:
        binary_string += '0'

    base64_encoded = ''
    for i in range(0, len(binary_string), 6):
        six_bit_chunk = binary_string[i:i+6]
        index = int(six_bit_chunk, 2)
        base64_encoded += base64_chars[index]
   
    while len(base64_encoded) % 4 != 0:
        base64_encoded += '='
    
    return base64_encoded

input_data = "mahdi dadashzadeh"
encoded_data = base64_encode(input_data)
print("-" * 30)
print("encoded data:", encoded_data)
# ------------------------------------
def base64_decode(encoded_data):

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    encoded_data = encoded_data.rstrip('=')
    
    binary_string = ''
    for char in encoded_data:
        index = base64_chars.index(char)
        binary_string += format(index, '06b')
    
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte_chunk = binary_string[i:i+8]
        if len(byte_chunk) == 8:
            byte_array.append(int(byte_chunk, 2))
    
    decoded_data = byte_array.decode('utf-8')
    
    return decoded_data

encoded_data = "bWFoZGkgZGFkYXNoemFkZWg"
decoded_data = base64_decode(encoded_data)
print("decoded data:", decoded_data)
print("-" * 30)

# 20  55 21 46