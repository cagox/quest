'''
module util simply holds various utility functions for use in our project.
'''
# Money
COPPER = 1
SILVER = COPPER * 100
GOLD = SILVER * 100
PLATINUM = GOLD * 100


def platinum_pieces(copper):
    """returns the platinum pieces portion of a copper value."""
    if copper < PLATINUM:
        return 0
    return copper//PLATINUM


def gold_pieces(copper):
    """returns the gold pieces portion of a copper value"""
    if copper < GOLD:
        return 0
    copper %= PLATINUM
    return copper//GOLD

def silver_pieces(copper):
    """returns the gsilver pieces portion of a copper value"""
    if copper < 100:
        return 0
    copper %= GOLD    # this is the same as copper = copper%GOLD
    return copper//SILVER

def copper_pieces(copper):
    """returns the copper pieces portion of a copper value"""
    if copper < 100:
        return copper
    return copper%SILVER

def money_string(copper):
    """Given a value in copper, returns a formatted string showing how much money the player has."""
    pp = platinum_pieces(copper)
    cp = copper_pieces(copper)
    sp = silver_pieces(copper)
    gp = gold_pieces(copper)
    return f"CP: {cp}  SP: {sp}  GP: {gp} PP: {pp}"

def pad_after(string, character, length):
    """Returns a string padded to match length for formatting. does not shorten long strings."""
    if len(string) >= length:
        return string
    pad_length = length - len(string)
    pad = character * pad_length
    return f"{string}{pad}"
