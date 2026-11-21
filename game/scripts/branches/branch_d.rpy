label branch_d_2_4:
    $ current_thought_block = "mind_read_barbara"
    lloyd_thinking thinking "Barbara agreed to ask around the area for whether any of her neighbours know who the man in the loud suit is."
    lloyd_thinking thinking "I know that the killer has been active in the area before and it’s possible that he’ll strike there again.[wait_1] Visiting her is the smartest move."
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I finish off my meal and pay.[wait_1] I manage to reach the station just as a train pulls in."
    lloyd_narrating neutral "I’m grateful for the timing of it; missing a train in the evening often leads to waits of up to half an hour.[wait_1] Eventually I reach my station and walk towards Icarus."
    scene bar with slow_dissolve
    lloyd_narrating neutral "The bar seems moderately popular tonight."
    lloyd_narrating neutral "A few tables are occupied, but it’s not so busy that I have to wait in line at the bar."
    lloyd_narrating neutral "I have to wait a few moments for Barbara to finish restocking some ice before she comes over to me."
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_228"
    show screen psychic_powers
    barbara "Hiya, Lloyd.[wait_1] What’s your poison?"
    $ current_thought = "barbara_thought_229"
    lloyd neutral "No drinks for me, Barbara.[wait_1] I’m more interested in hearing about the fruits of your labour."
    $ swap_sprites("barbara_thinking")
    barbara "Sorry?"
    $ current_thought = "barbara_thought_230"
    lloyd neutral "You said that you would look into the man in the loud suit today.[wait_1] Did you discover anything?"
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_231"
    barbara "Oh, right![wait_1] As a matter of fact, you’re in luck!"
    barbara "Take a look at this."
    lloyd_narrating neutral "She fumbles around for a few moments before finding a folded up piece of paper in her breast pocket."
    scene cg6_0 with slow_dissolve
    $ current_thought = "barbara_thought_232"
    barbara "Does this look like the right guy to you?"
    lloyd_narrating neutral "It’s a perfect match."
    lloyd_narrating neutral "The man in the loud suit, the man from my vision, is on a small advertisement flyer.[wait_1] It’s almost too convenient to be true."
    scene bar with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_233"
    lloyd neutral "It’s perfect.[wait_1] How did you find this?"
    $ current_thought = "barbara_thought_234"
    barbara "One of my competitors from a few blocks away came in earlier and asked whether I’d be willing to keep some of these flyers out for him.[wait_1] Apparently he’s been doing a big advertisement drive."
    $ current_thought = "barbara_thought_235"
    lloyd neutral "You’re willing to advertise for a competitor?"
    barbara "Eh, it’s good to maintain healthy relations in the industry.[wait_1] A bit of competition is good for our patrons."
    lloyd_narrating neutral "Whatever the reason, I’m grateful for the outcome.[wait_1] I read over the details of the flyer."
    lloyd_narrating neutral "The man in the loud suit –[wait_05] Sergei Maskelyne, according to the advertisement –[wait_05] is performing some sort of magic show at this other venue."
    lloyd_narrating neutral "It’s happening tonight, and it’s happening soon."
    $ current_thought = "barbara_thought_236"
    barbara "Anyway, can I interest you in a drink now?[wait_1] There’s this nice pilsner that I –"
    $ current_thought = "barbara_thought_237"
    lloyd neutral "Sorry, Barbara.[wait_1] I need to get to this show as soon as possible.[wait_1] I’ll have to save the drink for another night."
    barbara "Right.[wait_1] I get it."
    $ current_thought = "barbara_thought_238"
    barbara "I hope it’s good, and, hey –[wait_05] if you want to come past after the show’s over, I’ll still be open!"
    $ current_thought = "barbara_thought_239"
    lloyd neutral "I can’t make any promises.[wait_1] We’ll see how things go."
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "I walk away from the bar and look up the location of this other venue.[wait_1] I’ll need to hurry to get in on time."
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I walk downstairs into the venue and purchase a ticket at the door."
    scene venue_interior with slow_dissolve
    lloyd_narrating neutral "With the exception of the stage the lighting inside the venue is dim enough that I can’t make out the features of any other patrons."
    lloyd_narrating neutral "The architecture and age of the place would make for some interesting photos, although I wouldn’t be able to take any good pictures without a flashgun at the very least, if not a studio strobe."
    lloyd_narrating neutral "Some seats and tables that look easy to move have been set up for tonight’s audience."
    lloyd_narrating neutral "Short of barging through to the backstage area, there’s no apparent way for me to speak to Sergei."
    lloyd_narrating neutral "I sit down in a spare seat and wait for an opportunity to present itself.[wait_1] I don’t have long to wait before the show begins."
    $ swap_sprites("sergei_welcoming", quick_dissolve)
    sergei "Ladies, gentlemen, and all others!" 
    sergei "Welcome...[wait_05]to the greatest night of your life!"
    lloyd_narrating neutral "Sergei Maskelyne steps onto the stage and spreads out his arms as though he wants the entire world to join him."
    lloyd_narrating neutral "He’s flamboyant and enthusiastic; the perfect showman for his audience."
    if (person_visited("cat", "a", 0) or person_visited("cat", "c", 0)):
        lloyd_narrating neutral "Something about his voice and manner of speaking is familiar to me, but I can’t think of why."
    lloyd_narrating neutral "He takes a deep bow for his audience as we applaud.[wait_1] I study him carefully, trying to identify the trait of his which has placed him in the killer’s crosshairs."
    sergei "Thank you, thank you, all.[wait_1] Tonight shall be a night unlike any other for all of you."
    sergei "Tonight is the night that all of you are transformed –[wait_05] the night in which your lives change for the better after a touch with true magic, performed by a world-renowned master!"
    sergei "Tonight is the night in which you will see true, honest-to-god miracles, leaving your minds reeling and your hearts pounding!"
    sergei "Tonight is the night in which I share a little of my fantastic skills with you all, and steal all of your hearts!"
    lloyd_thinking thinking "Well, it’s definitely not his humility which has caught the killer’s attention."
    $ swap_sprites("sergei_winking")
    sergei "I’ll be starting in just a minute, but just a little disclaimer beforehand –[wait_05] please do not go looking for any hidden wires, smoke, or mirrors."
    sergei "What I am about to perform is true magic –[wait_05] so make sure you focus on me, or you’ll miss the best bits of the show!"
    $ swap_sprites("sergei_welcoming")
    sergei "And now, to start things off...[wait_05]let’s see what I have up my sleeve."
    hide sergei_welcoming with quick_dissolve
    lloyd_narrating neutral "For all of his showmanship and flamboyance Sergei’s act isn’t anything to write home about."
    lloyd_narrating neutral "I’m hardly the most ardent follower of magic, but even I’ve seen most of this act before, performed by more talented magicians."
    lloyd_narrating neutral "The reason why Sergei is playing in a relatively small venue soon becomes apparent and I wonder whether he’ll bring in enough money to justify keeping him on for another night."
    lloyd_narrating neutral "But after several basic tricks which mostly involve simple sleight of hand Sergei finally does something which gets my attention."
    $ swap_sprites("sergei_welcoming", quick_dissolve)
    sergei "That’s all that I can show you of my power to float pencils –[wait_05] frightfully useful when one rolls off the table!"
    sergei "For my next ability, I will require a volunteer from the audience."
    sergei "But don’t be too hasty to raise your hand, because I will be using my magical powers in a unique manner:[wait_05] to delve deeply into your mind and read your thoughts!"
    lloyd_narrating neutral "My hand instantly shoots into the air."
    lloyd_narrating neutral "I would have been invested enough in becoming a volunteer in order to get the chance to examine Sergei up close, but the mention of reading thoughts makes it a requirement."
    lloyd_narrating neutral "He scans the crowd as I wait for his decision."
    sergei "You there![wait_1] Yes, you, in the –[wait_05] is that a yellow coat?"
    sergei "My apologies, these stage lights are a little bright, and my magic can only compensate for my eyesight so far."
    sergei "Yes, you there –[wait_05] please, come on up to the stage!"
    lloyd_narrating neutral "Things couldn’t have gone better if I’d set them up myself.[wait_1] I climb up to the stage and stand next to Sergei."
    $ current_thought_block = "mind_read_sergei"
    $ current_thought = "sergei_thought_01"
    show screen psychic_powers
    lloyd_thinking thinking "I might not get another opportunity like this.[wait_1] I should read his mind and see whether I catch any thoughts that would indicate why he’s being targeted by the killer."
    sergei "Everybody give a big hand to this brave volunteer!"
    lloyd_narrating neutral "The sounds of the crowd indicate that they’re not expecting too much from this ability of Sergei’s."
    sergei "Young man, I’m about to use my magical powers to read your mind.[wait_1] You may feel a little ticklish sensation in your head, but nothing more than that."
    lloyd_thinking thinking "Young man?[wait_1] How old do you think I am?"
    $ swap_sprites("sergei_winking")
    sergei "Oh, and don’t worry –[wait_05] I won’t go reading anything that I don’t need to."
    lloyd_narrating neutral "The crowd laughs politely as Sergei retrieves something from his prop bag."
    $ swap_sprites("sergei_welcoming")
    sergei "Now, I wouldn’t want anybody to think that we’re in on this together, so to prove my magic powers, I’d like you to have this."
    lloyd_narrating neutral "Sergei passes me a sealed pack of cards.[wait_1] At his prompting I hold it up and confirm what it is to the crowd."
    sergei "For the next step, I’d like you to open up the pack and choose a card –[wait_05] but make sure that you don’t let me see what it is!"
    # Could potentially make this a little interface bit, where we choose a card from a selection? Nothing super fancy but it's something
    lloyd_narrating neutral "I do as he says, choosing the seven of clubs."
    sergei "Please pass the card to a member of the audience, and the rest of the deck to another member."
    sergei "Thank you –[wait_05] now, while the latter checks the deck to confirm that it has not been rigged in any way, I will use my amazing magical abilities to read your mind!"
    lloyd_narrating neutral "Sergei strikes an exaggerated pose while humming softly."
    lloyd_narrating neutral "I think that it’s nothing but theatrics at first, but then I feel something in my head.[wait_1] It’s as though my brain has an itch which moves around."
    lloyd_thinking thinking "Is he doing what I think he is?"
    lloyd_narrating neutral "Sergei confirms it a moment later."
    sergei "My amazing powers have reached into this young man’s head and pierced the barriers of his consciousness!"
    sergei "Although he tried hard to conceal it from me, he was unable to overpower my magic."
    sergei "You there![wait_1] Is the card he gave you...[wait_05]the seven of clubs?!"
    lloyd_narrating neutral "The audience member confirms it.[wait_1] In comparison to Sergei’s other tricks so far the applause is slightly louder, although I’m certain that plenty of the patrons still think that this is a trick of some kind."
    hide sergei_welcoming with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "I return to my seat and continue watching the show.[wait_1] After what should have been a genuine trick Sergei’s act resumes its previous level of quality."
    lloyd_narrating neutral "I find it hard to focus on it with the knowledge I have of Sergei now."
    lloyd_thinking thinking "Is the killer after Sergei because he used his abilities to discover something that he shouldn’t have?[wait_1] But how could the killer have discovered that?"
    lloyd_narrating neutral "A short while later the show takes a break for intermission."
    lloyd_narrating neutral "The cynic in me wonders whether the reason for it is that Sergei has to look up more simple tricks on the internet and get some quick practice in."
    lloyd_narrating neutral "I drum my fingers across the table in my impatience.[wait_1] The sooner that the show is over, the sooner that I can have a proper conversation with Sergei."
    lloyd_narrating neutral "If nothing else, I need to warn him that –"
    $ play_sound("gunshot.mp3")
    $ renpy.pause(1.0, hard=True)
    lloyd_thinking scared "That sounded like a gunshot![wait_1] And I know who the target is!"
    lloyd_narrating neutral "I leap up from the table and jump onto the stage."
    lloyd_narrating neutral "Most of the audience seems mildly confused, no doubt mistaking the weapon’s discharge for something falling over.[wait_1] I would have thought the same if it weren’t for my vision."
    lloyd_narrating neutral "I cross into the backstage and see something that shouldn’t be possible."
    $ swap_sprites("docherty_neutral", quick_dissolve)
    $ current_thought_block = "mind_read_docherty"
    $ current_thought = "docherty_thought_02"
    show screen psychic_powers
    lloyd scared "You – !"
    lloyd_thinking scared "It’s Docherty![wait_1] Looking exactly like he did in my vision, and in Eddie’s picture!"
    lloyd_thinking scared "But he’s supposed to be dead![wait_1] How is he –"
    lloyd_narrating neutral "I’m too stunned to react as he swings the handle of his gun at me."
    with red_flash
    hide docherty_neutral
    hide screen psychic_powers
    lloyd_narrating neutral "I land on the ground heavily.[wait_1] By the time I’ve picked myself back up to my feet he’s already gone."
    lloyd_thinking thinking "Someone might stop him before he leaves the building.[wait_1] I’ve got to reach Sergei while there’s still time."
    lloyd_narrating neutral "I run backstage and try to find Sergei.[wait_1] It doesn’t take me too long."
    lloyd_narrating neutral "All that I need to do is follow the stench of blood."
    scene cg3_2 with slow_dissolve
    lloyd_narrating scared "Blood drips down Sergei’s suit, dripping a dull red pattern into the floor."
    lloyd_narrating scared "The blood is clearly fresh and still oozing out of his chest.[wait_1] The thing that sticks out to me is how wet it all is."
    lloyd_narrating scared "Most day-to-day injuries bleed briefly before the wound seals itself up.[wait_1] This wound won’t dry or stop bleeding for a long time."
    lloyd_thinking thinking "It’s clearly too late for Sergei.[wait_1] Nobody could survive a wound as serious as this."
    lloyd_narrating neutral "Just as I think that Sergei speaks.[wait_1] It’s a very weak voice that he speaks with, and it’s clearly going to be the last thing that he’ll ever say."
    lloyd_narrating neutral "But he speaks nevertheless."
    sergei "{size=-8}Jack...[wait_1]he’s trying to kill all of us...[wait_1] Y-you need...[wait_1]to...{/size}"
    lloyd_narrating neutral "After a few seconds, his head drops down to his chest."
    lloyd_narrating neutral "He’s never going to move under his own power again."
    lloyd_narrating neutral "But I’m not thinking about any of that.[wait_1] Only one thought is going through my head."
    lloyd_thinking thinking "Who the hell is Jack?"
    scene black_bg with slow_dissolve
    mental_jack "Another one dead...[wait_05]bastard."

