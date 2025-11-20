label prologue_01:
    scene black_bg with quick_dissolve
    $ quick_menu = False
    call screen chapter_breaks("PROLOGUE", "In a bar downtown, a young man is currently drinking. He is thinking about how he should use his psychic powers tonight.")
    $ quick_menu = True

    scene bar with quick_dissolve
    jack smug "(Ah...[wait_1]nothing like going to the bar on a Monday.)"
    jack smug "(Lots of lovely booze, lots of quiet, and best of all...[wait_05]a sexy bartender, who literally only has eyes for me)."
    $ swap_sprites("barbara_angry", slow_dissolve)
    barbara "Hello?[wait_1] Did you hear me?" (name="Bartender")
    jack worried "(Shit![wait_1] Has she been talking this whole time?)"
    jack worried "(What’s gotten her turned off all of a sudden?)"
    jack worried "Hmm?[wait_1] Hi, is something...[wait_05]wrong?"
    barbara "I said, I’m going to need you to pass that drink over and leave." (name="Bartender")
    barbara "You’ve clearly had too much to drink, and I can’t have you hanging around here." (name="Bartender")
    jack angry "(Whatever happened to the good old national binge drink?)"
    jack angry "(Used to be that we were told off for not drinking enough...[wait_1]it’s political correctness gone mad.)"
    jack thinking "(Still though, I’d better listen to her.)"
    jack thinking "( I don’t think she’s the type of angry that makes me feel horny.)"
    #SFX: Glass sliding
    jack smug "Right, there you go then."
    jack smug "Farewell, sweet mademoiselle, and thank you for bringing pleasure to a thirsty man."
    barbara "..." (name="Bartender")
    jack angry "(What’s she still looking angry for?[wait_1] That’s barely an innuendo!)"
    barbara "The bar’s policy is that all tabs have to be paid before leaving.[wait_1] No exceptions." (name="Bartender")
    jack worried "(Shit.[wait_05] How much money do I have?)"
    #Add the interface showing our money
    jack worried "(That's...[wait_05]not a lot.)"
    barbara "We take both cash and card." (name="Bartender")
    barbara "Can even split it between the two if that’s easier for you, but it’s got to be paid." (name="Bartender")
    jack smug "(Alright, no biggie.)"
    jack smug "(Just have to do a little rewrite without letting the alcohol affect me.[wait_1] Easy.)"

    #narrator in a modal: "Click on the forget button to alter the bartender’s mind, so that she forgets that you haven’t paid for your drinks."
    #bring up the button; have it highlighted here

    jump prologue_02

