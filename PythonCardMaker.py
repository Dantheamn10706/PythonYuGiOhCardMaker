import sqlite3
import os
import json
import base64
import time
import re
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # For cleaner UI (optional but recommended)
from pathlib import Path


def set_layout_constants(SeriesNum):
    
    global CARD_NAME_BOX_TOP_LEFT, CARD_NAME_BOX_BOTTOM_RIGHT, CARD_NAME_Y_OFFSET, CARD_NAME_X_OFFSET,CARD_NAME_FONT_SIZE
    global TYPE_LINE_TOP_LEFT, TYPE_LINE_BOTTOM_RIGHT, TYPE_LINE_Y_OFFSET
    global DESC_BOX_MONSTER_TOP_LEFT, DESC_BOX_BOTTOM_RIGHT_MONSTER, DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP
    global DESC_BOX_SPELL_TRAP_TOP_LEFT, DESC_BOX_MONSTER_Y_OFFSET, DESC_BOX_SPELL_TRAP_Y_OFFSET
    global ATKDEF_FONT, ATK_BOX_TOP_LEFT, ATK_BOX_BOTTOM_RIGHT, ATK_Y_OFFSET, ATK_OFFSET_X
    global DEF_BOX_TOP_LEFT, DEF_BOX_BOTTOM_RIGHT, DEF_Y_OFFSET, DEF_OFFSET_X
    global LINK_RATING_X, LINK_RATING_Y,LINK_RATING_FONT_SIZE
    global ART_TOP_LEFT_REGULAR, ART_BOTTOM_RIGHT_REGULAR, ART_TOP_LEFT_PENDULUM, ART_BOTTOM_RIGHT_PENDULUM
    global PEND_LEFT_SCALE_POS, PEND_RIGHT_SCALE_POS, PEND_SCALE_SIZE
    global PEND_DESC_TOP_LEFT, PEND_DESC_BOTTOM_RIGHT
    
    globals_to_clear = [
        "CARD_NAME_BOX_TOP_LEFT", "CARD_NAME_BOX_BOTTOM_RIGHT", "CARD_NAME_Y_OFFSET", "CARD_NAME_X_OFFSET","CARD_NAME_FONT_SIZE",
        "TYPE_LINE_TOP_LEFT", "TYPE_LINE_BOTTOM_RIGHT", "TYPE_LINE_Y_OFFSET",
        "DESC_BOX_MONSTER_TOP_LEFT", "DESC_BOX_BOTTOM_RIGHT_MONSTER", "DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP",
        "DESC_BOX_SPELL_TRAP_TOP_LEFT", "DESC_BOX_MONSTER_Y_OFFSET", "DESC_BOX_SPELL_TRAP_Y_OFFSET",
        "ATKDEF_FONT", "ATK_BOX_TOP_LEFT", "ATK_BOX_BOTTOM_RIGHT", "ATK_Y_OFFSET", "ATK_OFFSET_X",
        "DEF_BOX_TOP_LEFT", "DEF_BOX_BOTTOM_RIGHT", "DEF_Y_OFFSET", "DEF_OFFSET_X",
        "LINK_RATING_X", "LINK_RATING_Y","LINK_RATING_FONT_SIZE",
        "ART_TOP_LEFT_REGULAR", "ART_BOTTOM_RIGHT_REGULAR", "ART_TOP_LEFT_PENDULUM", "ART_BOTTOM_RIGHT_PENDULUM",
        "PEND_LEFT_SCALE_POS", "PEND_RIGHT_SCALE_POS", "PEND_SCALE_SIZE",
        "PEND_DESC_TOP_LEFT", "PEND_DESC_BOTTOM_RIGHT"
    ]


    # Clear previous values
    CARD_NAME_BOX_TOP_LEFT = None
    CARD_NAME_BOX_BOTTOM_RIGHT = None
    CARD_NAME_Y_OFFSET = None
    CARD_NAME_X_OFFSET = None
    CARD_NAME_FONT_SIZE = None

    TYPE_LINE_TOP_LEFT = None
    TYPE_LINE_BOTTOM_RIGHT = None
    TYPE_LINE_Y_OFFSET = None

    DESC_BOX_MONSTER_TOP_LEFT = None
    DESC_BOX_BOTTOM_RIGHT_MONSTER = None
    DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = None
    DESC_BOX_SPELL_TRAP_TOP_LEFT = None
    DESC_BOX_MONSTER_Y_OFFSET = None
    DESC_BOX_SPELL_TRAP_Y_OFFSET = None

    ATKDEF_FONT = None
    ATK_BOX_TOP_LEFT = None
    ATK_BOX_BOTTOM_RIGHT = None
    ATK_Y_OFFSET = None
    ATK_OFFSET_X = None

    DEF_BOX_TOP_LEFT = None
    DEF_BOX_BOTTOM_RIGHT = None
    DEF_Y_OFFSET = None
    DEF_OFFSET_X = None

    LINK_RATING_X = None
    LINK_RATING_Y = None
    LINK_RATING_FONT_SIZE =None

    ART_TOP_LEFT_REGULAR = None
    ART_BOTTOM_RIGHT_REGULAR = None
    ART_TOP_LEFT_PENDULUM = None
    ART_BOTTOM_RIGHT_PENDULUM = None

    PEND_LEFT_SCALE_POS = None
    PEND_RIGHT_SCALE_POS = None
    PEND_SCALE_SIZE = None

    PEND_DESC_TOP_LEFT = None
    PEND_DESC_BOTTOM_RIGHT = None
   

    if SeriesNum == "3":
        CARD_NAME_BOX_TOP_LEFT = (80, 42)
        CARD_NAME_BOX_BOTTOM_RIGHT = (652, 115)
        CARD_NAME_Y_OFFSET = 15
        CARD_NAME_X_OFFSET = 0
        CARD_NAME_FONT_SIZE= 105
    
        TYPE_LINE_TOP_LEFT = (80, 925)
        TYPE_LINE_BOTTOM_RIGHT = (640, 940)
        TYPE_LINE_Y_OFFSET = 5

        DESC_BOX_MONSTER_TOP_LEFT = (80, 942)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (745, 1069)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (745, 1110)
        DESC_BOX_SPELL_TRAP_TOP_LEFT= (80,905)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT=36

        ATK_BOX_TOP_LEFT = (475, 1083)
        ATK_BOX_BOTTOM_RIGHT = (560, 1162)
        ATK_Y_OFFSET = -2
        ATK_OFFSET_X = 10

        DEF_BOX_TOP_LEFT = (640, 1083)
        DEF_BOX_BOTTOM_RIGHT = (725, 1162)
        DEF_Y_OFFSET = -2
        DEF_OFFSET_X = 5

        LINK_RATING_X = 720
        LINK_RATING_Y = 1085
        LINK_RATING_FONT_SIZE = 25

        ART_TOP_LEFT_REGULAR = (115, 259)
        ART_BOTTOM_RIGHT_REGULAR = (697, 845)
        ART_TOP_LEFT_PENDULUM = (68, 244)
        ART_BOTTOM_RIGHT_PENDULUM = (740, 760)

        PEND_LEFT_SCALE_POS = (100, 845)
        PEND_RIGHT_SCALE_POS = (710, 845)
        PEND_SCALE_SIZE = (28, 28)

        PEND_DESC_TOP_LEFT = (136, 767)
        PEND_DESC_BOTTOM_RIGHT = (671, 890)
    elif SeriesNum == "7":
        CARD_NAME_BOX_TOP_LEFT = (65, 45)
        CARD_NAME_BOX_BOTTOM_RIGHT = (692, 125)
        CARD_NAME_Y_OFFSET = 5
        CARD_NAME_X_OFFSET = 22
        CARD_NAME_FONT_SIZE= 105

        TYPE_LINE_TOP_LEFT = (75, 910)
        TYPE_LINE_BOTTOM_RIGHT = (650, 925)
        TYPE_LINE_Y_OFFSET = 8
        
        DESC_BOX_MONSTER_TOP_LEFT = (80, 930)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (745, 1069)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (745, 1115)
        DESC_BOX_SPELL_TRAP_TOP_LEFT= (80,895)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT=36

        ATK_BOX_TOP_LEFT = (480, 1083)
        ATK_BOX_BOTTOM_RIGHT = (565, 1162)
        ATK_Y_OFFSET = 0
        ATK_OFFSET_X = 10

        DEF_BOX_TOP_LEFT = (648, 1083)
        DEF_BOX_BOTTOM_RIGHT = (733, 1162)
        DEF_Y_OFFSET = 0
        DEF_OFFSET_X = 5

        LINK_RATING_X = 725
        LINK_RATING_Y = 1083
        LINK_RATING_FONT_SIZE = 25

        ART_TOP_LEFT_REGULAR = (115, 245)
        ART_BOTTOM_RIGHT_REGULAR = (697, 829)
        ART_TOP_LEFT_PENDULUM = (67, 233)
        ART_BOTTOM_RIGHT_PENDULUM = (739, 758)

        PEND_LEFT_SCALE_POS = (100, 845)
        PEND_RIGHT_SCALE_POS = (710, 845)
        PEND_SCALE_SIZE = (28, 28)

        PEND_DESC_TOP_LEFT = (136, 767)
        PEND_DESC_BOTTOM_RIGHT = (671, 890)
    elif SeriesNum == "9":
        CARD_NAME_BOX_TOP_LEFT = (50, 45)
        CARD_NAME_BOX_BOTTOM_RIGHT = (692, 125)
        CARD_NAME_Y_OFFSET = -3
        CARD_NAME_X_OFFSET = 22
        CARD_NAME_FONT_SIZE= 105

        TYPE_LINE_TOP_LEFT = (65, 902)
        TYPE_LINE_BOTTOM_RIGHT = (670, 922)
        TYPE_LINE_Y_OFFSET = 3
        
        DESC_BOX_MONSTER_TOP_LEFT = (65, 922)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (763, 1069)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (763, 1115)
        DESC_BOX_SPELL_TRAP_TOP_LEFT= (65,890)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT=36

        ATK_BOX_TOP_LEFT = (400, 1083)
        ATK_BOX_BOTTOM_RIGHT = (ATK_BOX_TOP_LEFT[0]+175, 1162)
        ATK_Y_OFFSET = -2
        ATK_OFFSET_X = 10

        DEF_BOX_TOP_LEFT = (570, 1083)
        DEF_BOX_BOTTOM_RIGHT = (DEF_BOX_TOP_LEFT[0]+175, 1162)
        DEF_Y_OFFSET = 0
        DEF_OFFSET_X = 5

        LINK_RATING_X = 725
        LINK_RATING_Y = 1083
        LINK_RATING_FONT_SIZE = 25

        ART_TOP_LEFT_REGULAR = (100, 219)
        ART_BOTTOM_RIGHT_REGULAR = (715, 835)
        ART_TOP_LEFT_PENDULUM = (53, 212)
        ART_BOTTOM_RIGHT_PENDULUM = (758, 740)


        PEND_LEFT_SCALE_POS = (90, 835)
        PEND_RIGHT_SCALE_POS = (720, 835)
        PEND_SCALE_SIZE = (28, 28)

        PEND_DESC_TOP_LEFT = (136, 747)
        PEND_DESC_BOTTOM_RIGHT = (671, 875)
    elif SeriesNum == "10":
        CARD_NAME_BOX_TOP_LEFT = (40, 50)
        CARD_NAME_BOX_BOTTOM_RIGHT = (572, 120)
        CARD_NAME_Y_OFFSET = -18
        CARD_NAME_X_OFFSET = -65
        CARD_NAME_FONT_SIZE= 80

        TYPE_LINE_TOP_LEFT = (50, 770)
        TYPE_LINE_BOTTOM_RIGHT = (670, TYPE_LINE_TOP_LEFT[1]+25)
        TYPE_LINE_Y_OFFSET = 3
        
        DESC_BOX_MONSTER_TOP_LEFT = (55, 793)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (650, 922)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (650, 945)
        DESC_BOX_SPELL_TRAP_TOP_LEFT= (60,765)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        
        ATKDEF_FONT=28
        
        ATK_BOX_TOP_LEFT = (310, 930)
        ATK_BOX_BOTTOM_RIGHT = (ATK_BOX_TOP_LEFT[0]+175, 1162)
        ATK_Y_OFFSET = -2
        ATK_OFFSET_X = 0

        DEF_BOX_TOP_LEFT = (455, 930)
        DEF_BOX_BOTTOM_RIGHT = (DEF_BOX_TOP_LEFT[0]+175, 1162)
        DEF_Y_OFFSET = -2
        DEF_OFFSET_X = -5

        LINK_RATING_X = 638
        LINK_RATING_Y = 928
        LINK_RATING_FONT_SIZE=25

        ART_TOP_LEFT_REGULAR = (85, 187)
        ART_BOTTOM_RIGHT_REGULAR = (613, 715)
        ART_TOP_LEFT_PENDULUM = (48, 182)
        ART_BOTTOM_RIGHT_PENDULUM = (650, 633)

        #SALE_FONT=
        PEND_LEFT_SCALE_POS = (77, 720)
        PEND_RIGHT_SCALE_POS = (623, 720)
        PEND_SCALE_SIZE = (28, 28)

        PEND_DESC_TOP_LEFT = (112, 639)
        PEND_DESC_BOTTOM_RIGHT = (590, 750)
        
          # TODO: Other series cases ("7", "9", "10") not shown here — keep those as-is

    # Dump values for debugging
    print("\n=== Layout Constants Dump ===")
    for var in globals_to_clear:
        print(f"{var}: {globals().get(var)}")
    print("=" * 40)


