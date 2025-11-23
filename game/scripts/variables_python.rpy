init python:
    _game_menu_screen = "pause_menu"

    config.fade_music = 1.0
    config.autosave_on_choice = False

    import datetime

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

    def check_boolean(value):
        return value in booleans

    def add_boolean(value):
        if (not check_boolean(value)):
            booleans.append(value)

    def unlock_cg(cg_id):
        if (cg_id not in persistent.cgs_unlocked):
            persistent.cgs_unlocked.append(cg_id)

    def lock_cg(cg_id):
        persistent.cgs_unlocked.remove(cg_id)

    # Menus
    def close_menu():
        if (renpy.get_screen("saves_list")):
            renpy.hide_screen("saves_list")
        elif (renpy.get_screen("preferences")):
            renpy.hide_screen("preferences")
        elif (renpy.get_screen("about")):
            renpy.hide_screen("about")

        renpy.transition(quick_dissolve)
        
        if (not main_menu and not renpy.get_screen("map_navigation")):
            renpy.show_screen("pause_menu")
    
    def clickable_button():
        if (not renpy.get_screen("saves_list") and not renpy.get_screen("preferences") and not renpy.get_screen("about")):
            return True

        return False

    # Save/load
    def add_date_suffix(date):
        date = int(date)
        date_suffix = ["th", "st", "nd", "rd"]

        if date % 10 in [1, 2, 3] and date not in [11, 12, 13]:
            return str(date) + date_suffix[date % 10] + " "
        else:
            return str(date) + date_suffix[0] + " "

    def default_save_name():
        return "Save " + (find_next_save().replace("1-", ""))

    def find_next_save():
        for i in range(15):
            if (not renpy.can_load("1-" + str(i + 1))):
                return "1-" + str(i + 1)

        return "0"

    # General gameplay
    def scene_setup(scene_length = 0, calendar_day="Monday", calendar=True, calendar_section=1, calendar_sections=4, convo_scene=True, history=True):
        global progress_convo, convo_progress, convo_length, _history_list
        progress_convo = convo_scene
        convo_progress = 0
        convo_length = scene_length
        _history_list.clear()

        if (calendar):
            renpy.show_screen("calendar", day=calendar_day, section=calendar_section, sections=calendar_sections)
        if (history):
            renpy.show_screen("conversation_history")


    # Navigation selection
    def find_locations(ids):
        return list(filter(lambda x: x["id"] in ids, destinations))

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