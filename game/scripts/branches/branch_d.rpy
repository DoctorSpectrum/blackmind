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
    # Unsure why it's still displaying here?? Debug this when tightening things up later
    hide sergei_winking
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

    return