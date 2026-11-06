label mind_read_barbara:
    # A-1
    if (current_thought == "barbara_thought_01"):
        bartender_thoughts "Whoa, who sent this hottie here?![wait_1] If he’s looking for a drink, I’d be more than happy to help him!"
    elif (current_thought == "barbara_thought_02"):
        bartender_thoughts "Is he a cop?[wait_1] He’s dressed pretty casually for –[wait_05] oh, wait, I get it."
    elif (current_thought == "barbara_thought_03"):
        bartender_thoughts "Is he here to do a story on the bar?[wait_1] Or – shit, was that drunk guy last night legitimate?[wait_1] Did he really want to write up a review?"
    elif (current_thought == "barbara_thought_04"):
        barbara_thoughts "Does he consider being a reviewer and a reporter different jobs?[wait_1] Or...[wait_05]is he here for some other reason?"
    elif (current_thought == "barbara_thought_05"):
        barbara_thoughts "Did he just dodge the question?[wait_1] What’s he here for?"
    elif (current_thought == "barbara_thought_06"):
        barbara_thoughts "And I’d better wrap this up quickly, so that I can get back to it - that door won’t fix itself!"
        $ add_boolean("barbara_broken_door")
    elif (current_thought == "barbara_thought_07"):
        barbara_thoughts "If people can get in so quietly, though, maybe that’s a sign that I should start locking it."
    elif (current_thought == "barbara_thought_08"):
        barbara_thoughts "Sheesh, talk about nosy!"
    elif (current_thought == "barbara_thought_09"):
        barbara_thoughts "Oh, he probably thought that it was a bar fight, or something like that.[wait_1] He’s jumping to the wrong conclusion, but it’s kind of cute that he’s thinking of my safety!"
    elif (current_thought == "barbara_thought_10"):
        barbara_thoughts "Let’s see if I can get him back on topic...[wait_1]there’s something suspicious about this guy."
    elif (current_thought == "barbara_thought_11"):
        barbara_thoughts "Okay, he’s definitely a cop.[wait_1] Undercover, but not doing a very good job of it."
    elif (current_thought == "barbara_thought_12"):
        barbara_thoughts "He’s a newbie, I’m guessing?[wait_1] It’s probably his first day on the job."
    elif (current_thought == "barbara_thought_13"):
        barbara_thoughts "Of course I know the other shop owners –[wait_05] my family’s been a part of the community for decades!"
        $ add_boolean("barbara_family_community")
    elif (current_thought == "barbara_thought_14"):
        barbara_thoughts "I guess I can try and help him...[wait_05]but I probably won’t actually be able to ask around for a day or two.[wait_1] There’s just too much I have to work on here."
    elif (current_thought == "barbara_thought_15"):
        barbara_thoughts "They probably wouldn’t normally say too much, but to a guy this good-looking?[wait_1] They’d probably make an exception."
    elif (current_thought == "barbara_thought_16"):
        barbara_thoughts "They –[wait_05] I hope that it’s more than that...[wait_05]that they respect me for who I am, and how I’ve been running things.[wait_1] That it’s not just my family name."
    elif (current_thought == "barbara_thought_17"):
        barbara_thoughts "This could be a good test, actually, to see how much the other shop owners respect me."
        barbara_thoughts "Do they appreciate what I’ve been trying to do, or have they just been polite to me so far because of my family?"
    elif (current_thought == "barbara_thought_18"):
        barbara_thoughts "Before I get too far into this, I should try and work out what this guy’s deal is, anyway."
    elif (current_thought == "barbara_thought_19"):
        barbara_thoughts "So...[wait_05]he wants my information, and my connections, but he doesn’t trust me enough to tell me what’s up.[wait_1] Brilliant."
    elif (current_thought == "barbara_thought_20"):
        barbara_thoughts "I guess that I’ll still help him out, though...[wait_1]I would like to get to know him a bit better."
    elif (current_thought == "barbara_thought_21"):
        barbara_thoughts "Running a bar involves a lot more than just pouring drinks, buddy!"
    elif (current_thought == "barbara_thought_22"):
        barbara_thoughts "He seems pretty nice...[wait_05]but I’m a little wary of his interest in this mysterious man.[wait_1] I hope he’s on the up-and-up."

    # A-1-4
    elif (current_thought == "barbara_thought_23"):
        barbara_thoughts "Oh, the hottie is back!"
    elif (current_thought == "barbara_thought_24"):
        barbara_thoughts "Crap, how could I forget his name already?[wait_1] Wait...[wait_05]no, I think that’s it!"
    elif (current_thought == "barbara_thought_25"):
        barbara_thoughts "Phew!"
    elif (current_thought == "barbara_thought_26"):
        barbara_thoughts "I’ve got to get rid of this damn stock![wait_1] He’d like a beer, right?"
    elif (current_thought == "barbara_thought_27"):
        barbara_thoughts "Ah, of course...[wait_05]I should have seen that coming." 
    elif (current_thought == "barbara_thought_28"):
        barbara_thoughts "I’m kind of relieved that none of them knew anything –[wait_05] his interest in this guy is still a little suspicious."
    elif (current_thought == "barbara_thought_29"):
        barbara_thoughts "Hopefully he gets the hint that I’m not his PA."
    elif (current_thought == "barbara_thought_30"):
        barbara_thoughts "He’s still happy to spend a bit of money and chat, right?"
    elif (current_thought == "barbara_thought_31"):
        barbara_thoughts "Damn...[wait_05]I was hoping that we could have a bit more of a casual conversation."
        barbara_thoughts "And maybe I could find out a bit more about what his connection with this guy is..."
    elif (current_thought == "barbara_thought_32"):
        barbara_thoughts "That has to be, what, the fourth in the last hour?" 
        barbara_thoughts "He’s been holding them well enough, but why is he drinking so much?"
    elif (current_thought == "barbara_thought_33"):
        barbara_thoughts "He’s been holding his drinks fine before now.[wait_1] Why is he pretending to be drunk?"
    elif (current_thought == "barbara_thought_34"):
        bartender_thoughts "That has to be, what, the fourth in the last hour?" 
        bartender_thoughts "He’s been holding them well enough, but why is he drinking so much?"
    elif (current_thought == "barbara_thought_35"):
        bartender_thoughts "He’s been holding his drinks fine before now.[wait_1] Why is he pretending to be drunk?"
    elif (current_thought == "barbara_thought_36"):
        barbara_thoughts "Wait...[wait_05]is he actually drunk?[wait_1] Was he just faking his sobriety really well before?"
    elif (current_thought == "barbara_thought_37"):
        barbara_thoughts "He’s changed completely.[wait_1] This is weird."
    elif (current_thought == "barbara_thought_38"):
        bartender_thoughts "Wait...[wait_05]is he actually drunk?[wait_1] Was he just faking his sobriety really well before?"
    elif (current_thought == "barbara_thought_39"):
        bartender_thoughts "He’s changed completely.[wait_1] This is weird."

    # A-2
    elif (current_thought == "barbara_thought_40"):
        if (person_visited("barbara", "a", 0)):
            barbara_thoughts "Is he hung over?[wait_1] I’m still not sure whether he was pretending to be drunk or not last night."
        else:
            bartender_thoughts "Is he hung over?[wait_1] I’m still not sure whether he was pretending to be drunk or not last night."
    elif (current_thought == "barbara_thought_41"):
        barbara_thoughts "I feel like I’m going to regret this."
    elif (current_thought == "barbara_thought_42"):
        bartender_thoughts "I feel like I’m going to regret this."
    elif (current_thought == "barbara_thought_43"):
        barbara_thoughts "Busy enough that I’ll kick you out if this isn’t worth my time."
    elif (current_thought == "barbara_thought_44"):
        barbara_thoughts "So he wasn’t faking his drunkenness?"
    elif (current_thought == "barbara_thought_45"):
        barbara_thoughts "I wouldn’t mind it so much if he was drunk in certain circumstances.[wait_1] Like, say, during a private evening?"
    elif (current_thought == "barbara_thought_46"):
        barbara_thoughts "Not that I can do much beyond banning him from the bar."
    elif (current_thought == "barbara_thought_47"):
        barbara_thoughts "What could I help him with?[wait_1] Does he want my number?"
    elif (current_thought == "barbara_thought_48"):
        barbara_thoughts "That doesn’t sound like he wants my number...[wait_05]damn."
    elif (current_thought == "barbara_thought_49"):
        barbara_thoughts "Weird question to ask.[wait_1] Why wouldn’t you know this?"
    elif (current_thought == "barbara_thought_50"):
        barbara_thoughts "I guess he seemed kind of smug, but I assume that was the alcohol in his system."
    elif (current_thought == "barbara_thought_51"):
        barbara_thoughts "Some of the things he said were –[wait_05] he probably doesn’t want to know how he was acting.[wait_1] I’ll downplay it a bit."
    elif (current_thought == "barbara_thought_52"):
        barbara_thoughts "It sounds like he’s trying to trace his steps for the night.[wait_1] Was he out somewhere before he came here, and was directed here?"
    elif (current_thought == "barbara_thought_53"):
        barbara_thoughts "Why do I have to keep telling people not to do that?!"
    elif (current_thought == "barbara_thought_54"):
        barbara_thoughts "Okay, he’s a keeper."
    elif (current_thought == "barbara_thought_55"):
        barbara_thoughts "He’s just staring off into the distance...[wait_05]I think that he’s forgotten I’m here."
    elif (current_thought == "barbara_thought_56"):
        barbara_thoughts "I have to seize this opportunity while I can![wait_1] It might never come again!"
    

    $ ignore_thoughts_length()
    return