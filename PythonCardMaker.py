from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# === Base Asset Directory ===
BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series 3")
ASSETS = {
    "frame": BASE_DIR / "frames" / "Synchro.png",
    "attribute": BASE_DIR / "Attributes" / "Divine.png",
    "level_star": BASE_DIR / "Level" / "LV 12.png",
    "font_name": BASE_DIR / "Fonts" / "911Fonts.com_MatrixRegularSmallCapsRegular__-_911fonts.com_fonts_owRo.ttf"
}

# === Load Base Card Frame ===
card = Image.open(ASSETS["frame"]).convert("RGBA")

# === Paste Attribute Icon (Full Frame-Aligned)
attr_icon = Image.open(ASSETS["attribute"]).convert("RGBA")
card.paste(attr_icon, (0, 0), attr_icon)

# === Paste 12 Level Stars (Full Frame-Aligned)
star = Image.open(ASSETS["level_star"]).convert("RGBA")
for _ in range(12):
    card.paste(star, (0, 0), star)  # No positioning for now

# === Draw Card Name ===
def draw_card_name(image, text, font_path, position=(82, 92), font_size=100):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(str(font_path), font_size)
    draw.text(position, text, font=font, fill="black")


# === Apply Name to Card
draw_card_name(card, "Test the Mighty Card", ASSETS["font_name"])

# === Save the Result
output_path = BASE_DIR / "test_card.png"
card.save(output_path)
print(f"Test card saved to: {output_path}")