label prologue_02:
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_pr_01"
    barbara "Whoa, I...[wait_05]sorry, mate, I got a bit dizzy there." (name="Bartender")
    barbara "What...[wait_05]what were we talking about, again?" (name="Bartender")
    jack smug "My tab.[wait_1] We were just, um, saying how I’d paid it all, and that I was going to leave."
    $ current_thought = "barbara_thought_pr_02"
    jack smug "(Might as well sweeten the deal a little...)"
    jack smug "...but not until after you give me some money."
    jack smug "You said that you were going to get me my change, remember?"
    $ current_thought = "barbara_thought_pr_03"
    barbara "Did I...?[wait_1] I don’t remember that..." (name="Bartender")
    jack smug "You definitely did."
    jack smug "You definitely said -[wait_05] I remember you saying -[wait_05] that you were surprised at how much money I’d given you, and that you were -[wait_05] you had a lot of cash to give me."
    $ current_thought = "barbara_thought_pr_04"
    barbara "..." (name="Bartender")
    jack worried "(Why aren’t you giving me my lovely money?[wait_1] What’s bloody wrong?)"
    
    #narrator in a modal: "Click on the mind-read button to read the bartender’s mind. By using the information you find in her mind, you can convince her that you’re correct."
    #bring up the button; have it highlighted here

    #jump to pr_04, jump back
    jack smug "It was, um, about fifty, that you owed me, by the way."
    jack smug "Fifty - and one hundred.[wait_1] One hundred and fifty."
    jack smug "That’s right, you owed me one hundred and fifty in change."
    $ current_thought = "barbara_thought_pr_05"
    $ swap_sprites("barbara_angry")
    barbara "Really?[wait_1] I think you might have miscalculated that a bit; that’s quite a lot of change to give." (name="Bartender")
    jack smug "Well, you know what they say about calculations...[wait_1]I mean, numbers don’t really mean anything, do they?"
    $ current_thought = "barbara_thought_pr_06"
    jack smug "What exactly is a number?[wait_1] Is it a thing you can see?"
    jack smug "Is it something you can touch, or...[wait_05]eat?"
    $ current_thought = "barbara_thought_pr_07"
    barbara "I think it’s safe to say that I’ll be able to see some numbers on the terminal."
    $ current_thought = "barbara_thought_pr_08"
    jack smug "Are you sure that you want to do that?"
    jack smug "Computers aren’t really all that good when it comes to numbers."
    $ current_thought = "barbara_thought_pr_09"
    jack smug "There’s a reason that banks are full of cash, and -[wait_05] and gold, rather than computers."
    jack smug "So thinking about it, they can’t really be that useful, can they?"
    $ current_thought = "barbara_thought_pr_10"
    jack smug "I mean, when this bar first opened, it wasn’t like they used computers, was it?[wait_1] And it was much better for it, I bet."
    $ current_thought = "barbara_thought_pr_11"
    jack smug "They didn’t -[wait_05] they would have used something more accurate, like calculators, or something, to work out the numbers, yeah?"
    $ current_thought = "barbara_thought_pr_12"
    barbara "Nice try, but I trust the terminal a lot more than I trust you." (name="Bartender")
    $ current_thought = "barbara_thought_pr_13"

    #TODO: Add in the flags for the options being unlocked; a booleans list
    menu:
        "Let her open it":
            jack smug "(This will be fine.)"
            jack smug "(Just because I haven’t paid her, that doesn’t mean anything.[wait_1] It’s not like she can make me pay her.)"
            jack smug "(If she did, that would be a mugging, and I’d basically be allowed to run, wouldn’t I?)"
            $ current_thought = "barbara_thought_pr_14"
            barbara "Looks like I owe you quite a bit less than you said." (name="Bartender")
            barbara "In fact, I think you might have who owes who around the wrong way." (name="Bartender")
            jack worried "(Shit![wait_1] Okay, new plan: rewrite her mind, and try this again)"
            #reset
            jack worried "(I should probably try reading her mind a bit more this time...[wait_1]I might get a bit more information that I can use on her)."
            jump prologue_02
        
        "But it has issues with certain cards" (locked=True, message="You have not read this information in the bartender's mind"):
            jack smug "Do you, though?[wait_1] That old thing?"
            jack smug "How much can you really trust a computer that has as many issues with cards as this one does?"
            $ current_thought = "barbara_thought_pr_15"
            $ swap_sprites("barbara_thinking")
            barbara "That’s true...[wait_1]it’s sometimes a little off when it comes to surcharges, and when I asked about it, they just said that they’d open a ticket about it." (name="Bartender")
            $ current_thought = "barbara_thought_pr_16"
            jack smug "Those bloody computer people.[wait_1] They’re always going on about tickets, aren’t they?"
            $ current_thought = "barbara_thought_pr_17"
            $ swap_sprites("barbara_smiling")
            barbara "They are![wait_1] It wouldn’t kill them to show a bit more support for their customers; I pay them enough fees each month!" (name="Bartender")
            jack smug "They’re taking the bloody piss![wait_1] And I don’t reckon we shouldn’t support them any further!"
            jack smug "Let’s just - let’s stop using terminals, and computers, and cards, and just pay customers what they’re owed!"
            $ current_thought = "barbara_thought_pr_18"
            barbara "Good point![wait_1] I’d better check whether the value that you gave me is actually the right calculation, though; if it isn’t then that’s another issue that I can bring up to them." (name="Bartender")
            jack worried "Wait, but -"
            $ current_thought = "barbara_thought_pr_19"
            $ swap_sprites("barbara_angry")
            barbara "Looking at this, it looks like the value is wrong.[wait_1] At least, compared to what you said." (name="Bartender")
            barbara "As it is, I think you might have who owes who around the wrong way." (name="Bartender")
            $ current_thought = "barbara_thought_pr_20"
            jack worried "(Shit![wait_1] Okay, new plan: rewrite her mind, and try this again)"
            #reset
            jack worried "(I need to read her mind and find something that I can use to stop her from using the computer...[wait_1]there’s got to be something in there if I read it at the right time)."
            jump prologue_02
        
        "This bar used to be better" (locked=True, message="You have not readt his information in the bartender's mind"):
            jack angry "This bar used to be better, you know."
            jack angry "It was a lot friendlier, and it didn’t feel like you were constantly getting harassed while you were drinking."
            $ current_thought = "barbara_thought_pr_21"
            jack angry "If this is the way that things are going to be moving forwards, then you can consider this to be my last drink here."
            $ current_thought = "barbara_thought_pr_22"
            barbara "Good! I don’t want clientele like yourself anyway!" (name="Bartender")
            $ current_thought = "barbara_thought_pr_23"
            jack angry "Oh, yeah, that’s great.[wait_1] I’m sure that saying that to your customers will totally get them coming back."
            jack angry "Yeah, this bar is going to last for years at this rate, and it definitely won’t get driven into the ground."
            $ current_thought = "barbara_thought_pr_24"
            barbara "..." (name="Bartender")
            jack angry "(Was that...[wait_05]the right thing to say?)"
            $ current_thought = "barbara_thought_pr_25"
            $ swap_sprites("barbara_sad")
            barbara "Sorry, I...[wait_05]I shouldn’t have said that.[wait_1] I’m still getting the hang of this thing." (name="Bartender")
            barbara "What they teach you with a business degree doesn’t always apply to the real-world." (name="Bartender")
            jack smug "(Hello...[wait_05]feeling a bit down?)"
            jack smug "(Maybe a nice little sympathy fuck will make you feel better?)"
            $ current_thought = "barbara_thought_pr_26"
            barbara "I just - I’m trying not to lose more than I can afford to, but I guess that makes me a bit more cautious when I should be more trusting." (name="Bartender")
            jack smug "(Just keep smiling and nodding.)"
            jack smug "(It’s cool, girl - I’ll listen to all of your problems, provided you don’t want me to remember what they are in five minutes.)"
            $ swap_sprites("barbara_smiling")
            $ current_thought = "barbara_thought_pr_27"
            barbara "Here - this change is yours.[wait_1] I can worry about the books later." (name="Bartender")
            #Interface: +$150
            jack smug "(Cha-ching!)"
            $ current_thought = "barbara_thought_pr_28"
            barbara "Once again, I’m sorry that I was a bit sceptical." (name="Bartender")
            jack smug "That’s fine, and...[wait_1]look, if you wanted to talk about it a bit more, maybe in a bit more of an...[wait_1]intimate setting?"
            $ current_thought = "barbara_thought_pr_29"
            $ swap_sprites("barbara_angry")
            barbara "Yeah, it’s definitely time for you to leave." (name="Bartender")
            hide barbara_angry with quick_dissolve
            jack angry "(Oh, sure, when it’s emotional support, you’re all too happy to receive it, but physical support is a step too far, is it?)"
            scene black_bg with slow_dissolve

