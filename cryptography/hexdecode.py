hexstr=input("enter an hex for decode:")

decode_str = bytes.fromhex(hexstr)
decode_str = decode_str.decode("ascii")

print(f"{decode_str}")