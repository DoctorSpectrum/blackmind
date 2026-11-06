label graves_investigation:
    $ current_thought_block = "mind_read_graves"
    if (branch == "a"):
        if (day == 1):
            jump graves_a_1
        elif (day == 2):
            jump graves_a_2
        elif (day == 3):
            jump graves_a_3
        elif (day == 4):
            jump graves_a_4
    
    return

label graves_a_1:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I’ve never had to hire, or even interact with, a private investigator. I chose this one because he’s not too far from my apartment – if I’m going to be seeing him often, I might as well make sure that it’s a short journey."
    lloyd_narrating neutral "It’s just crossing a few busy intersections, then pressing the intercom for the fourth floor of an office building."
    #SFX door reception buzz
    unknown "Whaddya want?"
    lloyd neutral "I’ve got someone that needs investigating.[wait_1] I hear that your office has the best people around for that kind of job."
    lloyd_narrating neutral "It’s a lie that I’m willing to tell.[wait_1] It never hurts to butter up the people you’ll be owing money to."
    lloyd_narrating neutral "The door unlocks a few seconds later, accompanied by the same voice as before."
    unknown "Come on in, kid."
    lloyd_narrating neutral "I do as the voice says and enter the building.[wait_1] The elevator claims to be out of order, so I climb the flight of aging stairs up to the fourth floor."
    scene detective_office with slow_dissolve
    lloyd_narrating neutral "It’s hardly the whiskey-soaked, chiaroscuro-styled office that Raymond Chandler would have you believe detectives work out of."
    lloyd_narrating neutral "It’s fairly small, and looks like it was only moved into a few hours ago."
    lloyd_narrating neutral "Much of the equipment is new, and there’s a very sterile smell in the air, as though the furniture’s only just come out of the box."
    $ swap_sprites("graves_intimidating", slow_dissolve)
    $ current_thought = "graves_thought_01"
    show screen psychic_powers
    detective "You’re the guy who called through?"
    lloyd_narrating neutral "The accent matches the person who responded on the intercom."
    lloyd_narrating neutral "I’m insulted by his prior referral to me as “kid” – he looks like he’s straight out of high school."
    $ current_thought = "graves_thought_02"
    lloyd neutral "Correct.[wait_1] Lloyd Chen, mister...?"
    lloyd_narrating neutral "I reach out a hand, and he warmly embraces it with one of his own."
    lloyd_narrating neutral "His hands aren’t overly hairy and his palm isn’t callused – he’s definitely younger than he’s acting."
    $ current_thought = "graves_thought_03"
    detective "Graves."
    lloyd_thinking neutral "Graves...?"
    $ current_thought = "graves_thought_04"
    graves "Yeah.[wait_1] They call me that because of how many friends I’ve had to bury."
    lloyd_narrating neutral "For a second he stares daggers at me, as though this fact is my fault."
    lloyd_narrating neutral "Then he bursts out laughing."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_05"
    graves "Ha ha ha![wait_1] Just kidding, mate –[wait_05] actually, my name is –[wait_05] my last name is Gravdahl."
    graves "But it makes for a nice – it’s not a bad nickname, right?"
    lloyd_narrating neutral "It’s an odd way to introduce yourself, and I wonder whether Gravdahl – Graves – is just a child playing at being an adult."
    lloyd_narrating neutral "Acting the way he thinks he should instead of the way he wants to.[wait_1] For a second I consider leaving."
    lloyd_narrating neutral "But I’m already here, and I might as well give him my pitch."
    $ current_thought = "graves_thought_06"
    lloyd neutral "It really isn’t.[wait_1] Mister Gravdahl –"
    graves "Graves, please![wait_1] It took me a long time to come up with such a great nickname!"
    $ current_thought = "graves_thought_07"
    lloyd neutral "Mister...[wait_05]Graves, shall we discuss the case I’ve come here for?"
    graves "Of course!"
    graves "Feel free to sit down at that desk.[wait_1] I’ve got a partner that –[wait_05] my partner is, um, out on a case, and so it’s –[wait_05] the seat there is free."
    lloyd_narrating neutral "I do as he suggests, adjust the height of the chair, and begin."
    $ current_thought = "graves_thought_08"
    lloyd neutral "I’ll put it to you simply, Mister Graves:[wait_05] there’s somebody in this city that I’m looking for."
    lloyd neutral "I’m not sure where exactly they are, but they’re here somewhere.[wait_1] I would like to find this person as quickly as possible."
    $ swap_sprites("graves_thinking")
    $ current_thought = "graves_thought_09"
    graves "Understood.[wait_1] May I enquire why exactly you’d like to – what the nature of your relationship with this individual is?"
    $ current_thought = "graves_thought_10"
    lloyd neutral "I’d rather keep that to myself."
    graves "Hmm.[wait_1] If you want it that way, then sure."
    $ current_thought = "graves_thought_11"
    lloyd neutral "If I were to hire you to find this individual, then how long do you anticipate it would take you to find them?"
    $ current_thought = "graves_thought_12"
    lloyd neutral "That depends.[wait_1] Can I get this person’s name, or is that also something that you’d – that you want to keep to yourself?"
    lloyd_thinking neutral "I have no idea what the man in black’s name is.[wait_1] If I explain that no doubt he’ll find it odd."
    lloyd_thinking neutral "I’m going to play my cards to my chest for now."
    $ current_thought = "graves_thought_13"
    lloyd neutral "I’d also rather keep that to myself."
    $ current_thought = "graves_thought_14"
    graves "Well, that complicates things.[wait_1] Do you have a picture?[wait_1] Or any other identifying information?"
    $ current_thought = "graves_thought_15"
    lloyd neutral "I can give you a physical description.[wait_1] A sketch, too, if you don’t mind an amateur’s hand."
    $ swap_sprites("graves_intimidating")
    graves "Is this some sort of –[wait_05] is this a joke?"
    graves "Or do you think that private investigators are –[wait_05] are magicians of some kind?"
    $ current_thought = "graves_thought_16"
    lloyd neutral "If I knew how to find this man beyond the...[wait_05]photo that I’ve been shown, I’d take care of this myself."
    graves "Fine then.[wait_1] Give me what you’ve got."
    $ swap_sprites("graves_thinking")
    lloyd_narrating neutral "I describe what I could see of the man in black during my vision to Graves."
    lloyd_narrating neutral "I tell him the exact tone of the man’s skin.[wait_1] I tell him about the shape of the man’s chin, and the angle of his cheekbones."
    lloyd_narrating neutral "I describe irrelevant details, such as the expression on his face and the clothes he was wearing."
    lloyd_narrating neutral "Throughout it all, Graves merely responds with a nod and a grunt from time to time."
    lloyd_narrating neutral "He isn’t taking any notes or recording any of what I’m saying, and my confidence in him is waning."
    lloyd_narrating neutral "I finally finish my description and wait for his response."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_17"
    graves "Alright then...[wait_05]I’ll tell you what, buddy: it’s a bit vague, but I’ll do what I can."
    graves "Of course, I’m in the middle of another case at the moment, so I’ve got a bit of work to do for that too."
    graves "So...[wait_05]realistically I can probably open up a file for you for now, and I’ll let you know how things are going after a few days."
    graves "How does that sound?"
    lloyd thinking "A few days isn’t fast enough![wait_1] The man in black could be killing again tonight – I need faster results!" 
    lloyd thinking "How can I get him to work faster?"
    menu:
        "Insist that he prioritise it":
            $ current_thought = "graves_thought_18"
            lloyd neutral "I’m going to need you to prioritise this.[wait_1] I can’t tell you why, but finding this man is incredibly important."
            $ current_thought = "graves_thought_19"
            graves "Like I said, I’ll do what I can, but at the same time –[wait_05] first come first serve."
            graves "If I get any opportunities, I’ll start on –[wait_05] I’ll do what I can for you, but you can’t blame me for wanting to finish off my existing case, right?"
            lloyd_thinking neutral "He’s got a point.[wait_1] I’m already committed now; I might as well wait and see what he turns up."
        "Call him out on his lie" (locked=not check_boolean("graves_no_cases"), message="You have not read the related thought"):
            lloyd_thinking neutral "I read his mind when I first came in, and he thought to himself that he didn’t have a case at the moment."
            lloyd_thinking neutral "He’s lying to me."
            lloyd_thinking neutral "I’m going to put some pressure on him and see how he reacts."
            $ current_thought = "graves_thought_20"
            lloyd neutral "You're lying."
            $ swap_sprites("graves_shocked")
            graves "What?![wait_1] What makes you –[wait_05] why would you say that?!"
            $ current_thought = "graves_thought_21"
            lloyd neutral "You don’t have another case to work on at the moment."
            lloyd neutral "There’s nothing stopping you from starting work on this today."
            graves "I –[wait_05] alright, I don’t know how you found that out, but it’s true."
            $ swap_sprites("graves_sad")
            $ current_thought = "graves_thought_22"
            graves "We’re –[wait_05] my partner and I, we’re still pretty new to this –[wait_05] to this work."
            graves "We’ve picked up a few cases here and there, but we –[wait_05] they’re not coming in as heavily as I –[wait_05] as we thought they would."
            graves "So I thought that if I –[wait_05] if I made out that I had a heavy workload, that this would take a few days, you’d be really impressed if I came back with something tomorrow, and –[wait_05] and maybe spread the word a bit."
            lloyd_thinking neutral "It’s a stupid business tactic.[wait_1] How many people might be turned off by lies like that?"
            $ current_thought = "graves_thought_23"
            graves "I’ll –[wait_05] I’ll start working on this once you leave."
            graves "I can’t guarantee that it’ll get very far along by the end of today, but I’ll at least get some momentum going."
            $ swap_sprites("graves_smiling")
            $ add_boolean("identify_graves_lie")
    $ current_thought = "graves_thought_24"
    graves "If you do want to come by later tonight, I can show you where things are sitting at the end of the day."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "I accept what he says and then spend some time filling out paperwork before leaving the office."
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Graves didn’t provide me with any guarantees, but he’s at least willing to be transparent about where he’s at by the end of the day."
    lloyd_narrating neutral "If I come by, I might be able to help steer him in the right direction, and he’ll hopefully have a better sense of how long things will take."

    $ visit_person("graves", "a", 0)
    return

label graves_a_2:
    $ visit_person("graves", "a", 1)
    return

label graves_a_3:
    $ visit_person("graves", "a", 2)
    return

label graves_a_4:
    $ visit_person("graves", "a", 3)
    return