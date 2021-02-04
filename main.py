def on_gesture_shake():
    # "random" loading time
    for y in range(randint(1,4)):
        for x in range(4):
            loading[x].show_image(0)
            basic.pause(100)
    # show answer
    basic.clear_screen()
    basic.show_string(possibleAnswers[randint(0,20)], 70)

input.on_gesture(Gesture.Shake, on_gesture_shake)

# total of 20 answers
possibleAnswers = (
            'It is certain.', 'It is decidedly so.', 'Without a doubt.',
            'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
            'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
            'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
            'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.",
            'My reply is no.', 'My sources say no.', 'Outlook not so good.',
            'Very doubtful.')

# loading list that needs to be looped to produce animation            
loading = [images.create_image("""
. . . . .
. . . . .
. # # # .
. . . . .
. . . . .
"""), images.create_image("""
. . . . .
. # . . .
. . # . .
. . . # .
. . . . .
"""), images.create_image("""
. . . . .
. . # . .
. . # . .
. . # . .
. . . . .
"""), images.create_image("""
. . . . .
. . . # .
. . # . .
. # . . .
. . . . .
"""),images.create_image("""
. . . . .
. . . . .
. # # # .
. . . . .
. . . . .
"""),
]