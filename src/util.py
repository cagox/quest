


# Money
COPPER = 1
SILVER = COPPER * 100
GOLD = SILVER * 100

def gold_pieces(copper):
    if(copper < GOLD):
        return 0
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
    cp = copper_pieces(copper)
    sp = silver_pieces(copper)
    gp = gold_pieces(copper)
    return f"CP: {cp}  SP: {sp}  GP: {gp}"