SeriesNum="3"
set_layout_constants(SeriesNum)
#set_layout_constants(SeriesNum)

safe_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.'-…()"



# Path to the database file
db_file_path = "F:/YGOPro/pics/templates/Automated templates/cards.cdb"
# === Exclude specific card IDs from rendering ===
excluded_ids = {
        #513000136, 513000134,513000135, 
        170000152, 170000151,170000153, 170000201, 
        10000000, 10000010, 10000020
    }

# download folder
download_dir = r"X:\Other\Downloads"

database_directories = [
    #"F:/YGOPro/Custom/Solo CDB"#,
    "F:/YGOPro/expansions",
    "F:/YGOPro/repositories/delta-bagooska/"
    
]

FRAME_FILE_TO_TYPE_ID = {
        "Normal.png": 17,
        "Effect.png": 33,
        "Fusion.png": 65,
        "Ritual.png": 129,
        "Synchro.png": 8193,
        "Xyz.png": 8388609,
        "Link.png": 67108865,
        "Pen_Normal.png": 16777233,
        "Pen_Effect.png": 50331681,
        "Pen_Fusion.png": 16777313,
        "Pen_Ritual.png": 16777377,
        "Pen_Synchro.png": 16785441,
        "Pen_Xyz.png": 25165857,
        "Token.png": 16401,
        "Dark_Synchro.png": 8225,
        "Legendary_Dragon": 102,
        "Obelisk.png": 103,
        "Ra.png": 104,
        "Slifer.png": 105,
        "Z-Arc.png": 106
    }

database_paths = []
for directory in database_directories:
    for file in os.listdir(directory):
        if file.lower().endswith(".cdb") and "skill" not in file.lower():
            database_paths.append(os.path.join(directory, file))


def launch_form_mode():
    import tkinter as tk
    from tkinter import filedialog, messagebox
    from pathlib import Path
    import time
    from PIL import Image

    BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series "+SeriesNum)
    OUTPUT_DIR = BASE_DIR


# 💡 Dump the list of loaded databases
print("Loaded the following databases:")
for path in database_paths:
    print(path)
print("=" * 50)

# print(database_paths)
# Attributes based on standard Yu-Gi-Oh attributes
ATTRIBUTES = {
    0x1: "EARTH",
    0x2: "WATER",
    0x4: "FIRE",
    0x8: "WIND",
    0x10: "LIGHT",
    0x20: "DARK",
    0x40: "DIVINE"
}

# Monster races based on the provided spoiler list
MONSTER_RACES = {
    1: "Warrior",
    2: "Spellcaster",
    4: "Fairy",
    8: "Fiend",
    16: "Zombie",
    32: "Machine",
    64: "Aqua",
    128: "Pyro",
    256: "Rock",
    512: "Winged-Beast",
    1024: "Plant",
    2048: "Insect",
    4096: "Thunder",
    8192: "Dragon",
    16384: "Beast",
    32768: "Beast-Warrior",
    65536: "Dinosaur",
    131072: "Fish",
    262144: "Sea Serpent",
    524288: "Reptile",
    1048576: "Psychic",
    2097152: "Divine-Beast",
    4194304: "Creator God",
    8388608: "Wyrm",
    16777216: "Cyberse",
    33554432: "Illusion"
}

# Card types separated by category
Monster_CARD_TYPES = {
    17: "Normal ",
    33: "Effect ",
    33554465: "Effect ",
    33558561: "Effect ",
    65: "Fusion ",
    97: "Fusion / Effect ",
    129: "Ritual ",
    161: "Ritual / Effect ",
    4257: "Ritual / Tuner / Effect ",
    673: "Ritual / Spirit / Effect ",
    2097313: "Ritual / Flip / Effect ",
    545: "Spirit / Effect",
    33554977: "Spirit / Effect",
    1057: "Union / Effect",
    5153: "Union / Tuner / Effect",
    2081: "Gemini / Effect",
    4113: "Tuner ",
    4129: "Tuner / Effect",
    4161: "Fusion / Tuner",
    4193: "Fusion / Tuner / Effect",
    8193: "Synchro ",
    8225: "Synchro / Effect ",
    12321: "Synchro / Tuner / Effect ",
    16401: "Token",
    20497: "Token / Tuner",
    2097185: "Flip / Effect ",
    2101281: "Flip / Tuner / Effect ",
    4194337: "Toon /Effect",
    37748769: "Toon / Effect",
    8388609: "Xyz ",
    8388641: "Xyz / Effect ",
    16777233: "Pendulum",
    16777249: "Pendulum / Effect",
    50331681: "Pendulum / Effect",
    16781329: "Pendulum / Tuner",
    18874401: "Pendulum / Flip / Effect",
    16777761: "Pendulum / Spirit / Effect",
    16781345: "Pendulum / Tuner / Effect",
    16777313: "Fusion / Pendulum / Effect",
    16777377: "Ritual / Pendulum / Effect",
    16785441: "Synchro / Pendulum / Effect",
    25165857: "Xyz / Pendulum / Effect",
    67108865: "Link",
    67108897: "Link/Effect",
    103: "Normal",
    104: "Normal",
    105: "Normal"

}

Spell_CARD_TYPES = {
    2: "Normal Spell ",
    65538: "Quick-Play Spell ",
    131074: "Continuous Spell ",
    262146: "Equip Spell ",
    130: "Ritual Spell",
    524290: "Field Spell ",
}

Trap_CARD_TYPES = {
    4: "Normal Trap ",
    1048580: "Counter Trap ",
    131076: "Continuous Trap "
}

