init python:
    # Future Sight
    def get_future_sight_info(id=None):
        global day, branch, person
        information = [{
                "person": None,
                "branch": None,
                "day": None,
                "picture": "jack_smug.png",
                "title": "UNKNOWN",
                "description": "Unknown future vision; please report this bug!",
                "current": [],
                "general": []
            }, {
                "person": "barbara_prologue",
                "branch": None,
                "day": 0,
                "picture": "barbara_smiling.png",
                "title": "BARTENDER",
                "description": "Jack is trying to get a free drink from the bartender",
                "current": [
                    {
                        "keyword": "ALCOHOL",
                        "discovered": check_boolean("prologue_bar_interested")
                    }
                ],
                "general": []
            }, {
                "person": "barbara_prologue_02",
                "branch": None,
                "day": 0,
                "picture": "barbara_smiling.png",
                "title": "BARTENDER",
                "description": "Jack is trying to get a free drink from the bartender",
                "current": [
                    {
                        "keyword": "EMPLOYER",
                        "discovered": check_boolean("prologue_bar_history")
                    },
                    {
                        "keyword": "IMPROVEMENTS",
                        "discovered": check_boolean("prologue_drink_policies")
                    },
                    {
                        "keyword": "CHEAPER",
                        "discovered": check_boolean("prologue_drink_discounts")
                    },
                    {
                        "keyword": "INCORRECT",
                        "discovered": check_boolean("prologue_drink_review")
                    }
                ],
                "general": [{
                        "keyword": "LEGACY",
                        "discovered": check_boolean("prologue_barbara_history_1")
                    },
                    {
                        "keyword": "QUALITY",
                        "discovered": check_boolean("prologue_barbara_history_2")
                    },
                ]
            }, {
                "person": "docherty_prologue",
                "branch": None,
                "day": 0,
                "picture": "docherty_neutral.png",
                "title": "???",
                "description": "",
                "current": [],
                "general": []
            }]

        if (id is not None):
            return information[id]

        for info in information:
            if (info["person"] == person and info["branch"] == branch and info["day"] == day):
                return info

        return information[0]

    def get_future_sight_history(id=None, person=None):
        history_list = [{
            "person": None,
            "history": [
                {
                    "history": "Error loading character's history",
                    "unlocked": True
                }
            ]
        }, {
            "person": "barbara_prologue_02",
            "history": [
                {
                    "history": "The bar has been in the bartender's family for three generations. Profitability has been down lately.",
                    "unlocked": check_boolean("prologue_barbara_history_1")
                },
                {
                    "history": "The bartender has attended business school.",
                    "unlocked": check_boolean("prologue_barbara_history_2")
                }
            ]
        }, {
            "person": "docherty_prologue",
            "history": []
        }]

        if (id is not None):
            return construct_history(history_list[id])

        for history in history_list:
            if (history["person"] == person):
                return construct_history(history)
        
        return construct_history(history_list[0])

    def construct_history(history):
        history_string = ""
        for h in history["history"]:
            if h["unlocked"] == True:
                history_string += h["history"] + "\r\n\r\n"

        return history_string if len(history_string) > 0 else "You have not discovered anything about this character yet."

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