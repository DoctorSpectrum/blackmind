label mind_read_docherty:
    if (current_thought == "docherty_thought_01"):
        man_in_black_thoughts "..."
        lloyd_thinking scared "I’m being blocked![wait_1] Somehow..."
    elif (current_thought == "docherty_thought_02"):
        docherty_thoughts "..."
        lloyd_thinking scared "I can’t read his mind![wait_1] But that means..."

    $ ignore_thoughts_length()
    return