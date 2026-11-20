init python:
    _game_menu_screen = "pause_menu"

    config.fade_music = 1.0
    config.autosave_on_choice = False
    config.pass_joystick_events = True
    config.overlay_screens.append("input_checker")

    import datetime, random

    #Functions
    def swap_sprites(new_sprite, transition = None, position = center):
        for sprite in renpy.list_images():
            if ((sprite[0:7] == "barbara" or sprite[0:6] == "graves" or sprite[0:5] == "eddie" or sprite[0:3] == "cat" or sprite[0:6] == "sergei" or sprite[0:7] == "killian") and sprite[0:13] != "killian_house"):
                renpy.hide(sprite)
        renpy.show(new_sprite, [position])
        if transition is not None:
            renpy.with_statement(transition)

    def play_music(song_title):
        if(song_title == "neutral_1"):
            renpy.music.play("audio/music/bourbon_mood.mp3", loop=True)
        elif (song_title == "tense_1"):
            renpy.music.play("audio/music/blundering_mistake.mp3", loop=True)
        elif (song_title == "ambient_1"):
            renpy.music.play("audio/music/before_midnight.mp3", loop=True)
        elif (song_title == "neutral_2"):
            renpy.music.play("audio/music/bitter_memories.mp3", loop=True)
        elif (song_title == "tense_2"):
            renpy.music.play("audio/music/beware_murderer.mp3", loop=True)
        
        unlock_music(song_title)

    def play_sound(effect_name, loop=False, volume=1.0, from_time="", pause=None, transition=None):
        if (renpy.is_skipping() == False):
            renpy.sound.play(from_time + "audio/sfx/" + effect_name, loop=loop, relative_volume=volume)
        if (transition is not None):
            renpy.with_statement(transition)
        if (pause is not None and not preferences.get_mute("sfx") and preferences.get_mixer("sfx") > 0 and not renpy.is_skipping()):
            renpy.pause(pause, hard=True)

    def jack_partial(line):
        voice("audio/voice/partials/jack/jack_" + line + ".ogg")

    def barbara_partial(line):
        voice("audio/voice/partials/barbara/barbara_" + line + ".ogg")

    def docherty_partial(line):
        voice("audio/voice/partials/docherty/docherty_" + line + ".ogg")

    def mind_read_line():
        #In the full version, account for whether we're having Lloyd or Jack read this line
        line = random.choice([
            "audio/voice/partials/jack/jack_mind_read_01.ogg",
            "audio/voice/partials/jack/jack_mind_read_02.ogg"
        ])
        voice(line)
        if (preferences.get_mute("voice") or preferences.get_mixer("voice") < 0.1):
            return {
                "time": 2.0,
                "line": "TELL ME\nWHAT YOU'RE \nTHINKING!"
            }
        elif (line == "audio/voice/partials/jack/jack_mind_read_01.ogg"):
            return {
                "time": 2.2,
                "line": "TELL ME\nWHAT YOU'RE \nTHINKING!"
            }
        elif (line == "audio/voice/partials/jack/jack_mind_read_02.ogg"):
            return {
                "time": 3.2,
                "line": "YOU CAN'T\nHIDE YOUR\nSECRETS\nFROM ME!"
            }

    def mind_rewind_line():
        line = random.choice([
            "audio/voice/partials/jack/jack_mind_wipe_01.ogg",
            "audio/voice/partials/jack/jack_mind_wipe_02.ogg"
        ])
        voice(line)
        if (preferences.get_mute("voice") or preferences.get_mixer("voice") < 0.1):
            return {
                "time": 2.0,
                "line": "FORGET ALL\nOF THIS!"
            }
        elif (line == "audio/voice/partials/jack/jack_mind_wipe_01.ogg"):
            return {
                "time": 2.2,
                "line": "FORGET ALL\nOF THIS!"
            }
        elif (line == "audio/voice/partials/jack/jack_mind_wipe_02.ogg"):
            return {
                "time": 2.8,
                "line": "YOU WILL NOT\nREMEMBER..."
            }

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
        renpy.set_screen_variable("pause_bar", True, screen="sound_room")

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
        if (check_boolean(value)):
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

    # Screens
    def hide_history():
        global history_expanded
        history_expanded = (renpy.get_screen_variable("expanded", "conversation_history") if renpy.get_screen("conversation_history") else history_expanded)
        renpy.hide_screen("conversation_history")

    def show_history():
        global history_expanded
        renpy.show_screen("conversation_history", history_expanded, True, history_expanded)

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
        renpy.choice_for_skipping()

        if (calendar):
            renpy.show_screen("calendar", day=calendar_day, section=calendar_section, sections=calendar_sections)
        if (history):
            show_history()

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
    def find_locations():
        if (day == 0):
            return [
                {
                    "key": "venue",
                    "label": "Music Venue",
                    "xcoord": 180,
                    "ycoord": 340,
                    "image": "images/backgrounds/venue_exterior.png",
                    "description": "Isn’t there some small underground place near here that plays jazz or one of those made-up music genres? They’ve got to have some booze there...people wouldn’t go there if they didn’t have any.",
                    "active": True,
                    "action": "prologue_music_venue",
                    "warning": False,
                    "hidden": False
                },
                {
                    "key": "restaurant",
                    "label": "Restaurant",
                    "xcoord": 182,
                    "ycoord": 312,
                    "image": "images/backgrounds/restaurant_night.png",
                    "description": "Do they have chips at this place? I kind of want chips now...Oh, I know! I’ll trick them into thinking they have chips if they don’t, and make them make some for me!",
                    "active": True,
                    "action": "prologue_restaurant",
                    "warning": False,
                    "hidden": False
                },
            ]

        return [
            {
                "key": "bar",
                "label": "Bar",
                "xcoord": 197,
                "ycoord": 300,
                "image": "images/backgrounds/bar.png",
                "description": get_location_description("bar"),
                "active": get_location_active("bar"),
                "action": "barbara_investigation",
                "warning": get_location_warning("bar"),
                "hidden": False
            },
            {
                "key": "library",
                "label": "Library",
                "xcoord": 294,
                "ycoord": 504,
                "image": "images/backgrounds/library_day.png",
                "description": get_location_description("library"),
                "active": get_location_active("library"),
                "action": "cat_investigation",
                "warning": get_location_warning("library"),
                "hidden": get_location_hidden("library")
            },
            {
                "key": "newspaper",
                "label": "Newspaper",
                "xcoord": 342,
                "ycoord": 362,
                "image": "images/backgrounds/office_interview_room.png",
                "description": get_location_description("newspaper"),
                "active": get_location_active("newspaper"),
                "action": "eddie_investigation",
                "warning": get_location_warning("newspaper"),
                "hidden": False
            },
            {
                "key": "detective",
                "label": "Detective Agency",
                "xcoord": 253,
                "ycoord": 419,
                "image": "images/backgrounds/detective_office.png",
                "description": get_location_description("detective"),
                "active": get_location_active("detective"),
                "action": "graves_investigation",
                "warning": get_location_warning("detective"),
                "hidden": get_location_hidden("detective")
            },
        ]
    
    def get_location_description(location):
        if (location == "bar"):
            if (branch == "a"):
                if (day == 1):
                    return "This bar isn’t too far from where I found the dying man last night, and they were the only place in the area that was open at night. If someone who’s working today was on shift last night, they might have heard or seen something related to the man in black."
                elif (day == 2 and person_visited("barbara", "a", 0)):
                    return "The most obvious solution is to return to Icarus and talk to Barbara. I’ll talk to her when she isn’t busy and find out my movements for the night – what I said and did the entire time I was there."
                elif (day == 2):
                    return "The most obvious solution is to return to the bar and talk to someone. I’ll be able to find out what my movements were for the night - what I said and did the entire time I was there."
                elif (day == 3):
                    return "The man with the white streak was killed fairly close to Icarus. Is there any chance that the bartender knows who he is or what he was doing in the area?"
                elif (day == 4):
                    return "Jack was found dead near the bar. It’s possible that he was a regular there and that I can find out more about him by asking."
            elif (branch == "b"):
                return "I don’t need to visit Barbara until the end of the day. She should have had enough time to review the security footage by then."
            elif (branch == "c" and day == 2 and person_visited("barbara", "a", 0)):
                return "I didn’t get anything from Barbara about Docherty, but she might still be able to help. If the man in the loud suit lives in the area, she might know of him and be able to help me."
            elif (branch == "c" and day == 2):
                return "This bar is near where the man with the white streak was killed. Whoever killed him might be making the area their killing ground. If I ask at the bar, they might recognise who he is."
            elif (branch == "c" and day == 3 and (person_visited("barbara", "a", 0) or person_visited("barbara", "c", 0))):
                return "Barbara’s workplace isn’t too far from the venue that Sergei was performing at. She might have encountered Sergei before and know about him."
            elif (branch == "c" and day == 3):
                return "This bar is near the venue that Sergei was performing at. If Sergei lived nearby then someone here might have encountered him before and know about him."
            elif (branch == "c" and day == 4 and (person_visited("barbara", "a", 0) or person_visited("barbara", "c", 0) or person_visited("barbara", "c", 1))):
                return "Barbara would have interacted with plenty of customers and gotten to know them. I’ll ask her if she’s ever met or interacted with Eisenhardt or Telemachus."
            elif (branch == "c" and day == 4):
                return "This bar might be a good place to ask about Eisenhardt and Telemachus."
            elif (branch == "d" and day == 3):
                return "Barbara already has some connections to the owners of the venue that Sergei was at. She may be able to discover whether Sergei had other associates or people that he worked with."
            elif (branch == "d" and day == 4):
                return "I can visit Barbara to check in and see how she’s doing. She would also appreciate being told that I don’t need her to find any more information."
            elif (branch == "e"):
                return "Hey hey, this is that bar where that hot bartender works! She seems pretty friendly with Lloyd – I reckon it’ll be easier than ever to get some free booze off her."
        elif (location == "library"):
            if (branch == "a"):
                if (day == 1):
                    return "I have no idea where my new abilities came from. I’m not sure how useful any books they have will be, but I can’t think of a better place to start enquiries. If I can discover more about my abilities, then I might be able to strengthen my vision of the future, and get more information about the man in black."
                elif (day == 2 and person_visited("cat", "a", 0) and check_boolean("cat_name_discovered")):
                    return "Even if Cat doesn’t know anything about my movements last night I want to go to the library. My psychic powers wiped part of my memory and if I can get access to those books then I might find a way to undo the damage."
                elif (day == 2 and person_visited("cat", "a", 0)):
                    return "Even if the librarian doesn’t know anything about my movements last night I want to go to the library. My psychic powers wiped part of my memory and if I can get access to those books then I might find a way to undo the damage."
                elif (day == 2):
                    return "I may not have any contacts here but that doesn’t justify ignoring it. My psychic powers wiped part of my memory. If I can find some books about them then I might find a way to undo the damage."
                elif (day == 3):
                    return "Cat was able to send me articles about the man in black’s first two victims. If I consult with her again she may be able to find out information about the man with the white streak."
                elif (day == 4):
                    return "I know Jack’s name now – it’s possible that the library might have some old newspapers or other records that he’s been mentioned in."
            elif (branch == "b"):
                return "I wasn’t able to acquire any of the books about psychics when I visited the library the other day. If I can borrow them then I can find something to track down others with abilities."
            elif (branch == "c" and day == 2 and person_visited("cat", "a", 0)):
                return "If I can get access to those books then I can learn more about my powers. I can understand the vision I saw and why I’m viewing a dead man kill somebody."
            elif (branch == "c" and day == 2):
                return "If I can do some research on my psychic abilities then I can learn more about my powers. I can understand the vision I saw and why I’m viewing a dead man kill somebody."
            elif (branch == "c" and day == 3):
                return "The library may have references to Sergei or his family if there’s a section on local history. Could there be something in his past that made the killer target him?"
            elif (branch == "c" and day == 4):
                return "Once the evening arrives I’ll travel here and get the remaining files from Cat. But why didn’t she give all of them to me at once?"
            elif (branch == "d" and day == 3):
                return "Although I want to look into who Jack is, I may have time to visit the library and research my psychic abilities. There are still too many unanswered questions about how I acquired them and how they function."
            elif (branch == "d" and day == 4):
                return "I should check in with Cat and see how she’s doing. I can thank her for what she has helped me with and inform her that I don’t require her assistance any more."
            elif (branch == "e" and (person_visited("cat", "a", 0) or person_visited("cat", "c", 0) or person_visited("cat", "d", 0))):
                return "There was a pretty hot chick working here when Lloyd visited. I wouldn’t normally want to be in a library, but it’s worth it to chat her up for a bit."
            elif (branch == "e"):
                return "I got a few vague flashes of Lloyd thinking about visiting here over the past few days. I dunno what for, but if he’s got a friend that works here, I can swing by and see how well I pull off the new look."
        elif (location == "newspaper"):
            if (branch == "a"):
                if (day == 1):
                    return "I know what the man in black looks like, but I don’t know anything else about him. I can’t get access to police records without looking suspicious, but I might be able to get some help with the power of the media."
                elif (day == 2 and person_visited("eddie", "a", 0)):
                    return "If I can arrange a meeting with Eddie he should be able to help me find out what happened last night. Even if it isn’t related to him he might have heard about some big news which would explain my drinking."
                elif (day == 2):
                    return "I don’t have any contacts here but I can still benefit from visiting the newspaper. I can use a reporter to research the man in black, and find out if there was any big news which would explain my drinking."
                elif (day == 3 and (person_visited("eddie", "a", 0) or person_visited("eddie", "a", 1))):
                    return "I’m unsure whether the man with the white streak’s death was reported by a newspaper. Either way Eddie should be able to dig up something about the man for me."
                elif (day == 3):
                    return "I’m unsure whether the man with the white streak’s death was reported by a newspaper. If I talk to someone there they might have information that the police released to the press."
                elif (day == 4):
                    return "Graves said that Jack had been taken to court in the past. The newspaper might have some people there who covered any trials and can provide me with more information."
            elif (branch == "b"):
                return "The newspaper will have hundreds of stories of unexplained phenomena and people with strange abilities. If I visit there I can get some names to follow up."
            elif (branch == "c" and day == 2):
                return "Eddie was angry with me last night but that may have faded by now. He could be able to help me find the man in the loud suit."
            elif (branch == "c" and day == 3):
                return "Eddie has access to all of the resources of a newspaper. If Sergei’s been a performer for years he should be able to dig something up."
            elif (branch == "c" and day == 4):
                return "Eddie’s got connections at the newspaper that I don’t have. He should be able to get me information about Eisenhardt and Telemachus."
            elif (branch == "d" and day == 3):
                return "Eddie should be able to do some research for me on Sergei. He may be able to turn up information about any associates for me."
            elif (branch == "d" and day == 4):
                return "I don’t need to visit Eddie until the end of the day. He should be available to discuss the events we experienced by then."
            elif (branch == "e"):
                return "Lloyd has a shittonne of photos on his camera. I bet I can sell them all to this newspaper, and get some nice cash for myself."
        elif (location == "detective"):
            if (branch == "a"):
                if (day == 1):
                    return "I’m trying to track down the man in black - who he is, and where he can be found. A private investigator should be able to help out with that. I’m not sure what the costs will be like, but if they don’t sound agreeable, I should be able to use my new abilities to get a bit of leverage."
                elif (day == 2 and person_visited("graves", "a", 0)):
                    return "If there’s anyone who would be able to find out what I was doing last night it would be a detective. Let’s see how good Graves is at his job."
                elif (day == 2):
                    return "If there’s anyone who would be able to find out what I was doing last night it would be a detective. I hope this one is good at his job."
                elif (day == 3 and (person_visited("graves", "a", 0) or person_visited("graves", "a", 1))):
                    return "Graves has already agreed to do some investigating for me. If I ask him to look into the man in black’s victim he’ll hopefully uncover something I can use."
                elif (day == 3):
                    return "I never ended up asking the detective here to investigate the man in black. I can ask him to discover who the man with the white streak was and what made him so significant."
                elif (day == 4):
                    return "I don’t need to visit Graves until the end of the day. He should have found out some information about Jack by then."
            elif (branch == "b" and (person_visited("graves", "a", 0) or person_visited("graves", "a", 1) or person_visited("graves", "a", 2))):
                return "Graves hasn’t been too helpful but I’m willing to bet on him for this. I trust that he’ll be able to find people with psychic abilities."
            elif (branch == "b"):
                return "Detectives often track down and find people. I’m certain that if I go here they’ll be able to find others with psychic abilities for me."
            elif (branch == "c" and day == 2 and person_visited("graves", "a", 0)):
                return "Graves was already looking into one person for me. Can he handle the pressure of looking for another?"
            elif (branch == "c" and day == 2):
                return "The man in the loud suit could be anywhere. A private investigator can narrow the search and help me find them before my vision comes true."
            elif (branch == "c" and day == 3 and (person_visited("graves", "a", 0) or person_visited("graves", "c", 0))):
                return "I know Sergei’s name and occupation now. That should be plenty for Graves to work with in uncovering his past."
            elif (branch == "c" and day == 3):
                return "A private investigator should be able to look into Sergei’s past if I give them his name and occupation. They may even be able to discover what the police know."
            elif (branch == "c" and day == 4 and (person_visited("graves", "a", 0) or person_visited("graves", "c", 0) or person_visited("graves", "c", 1))):
                return "Graves should be able to help me investigate Eisenhardt and Telemachus."
            elif (branch == "c" and day == 4):
                return "I’ve been planning to contact a private investigator for some time now. I should have the time today to do so."
            elif (branch == "d" and day == 3 and (person_visited("graves", "a", 0) or person_visited("graves", "c", 0))):
                return "I’m hoping that Graves can look into Sergei’s past and discover any associates that he had. He may be able to discover who this Jack person is."
            elif (branch == "d" and day == 3):
                return "A private investigator may be the best resource here. One may be able to discover who Jack is and how they know Sergei."
            elif (branch == "d" and day == 4):
                return "It feels like it’s been a while since I saw Graves. I should tell him that I don’t need him to investigate anything any further."
            elif (branch == "e"):
                return "Can’t believe that Lloyd went to the same guy I hired...can I trick him into giving me my money back?"
        
        return ""

    def get_location_active(location):
        if (location == "bar"):
            if (branch == "a"):
                return person_visited("barbara", "a", day - 1) == False
            elif (branch == "b"):
                return person_visited("barbara", "b", 0) == False
            elif (branch == "c"):
                return person_visited("barbara", "c", day - 2) == False
            elif (branch == "d"):
                return person_visited("barbara", "d", day - 3) == False
            elif (branch == "e"):
                return person_visited("barbara", "e", 0) == False
        elif (location == "library"):
            if (branch == "a"):
                return person_visited("cat", "a", day - 1) == False
            elif (branch == "b"):
                return person_visited("cat", "b", 0) == False
            elif (branch == "c"):
                return person_visited("cat", "c", day - 2) == False
            elif (branch == "d"):
                return person_visited("cat", "d", day - 3) == False
            elif (branch == "e"):
                return person_visited("cat", "e", 0) == False
        elif (location == "newspaper"):
            if (branch == "a"):
                return person_visited("eddie", "a", day - 1) == False
            elif (branch == "b"):
                return person_visited("eddie", "b", 0) == False
            elif (branch == "c"):
                return person_visited("eddie", "c", day - 2) == False
            elif (branch == "d"):
                return person_visited("eddie", "d", day - 3) == False
            elif (branch == "e"):
                return person_visited("eddie", "e", 0) == False
        elif (location == "detective"):
            if (branch == "a"):
                return person_visited("graves", "a", day - 1) == False
            elif (branch == "b"):
                return person_visited("graves", "b", 0) == False
            elif (branch == "c"):
                return person_visited("graves", "c", day - 2) == False
            elif (branch == "d"):
                return person_visited("graves", "d", day - 3) == False
            elif (branch == "e"):
                return person_visited("graves", "e", 0) == False

        return True

    def get_location_warning(location):
        if (day != 4):
            return False

        if (branch == "a" and location == "detective"):
            return True
        elif (branch == "b" and location == "bar"):
            return True
        elif (branch == "c" and location == "library"):
            return True
        elif (branch == "d" and location == "newspaper"):
            return True

        return False

    def get_location_hidden(location):
        if (day != 4 or branch != "d"):
            return False

        if (location == "library"):
            return not person_visited("cat", "a", 0) and not person_visited("cat", "c", 0) and not person_visited("cat", "d", 0)
        elif (location == "detective"):
            return not person_visited("graves", "a", 0) and not person_visited("graves", "c", 0) and not person_visited("graves", "d", 0)

        return False


    def visit_person(person, branch, day):
        days[branch][day].append(person)

    def person_visited(person, branch, day):
        return person in days[branch][day]

    #Classes
    class InputChecker(renpy.Displayable):
        def __init__(self, **kwargs):
            super(InputChecker, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            return renpy.Render(0, 0)

        def event(self, ev, x, y, st):
            import pygame
            if ev.type in (pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                store.current_input = "KB"
            elif ev.type in (pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION):
                store.current_input = "GP"
            return None