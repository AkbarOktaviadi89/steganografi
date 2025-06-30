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

