import qrcode


def generate_qr_code(url, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=8,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":

    url = input("Enter the URL: ")
    file_name = input("Enter the file name (without extension): ") + ".png"
    generate_qr_code(url, file_name)
 