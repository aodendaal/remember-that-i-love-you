# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define playerCharacter = Character("You", color="#A0A0A0")
define blueCharacter = Character("Blue", color="#4800FF")
define redCharacter = Character("Red", color="#CD1111")
define orangeCharacter = Character("Orange", color="#FF6A00")
define purpleCharacter = Character("Purple", color="#CC74F3")
define greenCharacter = Character("Green", color="#74F385")
define pinkCharacter = Character("Pink", color="#F374E1")

screen character_map:
    imagemap:
        ground "map_background2.png"
        hover "map_hover2.png"

        hotspot (314, 154, 466 - 314, 291 - 154) clicked Call(story + ".blue") #blue
        hotspot (509, 112, 661 - 509, 260 - 112) clicked Call(story + ".red") #red
        hotspot (317, 332, 471 - 317, 468 - 332) clicked Call(story + ".green") #green
        hotspot (527, 281, 679 - 527, 433 - 281) clicked Call(story + ".purple") #purple
        hotspot (331, 486, 495 - 331, 652 - 486) clicked Call(story + ".orange") #orange
        hotspot (532, 460, 679 - 532, 597 - 460) clicked Call(story + ".pink") #pink

# The game starts here.

label start:

    $ story = renpy.random.choice(["aliens"])

    call expression story + ".start" from _call_expression

    return

## Vocals ############################################################
######################################################################

label vocals:

label .male:

    $ r = renpy.random.randint(0, 5)

    if r == 0:
        play sound "audio/Vocals/Male/Greetings 1.mp3"
    elif r == 1:
        play sound "audio/Vocals/Male/Greetings 2.mp3"
    elif r == 2:
        play sound "audio/Vocals/Male/Hello 1.mp3"
    elif r == 3:
        play sound "audio/Vocals/Male/Hello 2.mp3"
    elif r == 4:
        play sound "audio/Vocals/Male/Howdy 1.mp3"
    elif r == 5:
        play sound "audio/Vocals/Male/Hello 2.mp3"

    return

label .female:

    $ r = renpy.random.randint(0, 5)

    if r == 0:
        play sound "audio/Vocals/Female/Greetings 1.mp3"
    elif r == 1:
        play sound "audio/Vocals/Female/Greetings 2.mp3"
    elif r == 2:
        play sound "audio/Vocals/Female/Greetings 3.mp3"
    elif r == 3:
        play sound "audio/Vocals/Female/Hello 1.mp3"
    elif r == 4:
        play sound "audio/Vocals/Female/Hello 2.mp3"
    elif r == 5:
        play sound "audio/Vocals/Female/Hello 3.mp3"

    return

## Aliens ############################################################
######################################################################

label aliens:

label .start:

    play music "audio/Far Out Mann_final_standard.mp3"

    scene bg stadium day

    show fbi1

    playerCharacter "I got called out to a sports stadium because people reported seeing flying saucers, loud noises and people screaming"

    playerCharacter "There's nothing in the sky now but the place is littered with scorch marked and occasional sprays of blood. Something definitely happened here"

    playerCharacter "I've managed to gather a group of witnesses but they're all terribly traumatised."

    playerCharacter "If I can help them find the person they're looking for, maybe I can get some answers to what happened here?"

    hide fbi1

    ## Blue Initialization
    $ hadBlueIntro = False
    $ foundTicketStubs = False
    $ blueOptions = ["option1", "option2", "option3"]

    ## Red Intialization
    $ hadRedIntro = False
    $ sharedHotdog = False
    $ redOptions = ["option1", "option2"]

    ## Orange Initialization
    $ hadOrangeIntro = False
    $ orangeOptions = []

    ## Purple Initialization
    $ hadPurpleIntro = False
    $ purpleOptions = []

    ## Green Initialization
    $ hadGreenIntro = False
    $ greenOptions = []

    ## Pink Initialization
    $ hadPinkIntro = False
    $ pinkOptions = []

    call aliens.map from _call_aliens_map
        
    return

label .map:

    call screen character_map

    return

## Blue ##############################################################

