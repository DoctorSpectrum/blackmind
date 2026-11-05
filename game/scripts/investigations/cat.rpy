label cat_investigation:
    $ current_thought_block = "mind_read_cat"
    if (branch == "a"):
        if (day == 1):
            jump cat_a_1
        elif (day == 2):
            jump cat_a_2
        elif (day == 3):
            jump cat_a_3
        elif (day == 4):
            jump cat_a_4
    
    return

label cat_a_1:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "The power to delve into peoples’ minds and see the future."
    lloyd_narrating neutral "Those are the abilities that I’ve somehow been gifted."
    lloyd_narrating neutral "I know too little about them.[wait_1] There are still too many unanswered questions, and I need to discover the answers."
    lloyd_narrating neutral "So where’s the best place to find answers?[wait_1] A library."
    lloyd_narrating neutral "I travel southwards through the city, passing into an area that’s more verdant and green than the rest."
    lloyd_narrating neutral "The library is in the middle of a park, with large trees providing abundant shade throughout it."
    lloyd_narrating neutral "The weather is warm and gentle, making for a relaxing journey through the park."
    lloyd_narrating neutral "The library itself is a modern building of glass and concrete; a sturdy fortress that’s more than sufficient to protect its fragile contents."
    # SFX of a camera shutter
    lloyd_narrating neutral "I take out my camera and snap a few shots of it; it’s too picturesque to pass up the opportunity."
    lloyd_narrating neutral "Then I enter its thick walls, hoping that within is the information that I need."
    scene library_day with slow_dissolve
    lloyd_narrating neutral "It’s been several years since I was last in a library."
    lloyd_narrating neutral "The atmosphere takes me back to studying photography in university – the correlation between the camera’s aperture and depth of field; learning how to use bracketing; about what aperture type works best for which photo orientation."
    lloyd_narrating neutral "The library feels welcoming despite my relapse, and I feel regret that it’s been so long.[wait_1] As long as I’m between jobs there’s little reason not to visit more often."
    lloyd_narrating neutral "I walk over to the shelves where the books I’m seeking should be.[wait_1] The library’s online catalogue was promising – there were books about psychic research the CIA and Soviets were conducting in the 1960s, new age books about opening up your mind, records of unexplained phenomena, and more."
    lloyd_narrating neutral "It may all be fiction and unrelated to my powers, but it’s a place to start."
    lloyd_narrating neutral "That’s the plan.[wait_1] But plans have a way of not working out the way you desire."
    lloyd_narrating neutral "Every single one of the books is missing; gone from the shelf."
    lloyd_narrating neutral "It’s as though someone wanted to keep any knowledge about psychic abilities – no matter the exact topic – away from everybody else."
    lloyd_narrating neutral "This shouldn’t be happening.[wait_1] The catalogue claimed that most of the books were available."
    lloyd_narrating neutral "I make my way to the nearest desk and talk to a librarian."
    $ swap_sprites("cat_neutral", slow_dissolve)
    $ current_thought = "cat_thought_01"
    show screen psychic_powers
    librarian "Can I...[wait_05]help you?"
    lloyd_narrating neutral "Her voice is soft and quiet, matching her demeanour."
    lloyd_narrating neutral "Her hands are lightly placed on the desk, at odds with the tension in her body."
    lloyd_narrating neutral "She seems withdrawn, as though she’s made of glass and is worried that touching something will shatter her into pieces."
    $ current_thought = "cat_thought_02"
    lloyd friendly "Hello.[wait_1] I was hoping to borrow some books here, but they aren’t on the shelf."
    $ current_thought = "cat_thought_03"
    lloyd_narrating neutral "I list the titles of several of the more promising books."
    lloyd_narrating neutral "The librarian takes it all in passively before typing them into her computer.[wait_1] Her keystrokes seem deliberately slow as she enters the terms."
    librarian "These books...[wait_1]they’ve been reserved."
    librarian "We’re holding them for someone...[wait_1]that’s why they’re not on the shelf."
    $ current_thought = "cat_thought_04"
    lloyd neutral "Every single one of them?"
    lloyd_narrating neutral "I run through the remaining books that I’d taken note of.[wait_1] Each one of them comes up as reserved on the librarian’s computer."
    $ current_thought = "cat_thought_05"
    librarian "If you want to borrow them...[wait_1]you’ll need to wait for them to be borrowed and returned."
    lloyd_narrating neutral "I feel a sense of frustration building within me."
    lloyd_narrating neutral "There are several other libraries in the city but I doubt they’ll have as large a range as this one."
    lloyd_narrating neutral "I could try looking at bookshops but the same problem applies."
    lloyd_narrating neutral "A thought then occurs to me."
    $ current_thought = "cat_thought_06"
    lloyd friendly "You said that they’re being held for someone – can I temporarily take them to a table and read through them?"
    lloyd friendly "If the person who reserved them arrives at the library they can still borrow them.[wait_1] I won’t be too long."
    lloyd_narrating neutral "Most of them will be irrelevant to my needs.[wait_1] All that I need to do is skim through them to see whether any mention details that match my newfound abilities."
    librarian "That’s...[wait_1]not how this works."
    librarian "They’ve been reserved...[wait_1]they need to be held for the person who’s borrowing them."
    $ current_thought = "cat_thought_07"
    lloyd neutral "I understand that, but I’m not going to prevent that person from borrowing them.[wait_1] I just want to look at them."
    $ swap_sprites("cat_cold")
    lloyd_narrating neutral "The librarian’s eyes narrow.[wait_1] She looks at me with venomous disgust as she speaks, the hatred naked on her face."
    $ current_thought = "cat_thought_08"
    librarian "Get out."
    lloyd neutral "...Pardon?"
    librarian "I’ve explained how this works...[wait_1]that they’re being kept aside for another patron."
    librarian "You’re not listening...[wait_1]or respecting the library.[wait_1] Get out."
    lloyd_narrating neutral "I’m tempted to mention something about the man in black."
    lloyd_narrating neutral "To say that if I read them then I can save lives."
    lloyd_narrating neutral "She wouldn’t believe me if I said so, though.[wait_1] Or she’d ask how it works."
    lloyd_narrating neutral "I do my best to convince her."
    $ current_thought = "cat_thought_09"
    lloyd neutral "You don’t understand.[wait_1] I need those books."
    lloyd neutral "If I read them then...[wait_05]it’s very important that I get access to them."
    lloyd_narrating neutral "But my best isn’t enough.[wait_1] She doesn’t care."
    $ current_thought = "cat_thought_10"
    librarian "I’m going to call security if you don’t leave now.[wait_1] Please don’t make a scene."
    lloyd_thinking thinking "Is there anything that I can say to convince her?"
    
    menu:
        "Give up":
            lloyd_thinking neutral "I’ve tried explaining it as best I can and she hasn’t listened to me at all."
            lloyd_thinking neutral "The longer I stay here the worse things will get."
            $ current_thought = "cat_thought_11"
            lloyd_thinking neutral "Fine.[wait_1] I’m leaving."
            $ current_thought = "cat_thought_12"
            librarian "Good.[wait_1] You’re not wanted."
            lloyd_thinking neutral "Her hostility goes beyond my disagreeing with the library’s rules...[wait_05]why is she so determined to keep me from those books?"
            hide cat_cold with quick_dissolve
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "I exit the library as I said I would."
            lloyd_narrating neutral "I won’t find what I’m looking for today, and the librarian’s wrath is building."
            lloyd_narrating neutral "Once I’m outside I take out my phone and check the library’s catalogue again."
            lloyd_thinking neutral "...None of the books are marked as reserved."
            lloyd_thinking neutral "She was lying to me.[wait_1] But why?"
            lloyd_thinking neutral "I can return here another day and try to decipher the mystery."
            lloyd_thinking neutral "For now I should go elsewhere and see what else I can learn."
        "I know that the books aren’t here" (locked=not check_boolean("cat_books_missing"), message="You have not read the related thought"):
            lloyd_thinking neutral "She thought to herself that the books aren’t here."
            lloyd_thinking neutral "What’s going on?[wait_1] I’ll put pressure on her and see how she reacts."
            $ current_thought = "cat_thought_13"
            lloyd neutral "I know that the books aren’t here.[wait_1] How about you tell me where they actually are?"
            $ current_thought = "cat_thought_14"
            librarian "...[wait_1]I don’t need to answer anything...[wait_1]but security is just a button press away."
            $ current_thought = "cat_thought_15"
            lloyd neutral "Should I ask one of your coworkers if they can help me instead?"
            lloyd_narrating neutral "She freezes.[wait_1] I guessed correctly that her coworkers don’t know about the books being missing."
            lloyd_narrating neutral "I wait to see what her response is, and it finally comes."
            $ current_thought = "cat_thought_16"
            librarian "Of course they would be able to...[wait_1]but I’d rather keep them away from you."
            librarian "I can let you look at some of the books...[wait_1]if the person who reserved them doesn’t borrow them by the end of the day."
            lloyd_narrating neutral "She’s still sticking to her lie, but I don’t push it.[wait_1] I’ve made some progress for now."
            $ current_thought = "cat_thought_17"
            librarian "Can you return here...[wait_1]later tonight?"
            $ current_thought = "cat_thought_18"
            lloyd neutral "Possibly.[wait_1] I might have other engagements."
            $ current_thought = "cat_thought_19"
            librarian "If you do...[wait_1]ask for Cat if you can’t find me.[wait_1] Now...[wait_1]leave me alone."
            $ add_boolean("cat_name_discovered")
            hide cat_cold with quick_dissolve
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "I do as she requests."
            lloyd_narrating neutral "This trip hasn’t been particularly fruitful but I made some progress."
            lloyd_narrating neutral "It could be worth returning here later tonight and taking a look at the books."
            lloyd_narrating neutral "If not then I can return another day."
    
    $ visit_person("cat", "a", 0)
    jump eddie_investigation

label cat_a_2:
    $ visit_person("cat", "a", 1)
    return

label cat_a_3:
    $ visit_person("cat", "a", 2)
    return

label cat_a_4:
    $ visit_person("cat", "a", 3)
    return 