label prologue_03:
    jack thinking "(There’s no need for me to go home just yet.)"
    jack thinking "(It’s not like there’s anything wrong with staying out late on a Monday, after all.)"
    jack thinking "(I mean, when was the last time somebody got yelled at about overdue rent when staying out?[wait_1] Never happens.)"
    jack thinking "(Where should I go?)"
    call screen map_navigation

label prologue_music_venue:
    #Description: "Isn’t there some small underground place near here that plays jazz or one of those made-up music genres? They should have some good booze there, and it probably has some hippies that I can scam - I mean, borrow some money off."
    scene black_bg with slow_dissolve
    jack smug "(If there’s some sort of fee to get in, I’ll just make the door person forget that I haven’t actually paid it.)"
    jack smug "(They probably get paid a tonne of money by the venue anyway.)"
    jack smug "(Or more likely, they’re already really rich, and doing it so they can listen to music for free.[wait_1] I mean, who would actually want to do a job like that, anyway?)"
    jack thinking "(It’s a good thing that I’ve got these psychic abilities, to make things like that easier.)"
    jack thinking "(They sort of came out of nowhere, back in my teens, but I probably got them for a good reason, yeah?)"
    jack smug "(It’s probably a reward from God or something.)"
    jack smug "(\"Hey, dude! You’re fucking cool and you’re not a loser, so have these powers that nobody else does!\")"
    jack smug "(\"You should use them to find out peoples' secrets and stuff![wait_1] Peace!\")"
    jack smug "(Maybe at this place I’ll be able to find out some random secrets or whatever that people want to hide away...[wait_05]that’s always a good way to get a bit of extra money.)"
    jack smug "(And it’s not like I’m actually going to tell anyone their secrets, so they can’t {i}really{/i} get angry at me.)"
    jack smug "(It’s a win-win situation when you think about it - I get money, they get to keep their secrets to themselves.)"
    jack smug "(What’s there to get mad about?)"
    scene venue_exterior with slow_dissolve
    jack smug "(Alright, same deal as always: start heading in, wipe the doorman’s memory, then keep going.[wait_1] Easy.)"
    jack angry "(God, not that I should have to do this.)"
    jack angry "(If I was a doorman I’d let anybody in.[wait_1] The venue owners would start out mad, but then they’d -)"
    call prologue_precognition
    jack thinking "(Am I abandoning everyone in the venue to be killed...?)"
    jack thinking "(No, of course not.)"
    jack thinking "(If there’s some sort of maniac in there, they’ll probably get impatient waiting for me and...[wait_1]have a drink?)"
    jack smug "(Yeah, they’ll have a lovely little bit of alcohol.)"
    jack smug "(Hell, they’ll probably be happy that I didn’t show up.[wait_1] They’ll probably have a funny story to tell all the other knife-wielding psychos and druggies and murderers.)"
    jack smug "(They definitely wouldn’t kill anybody else in the venue out of frustration.[wait_1] That would just be rude)."
    jump prologue_end

