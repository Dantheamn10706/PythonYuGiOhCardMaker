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
    
    global CARD_NAME_BOX_TOP_LEFT, CARD_NAME_BOX_BOTTOM_RIGHT, CARD_NAME_Y_OFFSET, CARD_NAME_X_OFFSET, CARD_NAME_FONT_SIZE
    global TYPE_LINE_TOP_LEFT, TYPE_LINE_BOTTOM_RIGHT, TYPE_LINE_Y_OFFSET, TYPE_LINE_X_ENDPOINT
    global DESC_BOX_MONSTER_TOP_LEFT, DESC_BOX_BOTTOM_RIGHT_MONSTER, DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP
    global DESC_BOX_SPELL_TRAP_TOP_LEFT, DESC_BOX_MONSTER_Y_OFFSET, DESC_BOX_SPELL_TRAP_Y_OFFSET
    global ATKDEF_FONT, ATK_BOX_TOP_LEFT, ATK_BOX_BOTTOM_RIGHT, ATK_Y_OFFSET, ATK_OFFSET_X
    global DEF_BOX_TOP_LEFT, DEF_BOX_BOTTOM_RIGHT, DEF_Y_OFFSET, DEF_OFFSET_X
    global LINK_RATING_X, LINK_RATING_Y, LINK_RATING_FONT_SIZE
    global ART_TOP_LEFT_REGULAR, ART_BOTTOM_RIGHT_REGULAR, ART_TOP_LEFT_PENDULUM, ART_BOTTOM_RIGHT_PENDULUM
    global PEND_LEFT_SCALE_POS, PEND_RIGHT_SCALE_POS, PEND_SCALE_SIZE
    global PEND_DESC_TOP_LEFT, PEND_DESC_BOTTOM_RIGHT
    
    globals_to_clear = [
        "CARD_NAME_BOX_TOP_LEFT", "CARD_NAME_BOX_BOTTOM_RIGHT", "CARD_NAME_Y_OFFSET", "CARD_NAME_X_OFFSET", "CARD_NAME_FONT_SIZE",
        "TYPE_LINE_TOP_LEFT", "TYPE_LINE_BOTTOM_RIGHT", "TYPE_LINE_Y_OFFSET", "TYPE_LINE_X_ENDPOINT",
        "DESC_BOX_MONSTER_TOP_LEFT", "DESC_BOX_BOTTOM_RIGHT_MONSTER", "DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP",
        "DESC_BOX_SPELL_TRAP_TOP_LEFT", "DESC_BOX_MONSTER_Y_OFFSET", "DESC_BOX_SPELL_TRAP_Y_OFFSET",
        "ATKDEF_FONT", "ATK_BOX_TOP_LEFT", "ATK_BOX_BOTTOM_RIGHT", "ATK_Y_OFFSET", "ATK_OFFSET_X",
        "DEF_BOX_TOP_LEFT", "DEF_BOX_BOTTOM_RIGHT", "DEF_Y_OFFSET", "DEF_OFFSET_X",
        "LINK_RATING_X", "LINK_RATING_Y", "LINK_RATING_FONT_SIZE",
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
    TYPE_LINE_X_ENDPOINT = None

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
    LINK_RATING_FONT_SIZE = None

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
        CARD_NAME_FONT_SIZE = 105
    
        TYPE_LINE_TOP_LEFT = (80, 925)
        TYPE_LINE_BOTTOM_RIGHT = (640, 940)
        TYPE_LINE_Y_OFFSET = 5
        TYPE_LINE_X_ENDPOINT = 730  # Added explicit X endpoint

        DESC_BOX_MONSTER_TOP_LEFT = (80, 942)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (745, 1069)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (745, 1110)
        DESC_BOX_SPELL_TRAP_TOP_LEFT= (80, 905)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT = 36

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
        CARD_NAME_FONT_SIZE = 105

        TYPE_LINE_TOP_LEFT = (75, 910)
        TYPE_LINE_BOTTOM_RIGHT = (650, 925)
        TYPE_LINE_Y_OFFSET = 8
        TYPE_LINE_X_ENDPOINT = 700  # Added explicit X endpoint
        
        DESC_BOX_MONSTER_TOP_LEFT = (80, 930)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (745, 1069)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (745, 1115)
        DESC_BOX_SPELL_TRAP_TOP_LEFT = (80, 895)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT = 36

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
        CARD_NAME_FONT_SIZE = 105

        TYPE_LINE_TOP_LEFT = (65, 902)
        TYPE_LINE_BOTTOM_RIGHT = (670, 922)
        TYPE_LINE_Y_OFFSET = 3
        TYPE_LINE_X_ENDPOINT = 670  # Added explicit X endpoint
        
        DESC_BOX_MONSTER_TOP_LEFT = (65, 922)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (763, 1069)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (763, 1115)
        DESC_BOX_SPELL_TRAP_TOP_LEFT = (65, 890)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT = 36

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
        CARD_NAME_FONT_SIZE = 80

        TYPE_LINE_TOP_LEFT = (50, 770)
        TYPE_LINE_BOTTOM_RIGHT = (670, TYPE_LINE_TOP_LEFT[1]+25)
        TYPE_LINE_Y_OFFSET = 3
        TYPE_LINE_X_ENDPOINT = 670  # Added explicit X endpoint
        
        DESC_BOX_MONSTER_TOP_LEFT = (55, 793)
        DESC_BOX_BOTTOM_RIGHT_MONSTER = (650, 922)
        DESC_BOX_BOTTOM_RIGHT_SPELL_TRAP = (650, 945)
        DESC_BOX_SPELL_TRAP_TOP_LEFT = (60, 765)
        DESC_BOX_MONSTER_Y_OFFSET = 0
        DESC_BOX_SPELL_TRAP_Y_OFFSET = 0

        ATKDEF_FONT = 28
        
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
        LINK_RATING_FONT_SIZE = 25

        ART_TOP_LEFT_REGULAR = (85, 187)
        ART_BOTTOM_RIGHT_REGULAR = (613, 715)
        ART_TOP_LEFT_PENDULUM = (48, 182)
        ART_BOTTOM_RIGHT_PENDULUM = (650, 633)

        PEND_LEFT_SCALE_POS = (77, 720)
        PEND_RIGHT_SCALE_POS = (623, 720)
        PEND_SCALE_SIZE = (28, 28)

        PEND_DESC_TOP_LEFT = (112, 639)
        PEND_DESC_BOTTOM_RIGHT = (590, 750)

    # Dump values for debugging
   # print("\n=== Layout Constants Dump ===")
  #  for var in globals_to_clear:
  #      print(f"{var}: {globals().get(var)}")
  #  print("=" * 40)
    
SeriesNum="3"
set_layout_constants(SeriesNum)
#set_layout_constants(SeriesNum)
safe_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.'-…()"
# Path to the database file
db_file_path = "F:/YGOPro/pics/templates/Automated templates/cards.cdb"
# === Exclude specific card IDs from rendering ===
excluded_ids = {
        #513000136, 513000134,513000135, 
        #170000152, 170000151,170000153, 170000201, 
        10000000, 10000010, 10000020,
        #511000246,511000261,511000234,
        #513000137,513000138,513000139
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
        "Evil_god.png": 106,
        "Raviel.png": 107,
        "Hamon.png": 108,
        "Uria.png": 109,
        "Z-Arc.png": 25174113
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
#print("Loaded the following databases:")
#for path in database_paths:
#    print(path)
#print("=" * 50)

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
    33554432: "Illusion",
    102: "Legendary Dragon"
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
    25174113: "Fusion / Synchro / Xyz / Pendulum / Effect",
    103: "Normal",
    104: "Normal",
    105: "Normal",
    106: "Normal",
    107: " Effect",
    108: " Effect",
    109: " Effect",
    25174113: " Effect"

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

Other_CARD_TYPES = {
    102: "Legendary Dragon",
    # You can add more special types here if needed
}

# Array to store unrecognized card types
unrecognized_cards = []

def get_card_category(card_type):
    if card_type in Monster_CARD_TYPES:
        return "Monster", Monster_CARD_TYPES[card_type]
    elif card_type in Spell_CARD_TYPES:
        return "Spell", Spell_CARD_TYPES[card_type]
    elif card_type in Trap_CARD_TYPES:
        return "Trap", Trap_CARD_TYPES[card_type]
    elif card_type in Other_CARD_TYPES:
        return "Other", Other_CARD_TYPES[card_type]
    else:
        return "Unknown", None
# Function to process all records in the database
# Prompt the user to enter the number of records they wish to access

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
    18874401, 16785441, 25165857, 25174113  # Added Z-Arc type ID here
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
            frame_file = "Evil_god.png"
        elif type_id == 107:
            frame_file = "Raviel.png"
        elif type_id == 108:
            frame_file = "Hamon.png"
        elif type_id == 109:
            frame_file = "Uria.png"    
        elif type_id == 25174113:
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
    if frame_file in {"Obelisk.png", "Slifer.png" ,"Uria.png","Raviel.png" }:
        name_font_color = special_hex_color
    elif frame_file in {"Ra.png", "Hamon.png"}:
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

    # Place artwork with alias support
    artwork_placed = False
    if type_id in pendulum_type_ids or frame_file.lower() == "z-arc.png":
        artwork_placed = place_card_art(card, card_info["passcode"], ART_TOP_LEFT_PENDULUM, ART_BOTTOM_RIGHT_PENDULUM, overrides=overrides, alias=card_info.get("alias", 0))
    else:
        artwork_placed = place_card_art(card, card_info["passcode"], ART_TOP_LEFT_REGULAR, ART_BOTTOM_RIGHT_REGULAR, overrides=overrides, alias=card_info.get("alias", 0))
    
    # Skip rendering if artwork couldn't be placed
    if not artwork_placed:
        print(f"Skipping render for {card_info['passcode']} due to missing artwork.")
        return False

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

    if type_id in pendulum_type_ids or frame_file.lower() == "z-arc.png":
        if card_info.get("pendulum_effect"):
            draw_pendulum_effect(card, card_info["pendulum_effect"], base_dir)
        if card_info.get("scale_left") is not None and card_info.get("scale_right") is not None:
            draw_pendulum_scales(card, card_info["scale_left"], card_info["scale_right"], base_dir)

    output_path = (save_dir or base_dir) / f"{card_info['passcode']}.png"
    card.save(output_path)
    print(f"✅ Card image saved to: {output_path}")
    return True

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
    for suffix in ["(Anime)", "(Manga)", "(VG)", "(Pre-Errata)", "(GOAT)", "(DM)", "(TF3)","(TF6)", "(GX)"]:
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
    
def place_card_art(image, passcode, top_left=ART_TOP_LEFT_REGULAR, bottom_right=ART_BOTTOM_RIGHT_REGULAR, overrides=None, alias=None):
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

    # Function to try loading artwork for a given passcode
    def try_load_artwork(code):
        search_dir = Path("X:/Temps/YGOpro pic project/all high res pics")
        code_str = str(code)
        for ext in [".jpg", ".jpeg", ".png"]:
            image_path = search_dir / f"{code_str}{ext}"
            if image_path.exists():
                art = Image.open(image_path).convert("RGBA")
                width = bottom_right[0] - top_left[0]
                height = bottom_right[1] - top_left[1]
                art = art.resize((width, height))
                image.paste(art, top_left, art)
                return True
        return False

    # Try with original passcode first
    if try_load_artwork(passcode):
        return True
    
    # If alias is provided and original artwork not found, try with alias
    if alias and alias != 0 and alias != passcode:
        print(f"[Art Fallback] Trying alias {alias} for passcode {passcode}")
        if try_load_artwork(alias):
            print(f"[Art Found] Using artwork from alias {alias} for passcode {passcode}")
            return True

    print(f"[Missing Art] Could not find artwork for passcode: {passcode}" + 
          (f" or alias: {alias}" if alias and alias != 0 else ""))
    return False

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
                    height_used += font_size
                    if lines:  # Only add spacing after the first line
                        height_used += spacing
                    if height_used + font_size > max_height:
                        fits = False
                        break
                    current_line = word
            if not fits:
                break
            if current_line:
                lines.append(current_line)
                height_used += font_size
                if lines:  # Only add spacing after the first line
                    height_used += spacing
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
def draw_card_type(image, cfg, debug=False):
    from PIL import Image, ImageDraw, ImageFont
    
    # Clean up text format
    text = cfg['text']
    
    if "Legendary Dragon" in text or "OTHER CARD" in text.upper() or "OTHER" in text.upper():
        formatted_text = "      "  # Always use this specific text for type 102
    else:
        if " / Tuner / Effect" in text:
            text = text.replace(" / Tuner / Effect", " / Tuner")
        clean_text = text.replace(' / Normal', '').replace(' / ', '/')
        formatted_text = f"[{clean_text}]"
    
    # Get font and setup drawing context
    font = ImageFont.truetype(str(cfg["font_path"]), cfg["font_size"])
    draw_img = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    
    # Get text metrics
    ascent, descent = font.getmetrics()
    text_height = ascent + descent
    
    # Get compression ratio based on text length
    compression = next((c for t, c in cfg["compression_rules"] if len(formatted_text) > t), 1.0)
    
    # Add extra spacing if uncompressed
    uncompressed_extra_spacing = 1.5  # Can be changed dynamically
    spacing = uncompressed_extra_spacing if compression == 1.0 else 0
    
    # Measure each character width
    char_widths = [draw_img.textlength(c, font=font) for c in formatted_text]
    total_width = sum(char_widths) + spacing * (len(formatted_text) - 1)
    
    # Check if width needs adjusting to reach TYPE_LINE_X_ENDPOINT
    max_width = TYPE_LINE_X_ENDPOINT - cfg["top_left"][0] - 5  # Small margin
    
    # Create temporary image
    temp_img = Image.new("RGBA", (int(total_width), int(text_height)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(temp_img)
    
    # Draw each character with appropriate spacing
    x = 0
    for c, w in zip(formatted_text, char_widths):
        draw.text((x, 0), c, font=font, fill=cfg["color"])
        x += w + spacing
    
    # If text is too long, compress it
    if total_width > max_width:
        scale_factor = max_width / total_width
        new_width = int(total_width * scale_factor)
        temp_img = temp_img.resize((new_width, int(text_height)), Image.BICUBIC)
    
    # Position calculation
    paste_x = cfg["top_left"][0]
    paste_y = cfg["bottom_right"][1] - temp_img.height + cfg["y_offset"]
    
    # Paste the text onto the main image
    image.paste(temp_img, (paste_x, paste_y), temp_img)
    
    # Debug information if enabled
    if debug:
        end_x = paste_x + temp_img.width
        draw_debug = ImageDraw.Draw(image)
        
        print(f"Type text debug info:")
        print(f"  - Type text: '{formatted_text}'")
        print(f"  - Compression ratio: {compression}")
        print(f"  - Extra spacing: {spacing}")
        print(f"  - Original width: {total_width} px")
        print(f"  - Final width: {temp_img.width} px")
        print(f"  - Maximum allowed width: {max_width} px")
        print(f"  - Distance from end to boundary: {TYPE_LINE_X_ENDPOINT - end_x} px")
        
        # Draw visual boundary lines
        red = (255, 0, 0, 255)
        for y in range(paste_y - 5, paste_y + text_height + 5):
            draw_debug.point((TYPE_LINE_X_ENDPOINT, y), fill=red)
            draw_debug.point((end_x, y), fill=(0, 255, 0, 255)) 
            
def draw_description(image, text, frame_name, cfg, type_box=None, debug=False):
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
    best_spacing = 0.0
    resized = False

    font_size = float(cfg["font_size"])
    original_font_size = font_size

    while font_size >= 8.0:
        main_font = ImageFont.truetype(str(base_font_path), font_size)
        fallback_font = ImageFont.truetype(str(fallback_font_path), font_size)
        # Modified spacing logic - no more 2.0 option
        spacing = 1.0 if font_size == 17.0 else 0.0

        lines = []
        height_used = 0.0
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
                    height_used += font_size + spacing
                    if height_used + font_size > max_height:
                        fits = False
                        break
                    current_line = word
            if not fits:
                break
            if current_line:
                lines.append((current_line, True))
                height_used += font_size + spacing
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

        font_size -= 0.25

    if resized and (original_font_size - best_font_size) > 2.0 and len(best_fit_lines) > 1:
        total_height = len(best_fit_lines) * best_font_size
        extra_space = max_height - total_height
        best_spacing += extra_space / (len(best_fit_lines) - 0.25)
        y = bottom_limit - (len(best_fit_lines) * best_font_size + (len(best_fit_lines) - 1) * best_spacing) + cfg["y_offset"]
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

        y += best_font_size
        if idx < len(best_fit_lines) - 1:
            y += best_spacing

    if debug:
        red = (255, 0, 0)
        x1, x2 = cfg["top_left"][0], cfg["bottom_right"][0]
        y_top = y_start
        y_bottom = bottom_limit - 1
        for px in range(x1, x2):
            image.putpixel((px, int(y_top)), red)
            image.putpixel((px, int(y_bottom)), red)

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
                
def has_glyph(font, char):
    try:
        font.getmask(char)
        return True
    except Exception:
        return False
    
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

    return image 
    
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
        "Legendary_Dragon.png": 102,
        "Obelisk.png": 103,
        "Ra.png": 104,
        "Evil_god.png": 106,
        "Raviel.png": 107,
        "Hamon.png": 108,
        "Uria.png": 109,
        "Z-Arc.png": 25174113
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
                    datas.attribute, datas.race, datas.atk, datas.def, datas.alias
                    FROM texts
                    JOIN datas ON texts.id = datas.id
                    WHERE datas.id = ?
                """
                cursor.execute(query, (passcode,))
                result = cursor.fetchone()
                if result:
                    print(f"Card found in: {db_path}")
                    card_name, card_id, description, card_type, level_rank, attribute, race, atk, defe, alias = result
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
                    elif card_category == "Other":
                        type_ability = "Legendary Dragon"  # Exact string to appear on the card
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
                        "type_id": card_type,
                        "alias": alias
                    }

                    pendulum_type_ids = {
                        16777233, 16777249, 50331681, 16781329,
                        16777313, 16777377, 16781345, 16777761,
                        18874401, 16785441, 25165857, 25174113  # Added Z-Arc type ID here
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

def get_multiline_input(prompt, default_text=""):
    """Creates a small GUI window for multiline text input with a submit button."""
    import tkinter as tk
    from tkinter import scrolledtext
    
    result = {"text": default_text}  # Using a dict to store the result so it can be modified in the inner function
    
    # Create the root window
    root = tk.Tk()
    root.title("Card Description Input")
    
    # Set a reasonable size for the window
    root.geometry("600x400")
    
    # Create a label with the prompt
    label = tk.Label(root, text=prompt, padx=10, pady=10)
    label.pack(anchor="w")
    
    # Create a scrolled text widget for multiline input
    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    text_widget.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    text_widget.insert(tk.INSERT, default_text)
    text_widget.focus_set()
    
    # Function to handle submission
    def on_submit():
        result["text"] = text_widget.get("1.0", tk.END).strip()
        root.destroy()
    
    # Create a submit button
    submit_button = tk.Button(root, text="Submit", command=on_submit, padx=20, pady=5)
    submit_button.pack(pady=10)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Run the window
    root.mainloop()
    
    # Return the text after the window is closed
    return result["text"]

def manual_mode_step_by_step(base_dir):
    import os
    from pathlib import Path
    from PIL import Image
    import tkinter as tk
    from tkinter import filedialog

    output_dir = base_dir
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
        "Evil_god.png": 106,
        "Raviel.png": 107,
        "Hamon.png": 108,
        "Uria.png": 109,
        "Z-Arc.png": 25174113,
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
        pendulum_effect_text = get_multiline_input("Enter Pendulum Effect text:")

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
        description = get_multiline_input("Enter description:")

    else:
        if frame_file != "Link.png" and "link" not in frame_file.lower():
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
        if type_id == 67108865 or type_id == 67108897 or "link" in frame_file.lower():  # Link
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
        description = get_multiline_input("Enter monster effect description:")

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
        print(f"[Missing Art] Could not find artwork: {artwork_path}")
        return

    debug_print_card_info(card_info)
    draw_card_image(card_info, base_dir, output_dir, overrides={
        "artwork": artwork_path,
        "frame": frame_file
    })
    
    print(f"✅ Card created successfully! Saved to {output_dir}")
    
def create_card_form_interface(base_dir):
    """
    Creates a comprehensive form interface for manual card creation.
    Optimized for 1080p resolution with a large initial window size.
    Includes live card preview and fields ordered as they appear on the card.
    
    Args:
        base_dir (Path): Base directory containing assets
    
    Returns:
        dict: Card information dictionary or None if canceled
    """
    import tkinter as tk
    from tkinter import ttk, filedialog
    from PIL import Image, ImageTk
    import os
    import threading
    import time
    from pathlib import Path
    
    # Card info to be returned
    card_info = {
        "name": "",
        "pendulum_effect": None,
        "description": "",
        "attribute": "DARK",
        "level": 4,
        "scale_left": 0,
        "scale_right": 0,
        "atk": "0",
        "def": "0",
        "type_ability": "",
        "category": "monster",
        "sf": "NO ICON",
        "passcode": "created",
        "type_id": 33  # Default to Effect Monster
    }
    
    # Selected artwork path
    artwork_path = None
    
    # Create the main window
    root = tk.Tk()
    root.title("Yu-Gi-Oh! Card Creator")
    
    # Get screen dimensions to set window size optimally for 1080p displays
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Set window size to 90% of screen dimensions for optimal visibility
    window_width = int(screen_width * 0.9)
    window_height = int(screen_height * 0.9)
    
    # Set geometry and position window centered on screen
    root.geometry(f"{window_width}x{window_height}+{(screen_width-window_width)//2}+{(screen_height-window_height)//2}")
    root.resizable(True, True)
    
    # Main frame to hold everything
    main_container = ttk.Frame(root)
    main_container.pack(fill=tk.BOTH, expand=True)
    
    # Create left panel for form fields (with scrollbar)
    left_panel = ttk.Frame(main_container, padding="10")
    left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Create right panel for card preview
    right_panel = ttk.Frame(main_container, padding="10")
    right_panel.pack(side=tk.RIGHT, fill=tk.BOTH)
    
    # Create scrollable frame for form fields
    canvas = tk.Canvas(left_panel)
    scrollbar = ttk.Scrollbar(left_panel, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Add mousewheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    # Setup preview panel
    preview_frame = ttk.LabelFrame(right_panel, text="Card Preview")
    preview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Create canvas for card preview
    preview_canvas = tk.Canvas(preview_frame, width=419, height=610, bg="white")
    preview_canvas.pack(padx=10, pady=10)
    
    preview_text = preview_canvas.create_text(
        210, 300, 
        text="Card preview will appear here\nafter you make selections", 
        font=("Arial", 14), 
        width=380,
        justify=tk.CENTER
    )
    
    # Store the preview image reference to prevent garbage collection
    preview_image_ref = None
    render_in_progress = False
    
    # ========== 1. FRAME SELECTION (appears first on card) ==========
    frame_section = ttk.LabelFrame(scrollable_frame, text="Card Frame")
    frame_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    frame_var = tk.StringVar()
    type_id_var = tk.IntVar(value=33)  # Default to Effect monster
    
    # Get frame files
    frame_files = []
    try:
        frame_files = [f for f in os.listdir(base_dir / "frames") if f.endswith(".png")]
    except Exception as e:
        print(f"Error loading frames: {e}")
    
    # Frame selection - create a grid of buttons
    frame_type_id_map = FRAME_FILE_TO_TYPE_ID.copy()
    frame_grid = ttk.Frame(frame_section)
    frame_grid.pack(padx=10, pady=5, fill=tk.BOTH)
    
    # Function to update card preview
    def update_preview(*args):
        nonlocal preview_image_ref, render_in_progress
        
        # Don't render if already in progress (debounce)
        if render_in_progress:
            return
            
        render_in_progress = True
        
        # Show "rendering" text
        preview_canvas.itemconfig(preview_text, text="Rendering preview...")
        
        # Get current values
        current_card_info = {
            "name": name_entry.get(),
            "pendulum_effect": pendulum_text.get("1.0", tk.END).strip() if "Pen_" in frame_var.get() or frame_var.get() == "Z-Arc.png" else None,
            "description": desc_text.get("1.0", tk.END).strip(),
            "attribute": attribute_var.get(),
            "level": level_var.get(),
            "scale_left": scale_var.get(),
            "scale_right": scale_var.get(),
            "atk": atk_entry.get() or "0",
            "def": def_entry.get() or "0",
            "type_ability": type_entry.get(),
            "category": "spell" if "Spell" in frame_var.get() else "trap" if "Trap" in frame_var.get() else "monster",
            "sf": banner_var.get(),
            "passcode": "preview",
            "type_id": type_id_var.get()
        }
        
        # Calculate Link DEF value from checkboxes if needed
        if "Link" in frame_var.get():
            link_def_value = 0
            for marker, (bit_value, _, _) in link_markers.items():
                if link_vars[marker].get():
                    link_def_value += bit_value
            current_card_info["def"] = str(link_def_value)
        
        # Create overrides dictionary
        overrides = {}
        if artwork_path:
            overrides["artwork"] = artwork_path
            
        # Create a temporary image file path
        temp_dir = Path(os.environ.get('TEMP', '.'))
        temp_file = temp_dir / "card_preview.png"
        
        # Function to render in background thread
        def render_task():
            nonlocal preview_image_ref, render_in_progress
            try:
                # Create a temporary image file
                draw_card_image(current_card_info, base_dir, temp_dir, overrides=overrides)
                
                # Load and display the preview
                if temp_file.exists():
                    img = Image.open(temp_file)
                    # Scale to fit preview canvas
                    img = img.resize((419, 610), Image.LANCZOS)
                    preview_img = ImageTk.PhotoImage(img)
                    
                    # Update on main thread
                    root.after(0, lambda: update_preview_image(preview_img))
            except Exception as e:
                print(f"Error rendering preview: {e}")
                # Show error on main thread
                root.after(0, lambda: preview_canvas.itemconfig(
                    preview_text, 
                    text=f"Preview error: {str(e)[:50]}..."
                ))
            finally:
                render_in_progress = False
        
        # Function to update preview image on main thread
        def update_preview_image(img):
            nonlocal preview_image_ref
            preview_image_ref = img  # Keep reference
            preview_canvas.delete("all")  # Clear canvas
            preview_canvas.create_image(210, 305, image=preview_image_ref)
        
        # Start render thread
        thread = threading.Thread(target=render_task)
        thread.daemon = True
        thread.start()
    
    def select_frame(frame_file):
        frame_var.set(frame_file)
        print(f"Frame selected: {frame_file}")  # Debug output

        # Update type_id based on frame
        if frame_file in frame_type_id_map:
            type_id_var.set(frame_type_id_map[frame_file])
    
        # Special handling for Z-Arc.png
        if frame_file == "Z-Arc.png":
            type_id_var.set(110)  # Z-Arc's specific type ID
            print("Z-Arc frame selected - using specific Z-Arc type ID")

        # Get selected frame image for thumbnail
        try:
            frame_img_path = base_dir / "frames" / frame_file
            if frame_img_path.exists():
                frame_img = Image.open(frame_img_path)
                # Scale down to thumbnail size while preserving aspect ratio
                frame_img.thumbnail((80, 110))
                frame_photo = ImageTk.PhotoImage(frame_img)
                frame_label.config(image=frame_photo, text="")
                frame_label.image = frame_photo  # Keep reference
                frame_name_label.config(text=frame_file)
        except Exception as e:
            print(f"Error loading frame preview: {e}")

        # First, hide all conditional sections
        for section in [pendulum_section, attribute_section, level_section, 
                       link_section, atk_def_section, banner_section]:
            section.pack_forget()

        # Check frame type
        is_spell = frame_file == "Spell.png"
        is_trap = frame_file == "Trap.png"
        is_link = "Link" in frame_file
        is_pendulum = "Pen_" in frame_file or frame_file == "Z-Arc.png"

        print(f"Frame type: Spell={is_spell}, Trap={is_trap}, Link={is_link}, Pendulum={is_pendulum}")  # Debug

        # Show type section first (needed for all cards)
        type_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
        # Handle Pendulum cards
        if is_pendulum:
            print("Showing pendulum section")  # Debug
            pendulum_section.pack(fill=tk.X, padx=10, pady=5, ipady=5, after=type_section)

        # Handle Spell/Trap cards
        if is_spell or is_trap:
            print("Showing banner section for Spell/Trap")  # Debug
            # Clear current card type field and set appropriate default
            type_entry.delete(0, tk.END)
            type_entry.insert(0, "Spell Card" if is_spell else "Trap Card")
        
            # Set attribute to SPELL or TRAP automatically
            attribute_var.set("SPELL" if is_spell else "TRAP")
        
            # Clear ATK/DEF values - these shouldn't be used for Spell/Trap
            atk_entry.delete(0, tk.END)
            atk_entry.insert(0, "")
            def_entry.delete(0, tk.END)
            def_entry.insert(0, "")
    
            # Show banner section
            banner_section.pack(fill=tk.X, padx=10, pady=5, ipady=5, after=type_section)
    
            # Pre-select appropriate banner options
            banner_var.set("NO ICON")  # Default
            for banner_file in banner_files:
                prefix = "Spell_" if is_spell else "Trap_"
                if banner_file.startswith(prefix):
                    banner_type = banner_file.split("_", 1)[1].replace(".png", "")
                    print(f"Setting banner to {banner_type.upper()}")  # Debug
                    banner_var.set(banner_type.upper())
                    break
        else:
            # For monster cards
            print("Showing monster sections")  # Debug
            attribute_section.pack(fill=tk.X, padx=10, pady=5, ipady=5, after=type_section)
    
            if is_link:
                print("Showing link section")  # Debug
                link_section.pack(fill=tk.X, padx=10, pady=5, ipady=5, after=attribute_section)
                # Clear any previous link selections
                clear_link_markers()
            else:
                print("Showing level section")  # Debug
                level_section.pack(fill=tk.X, padx=10, pady=5, ipady=5, after=attribute_section)
    
            # Always show ATK/DEF for monsters
            atk_def_section.pack(fill=tk.X, padx=10, pady=5, ipady=5, after=link_section if is_link else level_section)
        
            # Reset default ATK/DEF for monsters if they were previously cleared
            if not atk_entry.get():
                atk_entry.insert(0, "0")
            if not def_entry.get() and not is_link:
                def_entry.insert(0, "0")

        # Make sure all form elements have been updated before triggering preview
        scrollable_frame.update_idletasks()

        # Trigger preview update
        print("Updating preview...")  # Debug
        root.after(500, update_preview)
    
    # Top frame selection area - selected frame display
    frame_selection_area = ttk.Frame(frame_section)
    frame_selection_area.pack(fill=tk.X, padx=10, pady=5)
    
    # Frame preview thumbnail
    frame_display = ttk.Frame(frame_selection_area)
    frame_display.pack(side=tk.LEFT, padx=10)
    
    frame_label = ttk.Label(frame_display, text="No frame selected", width=15)
    frame_label.pack(pady=5)
    
    frame_name_label = ttk.Label(frame_display, text="")
    frame_name_label.pack(pady=5)
    
    # Place frame buttons in a grid (8 columns for wider display)
    for i, frame_file in enumerate(frame_files):
        row, col = divmod(i, 8)
        btn = ttk.Button(
            frame_grid, 
            text=frame_file.replace(".png", ""),
            command=lambda f=frame_file: select_frame(f),
            width=14
        )
        btn.grid(row=row, column=col, padx=3, pady=3)
    
    # ========== 2. NAME (appears at top of card) ==========
    name_section = ttk.LabelFrame(scrollable_frame, text="Card Name")
    name_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    name_frame = ttk.Frame(name_section)
    name_frame.pack(fill=tk.X, padx=10, pady=10)
    
    ttk.Label(name_frame, text="Card Name:").pack(side=tk.LEFT, padx=5)
    name_entry = ttk.Entry(name_frame, width=50)
    name_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    # Add trace to update preview
    name_entry.bind("<KeyRelease>", lambda e: root.after(1000, update_preview))
    
    # ========== 3. ARTWORK (appears in center of card) ==========
    artwork_section = ttk.LabelFrame(scrollable_frame, text="Card Artwork")
    artwork_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    artwork_frame = ttk.Frame(artwork_section)
    artwork_frame.pack(fill=tk.X, padx=10, pady=5)
    
    def select_artwork():
        nonlocal artwork_path, art_image, art_photo
        file_path = filedialog.askopenfilename(
            title="Select Card Artwork",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        
        if file_path:
            artwork_path = file_path
            try:
                # Load and resize artwork for preview
                art_image = Image.open(file_path)
                art_image = art_image.resize((150, 150), Image.LANCZOS)
                art_photo = ImageTk.PhotoImage(art_image)
                
                # Update preview
                art_preview_label.config(image=art_photo, text="")
                art_preview_label.image = art_photo  # Keep reference
                
                # Update filepath display
                art_path_label.config(text=os.path.basename(file_path))
                
                # Update card preview
                update_preview()
            except Exception as e:
                print(f"Error loading artwork: {e}")
    
    ttk.Button(artwork_frame, text="Select Artwork...", command=select_artwork).pack(side=tk.LEFT, padx=10)
    
    # Display selected file path
    art_path_label = ttk.Label(artwork_frame, text="No artwork selected")
    art_path_label.pack(side=tk.LEFT, padx=10)
    
    # Preview thumbnail
    art_preview_label = ttk.Label(artwork_frame, text="No artwork")
    art_preview_label.pack(side=tk.RIGHT, padx=10)
    
    # Artwork thumbnail
    art_image = None
    art_photo = None
    
    # ========== 4. ATTRIBUTE (appears on top right of monster cards) ==========
    attribute_section = ttk.LabelFrame(scrollable_frame, text="Attribute")
    attribute_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    attribute_frame = ttk.Frame(attribute_section)
    attribute_frame.pack(fill=tk.X, padx=10, pady=10)
    
    # Get attribute files
    attribute_files = []
    try:
        attribute_files = [f for f in os.listdir(base_dir / "Attributes") if f.endswith(".png")]
    except Exception as e:
        print(f"Error loading attributes: {e}")
    
    attribute_var = tk.StringVar(value="DARK")
    attribute_var.trace_add("write", update_preview)
    
    # Place attribute buttons in a single row
    for i, attr_file in enumerate(attribute_files):
        attr_name = attr_file.replace(".png", "").upper()
        
        # Try to load attribute icon
        attr_img = None
        try:
            attr_img_path = base_dir / "Attributes" / attr_file
            if attr_img_path.exists():
                attr_img = Image.open(attr_img_path)
                attr_img.thumbnail((24, 24))
                attr_img = ImageTk.PhotoImage(attr_img)
        except Exception as e:
            pass
            
        attr_frame = ttk.Frame(attribute_frame)
        attr_frame.pack(side=tk.LEFT, padx=10)
        
        attr_rb = ttk.Radiobutton(
            attr_frame,
            text=attr_name,
            variable=attribute_var,
            value=attr_name
        )
        attr_rb.pack(anchor=tk.CENTER)
        
        if attr_img:
            attr_label = ttk.Label(attr_frame, image=attr_img)
            attr_label.image = attr_img  # Keep reference
            attr_label.pack()
    
    # ========== 5. LEVEL/RANK (appears above art on monster cards) ==========
    level_section = ttk.LabelFrame(scrollable_frame, text="Level/Rank")
    level_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    level_frame = ttk.Frame(level_section)
    level_frame.pack(fill=tk.X, padx=10, pady=10)
    
    level_var = tk.IntVar(value=4)
    level_var.trace_add("write", update_preview)
    
    # Create buttons for each level 0-13
    level_buttons_frame = ttk.Frame(level_frame)
    level_buttons_frame.pack(fill=tk.X, padx=5, pady=5)
    
    for i in range(0, 14):  # Levels 0-13
        ttk.Radiobutton(
            level_buttons_frame,
            text=str(i),
            variable=level_var,
            value=i,
            width=3
        ).grid(row=i//7, column=i%7, padx=5, pady=5)
    
    # ========== 6. PENDULUM SCALE (for pendulum cards) ==========
    pendulum_section = ttk.LabelFrame(scrollable_frame, text="Pendulum")
    # Initially hidden, will show when Pendulum frame is selected
    
    pendulum_frame = ttk.Frame(pendulum_section)
    pendulum_frame.pack(fill=tk.X, padx=10, pady=10)
    
    scale_var = tk.IntVar(value=8)
    scale_var.trace_add("write", update_preview)
    
    ttk.Label(pendulum_frame, text="Pendulum Scale:", font=("Arial", 12)).pack(side=tk.LEFT, padx=20, pady=10)
    
    # Create buttons for each scale 0-13 with better spacing
    scale_grid = ttk.Frame(pendulum_frame)
    scale_grid.pack(side=tk.LEFT, padx=5, pady=5)
    
    for i in range(0, 14):  # Scales 0-13
        ttk.Radiobutton(
            scale_grid,
            text=str(i),
            variable=scale_var,
            value=i,
            width=3
        ).grid(row=0, column=i, padx=3, pady=3)
    
    # ========== 7. TYPE LINE (appears below art on monster cards) ==========
    type_section = ttk.LabelFrame(scrollable_frame, text="Card Type")
    type_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    type_frame = ttk.Frame(type_section)
    type_frame.pack(fill=tk.X, padx=10, pady=10)
    
    ttk.Label(type_frame, text="Type Line:").pack(side=tk.LEFT, padx=5)
    type_entry = ttk.Entry(type_frame, width=50)
    type_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    ttk.Label(type_frame, text="(e.g. 'Dragon / Effect')").pack(side=tk.RIGHT, padx=5)
    
    # Add trace to update preview
    type_entry.bind("<KeyRelease>", lambda e: root.after(1000, update_preview))
    
    # ========== 8. DESCRIPTION (appears below type line) ==========
    text_section = ttk.LabelFrame(scrollable_frame, text="Card Effects")
    text_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    # Main Card Effect
    effect_frame = ttk.Frame(text_section)
    effect_frame.pack(fill=tk.X, padx=10, pady=5)
    
    ttk.Label(effect_frame, text="Card Effect:").pack(anchor=tk.W, padx=5, pady=5)
    
    # Text entry with horizontal scrollbar to allow wider content
    desc_frame = ttk.Frame(effect_frame)
    desc_frame.pack(fill=tk.X, padx=5, pady=5)
    
    desc_text = tk.Text(desc_frame, width=60, height=8, wrap=tk.WORD, font=("Arial", 11))
    desc_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Add vertical scrollbar to description text
    desc_scrollbar_v = ttk.Scrollbar(desc_frame, orient="vertical", command=desc_text.yview)
    desc_text.configure(yscrollcommand=desc_scrollbar_v.set)
    desc_scrollbar_v.pack(side=tk.RIGHT, fill="y")
    
    # Add horizontal scrollbar
    desc_scrollbar_h = ttk.Scrollbar(effect_frame, orient="horizontal", command=desc_text.xview)
    desc_text.configure(xscrollcommand=desc_scrollbar_h.set)
    desc_scrollbar_h.pack(fill="x")
    
    # Add trace to update preview
    desc_text.bind("<KeyRelease>", lambda e: root.after(1000, update_preview))
    
    # Pendulum Effect
    pendulum_effect_frame = ttk.Frame(text_section)
    pendulum_effect_frame.pack(fill=tk.X, padx=10, pady=5)
    
    ttk.Label(pendulum_effect_frame, text="Pendulum Effect:").pack(anchor=tk.W, padx=5, pady=5)
    
    # Text entry with horizontal scrollbar
    pend_frame = ttk.Frame(pendulum_effect_frame)
    pend_frame.pack(fill=tk.X, padx=5, pady=5)
    
    pendulum_text = tk.Text(pend_frame, width=60, height=6, wrap=tk.WORD, font=("Arial", 11))
    pendulum_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Add vertical scrollbar to pendulum text
    pend_scrollbar_v = ttk.Scrollbar(pend_frame, orient="vertical", command=pendulum_text.yview)
    pendulum_text.configure(yscrollcommand=pend_scrollbar_v.set)
    pend_scrollbar_v.pack(side=tk.RIGHT, fill="y")
    
    # Add horizontal scrollbar
    pend_scrollbar_h = ttk.Scrollbar(pendulum_effect_frame, orient="horizontal", command=pendulum_text.xview)
    pendulum_text.configure(xscrollcommand=pend_scrollbar_h.set)
    pend_scrollbar_h.pack(fill="x")
    
    # Add trace to update preview
    pendulum_text.bind("<KeyRelease>", lambda e: root.after(1000, update_preview))
    
    # ========== 9. ATK/DEF (appears at bottom of monster cards) ==========
    atk_def_section = ttk.LabelFrame(scrollable_frame, text="ATK/DEF")
    atk_def_section.pack(fill=tk.X, padx=10, pady=5, ipady=5)
    
    atk_def_frame = ttk.Frame(atk_def_section)
    atk_def_frame.pack(fill=tk.X, padx=10, pady=10)
    
    # ATK row
    atk_row = ttk.Frame(atk_def_frame)
    atk_row.pack(fill=tk.X, pady=5)
    
    ttk.Label(atk_row, text="ATK:").pack(side=tk.LEFT, padx=5)
    atk_entry = ttk.Entry(atk_row, width=10)
    atk_entry.pack(side=tk.LEFT, padx=5)
    atk_entry.insert(0, "0")
    
    # Add trace to update preview
    atk_entry.bind("<KeyRelease>", lambda e: root.after(500, update_preview))
    
    # Common ATK values
    common_values = ["0", "100", "500", "1000", "1500", "2000", "2500", "3000", "?", "????"]
    
    # ATK quick buttons
    for val in common_values:
        ttk.Button(
            atk_row,
            text=val,
            command=lambda v=val: atk_entry.delete(0, tk.END) or atk_entry.insert(0, v) or update_preview(),
            width=4
        ).pack(side=tk.LEFT, padx=2)
    
    # DEF row
    def_row = ttk.Frame(atk_def_frame)
    def_row.pack(fill=tk.X, pady=5)
    
    ttk.Label(def_row, text="DEF:").pack(side=tk.LEFT, padx=5)
    def_entry = ttk.Entry(def_row, width=10)
    def_entry.pack(side=tk.LEFT, padx=5)
    def_entry.insert(0, "0")
    
    # Add trace to update preview
    def_entry.bind("<KeyRelease>", lambda e: root.after(500, update_preview))
    
    # DEF quick buttons
    for val in common_values:
        ttk.Button(
            def_row,
            text=val,
            command=lambda v=val: def_entry.delete(0, tk.END) or def_entry.insert(0, v) or update_preview(),
            width=4
        ).pack(side=tk.LEFT, padx=2)
    
    # ========== 10. LINK MARKERS (for Link monsters) ==========
    link_section = ttk.LabelFrame(scrollable_frame, text="Link Markers")
    # Initially hidden, will show when Link frame is selected
    
    link_frame = ttk.Frame(link_section)
    link_frame.pack(fill=tk.X, padx=10, pady=10)
    
    link_markers = {
        "Top-Left": (16, 0, 0),
        "Top": (128, 0, 1),
        "Top-Right": (64, 0, 2),
        "Left": (8, 1, 0),
        "Right": (32, 1, 2),
        "Bottom-Left": (1, 2, 0),
        "Bottom": (2, 2, 1),
        "Bottom-Right": (4, 2, 2)
    }
    
    link_vars = {}
    link_rating_var = tk.IntVar(value=0)
    
    def update_link_rating(*args):
        # Count selected markers
        count = sum(1 for var in link_vars.values() if var.get())
        link_rating_var.set(count)
        
        # Update preview
        update_preview()
    
    def clear_link_markers():
        for var in link_vars.values():
            var.set(False)
        update_link_rating()
        
    # ========== 11. SPELL/TRAP BANNER (for Spell/Trap cards) ==========
    banner_section = ttk.LabelFrame(scrollable_frame, text="Spell/Trap Type")
    # Initially hidden, will show when Spell/Trap frame is selected
    
    # Create a 3x3 grid for link markers with arrows
    link_grid = ttk.Frame(link_frame)
    link_grid.pack(side=tk.LEFT, padx=10, pady=10)
    
    # Use larger font size for arrow symbols
    arrow_font = ("Segoe UI Symbol", 16)
    
    # Create checkbuttons for each marker position
    for marker, (bit_value, row, col) in link_markers.items():
        var = tk.BooleanVar(value=False)
        var.trace_add("write", update_link_rating)
        link_vars[marker] = var
        
        # Determine arrow symbol based on position
        arrow_symbol = "↑"  # Default
        if marker == "Top-Left": arrow_symbol = "↖"
        elif marker == "Top": arrow_symbol = "↑"
        elif marker == "Top-Right": arrow_symbol = "↗"
        elif marker == "Left": arrow_symbol = "←"
        elif marker == "Right": arrow_symbol = "→"
        elif marker == "Bottom-Left": arrow_symbol = "↙"
        elif marker == "Bottom": arrow_symbol = "↓"
        elif marker == "Bottom-Right": arrow_symbol = "↘"
        
        # Create frame for each position to hold the checkbox
        cell_frame = ttk.Frame(link_grid, width=50, height=50)
        cell_frame.grid(row=row, column=col, padx=15, pady=15)
        cell_frame.grid_propagate(False)  # Don't shrink
        
        # Custom checkbox with larger symbol
        cb = ttk.Checkbutton(cell_frame, text=arrow_symbol, variable=var)
        cb.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    # Place "LINK" text in the center with a larger font
    link_label = ttk.Label(link_grid, text="LINK", font=("Arial", 12, "bold"))
    link_label.grid(row=1, column=1, padx=15, pady=15)
    
    # Link rating display and clear button
    link_control_frame = ttk.Frame(link_frame)
    link_control_frame.pack(side=tk.RIGHT, padx=20, pady=10)
    
    ttk.Label(link_control_frame, text="Link Rating:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    ttk.Label(link_control_frame, textvariable=link_rating_var, font=("Arial", 18, "bold")).grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    ttk.Button(link_control_frame, text="Clear All Markers", command=clear_link_markers).grid(row=1, column=0, columnspan=2, pady=10)
    
    # ========== 11. SPELL/TRAP BANNER (for Spell/Trap cards) ==========
    banner_section = ttk.LabelFrame(scrollable_frame, text="Spell/Trap Type")
    # Initially hidden, will show when Spell/Trap frame is selected
    
    banner_frame = ttk.Frame(banner_section)
    banner_frame.pack(fill=tk.X, padx=10, pady=10)
    
    # Get banner files
    banner_files = []
    try:
        banner_files = [f for f in os.listdir(base_dir / "Banner") if f.endswith(".png")]
    except Exception as e:
        print(f"Error loading banners: {e}")
    
    banner_var = tk.StringVar(value="NO ICON")
    banner_var.trace_add("write", update_preview)
    
    # Group banners by prefix (Spell/Trap)
    spell_banners = [f for f in banner_files if f.startswith("Spell_")]
    trap_banners = [f for f in banner_files if f.startswith("Trap_")]
    
    # Create a visual grid of buttons for banner selection
    banner_grid = ttk.Frame(banner_frame)
    banner_grid.pack(fill=tk.X, padx=10, pady=10)
    
    # Normal (No Icon) option
    ttk.Radiobutton(
        banner_grid,
        text="Normal (No Icon)",
        variable=banner_var,
        value="NO ICON"
    ).grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    
    # Spell banners (row 1)
    ttk.Label(banner_grid, text="Spell Types:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    for i, banner_file in enumerate(spell_banners):
        if "_" in banner_file:
            banner_type = banner_file.split("_", 1)[1].replace(".png", "")
        else:
            banner_type = banner_file.replace(".png", "")
            
        ttk.Radiobutton(
            banner_grid,
            text=banner_type,
            variable=banner_var,
            value=banner_type.upper()
        ).grid(row=1, column=i+1, padx=20, pady=10, sticky=tk.W)
    
    # Trap banners (row 2)
    ttk.Label(banner_grid, text="Trap Types:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    for i, banner_file in enumerate(trap_banners):
        if "_" in banner_file:
            banner_type = banner_file.split("_", 1)[1].replace(".png", "")
        else:
            banner_type = banner_file.replace(".png", "")
            
        ttk.Radiobutton(
            banner_grid,
            text=banner_type,
            variable=banner_var,
            value=banner_type.upper()
        ).grid(row=2, column=i+1, padx=20, pady=10, sticky=tk.W)
    
    # ========== Bottom Buttons ==========
    button_frame = ttk.Frame(scrollable_frame)
    button_frame.pack(fill=tk.X, pady=20)
    
    def cancel_form():
        root.destroy()
        return None
    
    def submit_form():
        nonlocal card_info
    
        # Calculate Link DEF value from checkboxes if needed
        link_def_value = 0
        if "Link" in frame_var.get():
            for marker, (bit_value, _, _) in link_markers.items():
                if link_vars[marker].get():
                    link_def_value += bit_value
    
        # Basic info
        card_info["name"] = name_entry.get()
        card_info["type_ability"] = type_entry.get()
    
        # Frame and Type
        selected_frame = frame_var.get()
        card_info["type_id"] = type_id_var.get()
    
        # Special handling for Z-Arc.png
        if selected_frame == "Z-Arc.png":
            card_info["type_id"] = 110  # Z-Arc's specific type ID
    
        # Set category based on frame
        is_spell = "Spell" in selected_frame
        is_trap = "Trap" in selected_frame
    
        if is_spell:
            card_info["category"] = "spell"
            card_info["attribute"] = "Spell"
            card_info["def"] = "0"  # Set to zero but won't be displayed
            card_info["atk"] = "0"  # Set to zero but won't be displayed
            card_info["sf"] = banner_var.get()
            card_info["level"] = 0  # No level for Spell cards
        elif is_trap:
            card_info["category"] = "trap"
            card_info["attribute"] = "Trap" 
            card_info["def"] = "0"  # Set to zero but won't be displayed
            card_info["atk"] = "0"  # Set to zero but won't be displayed
            card_info["sf"] = banner_var.get()
            card_info["level"] = 0  # No level for Trap cards
        else:
            card_info["category"] = "monster"
            card_info["attribute"] = attribute_var.get()
        
            # Link monsters use link_def_value
            if "Link" in selected_frame:
                card_info["def"] = str(link_def_value)
                card_info["level"] = 0  # Links don't have levels
                card_info["atk"] = atk_entry.get() or "0"
            else:
                card_info["atk"] = atk_entry.get() or "0"
                card_info["def"] = def_entry.get() or "0"
                card_info["level"] = level_var.get()
    
        # Pendulum scales
        if "Pen_" in selected_frame or selected_frame == "Z-Arc.png":
            card_info["scale_left"] = scale_var.get()
            card_info["scale_right"] = scale_var.get()
            card_info["pendulum_effect"] = pendulum_text.get("1.0", tk.END).strip()
        else:
            card_info["scale_left"] = 0
            card_info["scale_right"] = 0
            card_info["pendulum_effect"] = None
    
        # Text
        card_info["description"] = desc_text.get("1.0", tk.END).strip()
    
        # Create overrides dictionary
        overrides = {}
        if artwork_path:
            overrides["artwork"] = artwork_path
    
        # Always include the selected frame in overrides
        overrides["frame"] = selected_frame
    
        # Store the final result
        root.result = {
            "card_info": card_info,
            "overrides": overrides
        }
    
        root.destroy()
    
    # Create frame for buttons
    button_container = ttk.Frame(button_frame)
    button_container.pack(side=tk.RIGHT)
    
    ttk.Button(button_container, text="Create Card", command=submit_form).pack(side=tk.RIGHT, padx=5)
    ttk.Button(button_container, text="Cancel", command=cancel_form).pack(side=tk.RIGHT, padx=5)
    
    # Initialize form state - set a default frame to begin with
    if frame_files:
        select_frame(frame_files[1])  # Start with Effect monster frame
    
    # Set up the result attribute
    root.result = None
    
    # Add preview refresh button
    ttk.Button(
        right_panel, 
        text="Refresh Preview",
        command=update_preview
    ).pack(pady=10)
    
    # Run the main loop
    root.mainloop()
    
    # Return the result after the window is closed
    if hasattr(root, "result"):
        return root.result
    return None

def manual_mode_with_form(base_dir):
    """
    Uses the form interface for manual card creation with proper frame handling.
    
    Args:
        base_dir (Path): Base directory containing assets
    """
    from pathlib import Path
    import os
    
    # Get the form result
    result = create_card_form_interface(base_dir)
    
    # If canceled, return
    if not result:
        print("Card creation canceled.")
        return
    
    # Extract card info and overrides
    card_info = result["card_info"]
    overrides = result["overrides"]
    
    # Make sure the frame override is correctly handled
    if "frame" in overrides:
        # If the frame is a string path, convert it to the filename only
        if isinstance(overrides["frame"], str) and "/" in overrides["frame"]:
            overrides["frame"] = os.path.basename(overrides["frame"])
        
        # Special handling for Z-Arc frame
        if overrides["frame"] == "Z-Arc.png":
            # Force the correct type_id for Z-Arc
            card_info["type_id"] = 110  # Z-Arc's specific type ID
            print("Z-Arc frame selected - using specific Z-Arc type ID")
    
    # Output directory is the same as the base directory
    output_dir = base_dir
    
    # Debug info before drawing
    print("\n=== Final Card Parameters ===")
    print(f"Frame: {overrides.get('frame', 'default')}")
    print(f"Type ID: {card_info['type_id']}")
    print("=" * 30)
    
    # Draw the card
    debug_print_card_info(card_info)
    draw_card_image(card_info, base_dir, output_dir, overrides=overrides)
    
    print(f"✅ Card created successfully! Saved to {output_dir}")
    
    # Open the card image
    try:
        import subprocess
        image_path = os.path.join(output_dir, f"{card_info['passcode']}.png")
        if os.path.exists(image_path):
            print(f"Opening card image: {image_path}")
            subprocess.Popen(['start', '', image_path], shell=True)
    except Exception as e:
        print(f"Error opening card image: {e}")
  
def manual_mode_with_form(base_dir):
    """
    Uses the new form interface for manual card creation.
    
    Args:
        base_dir (Path): Base directory containing assets
    """
    from pathlib import Path
    
    # Get the form result
    result = create_card_form_interface(base_dir)
    
    # If canceled, return
    if not result:
        print("Card creation canceled.")
        return
    
    # Extract card info and overrides
    card_info = result["card_info"]
    overrides = result["overrides"]
    
    # Output directory is the same as the base directory
    output_dir = base_dir
    
    # Draw the card
    debug_print_card_info(card_info)
    draw_card_image(card_info, base_dir, output_dir, overrides=overrides)
    
    print(f"✅ Card created successfully! Saved to {output_dir}")

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

    # Check if we're processing all databases
    if filter_type == "a" or filter_type == "all":
        print("Processing all loaded databases...")
        db_paths_to_process = database_paths
    else:
        # User selects a single database
        root = tk.Tk()
        root.withdraw()
        cdb_path = filedialog.askopenfilename(
            title="Select a .cdb database file",
            filetypes=[("CDB files", "*.cdb")]
        )

        if not cdb_path:
            print("No .cdb file selected.")
            return
        
        db_paths_to_process = [cdb_path]

    # Process each database
    total_cards_processed = 0
    total_cards_rendered = 0
    
    for db_path in db_paths_to_process:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            query = """
                SELECT texts.name, datas.id, texts.desc, datas.type, datas.level,
                       datas.attribute, datas.race, datas.atk, datas.def, datas.alias
                FROM texts
                JOIN datas ON texts.id = datas.id
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            db_name = os.path.basename(db_path)
            print(f"📦 Processing {len(results)} cards from {db_name}...")
            
            cards_rendered = 0
            for result in results:
                total_cards_processed += 1
                card_name, card_id, description, card_type, level_rank, attribute, race, atk, defe, alias = result
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

                # Apply filter if provided (except for 'a'/'all' which we handled earlier)
                if filter_type and filter_type not in ["a", "all"] and filter_type not in card_type_description.lower():
                    continue

                if "Link" in card_type_description:
                    link_rating = level_rank
                    link_markers = get_link_marker_positions(defe)
                   
                if card_category == "Monster":
                    type_ability = MONSTER_RACES.get(race, "Unknown") if card_type_description.strip() == "Normal" \
                        else f"{MONSTER_RACES.get(race, 'Unknown')} / {card_type_description.strip()}"
                elif card_category == "Other":
                    type_ability = "Legendary Dragon"  # Exact string to appear on the card
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
                    "type_id": card_type,
                    "alias": alias  # Add alias to card_info
                }

                pendulum_type_ids = {
                    16777233, 16777249, 50331681, 16781329,
                    16777313, 16777377, 16781345, 16777761,
                    18874401, 16785441, 25165857, 25174113  # Added Z-Arc type ID here
                }

                if card_info["type_id"] in pendulum_type_ids:
                    pend, desc = extract_pendulum_parts(description)
                    card_info["pendulum_effect"] = pend
                    card_info["description"] = desc

                # Check if artwork can be found for passcode or alias
                passcode_str = str(card_id)
                # Manually check if artwork exists before attempting to draw
                found_artwork = False
                
                # Try with original passcode first
                search_dir = Path("X:/Temps/YGOpro pic project/all high res pics")
                for ext in [".jpg", ".jpeg", ".png"]:
                    image_path = search_dir / f"{passcode_str}{ext}"
                    if image_path.exists():
                        found_artwork = True
                        break
                
                # If alias is provided and original artwork not found, try with alias
                if not found_artwork and alias and alias != 0 and alias != card_id:
                    alias_str = str(alias)
                    for ext in [".jpg", ".jpeg", ".png"]:
                        image_path = search_dir / f"{alias_str}{ext}"
                        if image_path.exists():
                            found_artwork = True
                            break
                
                # If artwork was found, draw the card
                if found_artwork:
                    if draw_card_image(card_info, BASE_DIR, output_dir):
                        cards_rendered += 1
                        total_cards_rendered += 1
                else:
                    # Only add to missing art if both passcode and alias artwork are missing
                    if passcode_str not in existing_missing:
                        with open(ydk_path, "a", encoding="utf-8") as ydk:
                            ydk.write(f"{passcode_str}\n")
                        print(f"📝 Logged missing art: {passcode_str}")
                        existing_missing.add(passcode_str)
            
            print(f"✅ Rendered {cards_rendered}/{len(results)} cards from {db_name}")
        
        except sqlite3.Error as e:
            print(f"❌ Error reading from {db_path}: {e}")
        finally:
            conn.close()
    
    print(f"🎉 Process complete! Rendered {total_cards_rendered}/{total_cards_processed} cards total.")
    
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
                           datas.attribute, datas.race, datas.atk, datas.def, datas.alias
                    FROM texts
                    JOIN datas ON texts.id = datas.id
                    WHERE datas.id = ?
                """
                cursor.execute(query, (passcode,))
                result = cursor.fetchone()
                if result:
                    card_name, card_id, description, card_type, level_rank, attribute, race, atk, defe, alias = result
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
                    elif card_category == "Other":
                        type_ability = "Legendary Dragon"  # Exact string to appear on the card
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
                        "type_id": card_type,
                        "alias": alias  # Add the alias to card_info
                    }

                    pendulum_type_ids = {
                        16777233, 16777249, 50331681, 16781329,
                        16777313, 16777377, 16781345, 16777761,
                        18874401, 16785441, 25165857, 25174113  # Added Z-Arc type ID here
                    }

                    if card_info["type_id"] in pendulum_type_ids:
                        pend, desc = extract_pendulum_parts(description)
                        card_info["pendulum_effect"] = pend
                        card_info["description"] = desc

                    # We don't need the artwork pre-check anymore since our draw_card_image function
                    # will now handle this internally with alias support
                    if draw_card_image(card_info, BASE_DIR, output_dir):
                        found = True
                        break
                    else:
                        print(f"Skipping {card_info['passcode']}: Could not render card.")
                        continue
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

def main_menu_loop():
    global SeriesNum
    while True:
        print("\n=== Yu-Gi-Oh! Card Renderer ===")
        print(f"Current Layout Series: {SeriesNum}")
        print("Usage:")
        print("  P            → Draw a card by passcode")
        print("  Y            → Select a .ydk file and draw all cards inside")
        print("  D            → Select a .cdb database file and draw all cards inside")
        print("  D -pen       → Only draw Pendulum cards")
        print("  D -lin       → Only draw Link cards")
        print("  D -xyz       → Only draw Xyz cards")
        print("  D -a         → Process ALL loaded databases")
        print("  M            → Manually create a card step-by-step")
        print("  F            → Use the form-based manual creator")
        print("  S            → Switch layout series")
        print("  E            → Exit")
        
        mode_input = input("Mode: ").strip()
        match = re.match(r"^([A-Za-z])\s*-?(\w{3})?$", mode_input, re.IGNORECASE)

        if not match:
            print("❌ Invalid input format. Try 'D -pen', 'Y -xyz', 'D -a', etc.")
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
            manual_mode_with_form(BASE_DIR)
        elif mode == "F":
            launch_form_mode()
        else:
            print("❌ Unknown mode. Try again.")
            
# Start the main menu loop
main_menu_loop()