label branch_d_3_0:
    # power upgrade
    $ branch = "d"
    $ day = 3
    call screen chapter_breaks("THURSDAY", "Lloyd has failed to prevent another murder. He has failed to stop Docherty from escaping.\n\nBy the end of the day, another person will be dead.")
    scene apartment_day with slow_dissolve
    lloyd_narrating neutral "I wake up in my bed feeling renewed.[wait_1] It’s a good feeling."
    lloyd_narrating neutral "I’ll need the energy for the long day ahead of me."
    lloyd_thinking thinking "Who is this Jack person?[wait_1] What’s their connection to Sergei?"
    lloyd_thinking thinking "And most importantly –[wait_05] how will I find them?"
    lloyd_narrating neutral "It’s the only clue I have to go on next.[wait_1] After I heard Sergei’s last words, the police were called, the staff and patrons of the venue questioned."
    lloyd_narrating neutral "Enough testimonies confirmed that Docherty was running away from where Sergei’s body was found, that the gunshot was heard before I leapt up onto the stage, to clear me of any major suspicions."
    lloyd_narrating neutral "Nobody caught Docherty.[wait_1] He slipped past everybody like a ghost."
    lloyd_thinking thinking "If I can find this Jack person, they can tell me what Sergei wanted to talk to me about."
    lloyd_narrating neutral "I’ve briefly considered looking further into Sergei –[wait_05] into who exactly he was –[wait_05] but I concluded that it wouldn’t be helpful."
    lloyd_narrating neutral "He seemed to be nothing more than an amateur magician using his abilities to wow crowds."
    lloyd_thinking thinking "Who would be the best person to help me find Jack?"

    call screen map_navigation()