label prologue_restaurant:
    #Description: "There’s nothing better to do with money that’s yours than spend it! A nice meal sounds like a good way to follow up those drinks from before, and they’ll practically treat me like a king in there. I mean, I’m more or less paying their wages for them; they have to!"
    scene black_bg with slow_dissolve
    jack smug "(Do they have wine at this place?[wait_1] I don’t really like it, but I could buy a nice big bottle of it anyway and show everyone there how rich I currently am.)"
    jack smug "(Maybe I could even buy two bottles, and then drop one of them on purpose.)"
    jack smug "(Yeah...[wait_1]that’ll show them all!)"
    jack thinking "(It’s a good thing that I’m able to make so much money using these powers of mine.)"
    jack thinking "(They make everything so much easier.[wait_1] They sort of came out of nowhere, back in my teens, but I probably got them for a good reason, yeah?)"
    jack smug "(It’s probably a reward from God or something.)"
    jack smug "(\"Hey, dude! You’re fucking cool and you’re not a loser, so have these powers that nobody else does!\")"
    jack smug "(\"You should use them to find out peoples' secrets and stuff![wait_1] Peace!\")"
    jack thinking "(I know that overall I don’t have that much money right now, but if I keep using these abilities the way I have been, I’ll definitely run into a millionaire or something some day and I’ll just get them to make me their heir or something.)"
    jack smug "(Maybe I’ll even kill the old bastard once it’s done to speed things up.)"
    jack smug "(It’s got to happen at some point.)"
    jack smug "(There’s probably a statistic somewhere proving that everybody runs into a millionaire every few years.)"
    jack angry "(And if not, they should research something useful like that.[wait_1] It’d be way more interesting than all of that boring cancer and famine stuff.)"
    scene restaurant_night with slow_dissolve
    jack angry "(They’d better have some fucking tables left inside; I don’t want to sit out in the cold.)"
    jack smug "(Although I guess if they don’t have any, I can probably use my abilities to get somebody to go outside.)"
    jack smug "(It’s not like they’d know that I - )"
    call prologue_precognition
    jack worried "(It’s alright to run away.[wait_1] Nobody wants to be stabbed, and if I go in there, I will definitely be stabbed.)"
    jack worried "(Sure, somebody else might be killed if I don’t go in there, but that’s fine.)"
    jack worried "(It’s not like they’d know that I abandoned them and left them in there with a killer.)"
    jack smug "(Actually, it probably wouldn’t even matter that the killer’s in there.)"
    jack smug "(Everybody can probably just run away, like I am, if shit goes down.)"
    jack smug "(I mean, it’s just a knife.[wait_1] Not exactly a gun, is it?)"
    jack smug "(The killer probably can’t even run fast enough to get close to people and stab them.[wait_1] It’ll be fine!)"
    jump prologue_end

