basic.showIcon(IconNames.Asleep)
basic.pause(200)
basic.showLeds(`
    . # . # .
    . # . # .
    . . . . .
    . # # # .
    . . . . .
    `)
basic.pause(100)
basic.showIcon(IconNames.Happy)
basic.pause(500)
basic.forever(function () {
    if (input.pinIsPressed(TouchPin.P1)) {
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(100)
        basic.showIcon(IconNames.Heart)
    } else {
        basic.showIcon(IconNames.No)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
        servos.P2.setAngle(180)
        basic.pause(1000)
        servos.P2.setAngle(0)
        basic.pause(1000)
    }
})