label branch_d_3_4:
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "Today has been nothing but a waste of time.[wait_1] I’ve learned nothing valuable about Sergei or his associate, and the investigation has hit a dead end."
    lloyd_narrating neutral "All that I can do for now is take a break, visit my favourite restaurant, and hope that inspiration hits me while I’m eating."
    lloyd_thinking thinking "What do I want to order tonight...?"
    menu:
        "Twice-cooked pork":
            lloyd_narrating neutral "Although the sweet and sour pork looks appealing enough to turn my mind to thoughts of pig, it’s the twice-cooked pork which I end up choosing."
            lloyd_narrating neutral "The chilli bean paste included with the sauce adds a kick of spice which appeals to me more tonight than the flavour of the sweet and sour pork."
            lloyd_narrating neutral "The stir-fried vegetables included as part of the meal validate my decision, and I feel that I’ve made the right choice."
        "Sweet and Sour Pork":
            lloyd_narrating neutral "Although the twice-cooked pork looks appealing enough to turn my mind to thoughts of pig, it’s the sweet and sour pork which I ultimately choose."
            lloyd_narrating neutral "The taste of pineapple in the meal appeals to me more tonight than the spice of the twice-cooked pork, and once I’ve begun eating the sauce alone makes me feel that I’ve made the correct choice."
        "Char siu with rice":
            lloyd_narrating neutral "No vegetables are included with the meal, but I’m not particularly bothered by it."
            lloyd_narrating neutral "The rough texture of the meat combined with the strong umami flavour are exactly what I’m looking for, and from the first bite alone I’m convinced that the choice I made is the correct one."
    lloyd_narrating neutral "While I eat my meal I think about what the fruits of today’s labour are."
    lloyd_narrating neutral "I have no idea who Jack is."
    lloyd_narrating neutral "I have no idea why Sergei and the man with the white streak were killed, and no idea who Docherty’s next target is."
    lloyd_narrating neutral "I have no idea how Docherty is still alive after he was reported dead."
    lloyd_narrating neutral "I have no idea what my next step will be."
    lloyd_thinking thinking "There will still be a few hours left in the evening after I finish eating.[wait_1] What should I do with them?"
    menu:
        "Return home":
            lloyd_narrating neutral "It’s not as though I have any other option.[wait_1] I may as well retire for the night and hope that inspiration strikes me come the morning."
            lloyd_thinking thinking "Maybe I’ll try forcing another vision with my powers."
            lloyd_thinking thinking "I’d rather not given how excruciating the pain was last time, but it would be worth it to get more insight into Docherty’s actions."
            lloyd_narrating neutral "It’s not something that I’m looking forward to, but if I have to do it I will.[wait_1] If I can’t stop Docherty then at the very least I want to warn his next victim."
            lloyd_thinking thinking "Where will he strike next?[wait_1] And more importantly, how will I find the next target?"
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "All of these thoughts and more go through my head as I travel home."
            lloyd_narrating neutral "By the time I’ve arrived I’ve convinced myself to look more deeply into the future, no matter the cost to myself."
            scene apartment_night with slow_dissolve
            lloyd_narrating neutral "I’m sitting cross-legged on my bed."
            lloyd_narrating neutral "I’ve spent the better part of the last hour meditating and focusing my mind."
            lloyd_narrating neutral "But no matter how hard I concentrate or try to recreate the conditions of my last vision, I’m unable to pierce the veil of the future."
            lloyd_narrating neutral "Matters aren’t helped by my concentration constantly being broken by all of the different sounds finding their way into the apartment.[wait_1] I’m realising now that it’s a bit of a miracle that I was able to trigger my future vision last time."
            lloyd_narrating neutral "For the umpteenth time I’ve slowed my breathing down."
            lloyd_narrating neutral "I’m concentrating on my skull and imagining the flow of energy going to and from it."
            lloyd_narrating neutral "I’m feeling my psychic abilities as a tangible force."
            lloyd_narrating neutral "I get a sense of dizziness and begin to slip into a trance –"
            # SFX - door knocking
            lloyd_narrating neutral "– and then it’s broken by a knocking at the door."
            # What if we did a CG of Docherty at the door here? Kinda a waste for a one-off dead end but it'd be a good way to build tension
            lloyd neutral "I’m coming."
            lloyd_narrating neutral "I assume that it’s one of my neighbours coming to ask me for something, or to invite me to an event."
            lloyd_narrating neutral "It’s happened before in the past, with the events usually being related to a matter in the building."
            lloyd_narrating neutral "My assumption turns out to be incorrect, though.[wait_1] I’m dead wrong."
            $ swap_sprites("docherty_neutral", quick_dissolve)
            $ current_thought = "docherty_thought_01"
            show screen psychic_powers
            lloyd_thinking scared "Shit!"
            lloyd scared "Docherty![wait_1] You –"
            docherty "I aim to make this painless."
            $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
            hide screen psychic_powers
            scene black_bg
            narrator "GAME OVER"
            $ MainMenu()
        "Visit Eddie" (locked=not person_visited("eddie", "d", 0) or not check_boolean("eddie_investigates_docherty2"), message=("You did not visit Eddie today" if not person_visited("eddie", "d", 0) else "You did not convince Eddie to help you")):
            lloyd_narrating neutral "It’s not as though I have any other viable options."
            lloyd_narrating neutral "Eddie’s the only one of my contacts who suggested I visit him tonight, after his interest was piqued by my encounter with Docherty."
            lloyd_narrating neutral "If my story inspired him to look into Docherty once again and identify how he’s still alive, that will be a big help to my investigation."
            lloyd_narrating neutral "As much as I’d like to savour it, I make an effort to quickly finish the rest of my meal."
            lloyd_narrating neutral "I don’t know how long Eddie will stay at the office and I wouldn’t want to keep him waiting for longer than I need to."
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "As I make my way to Eddie’s workplace I feel my heart racing."
            lloyd_narrating neutral "If Eddie doesn’t have anything for me then I’ll be at a dead end."
            lloyd_narrating neutral "Will his access to newspaper archives and investigative journalism have been sufficient to discover the information that I need?[wait_1] Or am I wasting my time?"
            lloyd_narrating neutral "Should I turn my focus instead to what initially set me on this path, and try to trigger another vision of the future?"
            lloyd_thinking thinking "I’ll see what information Eddie has to begin with.[wait_1] If he doesn’t have anything then I’ll work out what my remaining options are."
            lloyd_narrating neutral "I arrive at the newspaper and ask whether Eddie is still in.[wait_1] Once again I’m directed to a side room for interviews."
            lloyd_narrating neutral "My back is placed to the rest of the office, a glass door behind me."
            scene office_interview_room with slow_dissolve
            lloyd_narrating neutral "Eddie sticks his head in the door briefly and tells me to wait while he gets some information together."
            lloyd_narrating neutral "From the way he words it I’m expecting to be waiting for five minutes, maybe ten at most.[wait_1] But when he finally returns it’s been over half an hour of waiting."
            $ swap_sprites("eddie_angry", slow_dissolve)
            $ current_thought = "eddie_thought_215"
            show screen psychic_powers
            lloyd neutral "Thanks for doing this, Eddie."
            $ current_thought = "eddie_thought_216"
            eddie "I was pretty reluctant at first, you know.[wait_1] But if what you’ve said is true –[wait_05] if Docherty really is still alive –[wait_05] then that raises a lot of questions."
            lloyd_narrating neutral "He raises a hand and holds up three fingers."
            $ current_thought = "eddie_thought_217"
            eddie "One:[wait_05] why was Docherty reported as dead?" 
            eddie "Two:[wait_05] why isn’t Docherty in prison?" 
            eddie "Three:[wait_05] what has he been up to this whole time?"
            $ swap_sprites("eddie_arrogant")
            lloyd_narrating neutral "Once all three fingers are lowered, Eddie cracks an arrogant smile."
            $ current_thought = "eddie_thought_218"
            eddie "Good thing for you, I’ve done a bit of digging.[wait_1] I can answer all the questions, but it’s going to cost you."
            lloyd_narrating neutral "I nod.[wait_1] I wasn’t expecting this, but I’m willing to pay whatever price I have to if it gives me progress."
            $ current_thought = "eddie_thought_219"
            lloyd neutral "Tell me what you’ve discovered."
            lloyd_narrating neutral "Eddie opens his mouth and begins talking, but I can’t hear him over the noise that erupts."
            $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
            $ current_thought = "eddie_thought_220"
            lloyd_narrating neutral "I feel something whizz past my head and embed itself in the wall at the opposite end of the room to me."
            lloyd_thinking thinking "What was that?[wait_1] Did something...?"
            lloyd_narrating neutral "It’s a bullet.[wait_1] Someone is trying to kill me."
            $ swap_sprites("eddie_angry")
            $ current_thought = "eddie_thought_221"
            eddie "Chen![wait_1] Get down!"
            $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
            lloyd_narrating scared "Eddie pushes the table to its side and then tackles me to the ground."
            lloyd_narrating scared "It’s not a moment too soon –[wait_05] another gunshot sounds.[wait_1] If I hadn’t been knocked down then it would have hit me."
            eddie "Chen –[wait_05] stay here and don’t do anything.[wait_1] I’m going to deal with this."
            lloyd scared "What do you –"
            $ current_thought = "eddie_thought_222"
            eddie "Shut up![wait_1] We don’t have much time!"
            hide eddie_angry with quick_dissolve
            hide screen psychic_powers
            lloyd_narrating scared "Eddie leaves the room, staying low to the ground as he moves out.[wait_1] I have no idea who’s shooting at me or what he plans to do about it."
            lloyd_thinking thinking "Both bullets were fired at me.[wait_1] I’m clearly the target."
            lloyd_thinking thinking "Will Eddie be safe out there?"
            menu:
                "Prioritise my safety":
                    lloyd_thinking thinking "Eddie was confident when he left the room.[wait_1] If he wanted my help or needed me to assist him he would have asked for it."
                    lloyd_narrating neutral "There’s a part of me that feels guilty.[wait_1] I don’t know what Eddie’s planning, nor do I know what the outcome of his action will be."
                    lloyd_narrating neutral "But I’m clearly the target of the shooter.[wait_1] If I stay in here and draw their attention then he can enact whatever plan he has."
                    lloyd_narrating neutral "It makes more sense for me to stay here.[wait_1] If I leave the room then things will go awry."
                    lloyd_narrating neutral "It’ll mess up whatever he’s planning.[wait_1] It’s for the best if I stay here."
                    lloyd_thinking thinking "Unless his plan doesn’t benefit me."
                    lloyd_narrating neutral "The thought comes into my head unbidden.[wait_1] Eddie might be acting in his own interests."
                    lloyd_narrating neutral "He said that he would deal with this, but that could mean anything.[wait_1] He might be calling the police and trusting me to survive on my own."
                    lloyd_narrating neutral "He could be using me as bait while he escapes to safety."
                    lloyd_thinking thinking "What’s the most likely way that Eddie would stop an armed gunman?"
                    lloyd_narrating neutral "Nothing comes to mind and I’m unsure what to do next."
                    lloyd_narrating neutral "Should I try to sneak out and elude the gunman?[wait_1] Or should I stay here and trust him to deal with it?"
                    lloyd_thinking thinking "Knowing Eddie...[wait_05]I think that he’s more likely to have left."
                    lloyd_thinking thinking "He’s probably sold me out and wants me to draw the gunman’s attention.[wait_1] I need to find a way to –"
                    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
                    lloyd_narrating scared "The sound of a gun firing startles me."
                    lloyd_narrating scared "But more startling is that it wasn’t fired into this room.[wait_1] It was fired somewhere in the newspaper office."
                    lloyd_thinking thinking "What’s happened to Eddie?[wait_1] Was he caught?"
                    lloyd_narrating neutral "I receive my answer a moment later."
                    $ swap_sprites("eddie_arrogant", quick_dissolve)
                    $ current_thought = "eddie_thought_223"
                    show screen psychic_powers
                    eddie "Come out, Chen.[wait_1] I stopped him."
                    $ current_thought = "eddie_thought_224"
                    lloyd scared "You –[wait_05] you did?"
                    $ current_thought = "eddie_thought_225"
                    eddie "I’ve got a gun in my desk.[wait_1] All that I needed to do was reach it."
                    lloyd_thinking thinking "He does?[wait_1] That’s convenient."
                    $ current_thought = "eddie_thought_226"
                    eddie "Follow me."
                    hide eddie_arrogant with quick_dissolve
                    hide screen psychic_powers
                    lloyd_thinking thinking "But how did he avoid getting shot?[wait_1] And why didn’t the gunman fire any more bullets once Eddie left?"
                    lloyd_narrating neutral "I’m not going to find answers to my questions in here.[wait_1] I follow Eddie into the office."
                    scene cg9_0 with slow_dissolve
                    lloyd_narrating neutral "Unsurprisingly, the shooter was Docherty.[wait_1] He’s the only person that I know with a gun who has committed murder before."
                    lloyd_narrating neutral "He probably wanted to silence me since I saw him last night."
                    lloyd_thinking thinking "But then how did he know that I was here?"
                    $ current_thought = "eddie_thought_227"
                    show screen psychic_powers
                    # Maybe do side portraits here for Eddie?
                    eddie "This is your killer.[wait_1] Allan Docherty, yeah?"
                    $ current_thought = "eddie_thought_228"
                    lloyd neutral "Yes.[wait_1] It looks like him."
                    $ current_thought = "eddie_thought_229"
                    eddie "Well, he definitely won’t be killing again.[wait_1] He’s a goner for sure."
                    lloyd_thinking thinking "We thought that he was dead once.[wait_1] Will this time stick?"
                    $ current_thought = "eddie_thought_230"
                    eddie "I’ll call the police now.[wait_1] Make sure that your story lines up with mine –[wait_05] that this was self defence."
                    lloyd neutral "Of course.[wait_1] I imagine the physical evidence will support it."
                    eddie "It had better."
                    scene office_interview_room with slow_dissolve
                    $ swap_sprites("eddie_arrogant", quick_dissolve)
                    lloyd_narrating neutral "Eddie takes out his mobile phone and calls the police.[wait_1] The call is fairly swift, and once it’s over he reports that we’ll only have to wait a few minutes."
                    $ current_thought = "eddie_thought_231"
                    eddie "Luckily, most of the other staff have gone home.[wait_1] We should gather everybody else that’s here though, and get our story straight."
                    lloyd_thinking thinking "He’s very keen to make sure that the story is consistent.[wait_1] I suppose that I would be too if I needed to keep the death from being mistaken for anything but self-defence."
                    hide eddie_arrogant with quick_dissolve
                    hide screen psychic_powers
                    lloyd_narrating neutral "There’s nothing else to do from here but gather the remaining staff and wait for the police, as Eddie said."
                    lloyd_narrating neutral "I’ve got an odd sense of anticlimax."
                    lloyd_narrating neutral "Docherty has been stopped.[wait_1] He can’t threaten anyone again."
                    lloyd_narrating neutral "Everything might not have been wrapped up with a neat bow, but there will be time to discover answers in the aftermath of it all."
                    scene black_bg with slow_dissolve
                    mental_jack "{size=-8}(Dammit...[wait_05]I’m too weak.){/size}"
                    mental_jack "{size=-8}(I thought I could build up my strength more...[wait_05]but I can’t.[wait_1] It’s all over. ){/size}"
                    mental_jack "{size=-8}(Still...[wait_05]at least...[wait_05]that fucker was offed...[wait_05]That’ll show him...)"
                "Back him up" (locked=not person_visited("graves", "d", 0), message="You are not selfless enough"):
                    jump branch_e_3_4