label prologue_precognition:
    scene black_bg
    #video with blood splatter
    #stabbing sfx
    #flash of red
    scene venue_exterior with quick_dissolve
    jack worried "(I...[wait_1]I can feel a knife in my stomach.)"
    jack worried "(It’s - it’s fucking cold, and I...)"
    jack worried "({size=-8}Mum.[wait_1] Mum, please come and -[wait_05] and help me![wait_1] It feels like...{/size})"
    jack worried "..."
    jack thinking "(No, I’m -[wait_05] I’m fine.)"
    jack thinking "(But then what the fuck was that?[wait_1] It felt so real, like I was actually - )"
    jack thinking "(Precognition.)"
    jack thinking "(The third of my psychic abilities, the one that likes to kick in when I’m not expecting it.)"
    jack thinking "..."
    jack worried "(If I go into that building, I’m going to die.[wait_1] That’s what it’s telling me.)"
    jack thinking "(Someone...[wait_1]someone stabbed me...[wait_1]It was intentional.)"
    jack thinking "(They were looking for me, and they - they somehow knew that I would be here.)"
    jack thinking "(Alright, so the next move is...[wait_1]get the fuck out of here?)"
    scene black_bg with slow_dissolve
    #SFX of feet running
    return

label prologue_end:
    scene street with slow_dissolve
    jack thinking "(Think that I can stop running now...[wait_1]I’ve probably put enough distance between myself and the scene.)"
    jack thinking "(If I was still in danger, my precognition would kick in and let me know probably.)"
    jack thinking "(I mean, it warned me the first time, didn’t it?)"
    jack worried "(Who the fuck would want to kill me, though?)"
    jack worried "(I haven’t done anything to piss anybody off lately other than that con I pulled last week.[wait_1] But he was practically asking for it!)"
    jack thinking "(Unless...[wait_1]could it have been - )"
    $ swap_sprites("docherty_neutral")
    $ current_thought = "docherty_thought_pr_1"
    jack smug "Sorry mate, you mind getting out of the way?[wait_1] I’m in a bit of a hurry, here."
    docherty "You are the source."
    jack angry "The fuck do you -"
    #SFX: slicing noise
    #Red flash
    #CG
    jack worried "(No...[wait_05]no!)"
    jack worried "(This fucking can’t be...[wait_05]I...[wait_05]I thought I stopped this?)"
    jack worried "(I wasn’t supposed to...[wait_05]{size=-8}this is bullshit...{/size})"
    scene black_bg with slow_dissolve
    return