# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define p = Character("You", color="#A0A0A0")
define b = Character("Blue", color="#4800FF")
define r = Character("Red", color="#CD1111")

screen character_map:
    imagemap:
        ground "map_background2.png"
        hover "map_hover2.png"

        hotspot (558, 25, 731 - 558, 190 - 25) clicked Call(story + ".blue") #blue
        hotspot (286, 220, 467 - 286, 396 - 220) clicked Call(story + ".red") #red

# The game starts here.

label start:

    $ story = renpy.random.choice(["aliens"])

    call expression story + ".start"

    return


## Aliens ############################################################
######################################################################

label aliens:

label .start:

    scene bg meadow

    show player

    p "I got called out to a sports stadium because people reported seeing flying saucers, loud noises and people screaming"

    p "There's nothing in the sky now but the place is littered with scorch marked and occasional sprays of blood. Something definitely happened here"

    p "I've managed to gather a group of witnesses but they're all terribly traumatised."

    p "If I can help them find the person they're looking for, maybe I can get some answers to what happened here?"

    hide player

    $ hadBlueIntro = False
    $ foundTicketStubs = False
    $ blueOptions = ["option1", "option2", "option3"]

    call aliens.map
        
    return

label .map:

    call screen character_map

    return

## Blue ##############################################################

label .blue:

    if hadBlueIntro == False:
        call aliens.blueIntro
        $ hadBlueIntro = True
    else:
        call aliens.blueContinue

    if len(blueOptions) == 0:
        call aliens.blueNoDialogue
    else:
        $ option = renpy.random.choice(blueOptions)
        $ blueOptions.remove(option)

        if option == "option1":
            call aliens.blueOption1
        elif option == "option2":
            call aliens.blueOption2
        elif option == "option3":
            call aliens.blueOption3

    if foundTicketStubs == False:
        call aliens.ticketStubs
        $ foundTicketStubs = True

    hide blue

    hide player

    call aliens.map

label .blueIntro:

    show player at left

    show blue at right

    p "Excuse me sir, I'd like to ask you a few questions if you don't mind?"

    b "Huh? Oh. Of course. *distracted* What do you want?"

    p "Can you tell me what happened?"

    return

label .blueContinue:

    show player at left

    show blue at right

    p "Is there anything else you remember?"

    return

label .blueNoDialogue:

    b "I can't think of anything more to tell you."

    return

label .blueOption1:

    b "If I close my eyes I see large silver discs in the sky making a loud humming noise."

    b "Then a bright green light with incredible heat. I remember people screaming and running."

    return

label .blueOption2:

    b "I remember laughing at our team's mascot chasing the other mascot around. It was such a perfect day."

    b "Now I think the world will never be the same again. I don't think I could even crack a smile."

    return


label .blueOption3:

    b "I think our team was winning and they were going to send that new player onto the field. I was really excited to see his debut."

    return

label .ticketStubs:

    b "I also found this pair of ticket stubs in my pocket. I must have been in the stands with someone, but I can't remember who."

    return

## Red ###############################################################

label .red:

    show red at left

    show player at right

    r "I'm Red and I only have 1 memory"

    hide red

    hide player

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