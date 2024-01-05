import random

message_list = [
    "Smokin' that Whoopi Goldberg south Egyptian furburger deluxe Mega Millions scratcher skunk bubba kush",
    "I'm bitin' the fart bubbles in the bath",
    "We smokin' Sequoia banshee boogers",
    "Call that pussy The Matrix because I'm in this bitch and I can't get out",
    "Don't be shy, gurl, I love me some pastrami mud flaps",
    "My bitch look like David Hasselhoff",
    "I balled so hard they thought I was a fuckin' nutsack",
    "I'm high on 12 Jason Bournes, looking to beat the cum out of a thick, fresh oak.",
    "We smoking Symbiotes.",
    "I'm on 12 vicodins, smoking on Scooby-Doo dick.",
    "We smoking shit in a glass pipe, blowing the Lord's bubbles.",
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