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
            hide screen psychic_powers
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
            hide screen psychic_powers
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "I do as she requests."
            lloyd_narrating neutral "This trip hasn’t been particularly fruitful but I made some progress."
            lloyd_narrating neutral "It could be worth returning here later tonight and taking a look at the books."
            lloyd_narrating neutral "If not then I can return another day."
    
    $ visit_person("cat", "a", 0)
    return

label cat_a_2:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I lost a large portion of my memories from last night."
    lloyd_narrating neutral "I have no idea why I went to that bar, why I drank so much, or what happened while I was there."
    lloyd_narrating neutral "It’s obvious that my psychic powers are to blame for the memory loss."
    lloyd_narrating neutral "I’ve been using them fairly liberally since I acquired them, without considering the side effects of them."
    lloyd_narrating neutral "There’s still too much that I don’t know about them or how they work."
    lloyd_narrating neutral "I need to research them, and the best place to do that is a library."
    lloyd_narrating neutral "If I can learn more about them I may be able to restore my missing memories."
    if (person_visited("cat", "a", 0)):
        lloyd_narrating neutral "Firstly I’ll need to convince that librarian to relinquish the books she does have."
        lloyd_narrating neutral "I’m confident that I can find an argument to persuade her today."
    lloyd_narrating neutral "I travel southwards through the city, to the large park where the library is located."
    lloyd_narrating neutral "It’s the largest in the city and so I believe I should focus my efforts on research here."
    lloyd_narrating neutral "There’s little sense in going after minnows while there are still sharks in the water."
    lloyd_narrating neutral "The open area of the park offers no cover from the chilly breeze that blows as I walk along a path, dragging a scattering of leaves in its wake."
    scene library_day with slow_dissolve
    lloyd_narrating neutral "A pair of sliding glass doors open up automatically and grant me access to the library."
    lloyd_narrating neutral "It’s as quiet as the stereotype goes, the sounds of mouses clicking, pages turning, and people walking being the closest to loud noises."
    lloyd_narrating neutral "As today is a weekday it’s not overly busy; most of the visitors appear to be the elderly, who simply want a quiet space to read in."
    if (person_visited("cat", "a", 0)):
        lloyd_narrating neutral "I don’t hold out any hope that the books I’m interested in have miraculously returned to the shelves."
        lloyd_narrating neutral "I make my way directly to the reception.[wait_1] The same librarian from yesterday is there today."
        $ swap_sprites("cat_neutral", slow_dissolve)
        $ current_thought = "cat_thought_29"
        show screen psychic_powers
        lloyd_narrating neutral "Three piles of books are before her."
    else:
        lloyd_narrating neutral "The library’s online catalogue showed what looked like some promising books, but I don’t make my way to the shelves."
        lloyd_narrating neutral "Instead I walk over to the library’s reception desk."
        lloyd_narrating neutral "I’m hoping that somebody here can provide me with some recommendations."
        $ swap_sprites("cat_neutral", slow_dissolve)
        $ current_thought = "cat_thought_01"
        show screen psychic_powers
        lloyd_narrating neutral "The closest librarian has three piles of books before her."
    lloyd_narrating neutral "She’s making her way through one of them, opening the cover of each book and examining it for a moment, then placing it in one of the other two piles."
    lloyd_narrating neutral "I’m unsure what exactly she’s doing.[wait_1] Frankly, I don’t care."

    if (person_visited("cat", "a", 0)):
        lloyd_narrating neutral "I place my hands on the desk with enough force to make her look up.[wait_1] From her expression it’s clear that she recognises me."
        $ current_thought = "cat_thought_30"
        lloyd neutral "Looks like this library isn’t missing all of its books.[wait_1] Just the ones that would be helpful for its patrons to borrow."
        if (check_boolean("cat_name_discovered")):
            cat "Was that...[wait_1]supposed to be a quip?[wait_1] I don’t understand it."
            lloyd neutral "The point, Cat, is that I want to have a look at those books I was asking about yesterday."
            lloyd neutral "I won’t take no for an answer."
        else:
            librarian "Was that...[wait_1]supposed to be a quip?[wait_1] I don’t understand it."
            lloyd neutral "The point is that I want to have a look at those books I was asking about yesterday."
            lloyd neutral "I won’t take no for an answer...[wait_05]you."
            $ current_thought = "cat_thought_31"
            librarian "I go by Cat."
            $ add_boolean("cat_name_discovered")
            lloyd neutral "Okay, Cat.[wait_1] I won’t take no for an answer –[wait_05] I want those books."
    else:
        lloyd_narrating neutarl "I clear my throat so that the librarian notices me.[wait_1] As she looks into my eyes, I wonder how much time she spends on her makeup each day."
        lloyd neutral "Hi.[wait_1] I’m Lloyd."
        librarian "Cat."
        lloyd_narrating neutral "I turn around, confused."
        lloyd neutral "In here?"
        $ current_thought = "cat_thought_31"
        librarian "No...[wait_1]I go by Cat."
        $ add_boolean("cat_name_discovered")
        lloyd neutral "Oh.[wait_1] Well, Cat, I’d like your assistance."
        $ current_thought = "cat_thought_32"
        lloyd_narrating neutral "I tell Cat what I’m looking for, asking about books on extrasensory research and unknown phenomena exhibited by people."
        lloyd_narrating neutral " I emphasise the need for concrete cases with evidence to back it up, not simple records of urban legends and tall tales."
        lloyd_narrating neutral "Her expression is completely blank throughout my description, and I’m unsure of what she’s thinking."
        lloyd_narrating neutral "Then, she speaks."
    
    $ current_thought = "cat_thought_33"
    cat "Those books aren’t available for you...[wait_1]to borrow.[wait_1] I can’t let you have them."
    lloyd neutral "I hear you, but I need to read them.[wait_1] They have information in them which could be very important to me."
    cat "They’re unavailable.[wait_1] I can’t give you books...[wait_1]that aren’t here in the library."
    if (person_visited("cat", "a", 0)):
        lloyd_thinking thinking "Exactly the same as yesterday.[wait_1] I shouldn’t have expected anything different from her."
        lloyd_thinking thinking "What could I say to get her to understand the importance?"
    else:
        lloyd_thinking thinking "When I browsed the library’s online catalogue earlier it showed that several of the books I’m interested in were available."
        lloyd_thinking thinking "I was hoping that she would simply give me some recommendations, but she’s insisting that they’re unavailable."
        lloyd_thinking thinking "That has to be a lie.[wait_1] What could I say to her to have her understand the importance?"
    
    menu:
        "There's been a death":
            $ current_thought = "cat_thought_34"
            lloyd_thinking "This might scare her off, and I don’t know how to tell her that it’s related to psychic research."
            lloyd_thinking "But if I tell her that somebody’s died, and that these books could help stop somebody else from dying, she might loosen up a bit."
            $ current_thought = "cat_thought_35"
            lloyd neutral "What if I told you that these books –[wait_05] the information in them –[wait_05] could save lives?"
            cat "Some books about...[wait_1]psychic phenomena?"
            $ current_thought = "cat_thought_36"
            lloyd neutral "It’s hard to explain.[wait_1] But I’m trying to stop a murder."
            lloyd_narrating neutral "I’m not expecting her to believe me.[wait_1] At best I’m expecting her to ask me how the information is related to stopping a murderer."
            lloyd_narrating neutral "But her reaction takes me by surprise."
            $ swap_sprites("cat_neutral")
            cat "That sounds serious.[wait_1] Tell me what’s happened."
            $ current_thought = "cat_thought_37"
            lloyd neutral "I –[wait_05] several nights ago I encountered a man who was bleeding out.[wait_1] I think that he had been shot."
            lloyd neutral "He spoke to me briefly before he –[wait_05] he didn’t make it."
            lloyd_narrating neutral "I’m keeping my voice low, not wanting to unsettle any patrons of the library or have them think that I’m disturbed."
            lloyd_narrating neutral "I’m surprised to see that Cat isn’t more unsettled herself."
            lloyd neutral "I think that he was killed by someone who –[wait_05] I think that he was killed by someone."
            lloyd neutral "That it was an intentional killing.[wait_1] And I think that the killer will strike again."
            $ current_thought = "cat_thought_38"
            cat "What makes you so certain that it’s a killer?[wait_1] Not a gangland killing...[wait_1]or a domestic dispute."
            lloyd_narrating neutral "I hesitate.[wait_1] It would be a valid question if I hadn’t seen a vision of the killer acting again."
            $ current_thought = "cat_thought_39"
            lloyd neutral "Call it a hunch."
            $ current_thought = "cat_thought_40"
            cat "I see.[wait_1] Has the killer ended the life of anybody other than this person that you found?"
            lloyd neutral "I don’t know.[wait_1] I’ve been more focused on the future than the past."
            $ current_thought = "cat_thought_41"
            cat "You’ve made a mistake.[wait_1] Finding connections between past victims will provide you with more information than one of those books will."
            cat "If he’s killed before and his victims have commonalities...[wait_1]you can narrow down his future victims."
            lloyd_narrating neutral "She makes a good point.[wait_1] The problem is that I don’t know whether the killer has acted before or not."
            $ current_thought = "cat_thought_42"
            lloyd neutral "How would I find whether he’s killed before?"
            lloyd neutral "I can’t exactly walk into a police station and ask them how many murder victims they’ve found recently."
            cat "Maybe not.[wait_1] But if there are victims then there will be reports."
            cat "I can find them for you."
            $ current_thought = "cat_thought_43"
            lloyd neutral "You will?[wait_1] Why would you help me?"
            cat "I’m a librarian.[wait_1] It’s what we do."
            lloyd neutral "Well...[wait_05]thank you, Cat."
            $ current_thought = "cat_thought_44"
            cat "Give me your phone number...[wait_1]I’ll send you any information that I find." 
            cat "But firstly...[wait_1]I’ll need to know everything about the victim that you found."
            lloyd_narrating neutral "I give her my phone number as requested then describe the man with the white streak."
            lloyd_narrating neutral "At her prompting I tell her when and where I found him, as well as what happened afterwards."
            $ current_thought = "cat_thought_45"
            cat "If I find any reports with similar information then I’ll share them with you."
            lloyd neutral "Thank you."
            cat "Is there anything else that I can help you with today?"
            lloyd_thinking neutral "She still hasn’t given me access to any of the books that I’m interested in."
            lloyd_thinking neutral "I still don’t know how I lost my memories or whether there’s any way to get them back."
            lloyd_thinking neutral "But she’s helping me out with the bigger picture.[wait_1] It’s probably best to stay on her good side."
            lloyd neutral "Nothing else, Cat."
            cat "Very well.[wait_1] Have a good day."
            hide cat_neutral with quick_dissolve
            hide screen psychic_powers
            lloyd_narrating neutral "She returns to her pile of books and I take the hint."
            lloyd_narrating neutral "I leave the library, wondering where I could find the way to recover my missing memories."
            $ add_boolean("cat_investigates_murders")
        "Tell her about my missing memories":
            $ current_thought = "cat_thought_34"
            lloyd_thinking thinking "I won’t tell her about my psychic powers and how they were responsible for removing some of my memories."
            lloyd_thinking thinking "It’s too dangerous to tell ordinary people about my abilities; I don’t know how she’d react."
            lloyd_thinking thinking "But I can tell her that I have a block of memories missing and that I believe the books will help me recover them."
            lloyd_thinking thinking "That should be safe enough."
            $ current_thought = "cat_thought_46"
            lloyd neutral "It’s important that I read those books.[wait_1] I’m missing a period of memories."
            lloyd_narrating neutral "Cat has been idly continuing her library work as I’ve been talking to her."
            lloyd_narrating neutral "But when I speak she pauses in her work and stares at me.[wait_1] After examining me for several seconds she speaks."
            $ current_thought = "cat_thought_47"
            cat "You have...[wait_1]amnesia?"
            lloyd neutral "Yes, that’s what missing memories means."
            $ current_thought = "cat_thought_48"
            lloyd neutral "Correct.[wait_1] Last night I remember going to bed at home, the same as any other night."
            lloyd neutral "I planned to get as much sleep as I could.[wait_1] For it to be an ordinary, if mundane, evening."
            lloyd neutral "But at some point I...[wait_05]woke up.[wait_1] I wasn’t in my apartment any more."
            lloyd_narrating neutral "The noises of the bar.[wait_1] The taste of alcohol in my mouth.[wait_1] A sticky sensation on my fingers."
            lloyd_narrating neutral "The experience is still vivid in my mind."
            cat "Interesting.[wait_1] You have no memory of waking up?[wait_1] Of leaving your apartment and travelling elsewhere?"
            lloyd neutral "None at all.[wait_1] It was as though I’d been thrown forwards in time."
            lloyd neutral "One moment I was drifting off, the next I was elsewhere."
            $ current_thought = "cat_thought_49"
            cat "Excuse me if this comes across as insensitive...[wait_1]do you have dissociative identity disorder?"
            lloyd neutral "Not to my knowledge."
            $ current_thought = "cat_thought_50"
            cat "Do you have any traumatic experiences in your past?"
            lloyd_thinking thinking "I saw a man die in front of me.[wait_1] I saw a vision of another man killing someone.[wait_1] Do they count?"
            lloyd neutral "Nothing more traumatic than the average person." 
            lloyd neutral "I take it that you think these could be explanations for my missing memories?"
            $ current_thought = "cat_thought_51"
            cat "I think that looking into mental illnesses will be more productive for you than looking into books on extrasensory research."
            lloyd_thinking thinking "She’s still pushing back against me.[wait_1] What’s in those books that she doesn’t want me to see?"
            lloyd neutral "Maybe it will be."
            lloyd neutral "But as a patron of the library I’m allowed to borrow what books I’d like.[wait_1] I’m permitted to read what I’d like, and if I am making a mistake, it’s on my head for making it."
            lloyd neutral "How do you think you’d feel if you were missing some of your memories?[wait_1] If you had an entire evening gone?"
            lloyd neutral "If I can’t get my memories back then I at least want answers."
            $ swap_sprites("cat_cold")
            $ current_thought = "cat_thought_52"
            cat "And why do you think that books about psychic phenomena and research will give you answers?"
            lloyd_thinking thinking "Do I tell her about my powers?[wait_1] That they’re responsible for wiping my memories?"
            lloyd_thinking thinking "...No."
            lloyd_thinking thinking "I don’t know how she’ll react, or why she’s so determined to keep me from the information."
            $ current_thought = "cat_thought_53"
            lloyd neutral "Call it a hunch."
            cat "Even if your hunch was right...[wait_1]that still wouldn’t make the books available."
            cat "I can’t check out books for you that aren’t here."
            lloyd_narrating neutral "I can see that I’m not winning this argument today."
            lloyd_narrating neutral "It’s a bitter pill to swallow, but she’s hostile enough to me already."
            lloyd_narrating neutral "I’m better off cutting my losses and leaving the library."
            $ current_thought = "cat_thought_54"
            lloyd neutral "Well...[wait_05]I hope that they’re available soon, then."
            cat "I hope for your sake...[wait_1]that they are as well."
            lloyd_thinking thinking "Keeping up the facade to the end."
            hide cat_cold with quick_dissolve
            hide screen psychic_powers
            lloyd_narrating neutral "Cat returns to her pile of books as though I’ve already left her."
            lloyd_narrating neutral "I take the hint and walk away.[wait_1] I won’t be gaining anything from the library today."

    scene black_bg with quick_dissolve
    $ visit_person("cat", "a", 1)
    return

label cat_a_3:
    $ visit_person("cat", "a", 2)
    return

label cat_a_4:
    $ visit_person("cat", "a", 3)
    return 