# Array to store unrecognized card types
unrecognized_cards = []

# Connect to the database
#conn = sqlite3.connect(db_file_path)
# = conn.cursor()

# Function to clear the console
# Function to determine the card category (Monster, Spell, Trap)
def get_card_category(card_type):
    if card_type in Monster_CARD_TYPES:
        return "Monster", Monster_CARD_TYPES[card_type]
    elif card_type in Spell_CARD_TYPES:
        return "Spell", Spell_CARD_TYPES[card_type]
    elif card_type in Trap_CARD_TYPES:
        return "Trap", Trap_CARD_TYPES[card_type]
    else:
        return "Unknown", None

# Function to process all records in the database
# Prompt the user to enter the number of records they wish to access
        
import re

SAFE_FONT_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.'-…()[]\"“”‘’:;!? ")

def prompt_series_selection():
    print("=== Select Card Layout Series ===")
    print("3 → Series 3 layout")
    print("7 → Series 7 layout")
    print("9 → Series 9 layout")
    print("10 → Series 10 layout")

    valid_choices = {"3", "7", "9", "10"}
    while True:
        choice = input("Enter the number for the Series: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid input. Please enter 3, 7, 9, or 10.")

# Prompt and apply layout

def get_font_for_char(char, primary_font, fallback_font):
    if char in SAFE_FONT_CHARS:
        return primary_font
    return fallback_font

def extract_pendulum_parts(full_text):
    import re

    pendulum_text = ""
    monster_text = ""

    # Normalize line breaks and trim the full text
    full_text = full_text.replace('\r\n', '\n').replace('\r', '\n').strip()

    # Split on divider (at least 5 dashes)
    parts = re.split(r'-{5,}', full_text)

    # Check for proper Pendulum section with divider and header
    if len(parts) == 2 and "[Pendulum Effect]" in parts[0] or "[ Pendulum Effect ]" in parts[0]:
        pendulum_part = parts[0].strip()
        other_part = parts[1].strip()

        # Remove Pendulum header
        pendulum_text = re.sub(r"^\[ *Pendulum Effect *\]", "", pendulum_part, flags=re.IGNORECASE).strip()

        # Check for Monster or Flavor text header
        if "[ Monster Effect ]" in other_part:
            monster_text = re.sub(r"^\[ *Monster Effect *\]", "", other_part, flags=re.IGNORECASE).strip()
        elif "[ Flavor Text ]" in other_part:
            monster_text = re.sub(r"^\[ *Flavor Text *\]", "", other_part, flags=re.IGNORECASE).strip()
        else:
            monster_text = other_part.strip()
    else:
        # Fallback: treat entire text as monster effect
        pendulum_text = ""
        monster_text = full_text

    return pendulum_text, monster_text

def get_asset_paths(card_info, base_dir):
    frame_map = {
        "normal": "Normal.png",
        "effect": "Effect.png",
        "fusion": "Fusion.png",
        "ritual": "Ritual.png",
        "synchro": "Synchro.png",
        "xyz": "Xyz.png",
        "spell": "Spell.png",
        "trap": "Trap.png"
    }

    link_type_ids = {67108865, 67108897}
    if type_id in link_type_ids:
        frame_file = "Link.png"


    # Pendulum frame overrides
    pendulum_normal_ids = {16777233}
    pendulum_effect_ids = {16781345, 16777761, 18874401, 16777249, 50331681, 16781329}
    pendulum_fusion_id = 16777313
    pendulum_ritual_id = 16777377
    pendulum_synchro_id = 16785441
    pendulum_xyz_id = 25165857

    type_id = card_info.get("type_id", 0)
    category = card_info.get("category", "").lower()
    frame_type = card_info["type_ability"].lower()

    if type_id in pendulum_normal_ids:
        frame_file = "Pen_Normal.png"
    elif type_id in pendulum_effect_ids:
        frame_file = "Pen_Effect.png"
    elif type_id == pendulum_fusion_id:
        frame_file = "Pen_Fusion.png"
    elif type_id == pendulum_ritual_id:
        frame_file = "Pen_Ritual.png"
    elif type_id == pendulum_synchro_id:
        frame_file = "Pen_Synchro.png"
    elif type_id == pendulum_xyz_id:
        frame_file = "Pen_Xyz.png"
    else:
        if category == "monster":
            if "fusion" in frame_type:
                frame_file = frame_map["fusion"]
            elif "ritual" in frame_type:
                frame_file = frame_map["ritual"]
            elif "synchro" in frame_type:
                frame_file = frame_map["synchro"]
            elif "xyz" in frame_type:
                frame_file = frame_map["xyz"]
            elif "effect" in frame_type:
                frame_file = frame_map["effect"]
            else:
                frame_file = frame_map["normal"]
        elif category == "spell":
            frame_file = frame_map["spell"]
        elif category == "trap":
            frame_file = frame_map["trap"]
        else:
            frame_file = frame_map["normal"]

    attr_icon = f"{card_info['attribute'].capitalize()}.png"
    attr_path = base_dir / "Attributes" / attr_icon
    frame_path = base_dir / "frames" / frame_file

    banner_path = None
    if "spell" in frame_type or "trap" in frame_type:
        sf_map = {
            "FIELD": "Field",
            "EQUIP": "Equip",
            "CONTINUOUS": "Continuous",
            "RITUAL": "Ritual",
            "QUICK-PLAY": "Quick-Play",
            "COUNTER": "Counter"
        }
        raw = card_info.get("sf", "").upper()
        if raw in sf_map:
            banner_type = sf_map[raw]
            prefix = "Spell" if "spell" in frame_type else "Trap"
            banner_path = base_dir / "Banner" / f"{prefix}_{banner_type}.png"

    if "xyz" in frame_type:
        level_icon = f"Rk {card_info['level']}.png"
    else:
        level_icon = f"LV {card_info['level']}.png"
    level_path = base_dir / "Level" / level_icon

    return {
        "frame": frame_path,
        "attribute": attr_path,
        "level_star": level_path,
        "banner": banner_path
    }

