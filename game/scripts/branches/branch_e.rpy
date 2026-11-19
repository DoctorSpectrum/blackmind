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

label branch_e_4_4:
    scene black_bg with slow_dissolve
    jack_possessing_thinking smug "I’d call that a pretty successful first day."
    jack_possessing_thinking smug "Pretty safe to say that I do a pretty seamless impersonation of Lloyd;[wait_05] nobody guessed that I wasn’t really him.[wait_1] I guess I’m just that good."
    jack_possessing_thinking angry "Just one last thing to deal with before I can really enjoy myself...[wait_05]Killian."
    jack_possessing_thinking angry "Bastard was coming after Lloyd...[wait_05]did he know that I was hiding at the back of his mind and wanted to eliminate me for good?"
    jack_possessing_thinking angry "Whatever, it doesn’t fucking matter.[wait_1] I would have gone to see him even if he hadn’t killed my old body."
    scene killian_house_exterior with slow_dissolve
    jack_possessing_thinking angry "It’s more modest than I expected.[wait_1] But I guess it’s easier for monsters to hide among ordinary people."
    jack_possessing_thinking angry "Alright...[wait_05]just need to get in there, confront him, and put all of this behind me.[wait_1] Then I can keep living the easy life as Lloyd."
    jack_possessing_thinking worried "Is there anything else I have to do before I meet Killian?"
    menu:
        "Yes" (locked=not (check_boolean("barbara_sympathetic") and check_boolean("cat_sympathetic") and check_boolean("eddie_sympathetic")) and not(check_boolean("barbara_sympathetic") and check_boolean("eddie_sympathetic") and check_boolean("graves_sympathetic")) and not (check_boolean("cat_sympathetic") and check_boolean("eddie_sympathetic") and check_boolean("graves_sympathetic")) and not (check_boolean("barbara_sympathetic") and check_boolean("cat_sympathetic") and check_boolean("graves_sympathetic")), message="Jack has not read sufficient thoughts related to Lloyd"):
            jump branch_f_4_4
        "No":
            jack_possessing_thinking smug "Yeah, didn’t think so.[wait_1] Alright, let’s get this shit done and dusted."
    # SFX - doorbell
    $ swap_sprites("killian_smiling", quick_dissolve)
    $ current_thought_block = "mind_read_killian"
    $ current_thought = "killian_thought_01"
    show screen psychic_powers
    killian "Hello, how can I –"
    $ swap_sprites("killian_shocked")
    killian "Oh.[wait_1] It’s you."
    jack_possessing smug "Heya, Killian.[wait_1] How d’ya feel about letting me inside and we can have a nice little chat, like civilised people?"
    $ swap_sprites("killian_smiling")
    killian "Somebody with manners.[wait_1] Yes, I think that sounds good.[wait_1] Come inside."
    jack_possessing_thinking smug "No witnesses to see what’s coming next...[wait_05]exactly how I want it."
    hide killian_smiling with quick_dissolve
    scene killian_house_interior with slow_dissolve
    $ swap_sprites("killian_smiling", quick_dissolve)
    killian "Please, take a seat."
    jack_possessing_thinking angry "If you insist, old man."
    killian "I’d offer you some tea or coffee, but you’ll probably make the assumption that it’s poisoned."
    killian "Now, would I be wrong in presuming that you are here as Docherty informed you about me once my control over him was broken?"
    killian "A pity about that.[wait_1] He really was a most excellent pawn."
    jack_possessing smug "Yeah, something like that."
    killian "I was hoping to replace him with that friend of yours –[wait_05] Mr. Thompson –[wait_05] but I made the mistake of introducing myself when I approached him earlier today for the initial contact."
    killian "He was too cautious and declined to have a meeting with me.[wait_1] I suppose that he also learned of me from Docherty."
    $ swap_sprites("killian_confident")
    $ play_sound("mind_read_l.mp3")
    killian "But anyway, enough about what could have been.[wait_1] I take it that you wish to ask me why I’ve been embarking on my little project, Mr...[wait_05]Long, is it?"
    jack_possessing angry "Actually, that’s the name of this body’s previous mind.[wait_1] I’m your victim from Monday;[wait_05] the name’s Jack."
    killian "...Jack?"
    jack_possessing angry "Yep.[wait_1] How about you?[wait_1] Do you want me to address you as Killian?"
    jack_possessing angry "Or is it alright if I call you Dad?"
    $ swap_sprites("killian_shocked")
    killian "What?![wait_1] No...[wait_05]you can’t be!"
    killian "I –[wait_05] Jack, how did you –[wait_05] I swear, I didn’t mean to kill you![wait_1] I –[wait_05] I didn’t even know that you’d inherited my abilities!"
    jack_possessing angry "But if it’s anyone other than me, killing ‘em is no biggie?"
    jack_possessing angry "Fuck, you really are everything that Mum said you were.[wait_1] There’s a reason why I switched to her surname, y’know –[wait_05] puts a bit more distance between us."
    $ swap_sprites("killian_despairing")
    killian "But I –[wait_05] Jack, don’t you see?[wait_1] This is our opportunity to –[wait_05] we’ve never had a chance to try and be a family."
    killian "I haven’t seen you since you were a baby.[wait_1] This –[wait_05] this might not be your original body, but you –[wait_05] surely you’ll give me a chance?[wait_1] Won’t you?"
    jack_possessing angry "You fucking kidding?[wait_1] Why the fuck did you think I rocked up here?"
    killian "I –[wait_05] I don’t know."
    jack_possessing angry "It’s because I want you dead, you fucking deadbeat."
    # TODO: Use powers to kill Killian
    hide screen psychic_powers
    hide killian_despairing
    scene cg12_0 with slow_dissolve
    jack_possessing_thinking worried "Whoo...[wait_05]all that energy at once...[wait_05]put a bit of strain on Lloyd’s body...[wait_05]but I’m alright...[wait_05]I think."
    jack_possessing_thinking worried "I’ve done what I needed to...[wait_05]wiped out Killian’s mind completely..."
    jack_possessing_thinking worried "He probably would have blocked it...[wait_05]but he let his guard down around me..."
    scene killian_house_interior with slow_dissolve
    jack_possessing_thinking smug "Alright...[wait_05]kill my monster of a father?[wait_1] Check."
    jack_possessing_thinking smug "Get rid of the threat to this body?[wait_1] Check."
    jack_possessing_thinking smug "Set myself up with a new body, new life, and enough cash to keep me going for a while?[wait_1] Check, check, and check."
    jack_possessing_thinking smug "Things are looking like they’ll be pretty good for Jack Usbourne."
    scene black_bg
    call screen chapter_breaks("LATER", "Jack has a new lease on life and new opportunities. He has a fresh new start that few are ever given.\n\nNobody actually believes that he’s going to use it wisely though, right?")
    scene bar with slow_dissolve
    $ current_thought_block = "mind_read_barbara"
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_308"
    show screen psychic_powers
    barbara "...when you put it that way –[wait_05] yeah, I can swing by your apartment after the bar closes!"
    jack_possessing_thinking smug "Oh yeah –[wait_05] gimme some sugar, baby."
    $ current_thought = "barbara_thought_309"
    jack_possessing smug "Thanks, babe –[wait_05] I mean Barbara.[wait_1] And you won’t forget the money?[wait_1] That you said I could borrow?"
    $ current_thought = "barbara_thought_310"
    barbara "Of course.[wait_1] I really feel like I can trust you, Lloyd."
    jack_possessing smug "You know it!"
    jack_possessing_thinking "Man, it’s a good life."
    hide screen psychic_powers
    scene black_bg
    narrator "ENDING E"
    $ MainMenu()