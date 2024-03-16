import os
from PIL import Image, ImageDraw, ImageFont
import qrcode

# URL for the QR code
url = 'http://futurejones.co.uk'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

# Dimensions for the final image (QR code + border + text space)
border_color = (255, 0, 127)  # Pink color in RGB
border_width = 20  # Width of the border
font_size = 40  # Set a fixed font size
text_height = 50  # Allocate space for the text "Scan me"
new_width = qr_img.width + 2 * border_width
new_height = qr_img.height + 2 * border_width + text_height
final_img = Image.new('RGB', (new_width, new_height), 'white')

# Draw the border
draw = ImageDraw.Draw(final_img)
draw.rectangle(
    [0, 0, new_width, new_height - text_height],
    outline=border_color,
    width=border_width
)

# Paste the QR code onto the final image
final_img.paste(qr_img, (border_width, border_width))

# Load the font (use a default font if the custom font fails to load)
script_dir = os.path.dirname(os.path.realpath(__file__))
font_path = os.path.join(script_dir, 'Updock-Regular.ttf')
try:
    font = ImageFont.truetype(font_path, font_size)
except Exception as e:
    print(f"Using default font due to error: {e}")
    font = ImageFont.load_default()

# Define the text to add below the QR code
text = "Scan me"

# Draw the text onto the image centered
# Since we're not calculating text width, this is an approximation
text_x = (new_width / 2) - (font_size * 1)  # Rough estimate to center "Scan me"
text_y = qr_img.height + (1.7 * border_width)  # Position below the QR code

draw.text((text_x, text_y), text, fill=border_color, font=font)

# Save the final image
final_img.save("futurejones_co_uk_qr_with_border.png")
print("QR code with custom border and text generated and saved.")
