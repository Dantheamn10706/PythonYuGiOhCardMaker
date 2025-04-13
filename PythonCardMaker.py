from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# === Base Asset Directory ===
BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series 3")
ASSETS = {
    "frame": BASE_DIR / "frames" / "Normal.png",
    "attribute": BASE_DIR / "Attributes" / "Light.png",
    "level_star": BASE_DIR / "Level" / "LV 8.png",
    "font_name": BASE_DIR / "Fonts" / "911Fonts.com_MatrixRegularSmallCapsRegular__-_911fonts.com_fonts_owRo.ttf"
}

# === Load Base Card Frame ===
card = Image.open(ASSETS["frame"]).convert("RGBA")

# === Paste Attribute Icon (Full Frame-Aligned) ===
attr_icon = Image.open(ASSETS["attribute"]).convert("RGBA")
card.paste(attr_icon, (0, 0), attr_icon)

# === Paste 12 Level Stars (Full Frame-Aligned) ===
star = Image.open(ASSETS["level_star"]).convert("RGBA")
for _ in range(12):
    card.paste(star, (0, 0), star)

# === Generate and Paste Name that Fills the Height of the Box ===
def render_and_paste_card_name(image, text, font_path, box, base_font_size=140, y_offset=12):
    # === Dynamic Padding Based on Text Length ===
    padding = 20 if len(text) > 16 else 18

    # === Stretch Settings ===
    stretch_thresholds = [
        (1.4, 1.15),
        (1.2, 1.10),
        (1.05, 1.05)
    ]
    default_stretch = 1.0

    # === Load Font ===
    font = ImageFont.truetype(str(font_path), base_font_size)

    # === Measure Character Widths ===
    char_widths = [font.getbbox(c)[2] - font.getbbox(c)[0] for c in text]
    text_width = sum(char_widths)
    text_height = max(font.getbbox(c)[3] - font.getbbox(c)[1] for c in text)

    # === Render to Temporary Image ===
    temp_img = Image.new("RGBA", (text_width + padding * 2, text_height + padding * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(temp_img)
    x = padding
    for c, w in zip(text, char_widths):
        draw.text((x, padding), c, font=font, fill="black")
        x += w

    # === Box Setup ===
    box_x, box_y, box_right, box_bottom = box
    box_w = box_right - box_x
    box_h = box_bottom - box_y

    # === Determine Vertical Stretch Based on Width Ratio ===
    text_ratio = temp_img.width / box_w
    vertical_stretch = default_stretch
    for threshold, stretch in stretch_thresholds:
        if text_ratio > threshold:
            vertical_stretch = stretch
            break

    # === Resize to Match Box Height (with Optional Stretch) ===
    scaled_width = int(temp_img.width * (box_h * vertical_stretch / temp_img.height))
    name_img = temp_img.resize((scaled_width, int(box_h * vertical_stretch)), resample=Image.BICUBIC)

    # === If Too Wide, Scale Down Horizontally ===
    if name_img.width > box_w:
        name_img = name_img.resize((box_w, name_img.height), resample=Image.BICUBIC)

    # === Paste onto Main Image ===
    paste_x = box_x + 2
    paste_y = box_bottom - name_img.height - 3 + y_offset
    image.paste(name_img, (paste_x, paste_y), name_img)

# === Place Artwork from /art Folder ===
def place_card_art(image, base_dir, top_left=(115, 258), bottom_right=(696, 845)):
    art_dir = base_dir / "art"
    for file in art_dir.iterdir():
        if file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp", ".bmp"]:
            art_path = file
            break
    else:
        print("No art image found in 'art' folder.")
        return

    art = Image.open(art_path).convert("RGBA")
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]
    art = art.resize((width, height))
    image.paste(art, top_left, art)

# === Apply Name and Artwork ===
card_name = "D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox"
name_box = (84, 52, 652, 125)
render_and_paste_card_name(card, card_name, ASSETS["font_name"], name_box, base_font_size=105, y_offset=18)
place_card_art(card, BASE_DIR)

# === Save and Show Result ===
output_path = BASE_DIR / "test_card.png"
card.save(output_path)
card.show()

print(f"Test card saved to: {output_path}")
