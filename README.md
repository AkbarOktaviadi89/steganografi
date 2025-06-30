
# 🖼️ Image Steganography CLI Tool

A simple yet powerful CLI-based steganography tool written in Python that allows you to **hide** and **reveal** secret messages inside images using **Least Significant Bit (LSB)** encoding.

---

## 🚀 Features

- Encode secret messages into images.
- Decode messages from steganographed images.
- Colorful CLI with banner and helpful prompts.
- Lightweight and beginner-friendly.
- Supports PNG and JPEG images.

---

## 📦 Requirements

- Python 3.x
- Pillow
- Colorama

### Install dependencies:

```bash
pip install pillow colorama
```

---

## 📂 Project Structure

```
image_steganography/
├── stegano.py       # Main CLI script
├── input.jpg        # Original image (example)
├── output.jpg       # Image with hidden message
└── README.md        # Documentation
```

---

## 💻 Usage

### Encode a Message into Image

```bash
python stegano.py encode -i input.jpg -o output.jpg -m "This is a secret message"
```

### Decode a Message from Image

```bash
python stegano.py decode -i output.jpg
```

---

## 🛠️ How it Works

This script hides messages inside image pixels using **LSB (Least Significant Bit)** encoding.
Each character is converted to binary and encoded into the RGB values of each pixel.

---

## ⚠️ Notes

- Works best with larger images for longer messages.
- Only supports hiding **text messages**, not files.
- Do **not** compress or resize the output image after encoding — it may corrupt the hidden data.

---

## 👨‍💻 Author

Created by **Akbar Oktaviadi**  
🔗 GitHub: [AkbarOktaviadi89](https://github.com/AkbarOktaviadi89)

---

## 📜 License

MIT License
