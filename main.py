basic.show_icon(IconNames.ASLEEP)
basic.pause(200)
basic.show_leds("""
    . # . # .
    . # . # .
    . . . . .
    . # # # .
    . . . . .
    """)
basic.pause(100)
basic.show_icon(IconNames.HAPPY)
basic.pause(500)

def on_forever():
    if input.pin_is_pressed(TouchPin.P1):
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(100)
        basic.show_icon(IconNames.HEART)
    else:
        basic.show_icon(IconNames.NO)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.IN_BACKGROUND)
        servos.P2.set_angle(180)
        basic.pause(1000)
        servos.P2.set_angle(0)
        basic.pause(1000)
basic.forever(on_forever)
