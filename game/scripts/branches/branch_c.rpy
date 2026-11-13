label branch_c_1_4:
    $ branch = "c"
    $ day = 1
    $ current_thought_block = "mind_read_eddie"

    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I finish my meal and pay for it then head eastwards.[wait_1] I hope that Eddie is still at the newspaper at this time of day."
    lloyd_narrating neutral "I try to think back to when we were both at {i}The Brief{/i} and what sort of worker he was."
    lloyd_narrating neutral "Nothing comes to mind.[wait_1] I can’t recall anything notable about him."
    lloyd_narrating neutral "He claimed that I screwed him over multiple times but I can’t think of a single incident that he’s referring to."
    lloyd_narrating neutral "If I did do something that affected him negatively did he keep it to himself?"
    lloyd_narrating neutral "Or does he think that I’m to blame for someone else’s mistake?"
    scene office_interview_room with slow_dissolve
    lloyd_narrating neutral "Once I reach the newspaper building I ask whether Eddie is still in.[wait_1] I’m told that he’s waiting for me and am brought back to the same room from earlier today."
    lloyd_narrating neutral "I don’t have to wait long before he joins me."
    $ swap_sprites("eddie_angry", slow_dissolve)
    $ current_thought = "eddie_thought_114"
    show screen psychic_powers
    eddie "So, you managed to make it after all.[wait_1] Would’ve been nice if you’d let me know in advance."
    lloyd neutral "Today’s been a busy day, Eddie.[wait_1] Were you able to discover anything about the man in black?"
    lloyd_narrating neutral "Eddie scoffs as he sits down.[wait_1] He has a manilla folder beneath his arm which he places on the table."
    $ current_thought = "eddie_thought_115"
    eddie "Yeah, you could say that."
    lloyd_narrating neutral "Eddie opens up the folder and holds up a printed photo."
    $ current_thought = "eddie_thought_116"
    eddie "Not that your description was any good, but is this the guy?"
    eddie "Because if it is, I found out a lot of interesting info about this supposed killer of yours."
    lloyd_narrating neutral "Eddie’s come through for me.[wait_1] The picture matches the face I saw in my vision exactly –[wait_05] not a single detail is out of place."
    lloyd_narrating neutral "That means that I can stop the killer."
    $ current_thought = "eddie_thought_117"
    lloyd neutral "Yes, it is." 
    lloyd neutral "What is his name?[wait_1] Do you have an address?"
    lloyd_narrating neutral "Eddie scoffs and turns the picture around so that he can examine it for a few moments."
    lloyd_narrating neutral "Then he places it on the table and takes out another page from the folder."
    $ swap_sprites("eddie_arrogant")
    $ current_thought = "eddie_thought_118"
    eddie "Allan Docherty, age 43.[wait_1] A carpenter, who by all accounts is pretty good at his job."
    eddie "A regular at his local pub, who likes a cheap pint of beer alongside a plate of whatever’s greasy and available."
    eddie "Seems like a pretty nice guy, right?"
    lloyd_narrating neutral "I stay quiet since he’s building up to something."
    lloyd_narrating neutral "It’s better to let him have his moment than interrupt or insist on him getting to the point."
    $ swap_sprites("eddie_angry")
    $ current_thought = "eddie_thought_119"
    eddie "Only thing is, there’s a bit of a secret that our man Docherty has.[wait_1] He’s not so happy with the state of things, and he wants more."
    eddie "More money.[wait_1] More assets.[wait_1] More everything."
    eddie "He gets talking to a mate of his at the pub.[wait_1] Why should other people have more than them?"
    eddie "Especially when they can’t even keep track of what they have?"
    lloyd_narrating neutral "I’m unsure where he’s going with this.[wait_1] I stay silent and wait patiently."
    $ swap_sprites("eddie_arrogant")
    $ current_thought = "eddie_thought_120"
    eddie "So Docherty and his pal, they decide to start moonlighting in a new career.[wait_1] Namely, burglary."
    eddie "They plan to start breaking into peoples’ houses when they’re out, stealing whatever isn’t nailed down, and keeping it for themselves."
    eddie "It’s the perfect way for them to get what they feel they’re owed, and the way they see it, it’s a victimless crime."
    lloyd_thinking thinking "How does this relate to him becoming a murderer?[wait_1] Did he get caught and end up on the run?"
    $ swap_sprites("eddie_angry")
    $ current_thought = "eddie_thought_121"
    eddie "At least, that’s how they thought it would go."
    eddie " But they fuck it up – the first house they try robbing, on their first night, the occupants are still inside.[wait_1] They get caught and the police are called."
    eddie "The two of them can’t get a good lawyer, and they end up charged with enough dirt to wind up in prison."
    eddie "Minimum security, mind you, and only for a few months, but it’s still not how they expected their burglary career to end up."
    lloyd neutral "What happens after he’s released?"
    lloyd_narrating neutral "Eddie gives me a cold stare as I realise that this is what he’s been building up to."
    lloyd_narrating neutral "The story’s coming to its end, but not in a way that I expected it to."
    $ current_thought = "eddie_thought_122"
    eddie "He’s dead.[wait_1] He died in prison."
    lloyd_narrating scared "The room seems to spin around me as what Eddie says hits me.[wait_1] It doesn’t make any sense."
    lloyd scared "How can he be dead?"
    $ current_thought = "eddie_thought_123"
    eddie "There’s a report filed by the prison, dated two weeks ago."
    eddie "It says that he got into an argument with another prisoner and was fatally stabbed."
    lloyd neutral "Are you sure that –"
    $ current_thought = "eddie_thought_124"
    eddie "Will you shut the hell up?![wait_1] I think that it’s my turn to ask the questions."
    lloyd_narrating neutral "Eddie bangs the table loudly as he shouts.[wait_1] His breathing is heavy and I can see a vein pulsing in his forehead."
    lloyd_narrating neutral "I have to be careful with what I say."
    $ current_thought = "eddie_thought_125"
    eddie "Are you –[wait_05] are you absolutely, positively, swear-on-your-mother’s-fucking-life certain that this guy –[wait_05] this Allan Docherty –[wait_05] is who your source reckons is the killer?[wait_1] No chance of a mistake?"
    lloyd_narrating neutral "Eddie holds up the picture again as though he’s hoping for me to realise that I’m mistaken."
    lloyd_narrating neutral "I study it once more but I’m certain.[wait_1] There’s no mistaking the face from my vision."
    $ current_thought = "eddie_thought_126"
    lloyd neutral "No chance at all."
    eddie "Dammit, Chen!"
    lloyd_narrating neutral "Eddie bangs the table again, more loudly than before."
    $ current_thought = "eddie_thought_127"
    eddie "I told you that I wanted a story that was worth my time.[wait_1] And you –[wait_05] you fucking assured me, you told me that this was something that mattered."
    eddie "But you lied to me, didn’t you?"
    eddie "This Docherty guy, he can’t kill anyone![wait_1] He’s dead!"
    $ current_thought = "eddie_thought_128"
    lloyd neutral "Eddie, I –[wait_05] I’m unsure what’s –"
    $ current_thought = "eddie_thought_129"
    eddie "Oh, you’re unsure![wait_1] You’re fucking unsure about what’s happened![wait_1] That’s great!"
    eddie "I bust my ass trying to get you the info, I call in a bunch of fucking favours, and you’re fucking unsure![wait_1] Real fucking great!"
    eddie "What do you want me to do for a follow-up?[wait_1] Go undercover because of a dream you had?"
    eddie "Infiltrate a gang on a hunch?[wait_1] Commit corporate espionage on a whim?"
    eddie "You made me waste my entire day, asshole."
    $ current_thought = "eddie_thought_130"
    lloyd neutral "My source –"
    eddie "Get fucking real, Lloyd."
    eddie "You don’t have a source –[wait_1] you just made that up to make your story more believable."
    eddie "If you had a source, then how were you able to identify Docherty from the photo?"
    lloyd_thinking thinking "He won’t believe me if I tell him about my vision of the future. I need to think of a good excuse."
    lloyd_narrating neutral "But no matter how hard I try I can’t come up with one.[wait_1] Eddie’s seen through all of my lies."
    $ current_thought = "eddie_thought_131"
    eddie "I don’t know why you wanted me to do this, or what you thought you’d get out of it."
    eddie "But don’t ever fucking ask me for a favour again, asshole."
    hide eddie_angry with quick_dissolve
    hide screen psychic_powers
    lloyd_thinking scared "I don’t understand it.[wait_1] I thought that I was seeing the future when I experienced that vision."
    lloyd_thinking scared "I thought that I could save people and make up for some of my past mistakes."
    lloyd_thinking scared "But if the killer –[wait_05] Allan Docherty –[wait_05] is dead, then I didn’t see the future."
    lloyd_thinking thinking "Was I wrong all this time?"
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I won’t be discovering the answer by staying here.[wait_1] I leave the building and return home."
    scene apartment_night with slow_dissolve
    lloyd_narrating neutral "I briefly consider visiting another one of the contacts I met today and seeing what they have to say but dismiss the idea."
    lloyd_narrating neutral "Eddie gave me enough detail about Docherty that I doubt they would give me anything new."
    lloyd_narrating neutral "All that I want to know now is what I saw in my vision."
    lloyd_thinking thinking "Was it the past?[wait_1] Or was I overthinking it the entire time?"
    lloyd_thinking thinking "Was it just a hallucination?[wait_1] Was it the surface thoughts of someone’s mind, and I delved into it too deeply through my inexperience?"
    lloyd_narrating neutral "It would be a satisfying answer if it weren’t for the fact that it felt completely different to reading somebody’s mind.[wait_1] It felt more real."
    lloyd_thinking thinking "If only the vision would trigger again.[wait_1] Then I could take in more details and try to work out what I’m seeing."
    lloyd_thinking thinking "Could I trigger it somehow?"
    lloyd_narrating neutral "It’s worth a shot.[wait_1] I sit cross-legged on my bed and concentrate on my breathing."
    lloyd_narrating neutral "After a while I focus on my head, trying to recall the sensation I felt of the vision the first time."
    lloyd_narrating neutral "I’m feeling calmer but no other changes are forthcoming."
    lloyd_narrating neutral "Still I stick with it, imagining the energy within and without my body.[wait_1] I picture the ebb and flow of the energy and how it passes through me."
    lloyd_narrating neutral "Then I feel it."
    lloyd_narrating neutral "Within my head a pain has made its presence known, just as it did the previous night.[wait_1] I focus on it and try to make it disappear as I did the last time I felt this pain."
    scene cg3_1 with slow_dissolve
    lloyd_narrating neutral "It’s definitely the man in Eddie’s photo.[wait_1] Allan Docherty."
    lloyd_narrating neutral "It’s the same vision as last time, with one difference:[wait_05] I can see more of the scene."
    # zoom out
    lloyd_narrating neutral "I can see Docherty’s victim."
    lloyd_narrating neutral "A man wearing a loud suit, his hair drowning in product."
    lloyd_narrating neutral "He’s completely calm, able to stare death in the eye without a reaction."
    man_in_black "You are in my way.[wait_1] You must be removed."
    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
    scene apartment_night
    lloyd_narrating neutral "I’m back in my apartment alongside a splitting migraine."
    lloyd_narrating neutral "It hurts to move, let alone think.[wait_1] Is this the consequence of forcing a vision to manifest?"
    lloyd_narrating neutral "If so then I’ll remember this cost.[wait_1] This isn’t something that I want to do again."
    lloyd_thinking thinking "Was that even worth it?"
    lloyd_thinking thinking "I saw Docherty once again even though he’s dead.[wait_1] I still have no idea what I’m seeing."
    lloyd_narrating neutral "There was one new thing that I saw.[wait_1] Docherty’s next victim, the man in the loud suit."
    lloyd_thinking thinking "Who is that?[wait_1] And why does Docherty want him dead?"
    lloyd_narrating neutral "The intense pain of the migraine is still drilling its way into my head."
    lloyd_narrating neutral "For a while I try to keep my head empty and focus on dealing with the pain."
    lloyd_narrating neutral "After a long time, once it’s dulled slightly, I come to a new conclusion."
    lloyd_thinking thinking "I don’t know why I’m seeing Docherty despite his death."
    lloyd_thinking thinking "I don’t know what this vision is or when it’s taking place."
    lloyd_thinking thinking "But I do know that a man could be in danger."
    lloyd_thinking thinking "I’m going to focus on finding out whether he’s still alive and contacting him."
    lloyd_thinking thinking "If he’s alive I can warn him that he might be in danger, and if he’s dead then I know that I’m seeing the past."
    lloyd_narrating neutral "My migraine continues to hammer its way into my skull, but I eventually drift off to a dreamless sleep."
    scene black_bg with slow_dissolve
    mental_jack "Dammit...[wait_05]the migraine is too much...[wait_05]I can’t do it tonight."
    mental_jack "I’ll have to try again another time."

    return

