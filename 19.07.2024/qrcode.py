import qrcode

def generate_qr_code(data, file_path):
    """Generate a QR code from the given data and save it as an image file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"QR code generated and saved to '{file_path}'.")

def main():
    data = input("Enter the data (URL or text) for the QR code: ")
    file_path = 'qrcode.png'
    generate_qr_code(data, file_path)

main()
