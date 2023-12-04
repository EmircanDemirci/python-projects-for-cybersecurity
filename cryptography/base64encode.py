import base64

str_for_encode = input("Enter string for encoding:")#entering a string for encode
encode_type = str_for_encode.encode("ascii")#string encode type ex/ascii
strbyte = base64.b64encode(encode_type)#base64 encode func

print(f"{strbyte}")
