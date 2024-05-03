import qrcode

def compute(url):
    """
    Generates a QR code image for the given URL.
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')

    return {"qr_code_path": 'qr_code.png'}


def test():
    """Test the compute function."""

    print("Running test")
