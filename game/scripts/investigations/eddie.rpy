label eddie_investigation:
    $ current_thought_block = "mind_read_eddie"
    if (branch == "a"):
        if (day == 1):
            jump eddie_a_1
        elif (day == 2):
            jump eddie_a_2
        elif (day == 3):
            jump eddie_a_3
        elif (day == 4):
            jump eddie_a_4
    
    return

label eddie_a_1:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I travel eastwards for a quarter of an hour with mixed feelings in my stomach throughout the duration of the journey."
    lloyd_narrating neutral "Of all the places to visit today this is both the one I’m most excited for, but also looking forward to the least."
    lloyd_narrating neutral "It’s been several weeks since I was inside the office of a newspaper, and it’s sure to stir up some bittersweet emotions within me."
    # SFX: Camera shutter
    lloyd_narrating neutral "I take a photo of the building once I’m standing outside it."
    lloyd_narrating neutral "It’s nothing particularly impressive – a skyscraper similar to those in the blocks surrounding it, the large sign out front the only thing that indicates anything special about it – but it feels like an appropriate homage to pay before entering."
    lloyd_narrating neutral "I enter one of the revolving doors and already feel like I’m home."
    lloyd_narrating neutral "I’ve already called ahead and arranged to speak with somebody about a story I’ve got."
    lloyd_narrating neutral "The meeting will be a balancing act on razor’s edge."
    lloyd_narrating neutral "Too much information about the man in black and his future plans will get me directed to the police, or dismissed as a crackpot trying to get his name in the news."
    lloyd_narrating neutral "Too little information, and the story won’t have enough juice to entice the reporter."
    scene office_interview_room with slow_dissolve
    lloyd_narrating neutral "The receptionist directs me to one of the many rooms for conducting interviews, telling me that I shouldn’t have to wait long."
    lloyd_narrating neutral "Several minutes pass before the door opens."
    $ swap_sprites("eddie_smiling", slow_dissolve)
    $ current_thought = "eddie_thought_01"
    show screen psychic_powers
    employee "Sorry for the wait –[wait_05] I had to edit some –"
    $ swap_sprites("eddie_angry")
    $ current_thought = "eddie_thought_02"
    employee "Wait...[wait_05]Lloyd fucking Chen?![wait_1] You?!"
    if (check_boolean("eddie_name_learned")):
        menu:
            "I don't believe we've met":
                jump eddie_unrecognised
            "You're Eddie Thompson":
                jump eddie_recognised
    else:
        jump eddie_unrecognised

    return

