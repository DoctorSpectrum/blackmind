label barbara_investigation:
    $ current_thought_block = "mind_read_barbara"
    if (branch == "a"):
        if (day == 1):
            jump barbara_a_1
        elif (day == 2):
            jump barbara_a_2
        elif (day == 3):
            jump barbara_a_3
        elif (day == 4):
            jump barbara_a_4
    
    return

label barbara_a_1:
    scene black_bg with quick_dissolve
    #sfx of train noises
    lloyd_narrating neutral "The bar I’ve identified is called Icarus."
    lloyd_narrating neutral "The easiest way to get to it is by heading downwards below the streets, then taking a train across the city to a nearby station."
    lloyd_narrating neutral "From there, it’s just a short walk through a few streets, and then I’m at the door."
    lloyd_narrating neutral "I’m sure that any drunks appreciate the proximity to the station and how much easier that makes returning home at night."
    #sfx of creaking door
    lloyd_narrating thinking "I wasn’t expecting too much at this hour – maybe a contact number for the owner, something that I couldn’t find online – but to my surprise, the door gently creaks open when I knock on it."
    lloyd_narrating thinking "A forgetful owner?[wait_1] Or a sign of a break-in?"
    lloyd_narrating thinking "I slowly enter the building and make my way in, trying not to make too much noise."
    scene bar with slow_dissolve
    lloyd_narrating neutral "It’s rare for me to drink, but I can’t say that this would be a bad place to do it in."
    lloyd_narrating neutral "The atmosphere seems pleasant enough, and they look to have a good variety of drinks on the shelves."
    lloyd_narrating neutral "There are no immediate signs of a break-in, or anything else illegal having happened, so I let myself relax a little."
    lloyd_narrating neutral "Just as I do so, a door swings open."
    $ swap_sprites("barbara_thinking", slow_dissolve)
    $ current_thought = "barbara_thought_01"
    show screen psychic_powers
    bartender "Um...[wait_05]hello.[wait_1] Are you –[wait_05] can I help you?"
    lloyd_narrating neutral "She looks to be about my age.[wait_1] She’s holding a screwdriver in one hand, and despite her obvious surprise, is holding herself casually enough."
    lloyd_narrating neutral "I haven’t considered how I’d like to play this interaction, but I quickly decide to go with friendly and honest.[wait_1] She shouldn’t have any reason to be hostile."
    $ current_thought = "barbara_thought_02"
    lloyd friendly "Good day.[wait_1] The name’s Lloyd.[wait_1] Do you have the time to answer a few questions?"
    $ current_thought = "barbara_thought_03"
    bartender "Hey, I’m Barbara.[wait_1] I should have a bit of time, but can I ask what this is about?[wait_1] Are you a reporter?"
    lloyd neutral "What makes you think that?"
    barbara "Well, the camera’s a bit of a giveaway."
    $ current_thought = "barbara_thought_04"
    lloyd neutral "Ah, that.[wait_1] I’m...[wait_05]not a reporter, no."
    lloyd_thinking neutral "I’d better change the topic.[wait_1] There’s no easy way to describe what I’m doing."
    $ current_thought = "barbara_thought_05"
    lloyd neutral "I’m surprised that you’re open at this hour –[wait_05] I was under the impression that the drinks didn’t start flowing until the evening."
    $ current_thought = "barbara_thought_06"
    barbara "Oh, they don’t –[wait_05] but I’ve got a few things to deal with after an incident last night."
    $ current_thought = "barbara_thought_07"
    barbara "You probably came in because the door was unlocked, right?[wait_1] I’m heading in and out a bit at the moment; it’s easier to keep it that way rather than constantly fumbling for keys."
    lloyd_thinking thinking "An incident last night?[wait_1] That could be related to the man in black...[wait_05]I should investigate this further."
    menu:
        "What was the incident?":
            $ current_thought = "barbara_thought_08"
            lloyd neutral "Could I ask you to clarify what you mean by an incident last night?"
            $ swap_sprites("barbara_angry")
            barbara "It’s nothing that you need to concern yourself with.[wait_1] Just usual bar stuff."
            $ swap_sprites("barbara_smiling")
        "Ask about the door" (locked=not check_boolean("barbara_broken_door"), message="You have not read the related thought"):
            lloyd_thinking thinking "If there’s a broken door, that could be indicative of someone breaking in.[wait_1] I’d better handle this carefully."
            $ current_thought = "barbara_thought_09"
            lloyd friendly "An incident last night, huh?[wait_1] I hope that you’re alright now!"
            barbara "Oh, of course![wait_1] It’s nothing too serious - just that I got a report from a patron that the door to one of the bathroom stalls was a bit unstable, so I’m going to replace the hinges."
            lloyd_thinking neutral "Alright, it’s not related to the man in black then.[wait_1] At least I solved the mystery."
    $ current_thought = "barbara_thought_10"
    barbara "Anyway, you said something about wanting me to answer a few questions?[wait_1] What exactly do you need from me?"
    $ current_thought = "barbara_thought_11"
    lloyd neutral "I’m currently trying to find a certain person."
    lloyd neutral "I don’t know where they are at present, but they were in this area last night."
    lloyd neutral "I was hoping to find out whether you or any of your staff had heard or seen anything that could help me."
    $ swap_sprites("barbara_thinking")
    barbara "That depends.[wait_1] Do you know this person’s name?[wait_1] Do you have a photo of them?"
    $ current_thought = "barbara_thought_12"
    lloyd neutral "Not exactly."
    lloyd_narrating neutral "I describe the man to Barbara as best as I can."
    lloyd_narrating neutral "Even though it’s been hours since I had the vision, I can still picture the man in black perfectly."
    lloyd_narrating neutral "His features – and what little I could make out of the scene – have been burned into my mind with perfect clarity.[wait_1] I couldn’t forget a detail if I tried."
    lloyd_narrating neutral "Her response isn’t overly positive, however."
    barbara "Sorry...[wait_05]I don’t think that I’ve seen anybody that matches that description."
    barbara "I was in the bar for –[wait_05] most evenings I’m working here, so unless he dropped by, I wouldn’t have run into him."
    lloyd_thinking thinking "That’s not overly helpful, but it does give me a little to work with."
    lloyd_thinking thinking "The man in black isn’t a patron of this bar –[wait_05] it could mean that he’s not from the area."
    lloyd_thinking thinking "It would be good to get confirmation of that fact."
    $ current_thought = "barbara_thought_13"
    lloyd neutral "Thanks anyway."
    lloyd neutral "Do you know any of the other shop owners around here?[wait_1] Could you ask them if they remember him?"
    $ swap_sprites("barbara_angry")
    barbara "I know them, sure, but I can’t afford to just go around and pester them."
    barbara "I’ve got work to do, buddy![wait_1] If you want their information, then you can go ask them yourself!"

    if (len(days["a"][0]) >= 1):
        lloyd_thinking neutral "I might be able to tomorrow, but I definitely don’t have any more time today."
    else:
        lloyd_thinking neutral "I’ve got much more promising places on my list – I need to prioritise visiting them."
    
    lloyd_thinking neutral "It would be much more convenient if Barbara spoke to the other shopowners for me."

    menu:
        "I don't have the time to talk to them":
            $ current_thought = "barbara_thought_14"
            lloyd neutral "I don’t have the time to talk to them today.[wait_1] Are you certain that you can’t work something out?"
            $ swap_sprites("barbara_smiling")
            barbara "I...[wait_1]look, I might be able to do something."
            barbara "I’m not sure, it’ll depend upon how long my tasks today take.[wait_1] I {i}have{/i} to prioritise them."
            lloyd_thinking thinking "That’s not what I wanted to hear.[wait_1] But I don’t know what else I could say to convince her."
            lloyd neutral "If you do get the opportunity, please do.[wait_1] It would really be appreciated."
        "They might respond better to a member of the community" (locked=not check_boolean("barbara_family_community"), message="You have not read the related thought"):
            lloyd_thinking thinking "Barbara seemed fairly proud of her family’s history in the area."
            lloyd_thinking thinking "If I appeal to that, her pride might not let her ignore it."
            $ current_thought = "barbara_thought_15"
            lloyd friendly "Oh, sorry.[wait_1] I just thought that they would be a bit more willing to divulge information to someone who’s already a part of the community."
            $ swap_sprites("barbara_smiling")
            barbara "Well, if nothing else, it would sound better if somebody they knew asked them whether they’d seen this guy, yeah."
            $ current_thought = "barbara_thought_16"
            lloyd neutral "So they’d mostly help you out just because you know them, then?"
            $ swap_sprites("barbara_angry")
            barbara "Of course not![wait_1] I’ve been a –[wait_05] my family’s been in these parts for decades now!"
            barbara "They’d help me out because this community supports one another!"
            $ current_thought = "barbara_thought_17"
            lloyd neutral "Are you certain?"
            barbara "I’ll prove it –[wait_1] I’ll ask around right away, and see if anyone’s heard anything about this guy you’re looking for!"
            barbara "Whatever information people have, I’ll find it out!"
            $ add_boolean("barbara_convinced_investigate")
    
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_18"
    barbara "What’s so important about this guy, anyway?[wait_1] Does he owe you money or something?"
    lloyd_thinking thinking "Is there anything that I could tell her that would show her the importance of finding the man in black?"
    lloyd_thinking thinking "If I tell her that he’s going to commit a murder, she might get scared off."
    $ current_thought = "barbara_thought_19"
    lloyd neutral "It’s...[wait_05]important.[wait_1] I can’t go into details, sorry."
    $ swap_sprites("barbara_angry")
    barbara "Right."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_20"
    barbara "Anyway, if you want to come over later tonight, I might have something for you by then."
    barbara "And if you can’t make it, feel free to come over any time during the next few days and ring the doorbell."
    $ current_thought = "barbara_thought_21"
    lloyd neutral "You’ll be here during the day then, too?"
    barbara "There’s always work to be done – marketing, restocking, paperwork...[wait_05]If I didn’t get it done during the day, I sure as heck wouldn’t have the time to do it in the evenings!"
    $ current_thought = "barbara_thought_22"
    lloyd friendly "Understood.[wait_1] Thank you for your assistance, Barbara – it’s appreciated."
    barbara "No prob![wait_1] Good luck finding this guy!"
    hide barbara_smiling with quick_dissolve
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I say my goodbyes and leave the bar."
    lloyd_narrating neutral "It wasn’t anything particularly concrete, but I know that the man in black was in this area last night."
    lloyd_narrating neutral "One of Barbara’s neighbours might have seen or heard something...[wait_05]but is returning here tonight the best use of my time?"
    
    $ visit_person("barbara", "a", 0)
    return

label barbara_a_2:
    $ visit_person("barbara", "a", 1)
    return

label barbara_a_3:
    $ visit_person("barbara", "a", 2)
    return

label barbara_a_4:
    $ visit_person("barbara", "a", 3)
    return 