label branch_d_4_0:
    # power upgrade
    $ branch = "d"
    $ day = 4
    call screen chapter_breaks("FRIDAY", "Docherty has been killed. There will be no more murders now.\n\nAll that Lloyd needs to do is tidy up some loose ends, and the case will be over.")
    scene apartment_day with slow_dissolve
    lloyd_narrating neutral "I wake up in my apartment feeling tired but satisfied."
    lloyd_narrating neutral "I was questioned by the police until the early hours of the morning, but they eventually released me."
    lloyd_narrating neutral "As with the deaths of the man with the white streak and Sergei, I was told to keep myself free for any follow-up questions, but I’m confident that there won’t be any."
    lloyd_narrating neutral "The police will continue investigating their deaths and discovering why Docherty killed them, but my part in things is over.[wait_1] Nobody else is going to die."
    lloyd_narrating neutral "As he was responsible for killing Docherty, Eddie was subjected to more questioning than me.[wait_1] He hadn’t been released by the time that I was."
    lloyd_narrating neutral "Before the police arrived we agreed to meet up at the newspaper tonight to discuss the story and what can be done."
    lloyd_narrating neutral "I’m unsure what Eddie will do during the day –[wait_05] he might take the day off after the stresses of the evening, or he might be questioned throughout the entirety of the day."
    lloyd_narrating neutral "Irrespective of his activities, I’ve got the day to myself."
    lloyd_thinking thinking "Where should I go today?"

    call screen map_navigation()