label eddie_unrecognised:
    lloyd_narrating neutral "The recognition is a surprise."
    lloyd_narrating neutral "This man’s face is a complete mystery to me.[wait_1] If we’ve crossed paths before, I don’t recall when."
    $ current_thought = "eddie_thought_03"
    lloyd friendly "I don’t believe we’ve met.[wait_1] Can I ask how you know me?"
    lloyd_narrating neutral "The man has a camera on him – it’s possible that he’s familiar with my work."
    lloyd_narrating neutral "I didn’t realise that I had enough of a reputation in the industry, though."
    employee "...You’re fucking joking, right?"
    $ current_thought = "eddie_thought_04"
    lloyd friendly "I didn’t realise that my reputation preceded me.[wait_1] May I get your name?"
    employee "Take a guess."
    lloyd_thinking neutral "Is he also someone that I’m supposed to know by reputation?"
    $ current_thought = "eddie_thought_05"
    lloyd friendly "I honestly couldn’t say."
    $ current_thought = "eddie_thought_06"
    employee "You really don’t fucking remember?"
    employee "Multiple years, repeatedly screwing me over, and I’m just a footnote to you."
    employee "The surprising thing is that I can be surprised by the way you act."
    lloyd_thinking neutral "Screwing him over?[wait_1] That can’t be right."
    lloyd_thinking neutral "But I’m not here to settle an old debt.[wait_1] I need to try and calm him down a bit and focus on my goal."
    $ current_thought = "eddie_thought_07"
    lloyd friendly "I don’t recall what you’re talking about, but I’ve come here for a reason.[wait_1] I –"
    $ current_thought = "eddie_thought_08"
    employee "Yeah, good point – why don’t you tell me why you’ve organised this little meeting with me?"
    $ current_thought = "eddie_thought_09"
    lloyd_narrating neutral "I do as he asks, describing the man in black and that he’s a dangerous individual."
    lloyd_narrating neutral "As far as this man knows I’ve heard all of this from a reliable source who’s too afraid to identify themselves."
    lloyd_narrating neutral "Eventually I finish explaining what I can.[wait_1] I’ve provided the bait, now he just has to bite."
    $ current_thought = "eddie_thought_10"
    employee "Cool story.[wait_1] I don’t care."
    $ current_thought = "eddie_thought_11"
    lloyd neutral "What?[wait_1] But surely you –"
    employee "Look, I know that for someone in your position, this must seem like big news, but for someone like me, with an actual job?"
    employee "I’ve got real stories to follow.[wait_1] And I have actual deadlines so –[wait_05] see ya."
    lloyd_narrating neutral "The man stands up and begins leaving.[wait_1] I’m trying to work out what to say that will make him stay when he clears his throat."
    $ current_thought = "eddie_thought_12"
    employee "Oh, and by the way, Chen:[wait_05] I know you won’t bother to look it up, or try to remember, so out of the kindness of my heart –[wait_05] Eddie Thompson."
    $ add_boolean("eddie_name_learned")
    eddie "I also worked at {i}The Brief{/i}.[wait_1] Dick."
    lloyd_narrating neutral "With that connection made, I vaguely recall a coworker who looked like him."
    lloyd_narrating neutral "I can’t think of what our relationship was like or even what his personality was."
    lloyd_narrating neutral "But now’s not the time for that.[wait_1] Eddie is leaving the room and if I want to act, now’s the time."
    menu:
        "Please reconsider":
            $ current_thought = "eddie_thought_13"
            lloyd neutral "Eddie, I’m sorry if I hurt you in the past, but please reconsider."
            lloyd neutral "I’d really like your help with this."
            eddie "Yeah, well I really wanted someone who didn’t fuck me over all the time in the past, so consider this to be me repaying the favour."
        "What are your intentions?" (locked=not check_boolean("eddie_pretend_indifference"), message="You have not read the related thought"):
            lloyd_thinking neutral "Eddie thought to himself that he’s only pretending not to care about the story."
            lloyd_thinking neutral "So what’s he actually going to do with the information I gave him?"
            $ current_thought = "eddie_thought_14"
            lloyd neutral "What are your intentions, Eddie?[wait_1] Are you planning to follow the story?"
            eddie "None of your business, Chen."
    hide screen psychic_powers
    hide eddie_angry with quick_dissolve
    lloyd_narrating neutral "Eddie leaves the room and closes the door behind him."
    lloyd_narrating neutral "I want to go after him but the moment has passed.[wait_1] For now I’ll have to leave."
    lloyd_thinking neutral "If I come back another day, he might be in a better mood.[wait_1] For now I’d better keep moving."
    return

