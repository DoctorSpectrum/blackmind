label branch_e_3_4:
    lloyd_narrating neutral "The temptation to stay put and look after myself is high.[wait_1] I don’t want the next bullet to hit me any more than Eddie wants it to hit him."
    lloyd_narrating neutral "But as I consider how that would play out I’m reminded of Graves."
    scene detective_office at greyscale_instant with slow_dissolve
    show graves_smiling at greyscale_instant, center with quick_dissolve
    graves "There’s no reason to prioritise my needs above others’."
    graves "My problems –[wait_05] my needs, they –[wait_05] they aren’t inherently any more important than yours, or anybody else’s, are." 
    graves "So why shouldn’t I help others if I can?"
    hide graves_smiling
    scene office_interview_room with quick_dissolve
    lloyd_thinking thinking "Graves is right.[wait_1] I shouldn’t prioritise myself."
    lloyd_thinking thinking "Eddie’s out there trying to stop someone who’s targeting me –[wait_05] he’s putting my needs above his."
    lloyd_thinking thinking "There’s no reason not to help him."
    lloyd_narrating neutral "I move away from the table and towards the shattered remains of the door, keeping low all the time."
    lloyd_narrating neutral "My instinct is to crawl on all fours and stay even lower to the ground but all of the scattered glass would shred my hands to ribbons."
    lloyd_narrating neutral "I move past the frame of the door and into the main office of the newspaper."
    lloyd_narrating neutral "I can’t see the shooter.[wait_1] That means that they’re probably hiding behind a table; I can’t imagine they’ve left after those two shots."
    lloyd_thinking thinking "How many other people are in the building?"
    lloyd_thinking thinking "Have any of them called the police?[wait_1] Are any of them still alive?"
    lloyd_narrating neutral "I force myself to stop asking irrelevant questions.[wait_1] Right now all that matters is finding the shooter and helping Eddie stop them."
    lloyd_thinking thinking "But where is Eddie?[wait_1] And what is he planning to do?"
    lloyd_narrating neutral "As I think the words I see the shooter."
    $ swap_sprites("docherty_neutral", quick_dissolve)
    lloyd_narrating neutral "Unsurprisingly it’s Docherty.[wait_1] I don’t know how he knew I would be here."
    lloyd_narrating neutral "I don’t know why he wants me dead.[wait_1] All that matters is that I stop him."
    lloyd_narrating neutral "If I can do that then his threat will be over."
    lloyd_narrating scared "But it won’t be possible."
    lloyd_narrating scared "Just as I’ve seen him, he’s also seen me, and he’s reacting faster."
    lloyd_narrating scared "His thumb is pulling back the hammer of his gun, and he’s raising it up towards me."
    lloyd_narrating scared "I can’t dodge a bullet, not at this range."
    # If we want to lock branches until we get certain endings, now would be an excellent one to lock with the requirement of ending D
    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
    lloyd_narrating neutral "The gun drops from Docherty’s hands.[wait_1] He falls to the ground."
    hide docherty_neutral
    $ swap_sprites("eddie_arrogant", quick_dissolve)
    $ current_thought = "eddie_thought_233"
    show screen psychic_powers
    eddie "You’re welcome, Chen."
    scene cg9_1 with slow_dissolve
    lloyd_narrating neutral "I’m not listening to Eddie."
    lloyd_narrating neutral "A pool of red is spreading below Docherty.[wait_1] His top is already soaked through with blood."
    lloyd_narrating neutral "Eddie has turned out to be a fantastic shot with his gun.[wait_1] Docherty won’t survive for long."
    lloyd_thinking thinking "His threat is over.[wait_1] He won’t harm anyone else again."
    lloyd_thinking thinking "Does he have anything to get off his chest before he dies?"
    lloyd_narrating neutral "I don’t think that there’s much to gain from Docherty when he’s this far gone."
    lloyd_narrating neutral "I also think that it would be cruel to turn my back on him in his dying moments, to not be with him as he dies."
    lloyd_narrating neutral "Eddie steps closer too and listens silently."
    $ current_thought_block = "mind_read_docherty"
    $ current_thought = "docherty_thought_03"
    docherty "{size=-8}Kill...[wait_1]Kill...{/size}"
    lloyd_narrating neutral "They’re the words of a raving madman."
    lloyd_narrating neutral "He’s clearly out of his mind; governed by a logic that only makes sense to his twisted mind."
    lloyd_narrating neutral "His words have no substance to them, and whatever motivation he had for killing his victims and targeting me is lost forever."
    lloyd_narrating neutral "That’s what I initially believe.[wait_1] But then he gathers his strength and tries again."
    docherty "{size=-8}Killian...[wait_1]Morgensen...[wait_1]he’s...[wait_1]the one...{/size}"
    # Potentially make it that here we can choose to read either Eddie or Docherty's mind?
    $ current_thought_block = "mind_read_eddie"
    $ current_thought = "eddie_thoughts_234"
    eddie "What?"
    lloyd_narrating neutral "Docherty’s voice is a wet cough as he struggles to continue.[wait_1] Blood pools out of his mouth and down his chin, creating a bloody mess."
    docherty "{size=-8}Thank you...[wait_1]for stopping...[wait_1]me...{/size}"
    docherty "{size=-8}His control...[wait_1]he’s...[wait_1]inhuman...{/size}"
    $ current_thought = "eddie_thoughts_235"
    eddie "Chen, does any of this make sense to you?"
    lloyd neutral "Who is Killian Morgensen?[wait_1] What do you mean?"
    docherty "{size=-8}Don’t trust...[wait_1]anyone...[wait_1]His...[wait_1]control...{/size}"
    lloyd_narrating neutral "Docherty erupts into a coughing fit then, spraying both Eddie and myself with blood.[wait_1] I don’t care about it; I just want answers."
    lloyd_narrating neutral "But it’s too late."
    scene cg9_0 with slow_dissolve
    lloyd_narrating neutral "Docherty has breathed his last."
    scene office_interview_room with slow_dissolve
    $ swap_sprites("eddie_angry", quick_dissolve)
    $ current_thought = "eddie_thought_229"
    eddie "Well, he definitely won’t be killing again.[wait_1] He’s a goner for sure."
    lloyd_thinking thinking "But is the threat over?[wait_1] It doesn’t sound like it."
    $ current_thought = "eddie_thought_230"
    eddie "I’ll call the police now.[wait_1] Make sure that your story lines up with mine –[wait_05] that this was self defence."
    lloyd neutral "Of course.[wait_1] I imagine the physical evidence will support it."
    eddie "It had better."
    lloyd_narrating neutral "Eddie takes out his phone to call the police."
    lloyd_narrating neutral "Throughout it I’m turning around Docherty’s dying words in my head."
    lloyd_narrating neutral "Was he being controlled by another psychic this entire time?[wait_1] This Killian Morgensen?"
    lloyd_thinking thinking "Eddie might think that it’s over, but I doubt that it is.[wait_1] Not by a long shot."
    hide eddie_angry with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    mental_jack "{size=-8}(Fucking Killian?![wait_1] He was responsible?!){/size}"
    mental_jack "{size=-8}(That bastard...[wait_05]I...[wait_05]I thought that I was too weak, but –[wait_05] no...[wait_05]I can’t just let myself fade away.){/size}"
    mental_jack "({size=-8}I{/size} – I won’t! He won’t get away with this!)"
    return

