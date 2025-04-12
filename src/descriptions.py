
from game import Game
import random

class RoomDescription:
    def __init__(self, name, description, outer_description):
        self.name = name
        self.description = description
        self.outer_description = outer_description

start_room_description = """
You are standing before a great stone door. Beyond the door is the maze.
"""

START_ROOM_DESCIPTION = RoomDescription("Start Room", 
                                        start_room_description, 
                                        "You see the beginning room.")
end_room_description = """
You have found the end of the maze.

Congratulations.
"""
END_ROOM_DESCRIPTION = RoomDescription("The End", 
                                       end_room_description, 
                                       "You have found the end of the maze.")


DESCRIPTIONS = [
    RoomDescription("A Sleepy Gratto", "You are in a quiet gratto. The water laps gently against the shore.", "It is cool and quiet."),
    RoomDescription("The Forgotten Library", "Dusty tomes line endless shelves, the scent of old parchment heavy in the air. Cobwebs hang between books that haven't been touched in centuries.", "An ancient library cloaked in dust and mystery."),
    RoomDescription("The Echoing Cavern", "The cavern stretches wide, stalactites looming above as water drips into unseen depths. Your footsteps echo eerily across the stone.", "A vast, echo-filled cavern."),
    RoomDescription("The Sunken Atrium", "Ruined columns rise from shallow, murky water. Moss and vines cling to marble once grand, now lost beneath time and tide.", "A flooded room with remnants of forgotten grandeur."),
    RoomDescription("Blackthorn Grove", "Twisted black trees encircle the clearing, their branches reaching like claws. Faint whispers drift on the wind.", "A haunted forest clearing surrounded by gnarled trees."),
    RoomDescription("The Crimson Hall", "Red banners hang faded and torn from cracked stone walls. The floor is slick with a dark stain that never dried.", "A blood-stained hall with tattered banners."),
    RoomDescription("Clockmaker's Workshop", "Gears tick and whir in the dim glow of oil lamps. Half-finished constructs and clocks frozen in time clutter every surface.", "A clutteed workshop filled with ticking machinery."),
    RoomDescription("The Mirror Room", "Every surface reflects a thousand versions of yourself. It's hard to tell which way is forward.", "A room of endless mirrors and illusions."),
    RoomDescription("Serpent’s Crossing", "Stone bridges snake over a chasm shrouded in fog. The silence is broken only by the occasional hiss.", "A dangerous crossing high above the abyss."),
    RoomDescription("The Hollow Chapel", "Broken pews face a shattered altar. Stained glass windows let in dim, colorless light.", "An abandoned chapel, silent and desecrated."),
    RoomDescription("Emberforge", "Molten metal flows beneath grates in the floor. The heat is oppressive, and the air hums with residual energy.", "A fiery forge chamber deep underground."),
    RoomDescription("The Velvet Parlor", "Silken drapes and plush furniture adorn this room. A faint perfume lingers in the air, oddly fresh.", "A luxurious parlor, oddly preserved."),
    RoomDescription("Driftwind Balcony", "High above the cliffs, wind howls through broken railings. The ocean stretches endlessly beyond.", "A wind-blasted balcony overlooking the sea."),
    RoomDescription("The Scribe’s Tomb", "Scrolls lie rotting in niches along the walls. A massive stone sarcophagus dominates the room.", "A tomb lined with ancient, crumbling scrolls."),
    RoomDescription("Lantern Court", "Glowing lanterns float gently in the air, casting shifting light on crumbling stone paths.", "A court lit by floating lanterns and fading hope."),
    RoomDescription("The Weeping Cellar", "Moisture drips from the walls, and the air is thick with mildew. Chains rattle faintly though no one is seen.", "A damp cellar filled with unseen sorrow."),
    RoomDescription("The Obsidian Gate", "A towering arch of black stone pulses with an inner light. It hums with ancient power, daring you to cross.", "A massive dark gate buzzing with energy."),
    RoomDescription("Frostvine Chamber", "Icy vines crawl along the walls, encasing frozen statues of those who came before. The air bites with cold.", "A frozen chamber tangled in icy vines."),
    RoomDescription("The Whispering Vault", "Soft, unintelligible voices echo from the stone walls. You can't tell if they're real or just in your mind.", "A vault filled with unsettling whispers."),
    RoomDescription("Grave of the Sentinel", "A rusting suit of armor kneels before a cracked tombstone. The ground trembles slightly beneath your feet.", "A knight's grave shrouded in mystery."),
    RoomDescription("The Hollow Observatory", "A shattered dome reveals stars swirling in unnatural constellations. Strange instruments lie dormant.", "A broken observatory under alien skies."),
    RoomDescription("Cradle of Embers", "Ash drifts like snow through the air. Blackened trees creak as if alive, glowing faintly at the core.", "A scorched glade still warm with dying flame."),
    RoomDescription("The Drowned Study", "Books float weightlessly, pages turning without wind. Everything is soaked, yet strangely preserved.", "A flooded study suspended in stillness."),
    RoomDescription("The Gilded Menagerie", "Cages of gold hold motionless, lifelike animals with gemstone eyes. None breathe, yet all watch.", "A golden zoo of eerily lifelike statues."),
    RoomDescription("The Spiral Sanctum", "Stairs coil endlessly upward and downward into darkness. Each landing looks the same as the last.", "A spiraling stairwell trapped in a loop."),
    RoomDescription("The Mourning Hearth", "A fire burns low in a ruined fireplace. Empty chairs face it, arranged for guests who never came.", "A desolate hearth filled with silent longing."),
    RoomDescription("Thornweave Path", "A trail of thorns winds through a dense thicket. Every step feels watched, every branch poised to strike.", "A menacing path through barbed underbrush."),
    RoomDescription("The Alchemist’s Den", "Shelves bow under the weight of vials and powders. Strange aromas rise from cracked cauldrons.", "A chaotic lab of chemical wonders."),
    RoomDescription("The Iron Garden", "Flowers made of rusted steel sway without wind. Their petals ring like chimes when touched.", "A metallic garden of rusted beauty."),
    RoomDescription("The Glass Sepulcher", "Transparent walls reveal the stars outside. A crystal coffin rests in the center, untouched by time.", "A celestial tomb of shimmering glass."),
    RoomDescription("Witchlight Crossing", "Lanterns flicker over a narrow bridge. The water beneath glows faintly green, hinting at something below.", "A fragile bridge lit by eerie witchfire."),
]



def decorate(game):
    start = game.player.location
    end = game.world.grid[game.world.max_x][game.world.max_y]
    start.name = START_ROOM_DESCIPTION.name
    start.description = START_ROOM_DESCIPTION.description
    start.outer_description = START_ROOM_DESCIPTION.outer_description
    end.name = END_ROOM_DESCRIPTION.name
    end.description = END_ROOM_DESCRIPTION.description
    end.outer_description = END_ROOM_DESCRIPTION.outer_description
    for x in range(game.world.cols()):
        for y in range(game.world.rows()):
            room = game.world.grid[x][y]
            if room != start and room != end:
                index = random.randrange(len(DESCRIPTIONS))
                description = DESCRIPTIONS[index]
                room.description = description.description
                room.name = description.name
                room.outer_description = description.outer_description