label branch_c_2_0:
    # power upgrade
    $ branch = "c"
    $ day = 2
    call screen chapter_breaks("WEDNESDAY", "Allan Docherty, the man in black, is dead.\n\nThere shouldn’t be any more murders now. Everything should be fine from here.")
    scene apartment_day with slow_dissolve
    lloyd_narrating neutral "I wake up the next day with my head feeling somewhat better and a better sense of what to do."
    lloyd_narrating neutral "Although Docherty is dead I saw a vision of him committing a murder.[wait_1] I was able to see a little more of the victim, but not enough to easily identify him."
    lloyd_narrating neutral "I’m less sure now than ever of how real the threat is."
    lloyd_thinking thinking "I won’t let that stop me.[wait_1] I’m going to find his victim and warn them."
    lloyd_thinking thinking "If what I’ve seen has any chance of coming true there’ll be a chance of stopping it."
    lloyd_thinking thinking "Where should I go to try and identify Docherty’s victim?"
    call screen map_navigation(find_locations([]))

label branch_c_2_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "The second day of my hunt for the serial killer has come to a close.[wait_1] I still don’t know whether what I’m doing even matters."
    lloyd_narrating neutral "Docherty is already dead, and the visions I’ve seen seem irrelevant."
    lloyd_narrating neutral "I don’t know who killed the man with the white streak or how I could stop them.[wait_1] But if I don’t do what I can then I won’t be able to forgive myself."
    lloyd_narrating neutral "I need to find the man with the loud suit and warn him."
    lloyd_narrating neutral "The only problem is that I have no idea who that man with the loud suit is or how I can find him."
    lloyd_narrating neutral " Ideally my contacts will have been doing the necessary work but there’s no guarantee that they’ve discovered anything."
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "I travel to my favourite restaurant.[wait_1] If I’m going to be thinking it over, there’s no reason not to have a good meal while I’m doing so."
    lloyd_thinking thinking "What sort of meal do I want, though...?"
    menu:
        "Kung Pao Chicken":
            lloyd_narrating neutral "The server passes me a plate stacked high enough with the kung pao chicken I’ve ordered that I’m moderately concerned it will spill off the edges."
            lloyd_narrating neutral "I carry it back to my table and as usual am delighted by how delicious the meal is."
            lloyd_narrating neutral "The chilli present has been absorbed well by the chicken and adds a satisfying kick to the meal."
            lloyd_narrating neutral "The soft texture of the chicken itself is contrasted well by the peanuts and vegetables, with the included rice rounding out the dish very well."
        "Yangzhou fried rice":
            lloyd_narrating neutral "I receive a steaming pile of fried rice from the server which I eagerly take to my table."
            lloyd_narrating neutral "At this restaurant it includes both pork and chicken, which provide a pleasant difference in both taste and texture to one another."
            lloyd_narrating neutral "The rice itself is slightly oily, but it’s packed with flavour and tastes just as good as the ingredients it was cooked with."
        "Zhajiangmian":
            lloyd_narrating neutral "I order the zhajiangmian, which earns me a nod of approval from the server in addition to a bowl containing my meal."
            lloyd_narrating neutral "The delicious crunch of the vegetables leaves no doubt in my mind that I’ve made the correct choice, which is proven further once I get to the noodles."
    lloyd_narrating neutral "But I’m not here to review food.[wait_1] I’m here to think about what my next step should be."
    lloyd_thinking thinking "Who would be the most likely to have made progress in discovering who the man in the loud suit is?"
    $ c_2_4_visited = None
    menu:
        "Barbara" (locked=not person_visited("barbara", "c", 0) or not check_boolean("barbara_investigates_sergei"), message=("You did not visit the bar today" if not person_visited("barbara", "c", 0) else "You did not convince Barbara to help find the man in the loud suit")):
            jump branch_d_2_4
        "Cat" (locked=not person_visited("cat", "c", 0), message="You did not visit the library today"):
            lloyd_thinking thinking "Cat definitely knew something about the man in the loud suit.[wait_1] I’d be stupid not to follow her up further."
            $ c_2_4_visited = "cat"
        "Eddie" (locked=not person_visited("eddie", "c", 0) or not check_boolean("eddie_investigates_sergei"), message=("You did not visit the newspaper today" if not person_visited("eddie", "c", 0) else "You did not convince Eddie to help find the man in the loud suit")):
            lloyd_thinking thinking "Eddie found me information on Allan Docherty.[wait_1] I’m going to trust that he found out about the man in the loud suit."
            $ c_2_4_visited = "eddie"
        "Graves" (locked=not person_visited("graves", "c", 0), message="You did not visit the detective agency today"):
            lloyd_thinking thinking "Graves was confident that he could find this person even with little information.[wait_1] I hope that his confidence isn’t unfounded."
            $ c_2_4_visited = "graves"
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I finish my meal and pay for it, then begin travelling.[wait_1] It’s getting cold, and at times like these I wish that I had a car."
    lloyd_narrating neutral "But I’ve always prioritised spending money on my camera, and there’s plenty of equipment that I want to buy before I think about purchasing something as expensive as a car."
    lloyd_thinking thinking "Still...[wait_1]the company cars at {i}The Brief{/i} were useful.[wait_1] Sometimes I miss working there."
    lloyd_narrating neutral "I recall my last few days at the newspaper.[wait_1] There were also plenty of times that I didn’t enjoy working there."
    if (c_2_4_visited == "cat"):
        scene library_night with slow_dissolve
        lloyd_narrating neutral "Fortunately for me, the library is still open despite the hour."
        lloyd_narrating neutral "I wander around for a few minutes, trying to find Cat.[wait_1] I assumed that she would be here, but now that I’m here it occurs to me that her shift may have ended earlier."
        lloyd_narrating neutral "I begin my second lap of the silent library when I see something that takes me by surprise."
        scene cg6_0 with slow_dissolve
        lloyd_thinking thinking "It’s the man in the loud suit![wait_1] And it’s telling me where to find him!"
        lloyd_narrating neutral "According to the flyer, the man’s name is Sergei Maskelyne, and he’s performing a “one-of-a-kind magic act” tonight."
        lloyd_narrating neutral "I don’t know whether the flyer was here during the day and I missed it, or whether it was placed up after I left."
        lloyd_narrating neutral "It doesn’t matter.[wait_1] I now know where I can find Sergei, so that I can warn him." 
        lloyd_narrating neutral "There’s just one issue."
        lloyd_thinking thinking "This venue...[wait_05]it’s in the north end of the city.[wait_1] How long will it take me to get there?"
        lloyd_narrating neutral "It’s doubtful that I can make it to the venue before the show starts, especially with how long I’ll have to wait for a train."
        lloyd_narrating neutral "But it’s worth the attempt regardless."
        scene black_bg with slow_dissolve
        lloyd_narrating neutral "My heart is racing as I leave the library and run towards the nearest train station."
        lloyd_narrating neutral "Sergei can be saved.[wait_1] If he’s willing to be open with me I may find out why he’s a target of the unknown assassin."
        lloyd_narrating neutral "This is a massive leap forwards in stopping the killer."
    elif (c_2_4_visited == "eddie"):
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "I’m slightly surprised when I’m told that Eddie is still present at the newspaper."
        lloyd_narrating neutral "I’m directed to the same interview room as before and asked to wait until he arrives."
        $ current_thought_block = "mind_read_eddie"
        $ swap_sprites("eddie_angry", slow_dissolve)
        $ current_thought = "eddie_thought_148"
        show screen psychic_powers
        eddie "Your good fortune is my bad, eh, Chen?"
        lloyd neutral "What do you mean?"
        eddie "Good news for you:[wait_05] I’m pretty sure that I’ve found your guy."
        eddie "Bad news for me:[wait_05] I wasted a tonne of time on it, so I’ve had to stay back to catch up on the work I missed."
        eddie "But hey, that’s more good news for you, right?[wait_1] Since it means that I’m here, now, to give you the info."
        $ current_thought = "eddie_thought_149"
        lloyd neutral "I’m sorry, Eddie.[wait_1] I didn’t think that you would –"
        eddie "Like hell you didn’t, Chen.[wait_1] But it’s not like any of that really matters to you, right?"
        lloyd neutral "Eddie, I –"
        eddie "Save it.[wait_1] The faster we get this over with, the sooner I can get back to the important shit."
        lloyd_narrating neutral "Eddie unfolds a piece of paper and passes it over to me."
        scene cg6_0 with slow_dissolve
        $ current_thought = "eddie_thought_150"
        eddie "This is the guy you wanted me to find, right?[wait_1] Sergei Maskelyne?"
        lloyd neutral "Yes.[wait_1] It’s a perfect match."
        eddie "Dunno why you couldn’t have told me that he was a magician...[wait_05]would have made things a lot easier."
        scene office_interview_room with quick_dissolve
        $ swap_sprites("eddie_angry", quick_dissolve)
        eddie "He’s playing a show tonight in the northern end of town."
        eddie "Not sure whether or not you can make it, but as far as I’m concerned, that’s your problem."
        lloyd_thinking thinking "The venue on the poster...[wait_05]how long will it take me to get there?"
        $ current_thought = "eddie_thought_151"
        lloyd neutral "Thank you, Eddie –[wait_05] I won’t forget this."
        eddie "Yeah, sure you won’t."
        hide eddie_angry with quick_dissolve
        hide screen psychic_powers
        scene black_bg with slow_dissolve
        lloyd_narrating neutral "I quickly leave the newspaper and begin walking towards the nearest train station."
        lloyd_narrating neutral "I might miss the opening of Sergei’s act, but I should be able to warn him in time and save him from the killer."
        lloyd_narrating neutral "Bit by bit, I’m making progress."
    elif (c_2_4_visited == "graves"):
        scene detective_office with slow_dissolve
        lloyd_narrating neutral "I’m incredibly relieved when Graves responds to the intercom and unlocks the door for me.[wait_1] I don’t know what I would have done if he hadn’t been in."
        $ current_thought_block = "mind_read_graves"
        $ swap_sprites("graves_smiling", quick_dissolve)
        $ current_thought = "graves_thought_160"
        show screen psychic_powers
        graves "Hey, Lloyd.[wait_1] Care to join me in a container of takeaway?"
        graves "Fair warning, though –[wait_05] I don’t think that we’ll both fit."
        lloyd_narrating neutral "He holds out a cheap plastic container to me, half-filled with noodles.[wait_1] I shake my head."
        $ current_thought = "graves_thought_161"
        lloyd neutral "Thank you, Graves, but I’d much rather hear whether you’ve discovered anything about the man in the loud suit."
        lloyd_thinking thinking "Because if you haven’t, I need to get out of here and seek a different source of information."
        graves "No worries, Lloyd.[wait_1] Take a squiz at this –[wait_05] look familiar?"
        scene cg6_0 with slow_dissolve
        lloyd_thinking thinking "It’s a perfect match for the man in the loud suit.[wait_1] It’s advertising a magic act of some kind."
        $ current_thought = "graves_thought_162"
        graves "If this is your guy, his name is Sergei Maskelyne.[wait_1] Apparently he’s playing at a venue up north tonight."
        lloyd neutral "Yes, you’re correct –[wait_05] this is the person I was looking for."
        lloyd_thinking thinking "The north end of the city...[wait_05]how long would it take me to get there?[wait_1] If I’d known that this was what I’d be told I’d have shown up earlier in the evening."
        $ current_thought = "graves_thought_163"
        scene detective_office with quick_dissolve
        $ swap_sprites("graves_smiling", quick_dissolve)
        graves "If you want to meet with the guy, you’ll have to hurry.[wait_1] I don’t know if you can make the start of the show, but it’s better to show up late and chat to him than not at all, yes?"
        lloyd neutral "Yes...[wait_05]you’re right, Graves."
        lloyd neutral "Thank you for the information –[wait_05] I really appreciate it."
        graves "Hey, no worries –[wait_05] it comes with the job.[wait_1] Anything else that I can help you with?"
        lloyd neutral "Not at present...[wait_05]I’d better get moving." 
        lloyd neutral "Thanks again, Graves."
        graves "You’re welcome.[wait_1] Good luck!"
        hide graves_smiling with quick_dissolve
        hide screen psychic_powers
        scene black_bg with slow_dissolve
        lloyd_thinking thinking "Thank goodness Graves understood that I didn’t want to talk for too long."
        lloyd_thinking thinking "I’ve got to get to the nearest train station and make my way northwards, and then things will be fine."
        lloyd_thinking thinking "I’ll talk to Sergei, warn him about the killer, and save him.[wait_1] I won’t fail him like I failed the man with the white streak."
    call screen chapter_breaks("LATER", "At 9:11 PM, Lloyd reaches the venue hosting Sergei’s show.\n\nSomebody else reached it at 8:32 PM.")
    # TODO: Add some red/blue slow flashes here
    scene venue_exterior with slow_dissolve
    lloyd_narrating neutral "I’m too late."
    lloyd_narrating neutral "Waiting for a train took long enough that I knew I wouldn’t be able to make the show itself.[wait_1] But I thought that the delay wouldn’t affect the evening drastically."
    lloyd_narrating neutral "I thought that I would be able to meet with Sergei, or at least to get his contact details from one of the venue staff."
    lloyd_narrating neutral "But as I approach the venue I see blue and red lights flashing, accompanying the police tape at the entrance to the venue."
    lloyd_thinking thinking "My vision did come true, then.[wait_1] At least, the part of it where Sergei was killed did."
    lloyd_thinking thinking "But who killed him?"
    lloyd_narrating neutral "A small crowd has gathered, and it’s clear that they’re not here because they want to go into the venue."
    lloyd_narrating neutral "Not when there’s a crime scene to investigate and clues to be found.[wait_1] Not when there’s a dead body inside, the skull opened up by a bullet at close range."
    lloyd_narrating neutral "I walk towards the closest person.[wait_1] I already know what’s happened but they might have information that I don’t have."
    $ current_thought_block = "mind_read_cat"
    $ swap_sprites("cat_neutral", quick_dissolve)
    show screen psychic_powers
    if (person_visited("cat", "a", 0) or person_visited("cat", "c", 0)):
        if (check_boolean("cat_name_discovered")):
            $ current_thought = "cat_thought_112"
            lloyd_narrating neutral "As I get closer I’m surprised to see that it’s Cat."
            lloyd_thinking thinking "What’s she doing here?"
            lloyd neutral "Hey, Cat."
        else:
            $ current_thought = "cat_thought_113"
            lloyd_narrating neutral "As I get closer I’m surprised to see that it’s the librarian."
            lloyd_thinking thinking "What’s she doing here?"
            lloyd neutral "Hey, um...[wait_05]you."
            lloyd_narrating neutral "She turns to me with a cold glare on her face."
            $ swap_sprites("cat_cold")
            $ current_thought = "cat_thought_112"
            librarian "Oh.[wait_1] You."
            lloyd neutral "It is."
            $ current_thought = "cat_thought_114"
            librarian "The name’s Cat."
            lloyd_thinking thinking "Short for Catherine?"
            $ current_thought = "cat_thought_115"
            lloyd neutral "Understood."
            $ swap_sprites("cat_neutral")
    else:
        lloyd neutral "Hey, my name’s Lloyd.[wait_1] Do you have a minute?"
        $ current_thought = "cat_thought_116"
        unknown "...I’m Cat."
        lloyd_thinking thinking "She didn’t say that I couldn’t talk to her."
    $ current_thought = "cat_thought_117"
    lloyd neutral "What happened here?"
    cat "There was...[wait_1]a show that was going on here.[wait_1] Stage magic."
    cat "During the intermission...[wait_1]the performer went backstage."
    cat "Then...[wait_1]maybe five minutes later there was a loud noise."
    $ current_thought = "cat_thought_118"
    lloyd neutral "Like a gunshot?"
    lloyd_narrating neutral "She nods slowly, as though only considering the possibility now."
    $ current_thought = "cat_thought_119"
    cat "The staff checked what happened...[wait_1]then we were told to leave while the police were called."
    cat "But not everybody...[wait_1]is here."
    lloyd_thinking thinking "She doesn’t seem overly surprised or shaken.[wait_1] Why is that?"
    $ current_thought = "cat_thought_120"
    lloyd neutral "Was there anyone suspicious around?"
    $ current_thought = "cat_thought_121"
    cat "No...[wait_1]not that I saw.[wait_1] But someone else might have seen something."
    lloyd neutral "Alright.[wait_1] Thank you for answering my questions."
    lloyd_narrating neutral "She stares at me for several seconds before returning her focus to the venue."
    hide cat_neutral with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "I ask a few other people whether they saw anyone suspicious but none of the answers are positive."
    lloyd_narrating neutral "From the sound of things if the loud bang –[wait_05] the gunshot –[wait_05] weren’t so loud none of the patrons would have guessed that anything was amiss."
    lloyd_narrating neutral "At the end of it all I haven’t learned anything conclusive."
    lloyd_narrating neutral "I have no new information, other than that I missed my opportunity to warn Sergei about the killer that was coming for him."
    lloyd_thinking thinking "But why was the killer coming for him?[wait_1] What was it about Sergei –[wait_05] and the man with the white streak –[wait_05] that made the killer determined to silence them?"
    lloyd_thinking thinking "I’ll have to look further into Sergei tomorrow –[wait_05] I know his name, but I don’t have enough information about who he is."
    lloyd_narrating neutral "I won’t learn anything else here.[wait_1] I return to the train station and head home."
    scene black_bg with slow_dissolve