def draw_pendulum_scales(image, left_scale, right_scale, base_dir):
    from PIL import ImageFont, ImageDraw, Image

    font_path = base_dir / "Fonts" / "Matrix Book.ttf"
    font_size = 64  # Render big for high-quality downscaling
    font = ImageFont.truetype(str(font_path), font_size)
    color = "black"
    target_size = PEND_SCALE_SIZE = (28, 28)  # Final desired visual size
    positions = {
        "left": PEND_LEFT_SCALE_POS,
        "right": PEND_RIGHT_SCALE_POS
    }

    def render_and_scale(scale_value):
        text = str(scale_value)
        bbox = font.getbbox(text)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]

        # Create canvas with correct full glyph box
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((-bbox[0], -bbox[1]), text, font=font, fill=color)  # Correct baseline offset

        # Resize to target size
        img_resized = img.resize(target_size, Image.BICUBIC)
        return img_resized

    # Render and paste left and right
    for label, coord in positions.items():
        scale = left_scale if label == "left" else right_scale
        scale_img = render_and_scale(scale)
        x, y = coord
        image.paste(scale_img, (x - scale_img.width // 2, y - scale_img.height // 2), scale_img)

#####################################################    

def draw_card_image(card_info, base_dir, save_dir=None, overrides=None):
    from PIL import Image
    from pathlib import Path

    frame_type = card_info["type_ability"].lower()
    category = card_info.get("category", "").lower()
    type_id = card_info.get("type_id", 0)

    pendulum_type_ids = {
        16777233, 16777249, 50331681, 16781329,
        16777313, 16777377, 16781345, 16777761,
        18874401, 16785441, 25165857
    }
    link_type_ids = {67108865, 67108897}

    frame_override = (overrides or {}).get("frame")
    if frame_override:
        frame_file = Path(frame_override).name
    else:
        if type_id == 16401:
            frame_file = "Token.png"
        #elif type_id == 8225:
        #    frame_file = "Dark_Synchro.png"
        elif type_id == 102:
            frame_file = "Legendary_Dragon.png"
        elif type_id == 103:
            frame_file = "Obelisk.png"
        elif type_id == 104:
            frame_file = "Ra.png"
        elif type_id == 105:
            frame_file = "Slifer.png"
        elif type_id == 106:
            frame_file = "Z-Arc.png"
        elif type_id in link_type_ids:
            frame_file = "Link.png"
        elif type_id == 16777313:
            frame_file = "Pen_Fusion.png"
        elif type_id == 16777377:
            frame_file = "Pen_Ritual.png"
        elif type_id == 16785441:
            frame_file = "Pen_Synchro.png"
        elif type_id == 25165857:
            frame_file = "Pen_Xyz.png"
        elif type_id == 16777233:
            frame_file = "Pen_Normal.png"
        elif type_id in {16781345, 16777761, 18874401, 16777249, 50331681, 16781329}:
            frame_file = "Pen_Effect.png"
        elif category == "monster":
            if "fusion" in frame_type:
                frame_file = "Fusion.png"
            elif "ritual" in frame_type:
                frame_file = "Ritual.png"
            elif "synchro" in frame_type:
                frame_file = "Synchro.png"
            elif "xyz" in frame_type:
                frame_file = "Xyz.png"
            elif "effect" in frame_type:
                frame_file = "Effect.png"
            else:
                frame_file = "Normal.png"
        elif category == "spell":
            frame_file = "Spell.png"
        elif category == "trap":
            frame_file = "Trap.png"
        else:
            frame_file = "Normal.png"

    if category == "spell":
        card_info["attribute"] = "Spell"
    elif category == "trap":
        card_info["attribute"] = "Trap"
        
    frame_type = Path(frame_file).stem.lower()
    frame_path = base_dir / "frames" / frame_file
    attribute_path = base_dir / "Attributes" / f"{card_info['attribute'].capitalize()}.png"

    # Handle level/rank image override
    level_override = (overrides or {}).get("level")
    if level_override and Path(level_override).exists():
        level_star_path = Path(level_override)
    else:
        level_type = "Rk" if "xyz" in frame_type else "LV"
        level_star_path = base_dir / "Level" / f"{level_type} {card_info['level']}.png"

    font_name_path = base_dir / "Fonts" / "911Fonts.com_MatrixRegularSmallCapsRegular__-_911fonts.com_fonts_owRo.ttf"
    font_type_path = base_dir / "Fonts" / "Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf"
    font_atk_def_path = base_dir / "Fonts" / "MatrixBoldFractions.otf"
    font_normal_desc = base_dir / "Fonts" / "Stone Serif ITC Medium.ttf"
    font_effect_desc = base_dir / "Fonts" / "Matrix Book.ttf"

    card = Image.open(frame_path).convert("RGBA")
    is_spell_or_trap = category in ("spell", "trap")

    if attribute_path.exists():
        attr_icon = Image.open(attribute_path).convert("RGBA")
        card.paste(attr_icon, (0, 0), attr_icon)

    # Banner logic
    if is_spell_or_trap:
        sf_value = card_info.get("sf", "").upper()
        banner_type = "Normal" if sf_value == "NO ICON" else sf_value.title()
        prefix = "Spell" if category == "spell" else "Trap"
        banner_filename = f"{prefix}_{banner_type}.png"
        banner_path = base_dir / "Banner" / banner_filename
        if banner_path.exists():
            banner_img = Image.open(banner_path).convert("RGBA")
            card.paste(banner_img, (0, 0), banner_img)
        else:
            print(f"[Missing Banner] {banner_filename} not found.")

    # Place level/rank stars (not for spell/trap or Link monsters)
    if not is_spell_or_trap and level_star_path.exists() and type_id not in link_type_ids:
        star = Image.open(level_star_path).convert("RGBA")
        for _ in range(min(card_info["level"], 12)):
            card.paste(star, (0, 0), star)

    # Setup text field configs
    desc_bottom_right = DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP if is_spell_or_trap else DESC_BOX_BOTTOM_RIGHT_MONSTER
    desc_y_offset = DESC_BOX_SPELL_TRAP_Y_OFFSET if is_spell_or_trap else DESC_BOX_MONSTER_Y_OFFSET
    special_hex_color = "#f3c77a"
    special_hex_color2 = "#ac8a4e"
    if frame_file in {"Obelisk.png", "Slifer.png"}:
        name_font_color = special_hex_color
    elif frame_file in {"Ra.png"}:
        name_font_color = special_hex_color2
    else:
        name_font_color = "white" if category in ("spell", "trap") or "xyz" in frame_type or "link" in frame_type else "black"


    TEXT_FIELDS = {
        "name": {
            "top_left": CARD_NAME_BOX_TOP_LEFT,
            "bottom_right": (652, 125),
            "font_path": font_name_path,
            "font_size": CARD_NAME_FONT_SIZE,
            "color": name_font_color,
            "text": card_info["name"],
            "padding": 20,
            "y_offset": CARD_NAME_Y_OFFSET,
        },
        "type": {
            "top_left": TYPE_LINE_TOP_LEFT,
            "bottom_right": TYPE_LINE_BOTTOM_RIGHT,
            "font_path": font_type_path,
            "font_size": 30,
            "color": "black",
            "text": card_info["type_ability"],
            "padding": 0,
            "y_offset": TYPE_LINE_Y_OFFSET,
            "compression_rules": [
                (20, 0.85),
                (16, 0.87),
                (0, 1.00),
            ],
        },
        "atk": {
            "top_left": ATK_BOX_TOP_LEFT,
            "bottom_right": ATK_BOX_BOTTOM_RIGHT,
            "font_path": font_atk_def_path,
            "font_size": ATKDEF_FONT,
            "color": "black",
            "text": card_info["atk"],
            "padding": 0,
            "y_offset": -2,
            "offset_x": 10,
        },
        "def": {
            "top_left": DEF_BOX_TOP_LEFT,
            "bottom_right": DEF_BOX_BOTTOM_RIGHT,
            "font_path": font_atk_def_path,
            "font_size": ATKDEF_FONT,
            "color": "black",
            "text": card_info["def"],
            "padding": 0,
            "y_offset": -2,
            "offset_x": 5,
        },
        "desc": {
            "top_left": DESC_BOX_SPELL_TRAP_TOP_LEFT if is_spell_or_trap else DESC_BOX_MONSTER_TOP_LEFT,
            "bottom_right": desc_bottom_right,
            "font_path_normal": font_normal_desc,
            "font_path_effect": font_effect_desc,
            "font_size": 26,
            "line_spacing": 4,
            "color": "black",
            "text": card_info["description"],
            "y_offset": desc_y_offset
        }
    }

    # Place artwork
    if type_id in pendulum_type_ids:
        place_card_art(card, card_info["passcode"], ART_TOP_LEFT_PENDULUM, ART_BOTTOM_RIGHT_PENDULUM, overrides=overrides)
    else:
        place_card_art(card, card_info["passcode"], ART_TOP_LEFT_REGULAR, ART_BOTTOM_RIGHT_REGULAR, overrides=overrides)


    # Link arrows and rating
    if type_id in link_type_ids:
        link_markers = get_link_marker_positions(int(card_info["def"]))
        draw_link_arrows(card, link_markers, base_dir)

    render_and_paste_card_name(card, TEXT_FIELDS["name"])

    if not is_spell_or_trap:
        draw_card_type(card, TEXT_FIELDS["type"])
        draw_stat_value(card, TEXT_FIELDS["atk"])
        if type_id in link_type_ids:
            draw_link_rating(card, get_link_marker_positions(int(card_info["def"])), base_dir)
        else:
            draw_stat_value(card, TEXT_FIELDS["def"])

    draw_description(
        card,
        TEXT_FIELDS["desc"]["text"],
        frame_name=frame_path.name,
        cfg=TEXT_FIELDS["desc"],
        type_box=TEXT_FIELDS["type"]["top_left"] if not is_spell_or_trap else None
    )

    if type_id in pendulum_type_ids:
        if card_info.get("pendulum_effect"):
            draw_pendulum_effect(card, card_info["pendulum_effect"], base_dir)
        if card_info.get("scale_left") is not None and card_info.get("scale_right") is not None:
            draw_pendulum_scales(card, card_info["scale_left"], card_info["scale_right"], base_dir)

    output_path = (save_dir or base_dir) / f"{card_info['passcode']}.png"
    card.save(output_path)
    print(f"✅ Card image saved to: {output_path}")


def draw_debug_text_box_guides(image):
    from PIL import ImageDraw

    draw = ImageDraw.Draw(image)

    # === Manually adjust these Y-values as needed ===
    y_top = 945   # Upper boundary of the desired text box
    y_bottom = 1075  # Lower boundary of the desired text box

    # X range (full card width)
    x_start = 0
    x_end = image.width

    red = (255, 0, 0)

    for x in range(x_start, x_end):
        image.putpixel((x, y_top), red)
        image.putpixel((x, y_bottom), red)

    return image  # ← this was missing

# === Render Name ===
def render_and_paste_card_name(image, cfg):
    from PIL import ImageFont, ImageDraw
    from pathlib import Path

    # Paths
    name_font_path = cfg["font_path"]
    matrix_path = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series " + SeriesNum + "/Fonts/Matrix Book.ttf")
    arial_path = "C:/Windows/Fonts/seguisym.ttf"

    # Load fonts at the desired size
    font_size = cfg["font_size"]
    name_font = ImageFont.truetype(str(name_font_path), font_size)
    desc_font = ImageFont.truetype(str(matrix_path), font_size)
    unicode_font = ImageFont.truetype(str(arial_path), font_size)

    # Utility to test if font supports a character
    def has_glyph(font, char):
        try:
            font.getmask(char)
            return True
        except Exception:
            return False

    # Strip unwanted suffixes
    text = cfg["text"].replace("\n", " ").replace("\r", " ").strip()
    for suffix in ["(Anime)", "(Manga)", "(VG)", "(Pre-Errata)", "(GOAT)", "(DM)"]:
        if text.endswith(suffix):
            text = text[: -len(suffix)].strip()

    padding = cfg["padding"]
    draw_test = ImageDraw.Draw(Image.new("RGBA", (1, 1)))

    char_fonts = []
    char_widths = []
    for c in text:
        if has_glyph(name_font, c):
            f = name_font
        elif has_glyph(desc_font, c):
            f = desc_font
        else:
            f = unicode_font
        char_fonts.append(f)
        char_widths.append(draw_test.textlength(c, font=f))

    text_width = sum(char_widths)
    text_height = name_font.getbbox("A")[3] - name_font.getbbox("A")[1]

    temp_img = Image.new("RGBA", (int(text_width + padding * 2), int(text_height + padding * 2)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(temp_img)
    x = padding
    for c in text:
        chosen_font = get_font_for_char(c, name_font, unicode_font)
        if chosen_font == unicode_font:
            # Scale special characters like @ smaller to visually match
            small_font = ImageFont.truetype(str(chosen_font.path), int(cfg["font_size"] * 0.55))
            draw.text((x, padding + 4), c, font=small_font, fill=cfg["color"])
            x += draw.textlength(c, font=small_font)
        else:
            draw.text((x, padding), c, font=chosen_font, fill=cfg["color"])
            x += draw.textlength(c, font=chosen_font)


    # === Use passed-in coordinates instead of hardcoded constants ===
    box_x, box_y = cfg["top_left"]
    box_right, box_bottom = cfg["bottom_right"]
    box_w = (box_right - box_x) + CARD_NAME_X_OFFSET
    box_h = box_bottom - box_y

    text_ratio = temp_img.width / box_w
    vertical_stretch = 1.0
    for threshold, stretch in [(1.4, 1.15), (1.2, 1.10), (1.05, 1.05)]:
        if text_ratio > threshold:
            vertical_stretch = stretch
            box_y = 52  # ← Restore legacy vertical offset if overflow detected
            box_h = box_bottom - box_y  # Recalculate height after Y adjustment
            break


    scaled_width = int(temp_img.width * (box_h * vertical_stretch / temp_img.height))
    name_img = temp_img.resize((scaled_width, int(box_h * vertical_stretch)), resample=Image.BICUBIC)

    if name_img.width > box_w:
        name_img = name_img.resize((box_w, name_img.height), resample=Image.BICUBIC)

    paste_x = box_x + 2
    paste_y = box_bottom - name_img.height - 3 + cfg["y_offset"]
    image.paste(name_img, (paste_x, paste_y), name_img)
    
def has_glyph(font, char):
    try:
        font.getmask(char)
        return True
    except Exception:
        return False
    
def draw_pendulum_effect(image, text, base_dir):
    from PIL import ImageFont, ImageDraw

    top_left = PEND_DESC_TOP_LEFT
    bottom_right = PEND_DESC_BOTTOM_RIGHT
    fallback_font_path = "C:/Windows/Fonts/arial.ttf"
    matrix_font_path = base_dir / "Fonts" / "Matrix Book.ttf"

    x_start = top_left[0]
    y_start = top_left[1]
    bottom_limit = bottom_right[1]
    max_width = bottom_right[0] - top_left[0]
    max_height = bottom_limit - y_start

    draw = ImageDraw.Draw(image)
    paragraphs = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')

    original_font_size = 26
    font_size = original_font_size
    best_fit_font = None
    best_fit_fallback = None
    best_fit_lines = []
    best_spacing = 0
    resized = False

    while font_size >= 12:
        main_font = ImageFont.truetype(str(matrix_font_path), font_size)
        fallback_font = ImageFont.truetype(str(fallback_font_path), font_size)
        spacing = 2 if font_size >= 18 else 1 if font_size == 17 else 0

        lines = []
        height_used = 0
        fits = True

        for paragraph in paragraphs:
            if not paragraph.strip():
                continue

            words = paragraph.split()
            current_line = ""
            for word in words:
                test_line = f"{current_line} {word}".strip()
                padded_line = f"L{test_line}y"
                test_font = fallback_font if "●" in padded_line else main_font
                if draw.textlength(padded_line, font=test_font) <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    height_used += font_size + spacing
                    if height_used + font_size > max_height:
                        fits = False
                        break
                    current_line = word
            if not fits:
                break
            if current_line:
                lines.append(current_line)
                height_used += font_size + spacing
                if height_used > max_height:
                    fits = False
                    break

        if fits:
            best_fit_font = main_font
            best_fit_fallback = fallback_font
            best_fit_lines = lines
            best_spacing = spacing
            resized = (font_size < original_font_size)
            break

        font_size -= 1

    if resized and (original_font_size - font_size) > 8 and len(best_fit_lines) > 1:
        total_height = len(best_fit_lines) * font_size
        extra_space = max_height - total_height
        best_spacing += int(extra_space // (len(best_fit_lines) - 0.25))
        y = bottom_limit - (len(best_fit_lines) * font_size + (len(best_fit_lines) - 1) * best_spacing)
    else:
        y = y_start

    for idx, line in enumerate(best_fit_lines):
        words = line.split()
        is_last_line = (idx == len(best_fit_lines) - 1 or len(words) == 1)
        total_word_width = sum(draw.textlength(w, font=best_fit_fallback if "●" in w else best_fit_font) for w in words)
        num_gaps = len(words) - 1

        if not is_last_line and num_gaps > 0:
            total_spacing = max_width - total_word_width
            space_between_words = total_spacing / num_gaps
        else:
            space_between_words = draw.textlength(" ", font=best_fit_font)

        cursor_x = x_start
        for i, word in enumerate(words):
            for char in word:
                char_font = best_fit_fallback if char == "●" else best_fit_font
                draw.text((cursor_x, y), char, font=char_font, fill="black")
                cursor_x += draw.textlength(char, font=char_font)
            if i < len(words) - 1:
                cursor_x += space_between_words
        y += font_size + best_spacing

# === Render Type ===
def draw_card_type(image, cfg):
    text = cfg['text']

    if " / Tuner / Effect" in text:
        text = text.replace(" / Tuner / Effect", " / Tuner")

    clean_text = text.replace(' / Normal', '').replace(' / ', '/')
    formatted_text = f"[{clean_text}]"

    font = ImageFont.truetype(str(cfg["font_path"]), cfg["font_size"])
    draw_img = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    ascent, descent = font.getmetrics()
    text_height = ascent + descent

    compression = next((c for t, c in cfg["compression_rules"] if len(formatted_text) > t), 1.0)

    # === NEW: extra spacing if uncompressed ===
    uncompressed_extra_spacing = 1.5  # <— you can change this dynamically
    spacing = uncompressed_extra_spacing if compression == 1.0 else 0

    # Measure characters
    char_widths = [draw_img.textlength(c, font=font) for c in formatted_text]
    total_width = sum(char_widths) + spacing * (len(formatted_text) - 1)

    # Create image
    temp_img = Image.new("RGBA", (int(total_width), int(text_height)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(temp_img)

    x = 0
    for c, w in zip(formatted_text, char_widths):
        draw.text((x, 0), c, font=font, fill=cfg["color"])
        x += w + spacing

    paste_x = cfg["top_left"][0]
    paste_y = cfg["bottom_right"][1] - temp_img.height + cfg["y_offset"]
    image.paste(temp_img, (paste_x, paste_y), temp_img)

def draw_link_arrows(image, markers, base_dir):
    from PIL import Image

    background_path = base_dir / "Link_Arrows" / "Backround.png"
    arrow_dir = base_dir / "Link_Arrows"

    # Draw the background first
    if background_path.exists():
        bg = Image.open(background_path).convert("RGBA")
        image.paste(bg, (0, 0), bg)

    # Draw each active arrow
    for marker in markers:
        arrow_path = arrow_dir / f"{marker}.png"
        if arrow_path.exists():
            arrow_img = Image.open(arrow_path).convert("RGBA")
            image.paste(arrow_img, (0, 0), arrow_img)
        else:
            print(f"[Missing Arrow] {marker}.png not found.")

# === Render ATK / DEF ===
def draw_stat_value(image, cfg):
    from PIL import Image, ImageDraw, ImageFont
    from pathlib import Path

    base_dir = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series "+SeriesNum)
    question_dir = base_dir / "Questions"
    text = str(cfg["text"]).strip().lower()

    # Determine stat type (ATK or DEF) based on x-coordinate
    is_atk = cfg["top_left"][0] == ATK_BOX_TOP_LEFT[0]
    is_def = cfg["top_left"][0] == DEF_BOX_TOP_LEFT[0]

    # Map special strings to specific image files
    if text in {"?", "????", "x000"}:
        image_map = {
            "?": "ATK_Question.png" if is_atk else "DEF_Question.png",
            "????": "ATK_Full_Question.png" if is_atk else "DEF_Full_Question.png",
            "x000": "ATK_X000.png" if is_atk else "DEF_X000.png"
        }
        image_file = question_dir / image_map[text]
        if image_file.exists():
            stat_img = Image.open(image_file).convert("RGBA")
            image.paste(stat_img, (0, 0), stat_img)
        return

    # === Render regular stat ===
    font = ImageFont.truetype(str(cfg["font_path"]), cfg["font_size"])
    draw = ImageDraw.Draw(image)
    text_width = draw.textlength(text, font=font)
    x = cfg["bottom_right"][0] - text_width + cfg["offset_x"]
    y = cfg["top_left"][1] + cfg["y_offset"]
    draw.text((x, y), text, font=font, fill=cfg["color"])

# == render Link Rating
def draw_link_rating(image, link_markers, base_dir):
    from PIL import ImageFont, ImageDraw

    font_path = base_dir / "Fonts" / "rog2_sans_serif_std_b_by_hammerbro101_dd8d7hb.otf"
    font_size = 25
    font = ImageFont.truetype(str(font_path), font_size)
    draw = ImageDraw.Draw(image)

    rating = str(len(link_markers))
    text_width = draw.textlength(rating, font=font)

    # Same position as DEF field
    x = LINK_RATING_X - text_width + 0  # bottom_right[0] - width + offset_x
    y = LINK_RATING_Y   # top_left[1] + y_offset

    draw.text((x, y), rating, font=font, fill="black")

# === Render Description ===
def draw_description(image, text, frame_name, cfg, type_box=None, debug=False):
    import re
    from PIL import ImageFont, ImageDraw

    text = re.split(r"\* *The above text is unofficial.*?OCG\.*", text)[0].strip()
    fallback_font_path = "C:/Windows/Fonts/arial.ttf"
    base_font_path = cfg["font_path_normal"] if "Normal" in frame_name else cfg["font_path_effect"]

    top_left = cfg["top_left"]
    bottom_limit = cfg["bottom_right"][1]
    max_width = cfg["bottom_right"][0] - 15 - top_left[0]
    y_start = top_left[1] + cfg["y_offset"]
    max_height = bottom_limit - y_start
    x = top_left[0]

    draw = ImageDraw.Draw(image)
    raw_lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')

    best_font_size = None
    best_fit_lines = []
    best_main_font = None
    best_fallback_font = None
    best_spacing = 0
    resized = False

    font_size = float(cfg["font_size"])
    original_font_size = font_size
    while font_size >= 12:
        main_font = ImageFont.truetype(str(base_font_path), round(font_size))
        fallback_font = ImageFont.truetype(str(fallback_font_path), round(font_size))
        spacing = 2 if font_size >= 18 else 1 if font_size == 17 else 0

        lines = []
        height_used = 0
        fits = True

        for raw_line in raw_lines:
            if not raw_line.strip():
                continue
            words = raw_line.split()
            current_line = ""
            for word in words:
                test_line = f"{current_line} {word}".strip()
                font = fallback_font if "●" in test_line else main_font
                if draw.textlength(test_line, font=font) <= max_width:
                    current_line = test_line
                else:
                    lines.append((current_line, False))
                    height_used += round(font_size) + spacing
                    if height_used + round(font_size) > max_height:
                        fits = False
                        break
                    current_line = word
            if not fits:
                break
            if current_line:
                lines.append((current_line, True))
                height_used += round(font_size) + spacing
                if height_used > max_height:
                    fits = False
                    break

        if fits and height_used <= max_height:
            best_font_size = font_size
            best_fit_lines = lines
            best_main_font = main_font
            best_fallback_font = fallback_font
            best_spacing = spacing
            resized = (font_size < cfg["font_size"])
            break

        font_size -= .5

    # Start drawing at y_start
    if resized and (original_font_size - best_font_size) > 8 and len(best_fit_lines) > 1:
        total_height = len(best_fit_lines) * round(best_font_size)
        extra_space = max_height - total_height
        best_spacing += extra_space // (len(best_fit_lines) - 0.25)
        y = bottom_limit - (len(best_fit_lines) * round(best_font_size) + (len(best_fit_lines) - 1) * best_spacing) + cfg["y_offset"]
    else:
        y = y_start


    for idx, (line, is_manual_line) in enumerate(best_fit_lines):
        words = line.split()
        is_last_line = (idx == len(best_fit_lines) - 1 or len(words) == 1 or is_manual_line)

        total_word_width = sum(draw.textlength(w, font=best_fallback_font if "●" in w else best_main_font) for w in words)
        num_gaps = len(words) - 1

        if not is_last_line and num_gaps > 0:
            total_spacing = max_width - total_word_width
            space_between_words = total_spacing / num_gaps
        else:
            space_between_words = draw.textlength(" ", font=best_main_font)

        cursor_x = x
        for i, word in enumerate(words):
            for char in word:
                char_font = best_fallback_font if char == "●" else best_main_font
                draw.text((cursor_x, y), char, font=char_font, fill=cfg["color"])
                cursor_x += draw.textlength(char, font=char_font)
            if i < len(words) - 1:
                cursor_x += space_between_words

        y += round(best_font_size) + best_spacing

    if debug:
        red = (255, 0, 0)
        x1, x2 = cfg["top_left"][0], cfg["bottom_right"][0]
        y_top = y_start
        y_bottom = bottom_limit - 1
        for px in range(x1, x2):
            image.putpixel((px, y_top), red)
            image.putpixel((px, y_bottom), red)

# === Place Card Art ===
def place_card_art(image, passcode, top_left=ART_TOP_LEFT_REGULAR, bottom_right=ART_BOTTOM_RIGHT_REGULAR, overrides=None):
    from PIL import Image
    from pathlib import Path

    # Use override path if available
    override_path = (overrides or {}).get("artwork")
    if override_path and Path(override_path).exists():
        art = Image.open(override_path).convert("RGBA")
        width = bottom_right[0] - top_left[0]
        height = bottom_right[1] - top_left[1]
        art = art.resize((width, height))
        image.paste(art, top_left, art)
        return True

    # Fallback: search by passcode in high-res directory
    search_dir = Path("X:/Temps/YGOpro pic project/all high res pics")
    passcode = str(passcode)
    for ext in [".jpg", ".jpeg", ".png"]:
        image_path = search_dir / f"{passcode}{ext}"
        if image_path.exists():
            art = Image.open(image_path).convert("RGBA")
            width = bottom_right[0] - top_left[0]
            height = bottom_right[1] - top_left[1]
            art = art.resize((width, height))
            image.paste(art, top_left, art)
            return True

    print(f"[Missing Art] Could not find artwork for passcode: {passcode}")
    return False
    
def debug_print_card_info(card_info):
    print("=== DEBUG CARD INFO ===")
    for key, value in card_info.items():
        print(f"{key}: {value}")
    print("=" * 40)

def extract_passcodes_from_ydk(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip().isdigit()]

def get_link_marker_positions(defense_value):
    
    markers = []
    if defense_value & 1: markers.append("Bottom-Left")
    if defense_value & 2: markers.append("Bottom")
    if defense_value & 4: markers.append("Bottom-Right")
    if defense_value & 8: markers.append("Left")
    if defense_value & 16: markers.append("Top-Left")
    if defense_value & 32: markers.append("Right")
    if defense_value & 64: markers.append("Top-Right")
    if defense_value & 128: markers.append("Top")
    return markers
        
def prompt_for_frame(base_dir):
    FRAME_FILE_TO_TYPE_ID = {
        "Normal.png": 17,
        "Effect.png": 33,
        "Fusion.png": 65,
        "Ritual.png": 129,
        "Synchro.png": 8193,
        "Xyz.png": 8388609,
        "Link.png": 67108865,
        "Pen_Normal.png": 16777233,
        "Pen_Effect.png": 50331681,
        "Pen_Fusion.png": 16777313,
        "Pen_Ritual.png": 16777377,
        "Pen_Synchro.png": 16785441,
        "Pen_Xyz.png": 25165857,
        "Token.png": 16401,
        "Dark_Synchro.png": 8225,
        "Legendary_Dragon": 102,
        "Obelisk.png": 103,
        "Ra.png": 104,
        "Slifer.png": 105,
        "Z-Arc.png": 106
    }

    frame_list = list(FRAME_FILE_TO_TYPE_ID.keys())

    print("\nAvailable Frames:")
    for idx, name in enumerate(frame_list):
        print(f"[{idx}] {name}")

    while True:
        choice = input("Select a frame by number: ").strip()
        if choice.isdigit() and 0 <= int(choice) < len(frame_list):
            selected_frame = frame_list[int(choice)]
            type_id = FRAME_FILE_TO_TYPE_ID[selected_frame]
            frame_path = base_dir / "frames" / selected_frame
            print(f"✅ Selected Frame: {selected_frame} → Type ID: {type_id}")
            return frame_path, type_id
        else:
            print("❌ Invalid selection. Please try again.")

def draw_card_by_passcode_mode():
    BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series "+SeriesNum)
    #output_dir = Path("F:/YGOPro/pics/")
    output_dir = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series "+SeriesNum)
    while True:
        passcode_input = input("Enter the passcode of the card you want to draw (or 'e' to exit): ").strip()
        if passcode_input.lower() == 'e':
            print("Exiting draw mode.")
            break

        if not passcode_input.isdigit():
            print("Invalid passcode. Please enter a numeric value.")
            continue

        passcode = int(passcode_input)
        found_card = False
        for db_path in database_paths:
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                query = """
                    SELECT texts.name, datas.id, texts.desc, datas.type, datas.level,
                           datas.attribute, datas.race, datas.atk, datas.def
                    FROM texts
                    JOIN datas ON texts.id = datas.id
                    WHERE datas.id = ?
                """
                cursor.execute(query, (passcode,))
                result = cursor.fetchone()
                if result:
                    print(f"Card found in: {db_path}")
                    card_name, card_id, description, card_type, level_rank, attribute, race, atk, defe = result
                    level = level_rank & 0xFF
                    scale_left = (level_rank >> 24) & 0xFF
                    scale_right = (level_rank >> 16) & 0xFF
                    card_category, card_type_description = get_card_category(card_type)

                    if card_category == "Unknown" or card_type_description is None:
                        print(f"Skipping {card_id}: Unknown card type ({card_type})")
                        found_card = True
                        break

                    # Link detection block
                    if "Link" in card_type_description:
                        link_rating = level_rank
                        link_markers = get_link_marker_positions(defe)
                        #print(f"🔗 Link Rating: {link_rating}")
                        #print(f"🔗 Link Markers: {', '.join(link_markers)}")

                    if card_category == "Monster":
                        if card_type_description.strip() == "Normal":
                            type_ability = MONSTER_RACES.get(race, "Unknown")
                        else:
                            type_ability = f"{MONSTER_RACES.get(race, 'Unknown')} / {card_type_description.strip()}"
                    else:
                        type_ability = f"{card_category} Card"

                    sf_icon = "NO ICON"
                    if card_category in ["Spell", "Trap"]:
                        icon_keywords = {
                            "field": "FIELD", "equip": "EQUIP", "continuous": "CONTINUOUS",
                            "ritual": "RITUAL", "quick-play": "QUICK-PLAY", "counter": "COUNTER"
                        }
                        for keyword, icon in icon_keywords.items():
                            if keyword in card_type_description.lower():
                                sf_icon = icon
                                break

                    card_info = {
                        "name": card_name,
                        "pendulum_effect": None,
                        "description": description,
                        "attribute": ATTRIBUTES.get(attribute, "Unknown"),
                        "level": level,
                        "scale_left": scale_left,
                        "scale_right": scale_right,
                        "atk": "?" if atk == -2 else str(atk),
                        "def": "?" if defe in (None, -2) else str(defe),
                        "type_ability": type_ability,
                        "category": card_category,
                        "sf": sf_icon,
                        "passcode": str(card_id),
                        "type_id": card_type
                    }

                    pendulum_type_ids = {
                        16777233, 16777249, 50331681, 16781329,
                        16777313, 16777377, 16781345, 16777761,
                        18874401, 16785441, 25165857
                    }
                    if card_info["type_id"] in pendulum_type_ids:
                        pend, desc = extract_pendulum_parts(description)
                        card_info["pendulum_effect"] = pend
                        card_info["description"] = desc

                    debug_print_card_info(card_info)
                    draw_card_image(card_info, BASE_DIR, output_dir)
                    #draw_debug_text_box_guides(Image.open(output_dir / f"{card_info['passcode']}.png")).save(output_dir / f"{card_info['passcode']}.png")


                    found_card = True
                    break
            except sqlite3.Error as e:
                print(f"Error searching {db_path}: {e}")
            finally:
                conn.close()

        if not found_card:
            print(f"No valid non-Pendulum, non-Link card found for passcode {passcode}.")

def manual_mode_step_by_step(base_dir):
    import os
    from pathlib import Path
    from PIL import Image

    output_dir = base_dir
    #artwork_path = "F:/YGOPro/pics/templates/PythonCardMaker/Series "+SeriesNum "/Art/dattmhl-56af50b4-f333-43ee-a7be.png"
    print("Please select the artwork image for the card.")
    artwork_path = filedialog.askopenfilename(
        title="Select Artwork Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not artwork_path or not Path(artwork_path).exists():
        print("❌ No valid artwork selected. Exiting manual mode.")
        return

    frames_folder = base_dir / "frames"
    banner_folder = base_dir / "Banner"
    attributes_folder = base_dir / "Attributes"

    # Step 1: Select frame
    frame_files = [f for f in os.listdir(frames_folder) if f.lower().endswith(".png")]
    print("Select a frame:")
    for idx, fname in enumerate(frame_files, start=1):
        print(f"{idx}: {fname}")
    while True:
        try:
            choice = int(input("Enter the number for the frame: "))
            if 1 <= choice <= len(frame_files):
                frame_file = frame_files[choice - 1]
                print(f"[DEBUG] Selected frame: {frame_file}")
                break
        except ValueError:
            pass

    special_frame_map = {
        "Token.png": 16401,
        "Dark_Synchro.png": 8225,
        "Legendary_Dragon.png": 102,
        "Obelisk.png": 103,
        "Ra.png": 104,
        "Slifer.png": 105,
        "Z-Arc.png": 106,
        "Link.png": 67108865,
        "Pen_Fusion.png": 16777313,
        "Pen_Ritual.png": 16777377,
        "Pen_Synchro.png": 16785441,
        "Pen_Xyz.png": 25165857,
        "Pen_Normal.png": 16777233,
        "Pen_Effect.png": 16781345,
    }

    type_id = special_frame_map.get(frame_file, FRAME_FILE_TO_TYPE_ID.get(frame_file, 0))
    if type_id == 0:
        print(f"[Warning] Frame file '{frame_file}' not mapped to a type_id.")

    scale_value = None
    pendulum_effect_text = None
    if "pen_" in frame_file.lower() or frame_file.lower() == "z-arc.png":
        while True:
            try:
                scale_value = int(input("Enter Pendulum Scale (0–13): "))
                if 0 <= scale_value <= 13:
                    break
                else:
                    print("Invalid input. Must be between 0 and 13.")
            except ValueError:
                print("Please enter a valid integer.")
        pendulum_effect_text = input("Enter Pendulum Effect text: ").strip()

    card_name = input("Enter card name: ").strip()

    category = "spell" if "spell" in frame_file.lower() else "trap" if "trap" in frame_file.lower() else "monster"
    sf_value = "NO ICON"
    level = 0
    type_line = ""
    attribute = "Unknown"
    atk = ""
    defense = ""
    description = ""

    if category in {"spell", "trap"}:
        banner_files = [f for f in os.listdir(banner_folder) if f.lower().endswith(".png")]
        print("Select a banner:")
        for idx, fname in enumerate(banner_files, start=1):
            print(f"{idx}: {fname}")
        while True:
            try:
                banner_choice = int(input("Enter the number for the banner: "))
                if 1 <= banner_choice <= len(banner_files):
                    selected_banner = banner_files[banner_choice - 1]
                    sf_value = selected_banner.split("_", 1)[-1].replace(".png", "").upper()
                    break
            except ValueError:
                pass
        description = input("Enter description: ").strip()

    else:
        if frame_file != "Link.png":
            while True:
                try:
                    level = int(input("Enter level (0–13): "))
                    if 0 <= level <= 13:
                        break
                    else:
                        print("Invalid input. Level must be between 0 and 13.")
                except ValueError:
                    print("Please enter a valid integer.")
        else:
            level = 0
        type_line = input("Enter type line (e.g., 'Dragon / Effect'): ").strip()

        attr_files = [f for f in os.listdir(attributes_folder) if f.lower().endswith(".png")]
        print("Select an attribute:")
        for idx, fname in enumerate(attr_files, start=1):
            print(f"{idx}: {fname}")
        while True:
            try:
                attr_choice = int(input("Enter the number for the attribute: "))
                if 1 <= attr_choice <= len(attr_files):
                    attribute = attr_files[attr_choice - 1].replace(".png", "").capitalize()
                    break
            except ValueError:
                pass

        atk = input("Enter ATK (e.g., 1800): ").strip()
        if type_id == 67108865 or type_id == 67108897:  # Link
            while True:
                try:
                    link_rating = int(input("Enter Link Rating (1–8): "))
                    if 1 <= link_rating <= 8:
                        break
                    else:
                        print("Link Rating must be between 1 and 8.")
                except ValueError:
                    print("Enter a valid integer.")

            marker_map = {
        "1": ("Bottom-Left", 1),
        "2": ("Bottom", 2),
        "3": ("Bottom-Right", 4),
        "4": ("Left", 8),
        "5": ("Top-Left", 16),
        "6": ("Right", 32),
        "7": ("Top-Right", 64),
        "8": ("Top", 128),
    }

            selected = set()
            marker_sum = 0
            print("Select Link Arrows:")
            for i in range(link_rating):
                print("Available options:")
                for k, (label, _) in marker_map.items():
                    if k not in selected:
                        print(f"{k}: {label}")
                while True:
                    choice = input(f"Arrow {i+1}/{link_rating}, select number: ").strip()
                    if choice in marker_map and choice not in selected:
                        selected.add(choice)
                        marker_sum += marker_map[choice][1]
                        break
                    else:
                        print("Invalid or duplicate choice.")
            defense = str(marker_sum)
        else:
            defense = input("Enter DEF (e.g., 1200): ").strip()
        description = input("Enter description: ").strip()
    card_info = {
        "name": card_name,
        "pendulum_effect": pendulum_effect_text,
        "description": description,
        "attribute": attribute,
        "level": level,
        "scale_left": scale_value if scale_value is not None else 0,
        "scale_right": scale_value if scale_value is not None else 0,
        "atk": atk,
        "def": defense,
        "type_ability": type_line,
        "category": category,
        "sf": sf_value,
        "passcode": "created",
        "type_id": type_id
    }

    if not Path(artwork_path).exists():
        print(f"[Missing Art] Could not find hardcoded artwork: {artwork_path}")
        return

    debug_print_card_info(card_info)
    draw_card_image(card_info, base_dir, output_dir, overrides={
        "artwork": artwork_path,
        "frame": frame_file
    })

def generate_by_database(filter_type=None):
    import tkinter as tk
    from tkinter import filedialog
    from pathlib import Path
    import sqlite3
    from PIL import Image
    import os

    BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series " + SeriesNum)
    output_dir = BASE_DIR / "manuel"
    output_dir.mkdir(exist_ok=True)

    # Prepare missing-art YDK path
    ydk_path = Path("F:/YGOPro/deck/[Missing Art].ydk")
    existing_missing = set()

    if ydk_path.exists():
        with open(ydk_path, "r", encoding="utf-8") as f:
            existing_missing = {line.strip() for line in f if line.strip().isdigit()}

    root = tk.Tk()
    root.withdraw()
    cdb_path = filedialog.askopenfilename(
        title="Select a .cdb database file",
        filetypes=[("CDB files", "*.cdb")]
    )

    if not cdb_path:
        print("No .cdb file selected.")
        return

    try:
        conn = sqlite3.connect(cdb_path)
        cursor = conn.cursor()
        query = """
            SELECT texts.name, datas.id, texts.desc, datas.type, datas.level,
                   datas.attribute, datas.race, datas.atk, datas.def
            FROM texts
            JOIN datas ON texts.id = datas.id
        """
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"📦 Processing {len(results)} cards from {os.path.basename(cdb_path)}...")

        for result in results:
            card_name, card_id, description, card_type, level_rank, attribute, race, atk, defe = result
            if card_id in excluded_ids:
                print(f"❌ Skipping {card_id}: Explicitly excluded.")
                continue
            level = level_rank & 0xFF
            scale_left = (level_rank >> 24) & 0xFF
            scale_right = (level_rank >> 16) & 0xFF
            card_category, card_type_description = get_card_category(card_type)

            if card_category == "Unknown" or card_type_description is None:
                print(f"Skipping {card_id}: Unknown card type ({card_type})")
                continue

            if filter_type and filter_type not in card_type_description.lower():
                continue

            if "Link" in card_type_description:
                link_rating = level_rank
                link_markers = get_link_marker_positions(defe)

            if card_category == "Monster":
                type_ability = MONSTER_RACES.get(race, "Unknown") if card_type_description.strip() == "Normal" \
                    else f"{MONSTER_RACES.get(race, 'Unknown')} / {card_type_description.strip()}"
            else:
                type_ability = f"{card_category} Card"

            sf_icon = "NO ICON"
            if card_category in ["Spell", "Trap"]:
                icon_keywords = {
                    "field": "FIELD", "equip": "EQUIP", "continuous": "CONTINUOUS",
                    "ritual": "RITUAL", "quick-play": "QUICK-PLAY", "counter": "COUNTER"
                }
                for keyword, icon in icon_keywords.items():
                    if keyword in card_type_description.lower():
                        sf_icon = icon
                        break

            card_info = {
                "name": card_name,
                "pendulum_effect": None,
                "description": description,
                "attribute": ATTRIBUTES.get(attribute, "Unknown"),
                "level": level,
                "scale_left": scale_left,
                "scale_right": scale_right,
                "atk": "?" if atk == -2 else str(atk),
                "def": "?" if defe in (None, -2) else str(defe),
                "type_ability": type_ability,
                "category": card_category,
                "sf": sf_icon,
                "passcode": str(card_id),
                "type_id": card_type
            }

            pendulum_type_ids = {
                16777233, 16777249, 50331681, 16781329,
                16777313, 16777377, 16781345, 16777761,
                18874401, 16785441, 25165857
            }

            if card_info["type_id"] in pendulum_type_ids:
                pend, desc = extract_pendulum_parts(description)
                card_info["pendulum_effect"] = pend
                card_info["description"] = desc

            test_img = Image.new("RGBA", (813, 1185), (0, 0, 0, 0))
            if not place_card_art(test_img, card_info["passcode"]):
                passcode_str = str(card_id)
                if passcode_str not in existing_missing:
                    with open(ydk_path, "a", encoding="utf-8") as ydk:
                        ydk.write(f"{passcode_str}\n")
                    print(f"📝 Logged missing art: {passcode_str}")
                    existing_missing.add(passcode_str)
                continue

            draw_card_image(card_info, BASE_DIR, output_dir)

    except sqlite3.Error as e:
        print(f"❌ Error reading from {cdb_path}: {e}")
    finally:
        conn.close()

def generate_from_ydk_file():
    import tkinter as tk
    from tkinter import filedialog
    from pathlib import Path
    import sqlite3
    from PIL import Image

    BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series "+SeriesNum)

    # Open file dialog
    root = tk.Tk()
    root.withdraw()
    ydk_path = filedialog.askopenfilename(
        title="Select a .ydk file",
        filetypes=[("YDK files", "*.ydk")]
    )

    if not ydk_path:
        print("No file selected. Returning to main menu.")
        return

    ydk_path = Path(ydk_path)
    passcodes = extract_passcodes_from_ydk(ydk_path)
    output_dir = BASE_DIR / ydk_path.stem
    output_dir.mkdir(exist_ok=True)

    for passcode in passcodes:
        found = False
        for db_path in database_paths:
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                query = """
                    SELECT texts.name, datas.id, texts.desc, datas.type, datas.level,
                           datas.attribute, datas.race, datas.atk, datas.def
                    FROM texts
                    JOIN datas ON texts.id = datas.id
                    WHERE datas.id = ?
                """
                cursor.execute(query, (passcode,))
                result = cursor.fetchone()
                if result:
                    card_name, card_id, description, card_type, level_rank, attribute, race, atk, defe = result
                    level = level_rank & 0xFF
                    scale_left = (level_rank >> 24) & 0xFF
                    scale_right = (level_rank >> 16) & 0xFF

                    card_category, card_type_description = get_card_category(card_type)
                    if card_category == "Unknown" or card_type_description is None:
                        print(f"Skipping {card_id}: Unknown card type ({card_type})")
                        found = True
                        break

                    if "Link" in card_type_description:
                        link_rating = level_rank
                        link_markers = get_link_marker_positions(defe)
                        print(f"{card_name} [{card_id}]")
                        print(f"🔗 Link Rating: {link_rating}")
                        print(f"🔗 Link Markers: {', '.join(link_markers)}")

                    if card_category == "Monster":
                        type_ability = MONSTER_RACES.get(race, "Unknown") if card_type_description.strip() == "Normal" \
                            else f"{MONSTER_RACES.get(race, 'Unknown')} / {card_type_description.strip()}"
                    else:
                        type_ability = f"{card_category} Card"

                    sf_icon = "NO ICON"
                    if card_category in ["Spell", "Trap"]:
                        icon_keywords = {
                            "field": "FIELD", "equip": "EQUIP", "continuous": "CONTINUOUS",
                            "ritual": "RITUAL", "quick-play": "QUICK-PLAY", "counter": "COUNTER"
                        }
                        for keyword, icon in icon_keywords.items():
                            if keyword in card_type_description.lower():
                                sf_icon = icon
                                break

                    card_info = {
                        "name": card_name,
                        "pendulum_effect": None,
                        "description": description,
                        "attribute": ATTRIBUTES.get(attribute, "Unknown"),
                        "level": level,
                        "scale_left": scale_left,
                        "scale_right": scale_right,
                        "atk": "?" if atk == -2 else str(atk),
                        "def": "?" if defe in (None, -2) else str(defe),
                        "type_ability": type_ability,
                        "category": card_category,
                        "sf": sf_icon,
                        "passcode": str(card_id),
                        "type_id": card_type
                    }

                    pendulum_type_ids = {
                        16777233, 16777249, 50331681, 16781329,
                        16777313, 16777377, 16781345, 16777761,
                        18874401, 16785441, 25165857
                    }

                    if card_info["type_id"] in pendulum_type_ids:
                        pend, desc = extract_pendulum_parts(description)
                        card_info["pendulum_effect"] = pend
                        card_info["description"] = desc

                    # Pre-check if artwork exists before rendering
                    test_img = Image.new("RGBA", (813, 1185), (0, 0, 0, 0))
                    if not place_card_art(test_img, card_info["passcode"]):
                        print(f"Skipping {card_info['passcode']}: Missing artwork.")
                        continue

                    draw_card_image(card_info, BASE_DIR, output_dir)
                    found = True
                    break
            except sqlite3.Error as e:
                print(f"Error accessing database {db_path}: {e}")
            finally:
                conn.close()

        if not found:
            print(f"Card not found or unsupported type for passcode: {passcode}")

    print("✅ Done processing .ydk file.")
    input("Press Enter to return to the main menu...")

def prompt_mode_selection():
    print("=== Yu-Gi-Oh! Card Renderer ===")
    print("Usage:")
    print("  P            → Draw a card by passcode")
    print("  Y            → Select a .ydk file and draw all cards inside")
    print("  D            → Select a .cdb file and draw all cards inside")
    print("  D -pen       → Only draw Pendulum cards")
    print("  D -lin       → Only draw Link cards")
    print("  D -xyz       → Only draw Xyz cards")
    print("  M            → Manually create a card step-by-step")
    print("  F            → Use the form-based manual creator")
    print("  E            → Exit")

    while True:
        raw_input = input("Mode: ").strip()
        if not raw_input:
            continue

        command = raw_input.split()[0].upper()
        if command in ("P", "Y", "D", "M", "F", "E"):
            return raw_input
        else:
            print("Invalid option. Please enter a valid mode.")

# === Main Menu Logic ===

import re

#SeriesNum = prompt_series_selection()


def main_menu_loop():
    global SeriesNum
    while True:
        print("\n=== Yu-Gi-Oh! Card Renderer ===")
        print(f"Current Layout Series: {SeriesNum}")
        print("Usage:")
        print("  P            → Draw a card by passcode")
        print("  Y            → Select a .ydk file and draw all cards inside")
        print("  D            → Select a .cdb file and draw all cards inside")
        print("  D -pen       → Only draw Pendulum cards")
        print("  D -lin       → Only draw Link cards")
        print("  D -xyz       → Only draw Xyz cards")
        print("  M            → Manually create a card step-by-step")
        print("  F            → Use the form-based manual creator")
        print("  S            → Switch layout series")
        print("  E            → Exit")
        
        mode_input = input("Mode: ").strip()
        match = re.match(r"^([A-Za-z])\s*-?(\w{3})?$", mode_input, re.IGNORECASE)

        if not match:
            print("❌ Invalid input format. Try 'D -pen', 'Y -xyz', etc.")
            continue

        mode = match.group(1).upper()
        arg = match.group(2).lower() if match.group(2) else None

        if mode == "E":
            print("👋 Exiting the program.")
            break
        elif mode == "S":
            SeriesNum = prompt_series_selection()
            set_layout_constants(SeriesNum)
        elif mode == "P":
            draw_card_by_passcode_mode()
        elif mode == "D":
            generate_by_database(arg)
        elif mode == "Y":
            generate_from_ydk_file()
        elif mode == "M":
            BASE_DIR = Path("F:/YGOPro/pics/templates/PythonCardMaker/Series " + SeriesNum)
            manual_mode_step_by_step(BASE_DIR)
        elif mode == "F":
            launch_form_mode()
        else:
            print("❌ Unknown mode. Try again.")

# Start the main menu loop
main_menu_loop()
