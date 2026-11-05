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

    $ ignore_thoughts_length()
    return