import random

message_list = [
    "Smokin' that Whoopi Goldberg south Egyptian furburger deluxe Mega Millions scratcher skunk bubba kush",
    "I'm a dog, I'm bitin' the fart bubbles in the bath",
    "We smokin' Sequoia banshee boogers",
    "Call that pussy The Matrix because I'm in this bitch and I can't get out",
    "Don't be shy, gurl, I love me some pastrami mud flaps",
    "My bitch look like David Hasselhoff",
    "I balled so hard they thought I was a fuckin' nutsack",
    "I'm high on 12 Jason Bournes, looking to beat the cum out of a thick, fresh oak.",
    "We smoking Symbiotes.",
    "I'm on 12 vicodins, smoking on Scooby-Doo dick.",
    "We smoking shit in a glass pipe, blowing the Lord's bubbles.",
    "Smoking fentanyl-laced cereal milk: I see God",
    "I hope them aliens are real so that I have more things to fuck!",
    "Gulping sea monkeys by the gallon, my tummy feel crazy",
    "This Smith & Wesson got me moving like an invasive species",
    "They needed a stealth soldier, so I put my hands on the hibachi hot plate at Benihana, and burned my fucking finger prints off, they will not find me",
    "Blew her back out using a mammoth-skin condom",
    "We smoking that IBM Quantum Computer",
    "These cops are interrogating me about an ounce of weed, as if I didn't kill an Applebee's hostess two miles away",
    "I keep my Glock at the Vatican",
    "My diamonds come from the most horrific situations possible",
    "The Vatican wants to wet me up with silver bullets, but I'm on a god damn samurai pill!",
    "I got strands of RNA in my hookah, every puff is an insult to God",
    "I hydrated the soot between her ass cheeks, and snorted that shit through my eyelids",
    "Read you like a book? Naw, I had my feelers in every orifice reading your private bumps like braille.",
]

random.shuffle(message_list)

base_crosshair_id = 'crosshair'
alias = 'alias'

for i, message in enumerate(message_list):
    print (
        alias, 'message' + str(i), '"say "' + message + '"' + ';',
        alias, 'say_message ' + 'message'+str((i + 1) % len(message_list)) + '"'
        # alias, 'next_message' + 
    )

print('')
print('// initialize messages')
print('alias say_message message0')
print('bind kp_plus say_message')