label branch_c_3_0:
    # Power upgrade
    $ branch = "c"
    $ day = 3
    call screen chapter_breaks("THURSDAY", "Despite his best efforts, Lloyd was unable to save Sergei Maskelyne from being killed. His psychic powers haven’t shown him any further visions.\n\nHe has no warning of what’s coming.")
    scene apartment_day with slow_dissolve
    lloyd_thinking thinking "I wasn’t able to save Sergei.[wait_1] If I’d found where he was sooner then I could have warned him about the killer."
    lloyd_thinking thinking "But I was too late.[wait_1] Once again I failed to save someone, and their blood is on my hands."
    lloyd_narrating neutral "I try not to dwell on my failure.[wait_1] I can’t change the choices that I’ve made, but that’s a bitter comfort."
    lloyd_narrating neutral "It’s too easy to consider what I could have done differently and wish for a way to make that change real.[wait_1] To linger on the past and imagine what things would look like in the present."
    lloyd_thinking thinking "I can’t change the past but I can move forward with what I have now."
    lloyd_thinking thinking "I may not have been able to save Sergei, but I did gain something:[wait_05] his death confirms the vision I had."
    lloyd_thinking thinking "I don’t know who his killer is or how they relate to Docherty, but he was the target, as I saw."
    lloyd_thinking thinking "Why was that?[wait_1] Why did he need to be silenced?"
    lloyd_thinking thinking "If I can discover more about who Sergei Maskelyne was, I might be able to work out why the killer silenced him –[wait_05] and from that, the killer’s next target."
    lloyd_thinking thinking "Where should I go to research Sergei?"
    call screen map_navigation(find_locations([]))

