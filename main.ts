input.onGesture(Gesture.Shake, function on_gesture_shake() {
    //  "random" loading time
    for (let y = 0; y < randint(1, 4); y++) {
        for (let x = 0; x < 4; x++) {
            loading[x].showImage(0)
            basic.pause(100)
        }
    }
    //  show answer
    basic.clearScreen()
    basic.showString(possibleAnswers[randint(0, 20)], 70)
})
//  total of 20 answers
let possibleAnswers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
//  loading list that needs to be looped to produce animation            
let loading = [images.createImage(`
. . . . .
. . . . .
. # # # .
. . . . .
. . . . .
`), images.createImage(`
. . . . .
. # . . .
. . # . .
. . . # .
. . . . .
`), images.createImage(`
. . . . .
. . # . .
. . # . .
. . # . .
. . . . .
`), images.createImage(`
. . . . .
. . . # .
. . # . .
. # . . .
. . . . .
`), images.createImage(`
. . . . .
. . . . .
. # # # .
. . . . .
. . . . .
`)]
