from PIL import Image
from colorama import Fore, Style, init
import argparse
import os

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
   _____ _                                      
  / ____| |                                     
 | (___ | |_ ___  __ _ _ __ ___   ___  _ __ ___ 
  \___ \| __/ _ \/ _` | '_ ` _ \ / _ \| '__/ __|
  ____) | ||  __/ (_| | | | | | | (_) | |  \__ \
 |_____/ \__\___|\__,_|_| |_| |_|\___/|_|  |___/
        Image Steganography Tool (CLI)
        Author: AkbarOktaviadi89
    """)

def encode_image(image_path, message, output_path):
    if not os.path.isfile(image_path):
        print(Fore.RED + f"[!] File '{image_path}' tidak ditemukan.")
        return

    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += chr(0)

    binary_message = ''.join([format(ord(c), '08b') for c in message])
    data_index = 0

    print(Fore.YELLOW + "[*] Menyisipkan pesan...")

    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_message):
                encoded.save(output_path)
                print(Fore.GREEN + f"[✓] Pesan berhasil disisipkan ke: {output_path}")
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
    print(Fore.GREEN + f"[✓] Pesan berhasil disisipkan ke: {output_path}")


def decode_image(image_path):
    if not os.path.isfile(image_path):
        print(Fore.RED + f"[!] File '{image_path}' tidak ditemukan.")
        return

    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""

    print(Fore.YELLOW + "[*] Membaca pesan tersembunyi...")

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

    print(Fore.GREEN + "[✓] Pesan ditemukan:")
    print(Fore.CYAN + decoded_message)


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Sisipkan atau ambil pesan dari gambar.")
    parser.add_argument("mode", choices=["encode", "decode"], help="Mode: encode atau decode")
    parser.add_argument("-i", "--input", help="Path ke gambar input", required=True)
    parser.add_argument("-o", "--output", help="Path gambar output (untuk encode)")
    parser.add_argument("-m", "--message", help="Pesan yang akan disisipkan (untuk encode)")

    args = parser.parse_args()

    if args.mode == "encode":
        if not args.message or not args.output:
            print(Fore.RED + "[!] Untuk mode encode, --message dan --output harus diisi.")
        else:
            encode_image(args.input, args.message, args.output)

    elif args.mode == "decode":
        decode_image(args.input)


if __name__ == "__main__":
    main()
