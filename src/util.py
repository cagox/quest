


# Money
COPPER = 1
SILVER = COPPER * 100
GOLD = SILVER * 100
PLATINUM = GOLD * 100

def platinum_pieces(copper):
    if (copper < PLATINUM):
        return 0
    return copper//PLATINUM 

def gold_pieces(copper):
    if(copper < GOLD):
        return 0
    copper %= PLATINUM
    return copper//GOLD
 
def silver_pieces(copper):
    if (copper < 100):
        return 0
    copper %= GOLD    # this is the same as copper = copper%GOLD
    return copper//SILVER
 
def copper_pieces(copper):
    if (copper < 100):
        return copper
    return copper%SILVER
  
def money_string(copper):
    pp = platinum_pieces(copper)
    cp = copper_pieces(copper)
    sp = silver_pieces(copper)
    gp = gold_pieces(copper)
    return f"CP: {cp}  SP: {sp}  GP: {gp} PP: {pp}"

def pad_after(string, character, length):
    if len(string) >= length:
        return string;
    pad_length = length - len(string)
    pad = character * pad_length
    return f"{string}{pad}"
