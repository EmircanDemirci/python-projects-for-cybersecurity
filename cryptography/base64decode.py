import base64

str_for_decode = input("Enter base64 for decode:")
str_for_decode_byte = str_for_decode.encode("ascii")

decode_str = base64.b64decode(str_for_decode_byte)

print(decode_str)