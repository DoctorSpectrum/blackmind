label mind_read_eddie:
    if (current_thought == "eddie_thought_01"):
        employee_thoughts "Hope this is something good –[wait_05] I need a –"
    elif (current_thought == "eddie_thought_02"):
        employee_thoughts "I should have recognised that stupid coat of his that he wears everywhere.[wait_1] The hell is he doing here?"
    elif (current_thought == "eddie_thought_03"):
        employee_thoughts "He has to be fucking joking.[wait_1] He has to be."
    elif (current_thought == "eddie_thought_04"):
        employee_thoughts "I think he’s serious.[wait_1] I think he actually doesn’t know who I fucking am."
    elif (current_thought == "eddie_thought_05"):
        employee_thoughts "Years, he spent, fucking me over, and he doesn’t even remember who I am.[wait_1] Unbe-fucking-lievable."
    elif (current_thought == "eddie_thought_06"):
        employee_thoughts "Typical Chen.[wait_1] Too far up his own ass to care about anyone else."
    elif (current_thought == "eddie_thought_07"):
        employee_thoughts "No apology, no nothing.[wait_1] All he cares about is his own shit."
    elif (current_thought == "eddie_thought_08"):
        employee_thoughts "Tell me, so that I can throw it back in your face."
    elif (current_thought == "eddie_thought_09"):
        employee_thoughts "Interesting that he knows all of this...I wonder what he’s not telling me."
    elif (current_thought == "eddie_thought_10"):
        employee_thoughts "Better act like I don’t care.[wait_1] He can’t know my intentions."
        $ add_boolean("eddie_pretend_indifference")
    elif (current_thought == "eddie_thought_11"):
        employee_thoughts "Yeah, that’s right, motherfucker.[wait_1] Squirm."
    elif (current_thought == "eddie_thought_12"):
        employee_thoughts "I bet he’ll still forget all about me the second he leaves the building."
    elif (current_thought == "eddie_thought_13"):
        eddie_thoughts "This guy’s a fucking joke."
    elif (current_thought == "eddie_thought_14"):
        eddie_thoughts "As if I’d tell you."
    elif (current_thought == "eddie_thought_15"):
        eddie_thoughts "Oh, please – this is how you try and win me over to your side?[wait_1] Act like we’re friends now and that we don’t have a history together?"
    elif (current_thought == "eddie_thought_16"):
        eddie_thoughts "If you’re going to be a dick, at least be honest about it."
    elif (current_thought == "eddie_thought_17"):
        eddie_thoughts "Sure, just gaslight me, why don’t you?"
    elif (current_thought == "eddie_thought_18"):
        eddie_thoughts "Fuck you, Chen."
    elif (current_thought == "eddie_thought_19"):
        eddie_thoughts "Revenge is a dish best served cold."
    elif (current_thought == "eddie_thought_20"):
        eddie_thoughts "...Alright, he has a point on the assignment."
    elif (current_thought == "eddie_thought_21"):
        eddie_thoughts "I guess if he was coming here with a story, I should listen to see if it’s any good."
    elif (current_thought == "eddie_thought_22"):
        eddie_thoughts "Interesting that he knows all of this...[wait_1]I wonder what he’s not telling me." 
    elif (current_thought == "eddie_thought_23"):
        eddie_thoughts "How does he know all of this?[wait_1] I need answers."
    elif (current_thought == "eddie_thought_24"):
        eddie_thoughts "Convenient, convenient...[wait_1]what are you hiding from me, Chen?"
    elif (current_thought == "eddie_thought_25"):
        eddie_thoughts "C’mon...[wait_05]just admit who they are."
    elif (current_thought == "eddie_thought_26"):
        eddie_thoughts "What I’m really interested in is how he knows all of this...[wait_1]is it worth doing what he suggests to earn his trust?"
    elif (current_thought == "eddie_thought_27"):
        eddie_thoughts "I don’t want to stay back too late but if it gets him out of my hair, it’s worth it."
    elif (current_thought == "eddie_thought_28"):
        eddie_thoughts "Oh, sure, get me to do the legwork then don’t even bother to hear what I’ve got to say."
    elif (current_thought == "eddie_thought_29"):
        eddie_thoughts "Joke’s on him – I’m the one with the job.[wait_1] I’m the better photographer."
    elif (current_thought == "eddie_thought_30"):
        eddie_thoughts "He probably won’t bother coming tonight, the bum."

    $ ignore_thoughts_length()
    return