label branch_d_4_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "It’s evening.[wait_1] If this were one of the past few days I would be making my way to my favourite restaurant for a meal after a busy day of investigating."
    lloyd_narrating neutral "I’m a little tempted to do so; a habit formed after several days of eating a prepared meal for dinner."
    lloyd_narrating neutral "Instead I travel towards Eddie’s workplace.[wait_1] I can’t guarantee that he’ll be present but it’s what we agreed on."
    lloyd_narrating neutral "Although Docherty has been stopped it still feels like there’s a lot to do."
    lloyd_narrating neutral "Eddie will no doubt have a story to tell about the dangerous serial killer who was only stopped by his efforts.[wait_1] I don’t blame him for making himself the hero."
    lloyd_narrating neutral "He did enough investigating and fired the fatal bullet, saving my life in the process.[wait_1] He’s earned it."
    lloyd_narrating neutral "For my part, I’m hoping that Eddie will put in a good word for me and allow me to provide photos for the article.[wait_1] This whole incident should let me get a foot in the door at the newspaper, and it will hopefully lead to a steady job once again."
    lloyd_narrating neutral "I’ve been thinking about the article that Eddie will write. He’s already done most of the research."
    lloyd_narrating neutral "From what he said before we were interrupted last night he has the answers to some of the questions that I don’t."
    lloyd_narrating neutral "There’s likely just one remaining mystery hanging over him:[wait_05] who is my source, and how did I know that Docherty was the killer?"
    lloyd_narrating neutral "I’ve decided to tell Eddie the truth.[wait_1] I’m going to tell him that I have psychic abilities, and that I initially discovered the truth through a vision of the future."
    lloyd_narrating neutral "I doubt that Eddie will believe me.[wait_1] I’d prefer it if he didn’t make the information public."
    lloyd_narrating neutral "But he has a right to know what I can do and where I acquired my information.[wait_1] It’s up to him to decide what to do with that."
    scene office_interview_room with slow_dissolve
    lloyd_narrating neutral "I’ve been directed to a different yet identical interview room as the other one is still having its doors fixed."
    lloyd_narrating neutral "I want this to be the last time that I’m on this side of the table."
    lloyd_narrating neutral "The next time that I enter this building I want to be asking which desk I should sit at as I begin work for the day."
    lloyd_narrating neutral "After a short while Eddie enters."
    $ swap_sprites("eddie_arrogant", quick_dissolve)
    $ current_thought = "eddie_thought_232"
    show screen psychic_powers
    lloyd neutral "Hello, Eddie.[wait_1] Everything with the police is dealt with, I take it?"
    eddie "Hmm?[wait_1] Oh, yeah, of course."
    eddie "They’re not going to be an issue for me any time soon."
    lloyd neutral "And how are you feeling after last night?[wait_1] Did you work today?"
    eddie "You mean here?[wait_1] At the newspaper?[wait_1] Heh."
    eddie "I’ve got much more important things to be doing, Chen."
    lloyd_thinking thinking "Is it my imagination, or is he acting strangely?"
    lloyd neutral "Do you mean that you were working on the story about Docherty?"
    eddie "Sure, let’s go with that."
    lloyd_narrating neutral "He is acting strangely."
    lloyd_narrating neutral "I’m unsure of the change in attitude but I continue regardless.[wait_1] I’ve already made up my mind."
    lloyd neutral "Regarding the story about Docherty...[wait_05]there’s something that I need to tell you about it."
    eddie "Oh yeah?"
    lloyd neutral "I told you several days ago that I needed you to find out who he was as I’d been told about him by a source.[wait_1] That was a lie."
    lloyd_thinking thinking "...No additional comments from him."
    lloyd neutral "I –[wait_05] I didn’t have a source that I was getting my information from."
    lloyd neutral "I was –[wait_05] I’d had a vision of the future."
    lloyd neutral "It sounds improbable, but I knew that it was real, because I had –[wait_05] I have psychic abilities."
    eddie "I know."
    lloyd scared "You –[wait_05] you know?"
    eddie "Of course I do."
    eddie "It was obvious from the way you were sticking your nose into my plans.[wait_1] You almost ruined them, too."
    lloyd scared "Your plans?[wait_1] But –[wait_05] but Docherty was –"
    scene cg10_0 with slow_dissolve
    eddie "Don’t you get it?[wait_1] Docherty wasn’t acting on his own."
    eddie "A man like him, working with such precision and care?[wait_1] Don’t be ridiculous."
    eddie "He was under my control the entire time."
    lloyd scared "But then why did you –"
    eddie "You think that I’m telling you this because I want to answer your questions?[wait_1] No, you fool."
    eddie "I’m telling you this because I want to give you some closure in your last moments."
    eddie "Goodbye, Chen."
    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
    hide screen psychic_powers
    scene black_bg
    narrator "ENDING D"
    $ MainMenu()