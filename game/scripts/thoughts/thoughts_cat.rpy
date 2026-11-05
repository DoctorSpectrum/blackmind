label mind_read_cat:
    # A-1
    if (current_thought == "cat_thought_01"):
        librarian_thoughts "I’m working right now...[wait_05]this had better be quick..."
    elif (current_thought == "cat_thought_02"):
        librarian_thoughts "Why make this my problem...?[wait_1] Look around and you’ll probably find them."
    elif (current_thought == "cat_thought_03"):
        librarian_thoughts "He shouldn’t be able to see my screen from there...[wait_1]he shouldn’t be able to see their status..."
    elif (current_thought == "cat_thought_04"):
        librarian_thoughts "Why can’t he just accept that they’re not available...[wait_1]?"
    elif (current_thought == "cat_thought_05"):
        librarian_thoughts "There...[wait_1]that should get rid of him..."
    elif (current_thought == "cat_thought_06"):
        librarian_thoughts "Why is he so insistent...?[wait_1] What does he want the books for...?"
    elif (current_thought == "cat_thought_07"):
        librarian_thoughts "He’s really starting to annoy me...[wait_1]why won’t he believe what I’m telling him?"
    elif (current_thought == "cat_thought_08"):
        librarian_thoughts "I need him to disappear before he finds out that the books aren’t here.[wait_1] He’s becoming a problem."
        $ add_boolean("cat_books_missing")
    elif (current_thought == "cat_thought_09"):
        librarian_thoughts "I’ll need to threaten him...[wait_1]if he keeps pushing this then he might make a scene."
    elif (current_thought == "cat_thought_10"):
        librarian_thoughts "This should get him to leave...[wait_1]before he finds out the truth about the books."
    elif (current_thought == "cat_thought_11"):
        librarian_thoughts "Thank goodness...[wait_1]if I’d had to explain why I needed security, they might have found out about the books."
    elif (current_thought == "cat_thought_12"):
        librarian_thoughts "Just leave...[wait_1]turn away and go..."
    elif (current_thought == "cat_thought_13"):
        librarian_thoughts "What...?[wait_1] How does he know that?[wait_1] Or...[wait_1]is he bluffing?"
    elif (current_thought == "cat_thought_14"):
        librarian_thoughts "I’ll keep intimidating him...[wait_1]have him think that his bluff failed..."
    elif (current_thought == "cat_thought_15"):
        librarian_thoughts "How should I handle this...?[wait_1] If he talks to one of them, and they check the records..."
    elif (current_thought == "cat_thought_16"):
        librarian_thoughts "If he sees one or two of them...[wait_1]it might be enough to get him to stay quiet."
    elif (current_thought == "cat_thought_17"):
        librarian_thoughts "Hopefully he’s busy...[wait_1]that will give me more time to work out what to do..."
    elif (current_thought == "cat_thought_18"):
        librarian_thoughts "He’s not giving anything away...[wait_1]Damn![wait_1] I’d better show up to be safe."
    elif (current_thought == "cat_thought_19"):
        librarian_thoughts "Please go away...[wait_1]please go away..."

    $ ignore_thoughts_length()
    return