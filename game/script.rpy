# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

screen character_map:
    imagemap:
        ground "map_background2.png"
        hover "map_hover2.png"

        hotspot (558, 25, 731 - 558, 190 - 25) clicked Call(story + ".chat1") #blue
        hotspot (286, 220, 467 - 286, 396 - 220) clicked Call(story + ".chat2") #red

# The game starts here.

label start:

    $ story = renpy.random.choice(["aliens"])

    call expression story + ".start"

    return


## Aliens ############################################################

label aliens:

label .start:

    "Green light. Shining metal. The eerie quiet. These are the things I remember"

    "I found six others but they don't remember much either"

    "They're all looking for someone they lost"

    $ chat1options = ["option1", "option2", "option3"]

    call aliens.map
        
    return

label .map:

    call screen character_map

    return

label .chat1:

    if len(chat1options) == 0:
        call aliens.chat1nodialogue
    else:
        $ option = renpy.random.choice(chat1options)
        $ chat1options.remove(option)

        if option == "option1":
            call aliens.chat1option1
        elif option == "option2":
            call aliens.chat1option2
        elif option == "option3":
            call aliens.chat1option3

    call aliens.map

label .chat1nodialogue:

    "I can't think of anything more"

    return

label .chat1option1:

    "I am Blue and this is memory 1"

    return

label .chat1option2:

    "I am Blue and this is memory 2"

    return


label .chat1option3:

    "I am Blue and this is memory 3"

    return

label .chat2:

    "I'm Red and I only have 1 memory"

    call aliens.map

## Kaiju #############################################################

label kaiju:

label .start:

    "This is the start of the kaiju story"

    call screen character_map

    return

label .chat:

    "This is kaiju chat"

    return

label .chat2:

    "This is kaiju chat 2"

    return

## Wizard ############################################################

label wizard:

label .start:

    "This is the start of the wizard story"

    call screen character_map

    return

label .chat:

    "This is wizard chat"

    return

label .chat2:

    "This is wizard chat 2"

    return

## Demons ############################################################

label demons:

label .start:

    "This is the start of the demons story"

    call screen character_map

    return

label .chat:

    "This is demons chat"

    return

label .chat2:

    "This is demons chat 2"

    return