label branch_c_3_4:
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "Once again I head to my favourite restaurant for a meal.[wait_1] I wouldn’t normally eat out this much but I want to keep things moving."
    lloyd_narrating neutral "There’s not enough time in the day to talk to everybody that I want to.[wait_1] For now though, I need to slow down and take a break."
    lloyd_thinking thinking "What am I in the mood for...?"
    menu:
        "Chow mein":
            lloyd_narrating neutral "The noodles of my meal glisten appealingly in the light as I bring the plate over to my table."
            lloyd_narrating neutral "Once I’ve sat down and begun eating it’s hard for me to stop."
            lloyd_narrating neutral "The sauce has been deeply absorbed into the pieces of chicken, meaning that every piece of meat is a veritable goldmine of flavour."
            lloyd_narrating neutral "The contrast of the softness of the noodles and meat against the crisp texture of the vegetables creates an enjoyable sensation even as I chew the food."
        "Lemon chicken":
            lloyd_narrating neutral "I order the lemon chicken with a side of rice and receive a plate of food for my troubles."
            lloyd_narrating neutral "I’ve been to several places in the past where the sauce is too thick, or too sticky, but that’s far from the case here –[wait_05] it’s the exact right texture, without being so sweet as to become sickening."
            lloyd_narrating neutral "The chicken itself has a generous coating of crumbs, and despite being a little colder than I’d like is still more than sufficient to satisfy me."
        "Dumplings":
            lloyd_narrating neutral "While waiting in line to order a new batch of dumplings has been taken out of the wok and placed into the display."
            lloyd_narrating neutral "They won’t get any better than this, and so ordering them is the obvious decision."
            lloyd_narrating neutral "The dumplings are crisp enough to create a satisfying crunch as I bite into each of them, immediately juxtaposed with the softness of their meat interiors."
            lloyd_narrating neutral "I notice how many dumplings I was served and regret not ordering more."
    lloyd_narrating neutral "As I eat my meal I think about my actions."
    lloyd_narrating neutral "Yesterday I could have saved Sergei if I’d arrived at the venue a bit earlier –[wait_05] how much later would I have been if I had returned home and cooked?"
    lloyd_narrating neutral "Eating at the restaurant is a good time, if not cost, saving measure, but I can’t spend all night here."
    lloyd_thinking thinking "And with that in mind...[wait_05]what is my next move from here?[wait_1] What should I do for the remainder of the evening?"
    menu:
        "Visit the venue":
            if (person_visited("barbara", "c", 1)):
                lloyd_thinking thinking "Barbara suggested that I travel to the venue where Sergei worked."
                lloyd_thinking thinking "She suggested that I talk to the owners there and ask what they know about Sergei and what sort of person they are."
            elif (person_visited("graves", "c", 1)):
                lloyd_thinking thinking "Graves said that investigating Sergei’s background would take a while, and suggested that I visit the venue where he performed to talk to the owners while he starts his investigation."
            lloyd_narrating neutral "It’s the obvious decision to make...[wait_05]so obvious, in fact, that I’m annoyed I didn’t think of it myself."
            lloyd_thinking thinking "I suppose that I was hoping for something more –[wait_05] something with more importance, something more secretive."
            lloyd_thinking thinking "But a lead is a lead.[wait_1] I’ll finish this meal and visit the venue."
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "Once I’m done I wait for a train at the station, the cold wind from the tunnel chilling me.[wait_1] It eventually arrives and I’m brought to my station."
            lloyd_narrating neutral "There’s nothing else to do from here but walk to the venue."
            scene venue_exterior with slow_dissolve
            lloyd_narrating neutral "The police tape is still present but the flashing lights are gone."
            lloyd_narrating neutral "A handwritten note says that the venue has closed for the next several nights." 
            lloyd_narrating neutral "I suppose that they have a bit of damage control to do –[wait_05] they can’t have potential attendees fearful that the same incident will repeat itself."
            lloyd_narrating neutral "I duck under the police tape and enter the venue."
            lloyd_narrating neutral "If the staff aren’t present I may still be able to find some physical evidence that can tell me what sort of person Sergei was."
            lloyd_narrating neutral "I doubt that the police will still combing for clues nearly twenty-four hours after the murder, but if I am questioned I can claim to be an employee of the venue."
            scene venue_interior with slow_dissolve
            lloyd_narrating neutral "The interior of the venue is more or less what I expected it to be."
            lloyd_narrating neutral "There’s a stage where Sergei –[wait_05] or a band –[wait_05] could perform while people eat or drink."
            lloyd_narrating neutral "The atmosphere is dim and moody, but it’s clearly been intentionally cultivated by the owners."
            lloyd_narrating neutral "Does it lead to more alcoholic purchases?[wait_1] Or it to accompany the act on the stage?"
            lloyd_narrating neutral "It’s clear that I won’t find any clues around here, but there might be a private locker or storage of Sergei’s in the back of the venue."
            lloyd_narrating neutral "I step up onto the stage and cross it."
            unknown "Hey, you![wait_1] What are you doing here?"
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "My assumption turns out to be wrong.[wait_1] The police are still here, waiting to see whether the killer will return to the scene of the crime."
            lloyd_narrating neutral "I’m questioned by the officer who caught me and although I protest my innocence, they stop listening once I’m recognised as the person who was found with the man with the white streak."
            lloyd_narrating neutral "If I hadn’t gone to Sergei’s venue, I wouldn’t have been locked up for questioning."
            lloyd_narrating neutral "And while I doubt that I’ll end up with strong charges, for now my role in the investigation is done."
            narrator "GAME OVER"
            $ MainMenu()
        "Visit Cat" (locked=not person_visited("cat", "c", 1) or not check_boolean("cat_retrieves_notes"), message=("You did not visit the library today" if not person_visited("cat", "c", 1) else "You did not convince Cat to retrieve Sergei's notes")):
            lloyd_thinking thinking "Visiting Cat is the obvious decision to make."
            lloyd_thinking thinking "She said that she could get me some notes that Sergei has.[wait_1] It’s the next best thing to talking to the man himself and discovering why he was targeted by the killer."
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "I finish my meal and then travel towards the library that Cat works at."
            lloyd_narrating neutral "She won’t be working at this hour –[wait_05] it will be the home ground advantage that’s decided the meeting place."
            lloyd_narrating neutral "I’m wary of what she hopes to get out of this but all that I can do is follow her lead."
            lloyd_narrating neutral "The park is a strong contrast in the evening to how it was during the day."
            lloyd_narrating neutral "Occasionally a cyclist rides past me, and I can hear the sounds of some skateboarders from somewhere else, but otherwise it’s both empty and quiet."
            lloyd_narrating neutral "I photograph some trees as I go, silhouetting them against the moon."
            lloyd_narrating neutral "I wonder what information Cat will give me, and how she acquired it."
            scene library_night with slow_dissolve
            $ swap_sprites("cat_neutral", slow_dissolve)
            $ current_thought = "cat_thought_135"
            show screen psychic_powers
            lloyd_narrating neutral "Cat is standing with her off to the side with her back to the wall, every bit a living shadow."
            lloyd_narrating neutral "She doesn’t acknowledge my presence in any way as I approach."
            lloyd neutral "Hello, Cat."
            cat "Hello."
            lloyd_narrating neutral "She holds up something small and silver.[wait_1] After a moment I recognise it as a USB drive."
            $ current_thought = "cat_thought_136"
            cat "This USB contains a PDF...[wait_1]it has notes written by Sergei."
            cat "You should find them very...[wait_1]illuminating."
            $ current_thought = "cat_thought_137"
            lloyd neutral "Notes written by Sergei?[wait_1] How did you acquire them?"
            lloyd_thinking thinking "Was she able to access his personal computer?[wait_1] How did she do that?"
            cat "That’s my business...[wait_1]not yours." 
            cat "Do you want the drive...[wait_1]or not?"
            lloyd_narrating neutral "I’m wary of why she’s giving me this information so freely."
            lloyd_narrating neutral "Does she want something in return?[wait_1] Or is she attempting to mislead me?"
            lloyd_narrating neutral "I don’t have a computer on me and can’t verify that it really contains the file she claims."
            $ current_thought = "cat_thought_138"
            lloyd neutral "Why didn’t you ask for my email address and send the file to me that way?[wait_1] Or upload the file to the cloud?"
            lloyd_narrating neutral "Her head shakes almost imperceptibly.[wait_1] It’s the most emotion that she’s shown thus far."
            cat "This is...[wait_1]for your eyes only."
            lloyd_thinking thinking "That doesn’t answer the question.[wait_1] I don’t think that I’ll get a straight answer from her."
            lloyd_narrating neutral "I’m still uncertain of her motivations.[wait_1] There has to be some catch to this but I can’t identify it."
            lloyd_narrating neutral "And I want those notes."
            $ current_thought = "cat_thought_139"
            lloyd neutral "Alright.[wait_1] I’d like the USB then."
            lloyd_narrating neutral "She passes it to me without issue."
            $ current_thought = "cat_thought_140"
            cat "If you’d like to meet again...[wait_1]come back here tomorrow evening."
            hide cat_neutral with quick_dissolve
            hide screen psychic_powers
            lloyd_narrating neutral "Cat walks further into the depths of the library, melting into the shadows as she goes."
            lloyd_narrating neutral "I debate going after her but decide that it isn’t worth it.[wait_1] I got what I wanted from the meeting."
            lloyd_thinking thinking "Why did she say that I can meet her again tomorrow?"
            lloyd_thinking thinking "Does she think that something in the file will make me want to?[wait_1] She has to have read it herself."
            lloyd_narrating neutral "The only way that I’ll find out is by seeing what’s on the USB.[wait_1] I exit the library and return to my apartment."
            scene black_bg with slow_dissolve
            scene apartment_night with slow_dissolve
            lloyd_narrating neutral "I’ve turned on my computer and connected the USB drive."
            lloyd_narrating neutral "Normally my computer is primarily used for editing my photographs and reading my emails."
            lloyd_narrating neutral "It’s more than up to the task of reading a simple PDF, though."
            lloyd_narrating neutral "I click on the file and read through the first few pages."
            call screen read_pdf()
            lloyd_narrating neutral "What I find in the file astonishes me."
            lloyd_thinking thinking "According to this file, Sergei has –[wait_05] had –[wait_05] psychic abilities.[wait_1] I don’t believe his claims about their origin, but he writes that it isn’t the only way to acquire powers."
            lloyd_thinking thinking "One of the other methods is to be near someone with psychic abilities who dies –[wait_05] their powers can be passed on, often involuntarily."
            lloyd_narrating neutral "I stop and think about this."
            lloyd_narrating neutral "I’ve been using my psychic abilities for the past three days fairly liberally without thinking too much about where they came from.[wait_1] It was hardly the most important mystery that I had to solve."
            lloyd_narrating neutral "This information puts it in a new light."
            lloyd_thinking thinking "The man with the white streak...[wait_05]I was near him when he died.[wait_1] Is it possible that he had psychic abilities?"
            lloyd_narrating neutral "He could have passed them on to me.[wait_1] The headache which led to my powers only began once I touched his hand."
            lloyd_narrating neutral "It lines up well enough that I’m wondering why I didn’t consider it before."
            lloyd_thinking thinking "Did the killer know that the man with the white streak had psychic abilities?"
            # Potentially make it that players need to rescroll here themselves?
            lloyd_narrating neutral "I scroll back to the top of the document to confirm the information that I saw earlier."
            lloyd_narrating neutral "Sergei claimed to have psychic abilities of his own.[wait_1] That makes one thing that he and the man with the white streak have in common."
            lloyd_narrating neutral "That, and having the same killer."
            lloyd_thinking thinking "The man in black has killed at least two psychics.[wait_1] Likely he has others on his hit-list."
            lloyd_thinking thinking "But what could his motivation be?[wait_1] He didn’t appear to have taken anything from the man with the white streak."
            lloyd_narrating neutral "A moment later the realisation hits me."
            lloyd_thinking thinking "Wait...[wait_05]that’s it.[wait_1] The killer didn’t take anything from him, but I did –[wait_05] his psychic powers."
            lloyd_thinking thinking "The killer is murdering psychics so that he can try to acquire their powers.[wait_1] He wants to become a psychic himself."
            lloyd_narrating neutral "Does he want to read minds and discover what secrets he can?[wait_1] Look into the future and change the outcome?[wait_1] Wipe minds and remove memories of his crimes?"
            lloyd_narrating neutral "I can’t say for sure but it’s more evidence that the man in black needs to be stopped."
            lloyd_narrating neutral "I return to Sergei’s notes to see what other insights they might have." 
            # Another potential scroll bit
            lloyd_narrating neutral "But when I scroll further down the PDF I discover an issue."
            lloyd_thinking thinking "The file –[wait_05] it’s been truncated![wait_1] By Cat, I’d be willing to bet."
            lloyd_thinking thinking "That’s why she told me that we could meet again tomorrow –[wait_05] she’s planning something."
            if (check_boolean("cat_preparing_trap")):
                lloyd_thinking thinking "That also explains why she was thinking about lowering my guard.[wait_1] She knew that I would have no choice to return."
            lloyd_narrating neutral "I mull my thoughts around in my head.[wait_1] Cat has further information of Sergei’s which could prove to be important."
            lloyd_narrating neutral "Nothing’s forcing me to see her, but the existing notes have given me insight and motivation into the killer."
            lloyd_thinking thinking "It’s no choice at all.[wait_1] I have to discover what’s in those notes."
            lloyd_thinking thinking "They could contain other important information."
            lloyd_narrating neutral "My main priority for tomorrow, then, will be visiting Cat in the evening and retrieving Sergei’s remaining notes from her."
            lloyd_narrating neutral "Or...[wait_05]should I?[wait_1] Waiting around all day would be a waste of my time."
            lloyd_narrating neutral "Every day that passes is a ticking clock until the killer murders once again."
            lloyd_thinking thinking "What were the names of the people that Sergei said assisted him with these notes...?[wait_1] Charles Eisenhardt and Morty Telemachus."
            lloyd_thinking thinking "If I can contact one of them they might be able to give me the notes.[wait_1] It’s worth a try."
            lloyd_narrating neutral "I enter Charles’ name into a search engine.[wait_1] The result isn’t what I expected."
            lloyd_thinking thinking "Dead.[wait_1] Killed by an unknown assailant, via gunshot.[wait_1] It’s the same for Telemachus."
            lloyd_narrating neutral "If I had any doubts that the killer is targeting psychics they’ve been erased by now."
            lloyd_narrating neutral "Eisenhardt and Telemachus clearly had psychic abilities of their own, and I’ve deduced that the man with the white streak had some."
            lloyd_narrating neutral "I’ll have to go to Cat for the remaining notes after all."
            lloyd_thinking thinking "But I won’t be idling during the day.[wait_1] I still have no idea how the killer discovered that any of his victims were psychic."
            lloyd_thinking thinking "I’ll do what I can to discover who they were, and whether there was some telltale sign of their abilities which put them in the killer’s crosshairs."
            lloyd_narrating neutral "It’s a solid plan."
            lloyd_narrating neutral "With no other information that I can retrieve from the notes I turn off my laptop and go to bed."
            lloyd_narrating neutral "It’s getting late and I want to catch up on my rest."
            scene black_bg with slow_dissolve
            mental_jack "{size=-8}(Dammit...[wait_05]I’m too weak.){/size}"
            mental_jack "{size=-8}(I thought I could build up my strength more...[wait_05]but I can’t.[wait_1] It’s all over.){/size}"
            mental_jack "{size=-8}(I didn’t even get to have any fun the other night...){/size}"
    return