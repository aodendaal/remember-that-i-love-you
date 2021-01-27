# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

screen character_map:
    imagemap:
        ground "map_background.png"
        hover "map_hover.png"

        hotspot (100, 100, 100, 100) clicked Jump("chat")
        hotspot (600, 100, 100, 100) clicked Jump("chat2")

# The game starts here.

label start:

    jump showmap

label showmap:

    call screen character_map

label whatwhat:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show andrew happy at right

    show martha at left

    show bobo

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label chat:

    scene bg room

    show marc

    e "Thank you for clicking on me"

    jump showmap

label chat2:

    scene bg room

    show bob

    e "This is bobo"

    jump showmap