label .blue:

    call vocals.male

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
            call aliens.blueOption1 from _call_aliens_blueOption1
        elif option == "option2":
            call aliens.blueOption2 from _call_aliens_blueOption2
        elif option == "option3":
            call aliens.blueOption3 from _call_aliens_blueOption3

    if foundTicketStubs == False:
        call aliens.blueTicketStubs from _call_aliens_ticketStubs
        $ foundTicketStubs = True

    hide blue

    hide fbi1

    call aliens.map from _call_aliens_map_1

label .blueIntro:

    show fbi1 at left

    show blue at right

    playerCharacter "Excuse me sir, I'd like to ask you a few questions if you don't mind?"

    blueCharacter "Huh? Oh. Of course. *distracted* What do you want?"

    playerCharacter "Can you tell me what happened?"

    return

label .blueContinue:

    show fbi1 at left

    show blue at right

    playerCharacter "Is there anything else you remember?"

    return

label .blueNoDialogue:

    blueCharacter "I can't think of anything more to tell you."

    return

label .blueOption1:

    blueCharacter "If I close my eyes I see large silver discs in the sky making a loud humming noise."

    blueCharacter "Then a bright green light with incredible heat. I remember people screaming and running."

    return

label .blueOption2:

    blueCharacter "I remember laughing at our team's mascot chasing the other mascot around. It was such a perfect day."

    blueCharacter "Now I think the world will never be the same again. I don't think I could even crack a smile."

    return


label .blueOption3:

    blueCharacter "I think our team was winning and they were going to send that new player onto the field. I was really excited to see his debut."

    return

label .blueTicketStubs:

    blueCharacter "I also found this pair of ticket stubs in my pocket. I must have been in the stands with someone, but I can't remember who."

    return

## Red ###############################################################

label .red:

    call vocals.female

    if hadRedIntro == False:
        call aliens.redIntro
        $ hadRedIntro = True
    else:
        call aliens.redContinue

    if sharedHotdog == False:
        call aliens.redHotdog
        $ sharedHotdog = True

    if len(redOptions) == 0:
        call aliens.redNoDialogue
    else:
        $ option = renpy.random.choice(redOptions)
        $ redOptions.remove(option)

        if option == "option1":
            call aliens.redOption1
        elif option == "option2":
            call aliens.redOption2
        elif option == "option3":
            call aliens.redOption3

    hide red

    hide fbi1

    call aliens.map

label .redIntro:

    show fbi1 at left

    show red at right

    playerCharacter "Excuse me mam, can you tell me what you saw?"

    redCharacter "It was so horrifying, I think I blacked out."

    playerCharacter "Please can you try and tell me what you can remember?"

    return

label .redContinue:

    show fbi1 at left

    show red at right

    playerCharacter "Can you tell me anything else you remember?"

    redCharacter "Um..."

    return

label .redNoDialogue:

    hide fbi1

    show red at center

    redCharacter "Please. Don't ask me any more questions. I don't want to remember."

    return

label .redHotdog:

    redCharacter "I remember sharing a hotdog with someone. The day was perfect. I think we were in love."

    playerCharacter "I'm sorry to hear that"

    redCharacter "Please! You have to help me find them *sobs*"

    return

label .redOption1:

    redCharacter "We were watching the game when suddenly it went dark. Then there was a blinding light."

    redCharacter "I remember screaming and crying"

    return

label .redOption2:

    redCharacter "We were watching the game when suddenly it went dark. Then there was a blinding light."

    redCharacter "I remember screaming and crying"

    return

## Orange ############################################################

label .orange:

    call vocals.male

    if hadOrangeIntro == False:
        call aliens.orangeIntro
        $ hadOrangeIntro = True
    else:
        call aliens.orangeContinue

    if len(orangeOptions) == 0:
        call aliens.orangeNoDialogue
    else:
        $ option = renpy.random.choice(orangeOptions)
        $ orangeOptions.remove(option)

        if option == "option1":
            call aliens.orangeOption1
        elif option == "option2":
            call aliens.orangeOption2
        elif option == "option3":
            call aliens.orangeOption3

    hide orange

    hide fbi1

    call aliens.map 