label eddie_recognised:
    lloyd_thinking neutral "I know who he is this time.[wait_1] If I act friendly to him I can gain his trust and make him believe me."
    $ current_thought = "eddie_thought_15"
    lloyd friendly "Eddie?[wait_1] Eddie Thompson?![wait_1] From back at {i}The Brief{/i}?!"
    $ current_thought = "eddie_thought_16"
    eddie "You don’t have to act like you’ve ever considered me a friend, Chen.[wait_1] In fact, I’d rather you just act like your natural self."
    lloyd_thinking neutral "That didn’t work as well as I hoped it would.[wait_1] But I have to stick with it."
    $ current_thought = "eddie_thought_17"
    lloyd friendly "Hey, now, Eddie – that’s not fair.[wait_1] We had plenty of great times at {i}The Brief{/i}, didn’t we?"
    eddie "Oh, sure, there were plenty of great times."
    eddie "At least, for you there might have been.[wait_1] But for me?"
    eddie "There’s a reason that I left for greener pastures – for somewhere that I wouldn’t be repeatedly screwed over."
    $ current_thought = "eddie_thought_18"
    lloyd friendly "Well, that’s –"
    $ swap_sprites("eddie_arrogant")
    $ current_thought = "eddie_thought_19"
    eddie "But enough about my kick-ass job –[wait_05] how about you?[wait_1] What are you up to now?"
    eddie "Oh, that’s right –[wait_05] didn’t I hear something about you getting fired?"
    eddie "Something about how you haven’t gotten any work in months?"
    lloyd neutral "..."
    eddie "Word travels, Chen.[wait_1] And now that the tables have turned, you’ve come crawling to me."
    eddie "Isn’t that right?"
    $ current_thought = "eddie_thought_20"
    lloyd neutral "I didn’t know that you were here, Eddie.[wait_1] Or that you would be assigned to talk to me."
    lloyd_thinking neutral "Or who you were."
    $ current_thought = "eddie_thought_21"
    $ swap_sprites("eddie_angry")
    eddie "...Fine.[wait_1] What have you got?"
    $ current_thought = "eddie_thought_22"
    lloyd_narrating neutral "I tell him that I’ve got a source who believes there’s a killer in the city.[wait_1] I tell him that they’ve already killed at least once."
    lloyd_narrating neutral "I tell him that it’s the sort of story the public love – bloody murders, a compelling mystery, a deadly villain."
    lloyd_narrating neutral "I explain all about the man in black and how if he can be found before he kills again, not only will lives have been saved, but the story will be an exclusive scoop."
    $ current_thought = "eddie_thought_23"
    eddie "...I dunno."
    eddie "Can I talk to your source on this?[wait_1] It’s pretty vague at this point – I need something with a few less unknowns."
    $ current_thought = "eddie_thought_24"
    lloyd neutral "My source is...[wait_05]they’re uncomfortable meeting with anyone.[wait_1] They’re worried that their life is in danger."
    $ current_thought = "eddie_thought_25"
    eddie "And yet they met with you."
    $ current_thought = "eddie_thought_26"
    lloyd neutral "They had to tell someone.[wait_1] Will you look into the story or not?"
    lloyd_narrating neutral "Eddie thinks over it for a few moments.[wait_1] Despite my best efforts he hasn’t fully swallowed the bait."
    lloyd_narrating neutral "I’m starting to think that this might be going nowhere when he nods slowly."
    $ current_thought = "eddie_thought_27"
    eddie "Alright, I can do a little bit of research into this – trying to find out any details of this guy wearing black."
    eddie "Can you come back later tonight?"
    $ current_thought = "eddie_thought_28"
    lloyd neutral "Maybe.[wait_1] My schedule is erratic at the moment."
    $ current_thought = "eddie_thought_29"
    eddie "I guess when you don’t have a job, you can afford to just laze around and do whatever you want, whenever you want."
    lloyd_narrating neutral "Eddie checks the notes that he’s been taking and stands up from the table."
    lloyd_narrating neutral "He doesn’t look any more cheerful than when he first recognised me, but at least he’s on my side."
    $ current_thought = "eddie_thought_30"
    eddie "If you can’t make it, come by tomorrow, or another day.[wait_1] I’ll let you know what I’ve got."
    lloyd neutral "Understood.[wait_1] Thank you, Eddie."
    $ current_thought = "eddie_thought_18"
    eddie "Oh, and Lloyd?"
    lloyd neutral "Yes?"
    eddie "This story had better be fuckin’ worth my time."
    hide eddie_angry with quick_dissolve
    lloyd_narrating neutral "With those words of wisdom he leaves the room."
    lloyd_narrating neutral "I have no more reason to stay in this building and exit it."
    scene black_bg with slow_dissolve
    lloyd_thinking neutral "Eddie’s contacts will hopefully be far-reaching, and able to find out information on the man in black."
    lloyd_thinking neutral "But he made it clear that he’s not happy to work with me."
    lloyd_thinking neutral "I can return here later, but will he tell me anything that I couldn’t discover on my own?"

    return

label eddie_a_2:
    return

label eddie_a_3:
    return

label eddie_a_4:
    return 