#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# Circuit python 6


import ugame
import stage

import constants


# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# a list of sprites that will be updated every frame
sprites = []


def main():
    # this function is a scene
    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2 -
                        constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE +
                        constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at the top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # (keys)
        if keys & ugame.K_X != 0:  # a button (fire)
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_O:  # b
            pass
        if keys & ugame.K_START:  # start
            pass
        if keys & ugame.K_SELECT:  # select
            pass
        if keys & ugame.K_RIGHT != 0:  # right
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)
            pass
        if keys & ugame.K_LEFT != 0:  # left
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
            pass
        if keys & ugame.K_UP:  # up
            ship.move(ship.x, ship.y - 1)
            pass
        if keys & ugame.K_DOWN:  # down
            ship.move(ship.x, ship.y + 1)
            pass
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
