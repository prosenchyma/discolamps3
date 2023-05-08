strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
ループ　= True

def on_button_pressed_a():
    global ループ
    ループ　= True
    strip.set_pixel_color(0, neopixel.rgb(102,84,94))
    strip.set_pixel_color(1, neopixel.rgb(163,145,147))
    strip.set_pixel_color(2, neopixel.rgb(170,111,115))
    strip.set_pixel_color(3, neopixel.rgb(238,169,144))
    strip.set_pixel_color(4, neopixel.rgb(246,224,181))
    strip.show()
    while ループ == True:
        strip.rotate(1)
        strip.show()
        basic.pause(250)
        
def on_button_pressed_b():
    global ループ
    ループ　= False

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
