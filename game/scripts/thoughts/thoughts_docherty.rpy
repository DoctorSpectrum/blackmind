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

label mind_read_killian:
    if (current_thought == "killian_thought_01"):
        killian_thoughts "..."
        jack_possessing_thinking worried "Nope, that won’t work."

    $ ignore_thoughts_length()
    return