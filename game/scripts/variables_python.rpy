init python:
    _game_menu_screen = "pause_menu"

    config.fade_music = 1.0
    config.autosave_on_choice = False

    #Functions
    def swap_sprites(new_sprite, transition = None, position = center):
        for sprite in renpy.list_images():
            if (sprite[0:7] == "barbara" or sprite[0:6] == "graves" or sprite[0:5] == "eddie" or sprite[0:3] == "cat"):
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

    def visit_location(location):
        if (len(days[0]) < 3):
            days[0].append(location)
        elif (len(days[1]) < 3):
            days[1].append(location)
        elif (len(days[2]) < 3):
            days[2].append(location)
        elif (len(days[3]) < 3):
            days[3].append(location)

        #if (len(days[0]) == 3 and len(days[1]) == 0):
        #    renpy.save(str(game_id) + "_A_01_03")
        #    [id]_[branch]_[day]_[section]
        #elif (len(days[1]) == 3 and len(days[2]) == 0):
        #    renpy.save(str(game_id) + "_A_02_03")
        #elif (len(days[2]) == 3 and len(days[3]) == 0):
        #    renpy.save(str(game_id) + "_A_03_03")
        #elif (len(days[3]) == 3):
        #    renpy.save(str(game_id) + "_A_04_03")

    def add_date_suffix(date):
        date = int(date)
        date_suffix = ["th", "st", "nd", "rd"]

        if date % 10 in [1, 2, 3] and date not in [11, 12, 13]:
            return str(date) + date_suffix[date % 10] + " "
        else:
            return str(date) + date_suffix[0] + " "