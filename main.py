def decode_hex(encoded_str: str) -> str:
    try:
        # 将十六进制字符串转换为字节串
        byte_str = bytes.fromhex(encoded_str)
        # 将字节串解码为 UTF-8 字符串
        decoded_str = byte_str.decode('utf-8')
        return decoded_str
    except Exception as e:
        print(f"Hex decoding error: {e}")
        return None

encoded_str = "zmxhz3tizhnjamhia3ptbmzyzghidmnrawpuzhnrdmjramrzywj9"
decoded_str = decode_hex(encoded_str)
if decoded_str:
    print(f"Decoded string: {decoded_str}")
else:
    print("Not a valid Hex encoded string")
