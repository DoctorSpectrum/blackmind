label mind_read_sergei:
    if (current_thought == "sergei_thought_01"):
        if (not check_boolean("sergei_mind_read")):
            sergei_thoughts "..."
            lloyd_narrating neutral "I reach out to try and read his thoughts but something stops me."
            lloyd_narrating neutral "It’s as though a wall has appeared before a car that I’m driving at top speed.[wait_1] My head aches badly, but I still manage to catch Sergei’s whisper."
            sergei "{size=-8}Then you must be the other one.[wait_1] We should talk after the show.{/size}"
            $ add_boolean("sergei_mind_read")
        else:
            lloyd_thinking thinking "My head is still aching from that initial attempt.[wait_1] I should talk to Sergei after the show, as he said."
        

    $ ignore_thoughts_length()
    
    return