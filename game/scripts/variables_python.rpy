init python:
    #_game_menu_screen = "pause"

    config.fade_music = 1.0
    config.autosave_on_choice = False

    #Functions
    def swap_sprites(new_sprite, transition = None, position = center):
        for sprite in renpy.list_images():
            if (sprite[0:14] == "character_name"):
                renpy.hide(sprite)
        renpy.show(new_sprite, [position])
        if transition is not None:
            renpy.with_statement(transition)

    def play_music(song_title):
        if(song_title == "song_title"):
            renpy.music.play("<from 0.0 to 44.000>audio/music/song_title.mp3", loop=True)

    def play_sound(effect_name, loop=False, volume=1.0, from_time="", pause=None):
        if (renpy.is_skipping() == False):
            renpy.sound.play(from_time + "audio/sfx/" + effect_name, loop=loop, relative_volume=volume)
        if (pause is not None and not preferences.get_mute("sfx") and preferences.get_mixer("sfx") > 0 and not renpy.is_skipping()):
            renpy.pause(pause, hard=True)

    def queue_sound(effect_name, loop=False):
        if (renpy.is_skipping() == False):
            renpy.sound.queue("audio/sfx/" + effect_name, loop=loop)

    def disable_rollback():
        config.rollback_enabled = False

    def enable_rollback():
        renpy.block_rollback()
        config.rollback_enabled = True

    def clear_rollback():
        disable_rollback()
        enable_rollback()

    def unlock_cg(cg_id):
        if (cg_id not in persistent.cgs_unlocked):
            persistent.cgs_unlocked.append(cg_id)

    def lock_cg(cg_id):
        persistent.cgs_unlocked.remove(cg_id)