label branch_e_4_0:
    # power upgrade
    $ branch = "e"
    $ day = 4
    call screen chapter_breaks("FRIDAY", "Lloyd went to bed determined to find out who Killian Morgensen is.\n\nThe next day, it isn’t Lloyd who wakes up in his body.")
    scene cg11_0 with slow_dissolve
    jack_possessing_thinking smug "I’m pretty damn good." (name="???")
    jack_possessing_thinking smug "Who else would feel their psychic abilities transferring into another person’s body as the life started bleeding out of them, and think to push the rest of their mind along with them?" (name="???")
    jack_possessing_thinking smug "Who else would be able to hide in the back of the new host’s mind without being noticed?" (name="???")
    jack_possessing_thinking smug "Who else would manage to gather their strength up and overtake that person’s mind, scrunching them up into a tiny ball and throwing them into the back of the brain?" (name="???")
    jack_possessing_thinking smug "Jack Usbourne, that’s who." (name="???")
    jack_possessing_thinking smug "Sure, I might have tried borrowing the body for a bit the other day and failed since this Lloyd guy had a migraine."
    jack_possessing_thinking smug "Sure, I might not have been able to perceive everything that he’s been up to, and a lot of it’s come through kinda blurry, real distorted and shit."
    jack_possessing_thinking smug "But I’ve got his body now, and I got enough info about who he is that I can definitely impersonate him for the rest of my life."
    jack_possessing_thinking worried "The only problem is the psychic powers.[wait_1] I guess they were weakened or something when they were transferred to this body, because they’re not as strong as when I had them."
    jack_possessing_thinking smug "But it’s cool.[wait_1] I’ll definitely make them stronger and able to be used more over time; it’ll be just like training a muscle."
    jack_possessing_thinking smug "From today on, my new life begins."
    jack_possessing_thinking smug "It’ll take me a little while to get used to pretending to be Lloyd, and I’m pretty torn up about what I’ve done to him.[wait_1] But I reckon he’d agree that it was a worthy sacrifice to undo my premature death."
    jack_possessing_thinking smug "He seemed like a decent enough guy that he definitely would have been okay with it if he’d known about me."
    jack_possessing_thinking smug "Anyway, the best way to get used to my new life is to get out there and start practicing.[wait_1] Meet with some of Lloyd’s friends and get the hang of interacting with them."
    jack_possessing_thinking smug "Who should I start with?"

    call screen map_navigation(find_locations([]))