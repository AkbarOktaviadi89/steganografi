from PIL import Image

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += chr(0)  # terminator

    data_index = 0
    binary_message = ''.join([format(ord(c), '08b') for c in message])

    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_message):
                encoded.save(output_path)
                print(f"[+] Pesan berhasil disisipkan ke: {output_path}")
                return

            r, g, b = img.getpixel((x, y))
            r = (r & ~1) | int(binary_message[data_index])
            data_index += 1

            if data_index < len(binary_message):
                g = (g & ~1) | int(binary_message[data_index])
                data_index += 1

            if data_index < len(binary_message):
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1

            encoded.putpixel((x, y), (r, g, b))

    encoded.save(output_path)
    print(f"[+] Pesan berhasil disisipkan ke: {output_path}")


def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ""
    for byte in all_bytes:
        char = chr(int(byte, 2))
        if char == chr(0):
            break
        decoded_message += char

    print("[+] Pesan ditemukan:")
    print(decoded_message)

