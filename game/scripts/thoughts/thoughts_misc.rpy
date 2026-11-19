label mind_read_docherty:
    if (current_thought == "docherty_thought_01"):
        man_in_black_thoughts "..."
        lloyd_thinking scared "I’m being blocked![wait_1] Somehow..."
    elif (current_thought == "docherty_thought_02"):
        docherty_thoughts "..."
        lloyd_thinking scared "I can’t read his mind![wait_1] But that means..."
    elif (current_thought == "docherty_thought_03"):
        docherty_thoughts "{size=-8}Pain...[wait_1]hurts...[wait_1]to breathe...{/size}"

    $ ignore_thoughts_length()
    return

label mind_read_jack:
    if (current_thought == "jack_thought_01"):
        lloyd_thinking "...It doesn’t look like I can read his mind."
    elif (current_thought == "jack_thought_02"):
        unknown_thoughts "What I really hope...[wait_05]is that you enjoy the surprise."
        $ add_boolean("ending_g_unlocked")

    $ ignore_thoughts_length()
    return

label mind_read_killian:
    if (current_thought == "killian_thought_01"):
        killian_thoughts "..."
        jack_possessing_thinking worried "Nope, that won’t work."
    elif (current_thought == "killian_thought_02"):
        killian_thoughts "..."
        lloyd_ws_thinking neutral "No...[wait_05]I can’t read his mind."
    elif (current_thought == "killian_thought_03"):
        killian_thoughts "I didn’t feel him in my mind![wait_1] How did he –[wait_05] no, he’s reading my thoughts now!" 
        killian_thoughts "GET OUT!"
        $ current_thought = "killian_thought_01"
    elif (current_thought == "killian_thought_04"):
        killian_thoughts "..."
    elif (current_thought == "killian_thought_05"):
        killian_thoughts "Who is this person?[wait_1] What is he doing here?"
    elif (current_thought == "killian_thought_06"):
        killian_thoughts "I have to assume that he doesn’t know about my powers...[wait_05]how did I meet this man?"
    elif (current_thought == "killian_thought_07"):
        killian_thoughts "Does he know about my powers?"
    elif (current_thought == "killian_thought_08"):
        lloyd_ws_thinking "No.[wait_1] I’m not going to read his mind.[wait_1] I don’t want to betray his trust."
    elif (current_thought == "killian_thought_09"):
        killian_thoughts "Now now, Lloyd, you shouldn’t go peeking in here.[wait_1] You wouldn’t want to spoil the surprise, would you?"

    $ ignore_thoughts_length()
    return

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