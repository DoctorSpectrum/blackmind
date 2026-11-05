label mind_read_graves:
    # A-1
    if (current_thought == "graves_thought_01"):
        detective_thoughts "Thank goodness he did come up...[wait_05]I’ve been itching to start a new case ever since the previous one finished."
        $ add_boolean("graves_no_cases")
    elif (current_thought == "graves_thought_02"):
        detective_thoughts "He’s not too bad-looking...[wait_05]he seems to be in fairly good shape, if nothing else."
    elif (current_thought == "graves_thought_03"):
        detective_thoughts "He’s probably expecting a grizzled, hard-boiled detective – I’ll try to meet his expectations."
    elif (current_thought == "graves_thought_04"):
        graves_thoughts "One is more than most people have to."
    elif (current_thought == "graves_thought_05"):
        graves_thoughts "He’s very quiet – better try and get him a bit more relaxed! I don’t want him thinking that I’m {i}too{/i} grizzled!"
    elif (current_thought == "graves_thought_06"):
        graves_thoughts "C’mon, mate, at least try and stick with it!"
    elif (current_thought == "graves_thought_07"):
        graves_thoughts "Hopefully this is interesting.[wait_1] Let’s see what he’s got for me."
    elif (current_thought == "graves_thought_08"):
        graves_thoughts "What’s his relationship with this person, I wonder?[wait_1] A distant relative?[wait_1] An old lover?"
    elif (current_thought == "graves_thought_09"):
        graves_thoughts "Better sort this out quickly – I don’t want to wind up helping with something illegal."
    elif (current_thought == "graves_thought_10"):
        graves_thoughts "Very evasive...[wait_05]let’s see where exactly he’s going with this."
    elif (current_thought == "graves_thought_11"):
        graves_thoughts "If he gives me more information then I’ll be able to actually answer that..."
    elif (current_thought == "graves_thought_12"):
        graves_thoughts "He’s got to have a name, right?"
    elif (current_thought == "graves_thought_13"):
        graves_thoughts "Okay, that’s very interesting.[wait_1] If I knew this person’s name, and looked them up, I wonder what I’d find?"
    elif (current_thought == "graves_thought_14"):
        graves_thoughts "I might be able to do a reverse image search...[wait_1]I’m really damn curious about who this person is, now."
    elif (current_thought == "graves_thought_15"):
        graves_thoughts "At least when Usbourne hired us, he gave us a name."
    elif (current_thought == "graves_thought_16"):
        graves_thoughts "I guess this does make sense...[wait_05]but I’m still not sure why he wants me to find this guy."
    elif (current_thought == "graves_thought_17"):
        graves_thoughts "I’ll probably need a few days, so I’ll start by tempering his expectations a bit."
    elif (current_thought == "graves_thought_18"):
        graves_thoughts "What {i}is{/i} this guy’s relationship?[wait_1] Is he a spy trying to catch a terrorist?[wait_1] A gangster trying to find someone who squealed?"
    elif (current_thought == "graves_thought_19"):
        graves_thoughts "He’ll just have to wait for a bit.[wait_1] He’ll have to be patient, like everybody else."
    elif (current_thought == "graves_thought_20"):
        graves_thoughts "Shit, what does he –[wait_05] how does he know that?![wait_1] What did I say to him earlier?"
    elif (current_thought == "graves_thought_21"):
        graves_thoughts "I should just bluff and tell him he’s wrong, but –[wait_05] no, he’d be able to tell that it’s a lie.[wait_1] I reacted too strongly."
    elif (current_thought == "graves_thought_22"):
        graves_thoughts "Nothing to do now but tell the truth...[wait_05]well, most of it, at least."
    elif (current_thought == "graves_thought_23"):
        graves_thoughts "At least this doesn’t change any of my current plans."
    elif (current_thought == "graves_thought_24"):
        graves_thoughts "Not that I’m expecting them to be much, but if I can show him that I’ve started, that’ll hopefully give him some confidence in me."
    

    $ ignore_thoughts_length()
    return