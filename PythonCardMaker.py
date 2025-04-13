from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# === Base Asset Directory ===
BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series 3")
ASSETS = {
    "frame": BASE_DIR / "frames" / "Spell.png",
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

# === Draw Card Type Field with Compression ===
def draw_card_type(image, text, font_path, box=(85, 925, 640, 940), font_size=32, y_offset=0):
    formatted_text = f"[{text}]"
    font = ImageFont.truetype(str(font_path), font_size)

    # Metrics and temporary image for text
    ascent, descent = font.getmetrics()
    draw_img = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    text_width = draw_img.textlength(formatted_text, font=font)
    text_height = ascent + descent

    temp_img = Image.new("RGBA", (int(text_width), text_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(temp_img)
    draw.text((0, 0), formatted_text, font=font, fill="black")

    # Extract box dimensions
    box_x, box_y, box_right, box_bottom = box
    box_w = box_right - box_x

    # === Compression Tier System ===
    char_count = len(formatted_text)

    if char_count > 20:
        compression = 0.85  # Strong compression
    elif char_count > 16:
        compression = 0.87  # Light compression
    else:
        compression = 1.00  # No compression

    # Apply compression if needed
    if compression < 1.0:
        new_width = int(temp_img.width * compression)
        temp_img = temp_img.resize((new_width, temp_img.height), resample=Image.BICUBIC)

    # Paste bottom-left aligned
    paste_x = box_x
    paste_y = box_bottom - temp_img.height + y_offset
    image.paste(temp_img, (paste_x, paste_y), temp_img)
    
def draw_atk_value(image, value, font_path, box=(470, 984, 555, 1000), font_size=7.5):
    font = ImageFont.truetype(str(font_path), int(font_size))
    draw = ImageDraw.Draw(image)

    text = str(value)
    text_width = draw.textlength(text, font=font)

    box_x, box_y, box_right, box_bottom = box
    x = box_right - text_width  # Right-aligned
    y = box_y  # Top aligned (adjust if needed)

    draw.text((x, y), text, font=font, fill="black")

def draw_def_value(image, value, font_path, box=(575, 1091, 660, 1170), font_size=35):
    font = ImageFont.truetype(str(font_path), int(font_size))
    draw = ImageDraw.Draw(image)

    text = str(value)
    text_width = draw.textlength(text, font=font)

    box_x, box_y, box_right, box_bottom = box
    x = box_right - text_width  # Right-aligned
    y = box_y

    draw.text((x, y), text, font=font, fill="black")
    
def draw_description(image, text, base_dir, frame_name, type_box=None, desc_box_right=660, font_size=32, line_spacing=4):
    from PIL import ImageFont, ImageDraw

    # === Font Selection ===
    normal_font = base_dir / "Fonts" / "Stone Serif ITC Medium.ttf"
    effect_font = base_dir / "Fonts" / "Matrix Book.ttf"
    font_path = normal_font if "Normal" in frame_name else effect_font

    # === Default Coordinates if type_box is None ===
    if type_box:
        base_x = type_box[0]
        base_y = type_box[1]
    else:
        base_x = 85
        base_y = 925

    # === Spell/Trap Adjustments ===
    is_spell_or_trap = "Spell" in frame_name or "Trap" in frame_name
    y_start = base_y - 10 if is_spell_or_trap else base_y + 15
    bottom_limit = 1075 + 70 if is_spell_or_trap else 1075

    x = base_x
    max_width = (desc_box_right - 15) - x
    draw = ImageDraw.Draw(image)

    # === Normalize Text ===
    paragraphs = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')

    # === Font Shrinking Loop ===
    current_font_size = font_size
    best_fit_font = None
    best_fit_lines = []

    while current_font_size >= 12:
        font = ImageFont.truetype(str(font_path), current_font_size)
        lines = []
        y = y_start
        fits = True

        for paragraph in paragraphs:
            words = paragraph.split()
            current_line = ""
            for word in words:
                test_line = f"{current_line} {word}".strip()
                width = draw.textlength(test_line, font=font)
                if width <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    y += current_font_size + line_spacing
                    if y + current_font_size > bottom_limit:
                        fits = False
                        break
                    current_line = word
            if not fits:
                break
            if current_line:
                lines.append(current_line)
                y += current_font_size + line_spacing
                if y + current_font_size > bottom_limit:
                    fits = False
                    break

        if fits:
            best_fit_font = font
            best_fit_lines = lines
            break
        else:
            current_font_size -= 1

    # === Final Render Pass ===
    y = y_start
    for line in best_fit_lines:
        draw.text((x, y), line, font=best_fit_font, fill="black")
        y += best_fit_font.size + line_spacing

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
card_name = "Blue-Eyes White Dragon"
name_box = (84, 52, 652, 125)
render_and_paste_card_name(
    card,
    card_name,
    ASSETS["font_name"],
    name_box,
    base_font_size=105,
    y_offset=18
)

place_card_art(card, BASE_DIR)

# === Draw Type Line ===
#type_text = "Dragon"
#type_font = BASE_DIR / "Fonts" / "Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf"
#type_box = (85, 925, 640, 940)
#draw_card_type(
#    card,
#    type_text,
#    type_font,
#    box=type_box,
#    font_size=32,
#    y_offset=5
#)

# === Load Description from File (as a flat string) ===
desc_file = BASE_DIR / "temp" / "desc.txt"
with open(desc_file, encoding="utf-8") as f:
    desc_text = f.read().strip()  # Don't split or transform into a list

draw_description(
    card,
    desc_text,
    BASE_DIR,
    frame_name=ASSETS["frame"].name,
    desc_box_right=750,
    font_size=26,
    line_spacing=4
)



# === Draw ATK Value ===
#atk_value = 3000
#atk_font = BASE_DIR / "Fonts" / "MatrixSmallCaps-Bold.otf"
#atk_box = (475, 1091, 560, 117)
#draw_atk_value(card, atk_value, atk_font, box=atk_box, font_size=35)

# === Draw DEF Value ===
#def_value = 2500
#def_font = BASE_DIR / "Fonts" / "MatrixSmallCaps-Bold.otf"
#def_box = (640, 1091, 725, 1170)
#draw_def_value(card, def_value, def_font, box=def_box, font_size=35)

# === Save and Show Result ===
output_path = BASE_DIR / "test_card.png"
card.save(output_path)
card.show()

print(f"Test card saved to: {output_path}")
