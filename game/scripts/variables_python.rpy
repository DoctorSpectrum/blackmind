init python:
    _game_menu_screen = "pause_menu"

    config.fade_music = 1.0
    config.autosave_on_choice = False

    import datetime, random

    #Functions
    def swap_sprites(new_sprite, transition = None, position = center):
        for sprite in renpy.list_images():
            if (sprite[0:7] == "barbara" or sprite[0:6] == "graves" or sprite[0:5] == "eddie" or sprite[0:3] == "cat"):
                renpy.hide(sprite)
        renpy.show(new_sprite, [position])
        if transition is not None:
            renpy.with_statement(transition)

    def play_music(song_title):
        if(song_title == "neutral_1"):
            renpy.music.play("audio/music/Blackmind Track 1 - 97 BPM (D minor)v2- LOOPABLE.wav", loop=True)
            #renpy.music.play("audio/music/PSYNCIN' IN THE CURTaiN.mp3", loop=True)
        elif (song_title == "tense_1"):
            #renpy.music.play("audio/music/08 警戒 -keikAI-.mp3", loop=True)
            renpy.music.play("audio/music/Blackmind Track 2.wav", loop=True)
        elif (song_title == "ambient_1"):
            #renpy.music.play("audio/music/1-01. Prelude - The “Night” Begins.mp3", loop=True)
            renpy.music.play("audio/music/Blackmind Track 3 - 140 BPM (C minor) - LOOPABLE.wav", loop=True)
        elif (song_title == "neutral_2"):
            #renpy.music.play("audio/music/1-13. Madam - Perfumed Lady.mp3", loop=True)
            renpy.music.play("audio/music/Track #4.wav")
        elif (song_title == "tense_2"):
            #renpy.music.play("audio/music/31 PSYNCIN' IN THE VILLaiN.mp3", loop=True)
            renpy.music.play("audio/music/Track #5 128 BPM G Maj.wav", loop=True)
        
        unlock_music(song_title)

    def play_sound(effect_name, loop=False, volume=1.0, from_time="", pause=None, transition=None):
        if (renpy.is_skipping() == False):
            renpy.sound.play(from_time + "audio/sfx/" + effect_name, loop=loop, relative_volume=volume)
        if (transition is not None):
            renpy.with_statement(transition)
        if (pause is not None and not preferences.get_mute("sfx") and preferences.get_mixer("sfx") > 0 and not renpy.is_skipping()):
            renpy.pause(pause, hard=True)

    def jack_partial(line):
        if (line == "cocky_01"):
            voice("audio/voice/partials/jack/jack_cocky_01.ogg")
        elif (line == "cocky_02"):
            voice("audio/voice/partials/jack/jack_cocky_02.ogg")
        elif (line == "cocky_03"):
            voice("audio/voice/partials/jack/jack_cocky_03.ogg")
        elif (line == "analytical_01"):
            voice("audio/voice/partials/jack/jack_analytical_01.ogg")
        elif (line == "analytical_02"):
            voice("audio/voice/partials/jack/jack_analytical_02.ogg")
        elif (line == "analytical_03"):
            voice("audio/voice/partials/jack/jack_analytical_03.ogg")
        elif (line == "scared_01"):
            voice("audio/voice/partials/jack/jack_scared_01.ogg")
        elif (line == "scared_02"):
            voice("audio/voice/partials/jack/jack_scared_02.ogg")
        elif (line == "irritated_01"):
            voice("audio/voice/partials/jack/jack_irritated_01.ogg")
        elif (line == "irritated_02"):
            voice("audio/voice/partials/jack/jack_irritated_02.ogg")
        elif (line == "dismissive_01"):
            voice("audio/voice/partials/jack/jack_dismissive_01.ogg")
        elif (line == "dismissive_02"):
            voice("audio/voice/partials/jack/jack_dismissive_02.ogg")
        elif (line == "confused_01"):
            voice("audio/voice/partials/jack/jack_confused_01.ogg")
        elif (line == "confused_02"):
            voice("audio/voice/partials/jack/jack_confused_02.ogg")
        elif (line == "friendly_01"):
            voice("audio/voice/partials/jack/jack_friendly_01.ogg")
        elif (line == "cheerful_01"):
            voice("audio/voice/partials/jack/jack_cheerful_01.ogg")
        elif (line == "angry_01"):
            voice("audio/voice/partials/jack/jack_angry_01.ogg")
        elif (line == "disappointed_01"):
            voice("audio/voice/partials/jack/jack_disappointed_01.ogg")

    def barbara_partial(line):
        if (line == "irritated_01"):
            voice("audio/voice/partials/barbara/barbara_irritated_01.ogg")

    def docherty_partial(line):
        if (line == "calm_01"):
            voice("audio/voice/partials/docherty/docherty_calm_01.ogg")

    def mind_read_line():
        #In the full version, account for whether we're having Lloyd or Jack read this line
        line = random.choice([
            "audio/voice/partials/jack/jack_mind_read_01.ogg",
            "audio/voice/partials/jack/jack_mind_read_02.ogg"
        ])
        voice(line)
        if (preferences.get_mute("voice") or preferences.get_mixer("voice") < 0.1):
            return 2.0
        elif (line == "audio/voice/partials/jack/jack_mind_read_01.ogg"):
            return 2.2
        elif (line == "audio/voice/partials/jack/jack_mind_read_02.ogg"):
            return 3.2

    def mind_rewind_line():
        line = random.choice([
            "audio/voice/partials/jack/jack_mind_wipe_01.ogg",
            "audio/voice/partials/jack/jack_mind_wipe_02.ogg"
        ])
        voice(line)
        if (preferences.get_mute("voice") or preferences.get_mixer("voice") < 0.1):
            return 2.0
        elif (line == "audio/voice/partials/jack/jack_mind_wipe_01.ogg"):
            return 2.2
        elif (line == "audio/voice/partials/jack/jack_mind_wipe_02.ogg"):
            return 2.8

    def unlock_music(handle):
        tracks = list(filter(lambda x: x["handle"] == handle, persistent.music_tracks))
        if (len(tracks) > 0):
            tracks[0]["unlocked"] = True

    def lock_music(handle):
        tracks = list(filter(lambda x: x["handle"] == handle, persistent.music_tracks))
        if (len(tracks) > 0):
            tracks[0]["unlocked"] = False

    def jump_sound(value):
        currently_playing = renpy.get_screen_variable("currently_playing", "sound_room")
        renpy.music.play("<from " + (str(value)) + ">audio/music/" + currently_playing["file"], loop=False)

    def convert_to_time(value):
        if (value == None):
            return ""
        return '{0:02.0f}:{1:02.0f}'.format(*divmod(value, 60))

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

    def remove_boolean(value):
        if (value in booleans):
            booleans.remove(value)

    def cg_index_unlocked(index):
        return list(filter(lambda x: x["locked"] == False, persistent.cgs[index]["images"]))

    def total_cgs_unlocked():
        total = 0
        for i in range(1):
            total += len(cg_index_unlocked(i))

        return total

    def unlock_cg(cg_index, file_index):
        persistent.cgs[cg_index]["images"][file_index]["locked"] = False

    def lock_cg(cg_index, file_index):
        persistent.cgs[cg_index]["images"][file_index]["locked"] = True

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
        remove_boolean("psychic_splash_read")
        remove_boolean("psychic_splash_rewind")

        if (calendar):
            renpy.show_screen("calendar", day=calendar_day, section=calendar_section, sections=calendar_sections)
        if (history):
            renpy.show_screen("conversation_history")

    def set_convo_length(length, progress=0):
        global convo_progress, convo_length
        convo_progress = progress
        convo_length = length

    def extend_convo_length(extension):
        global convo_progress, convo_length
        set_convo_length(convo_length + extension, convo_progress)

    def ignore_thoughts_length(subtract=1):
        global convo_progress, progress_convo, reading_mind
        if (progress_convo):        #We only need to subtract it if it's been added to the length
            convo_progress -= subtract
        progress_convo = True
        reading_mind = False
        renpy.show_screen("psychic_powers")

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