label .orangeIntro:

    show fbi1 at left

    show orange at right

    playerCharacter "Excuse me sir, can you tell me what you saw?"

    orangeCharacter "It was so horrifying, I think I blacked out."

    playerCharacter "Please can you try and tell me what you can remember?"

    return

label .orangeContinue:

    show fbi1 at left

    show orange at right

    playerCharacter "Can you tell me anything else you remember?"

    return

label .orangeNoDialogue:

    hide fbi1

    show orange at center

    orangeCharacter "I can't think of anything else"

    return

## Purple ############################################################

label .purple:

    call vocals.male

    if hadPurpleIntro == False:
        call aliens.purpleIntro
        $ hadPurpleIntro = True
    else:
        call aliens.purpleContinue

    if len(purpleOptions) == 0:
        call aliens.purpleNoDialogue
    else:
        $ option = renpy.random.choice(purpleOptions)
        $ purpleOptions.remove(option)

        if option == "option1":
            call aliens.purpleOption1
        elif option == "option2":
            call aliens.purpleOption2
        elif option == "option3":
            call aliens.purpleOption3

    hide purple

    hide fbi1

    call aliens.map 

label .purpleIntro:

    show fbi1 at left

    show purple at right

    playerCharacter "Excuse me sir, can you tell me what you saw?"

    purpleCharacter "It was so horrifying, I think I blacked out."

    playerCharacter "Please can you try and tell me what you can remember?"

    return

label .purpleContinue:

    show fbi1 at left

    show purple at right

    playerCharacter "Can you tell me anything else you remember?"

    return

label .purpleNoDialogue:

    hide fbi1

    show purple at center

    purpleCharacter "I can't think of anything else"

    return

## Green #############################################################

label .green:

    call vocals.female

    if hadGreenIntro == False:
        call aliens.greenIntro
        $ hadGreenIntro = True
    else:
        call sliens.greenContinue

    if len(greenOptions) == 0:
        call aliens.greenNoDialogue
    else:
        $ option = renpy.random.choice(greenOptions)
        $ greenOptions.remove(option)

        if option == "option1":
            call aliens.greenOption1
        elif option == "option2":
            call aliens.greenOption2
        elif option == "option3":
            call aliens.greenOption3

    hide green

    hide fbi1

    call aliens.map 

label .greenIntro:

    show fbi1 at left

    show green at right

    playerCharacter "Excuse me mam, can you tell me what you saw?"

    greenCharacter "It was so horrifying, I think I blacked out."

    greenCharacter "Please can you try and tell me what you can remember?"

    return

label .greenContinue:

    show fbi1 at left

    show green at right

    greenCharacter "Can you tell me anything else you remember?"

    return

label .greenNoDialogue:

    hide fbi1

    show green at center

    greenCharacter "I can't think of anything else"

    return

## Pink ##############################################################

label .pink:

    call vocals.female

    if hadPinkIntro == False:
        call aliens.pinkIntro
        $ hadPinkIntro = True
    else:
        call aliens.pinkContinue

    if len(pinkOptions) == 0:
        call aliens.pinkNoDialogue
    else:
        $ option = renpy.random.choice(pinkOptions)
        $ pinkOptions.remove(option)

        if option == "option1":
            call aliens.pinkOption1
        elif option == "option2":
            call aliens.pinkOption2
        elif option == "option3":
            call aliens.pinkOption3

    hide pink

    hide fbi1

    call aliens.map 

label .pinkIntro:

    show fbi1 at left

    show pink at right

    playerCharacter "Excuse me mam, can you tell me what you saw?"

    pinkCharacter "It was so horrifying, I think I blacked out."

    pinkCharacter "Please can you try and tell me what you can remember?"

    return

label .pinkContinue:

    show fbi1 at left

    show pink at right

    pinkCharacter "Can you tell me anything else you remember?"

    return

label .pinkNoDialogue:

    hide fbi1

    show pink at center

    pinkCharacter "I can't think of anything else"

    return
