def on_a_pressed():
    global projectile
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 2 2 2 2 2 2 2 2 2 2 2 
                    . . . . 2 2 2 2 2 2 2 2 2 2 2 2 
                    . . . . 2 2 2 2 2 2 2 2 2 2 2 2 
                    . . . . 2 2 2 2 2 2 2 2 2 2 2 2 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.UNTIL_DONE)
    otherSprite2.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
spacePlane: Sprite = None
spacePlane = sprites.create(img("""
        8 8 8 8 8 . . . . . . . . . . . 
            8 5 5 5 5 8 . . . . . . . . . . 
            8 5 5 5 5 5 8 . . . . . . . . . 
            8 5 5 5 5 5 5 8 . . . . . . . . 
            8 5 5 5 5 5 5 5 8 . . . . . . . 
            8 5 5 5 5 5 5 5 5 8 . . . . . . 
            8 5 5 5 5 5 5 5 5 5 2 . . . . . 
            8 5 5 5 5 5 5 5 5 5 8 2 . . . . 
            8 5 5 5 5 5 5 5 5 5 2 . . . . . 
            8 5 5 5 5 5 5 5 5 8 . . . . . . 
            8 5 5 5 5 5 5 5 8 . . . . . . . 
            8 5 5 5 5 5 5 8 . . . . . . . . 
            8 5 5 5 5 5 8 . . . . . . . . . 
            8 5 5 5 5 8 . . . . . . . . . . 
            8 5 5 5 8 . . . . . . . . . . . 
            8 8 8 8 . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(spacePlane, 50, 50)
spacePlane.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . a a a a a a a a a a a . . 
                    . . a a a a a a a a a a a a . . 
                    . . a a a a a a a a a a a a . . 
                    . . a a a a 1 1 1 1 1 a a a a . 
                    . . a a a a 1 f f f 1 a a a a . 
                    . . a a a a 1 f f f 1 a a a a . 
                    . . a a a a 1 1 1 1 1 a a a a . 
                    . . a a a a a a a a a a a a a . 
                    . . a a a a a a a a a a a a a . 
                    . . a a a a a a a a a a a a a . 
                    . . . . a . . . . . . a . . . . 
                    . . . . a . . . . . . a . . . . 
                    . . . . a . . . . . . a . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-50, 0)
    bogey.set_position(160, randint(5, 115))
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval)
