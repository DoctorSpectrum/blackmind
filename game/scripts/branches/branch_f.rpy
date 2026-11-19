label branch_f_4_4:
    jack_possessing_thinking worried "Yeah...[wait_05]still got one thing to do.[wait_1] Kinda don’t want to...[wait_05]but...[wait_05]I guess it’s the right thing to do."
    scene black_bg with slow_dissolve
    lloyd_ws_narrating neutral "I open up my eyes and find myself in a strange place."
    scene killian_house_exterior with slow_dissolve
    show jack_smug at semi_trans, center with slow_dissolve
    $ current_thought_block = "mind_read_jack"
    $ current_thought = "jack_thought_01"
    show screen psychic_powers
    lloyd_ws_narrating neutral "The man with the white streak is standing before me, slightly translucent.[wait_1] He looks to be in perfect health."
    unknown "Hey, Lloyd.[wait_1] You prolly don’t really know what’s going on, do ya?"
    lloyd_ws neutral "I...[wait_05]saw you die."
    unknown "Kinda, yeah.[wait_1] My body died, but when my powers transferred themselves to you, I was able to jump ship with ‘em."
    unknown "I’ve been hiding out in the back of your mind, waiting to take over and keep livin’ the good life.[wait_1] Which is what I did today."
    lloyd_ws neutral "What do you mean?"
    unknown "I took over your body, Lloyd.[wait_1] Scrunched up your mind into a tiny ball and threw it into a deep, dark, corner, where it wouldn’t see the light."
    unknown "I wanted to live again, and I hijacked you to do it."
    lloyd_ws_thinking neutral "That somewhat explains why I don’t remember anything since last night."
    lloyd_ws neutral "And...[wait_05]you want to...[wait_05]what?[wait_1] Share my body now?"
    unknown "Nah.[wait_1] I...[wait_05]I’ve done some thinking, Lloyd."
    unknown "I got a bit of a glimpse at your life today.[wait_1] It looks like you’ve got a few people who care about you;[wait_05] that appreciate you being in their lives."
    hide jack_smug
    show jack_worried at semi_trans, center
    unknown "I...[wait_05]I’ve never had that, y’know."
    unknown "All I’ve ever had is...[wait_05]people blaming me for shit, or not wanting to be around me."
    unknown "I always thought that it was cos they were jerks –[wait_05] fuckers who weren’t giving me a chance."
    unknown "But the people I met today –[wait_05] I know that you only met them within the last few days, but they still care about you.[wait_1] They like you, and it’s ‘cos you treated ‘em decent."
    unknown "And that got me thinking that I –[wait_05] if the people around me didn’t like me, it’s ‘cos of how I treated ‘em."
    unknown "I was too selfish, Lloyd."
    unknown "All I cared about was myself, and where did it get me?[wait_1] Dead in a ditch."
    unknown "I did some thinking, and...[wait_1]I reckon if I take over your body, nothing’ll change."
    unknown "I’ll still be wasting the life I got, and it won’t be long before I piss someone off and get killed again, or something.[wait_1] I’ll just end up right where I was before."
    unknown "So...[wait_05]I might as well give you your body back."
    unknown "I don’t think that I’ll end up anywhere good, but you –[wait_05] you’ve really got a chance to make something of your life."
    unknown "To...[wait_05]actually live."
    unknown "You seem like a decent guy, and you deserve it more than me."
    lloyd_ws neutral "Are you sure?[wait_1] We may be able to work something out for –"
    hide jack_worried
    show jack_smug at semi_trans, center
    unknown "Nah, don’t bother.[wait_1] I’ve had my chance, and this is what I want."
    unknown "Just do me a favour and kick Killian’s ass for me.[wait_1] This is his place, y’know."
    lloyd_ws neutral "You...[wait_05]know about Killian?"
    unknown "Heh, you could say that."
    unknown "Actually, speaking of him –[wait_05] I oughta see myself out.[wait_1] Should give you a bit more mental energy for when you confront him."
    lloyd_ws neutral "..."
    # TODO: only do this if we've got the other endings
    $ current_thought = "jack_thought_02"
    unknown "Goodbye, Lloyd.[wait_1] I hope you have a good life."
    unknown "Heh. You know, now that I’m disappearing...[wait_05]{size=-8}I think I kinda like this whole helping people out thing.{/size}"
    show jack_smug at semi_trans(0.75), center
    unknown "{size=-9}Should’ve tried it much sooner...[wait_05]it feels nice.{/size}"
    hide jack_smug with slow_dissolve
    hide screen psychic_powers
    lloyd_ws_thinking neutral "...I never even got his name."
    lloyd_ws_narrating neutral "I’m feeling perplexed more than anything.[wait_1] It’s the end of the day, and the man with the white streak was able to find Killian Morgensen in that time."
    lloyd_ws_narrating neutral "I don’t know what he spent the day doing, but he used the time well."
    lloyd_ws_thinking neutral "I’m here now.[wait_1] There’s no reason to hold off on this any further."
    # SFX - Doorbell
    lloyd_ws_narrating neutral "I approach the door and ring the bell.[wait_1] It feels odd to be approaching the house of the man who masterminded the killings so politely, but I’m not the type to kick the door down and fight my way in."
    # TODO - make this bring up the option for whether we get ending F or G
    if (check_boolean("ending_g_unlocked")):
        jump branch_g_4_4
    $ swap_sprites("killian_smiling", quick_dissolve)
    $ current_thought_block = "mind_read_killian"
    $ current_thought = "killian_thought_02"
    show screen psychic_powers
    killian "Hello, how can I –"
    $ swap_sprites("killian_shocked")
    killian "Oh.[wait_1] It’s you."
    lloyd_ws neutral "Hello.[wait_1] Can I...[wait_05]come in?"
    $ swap_sprites("killian_smiling")
    killian "Why not?[wait_1] Let’s discuss this as civilised people.[wait_1] Follow me inside."
    hide killian_smiling
    hide screen psychic_powers
    scene killian_house_interior with slow_dissolve
    $ swap_sprites("killian_smiling")
    show screen psychic_powers
    killian "Please, take a seat.[wait_1] I’d offer you some tea or coffee, but you’ll probably make the assumption that it’s poisoned."
    lloyd_ws_narrating neutral "I do as he suggests.[wait_1] Thankfully, the armchair isn’t coated in poison."
    killian "Now, would I be wrong in presuming that you are here as Docherty informed you about me once my control over him was broken?"
    lloyd_ws neutral "Correct.[wait_1] Why were you using him to kill?"
    $ play_sound("mind_read_l.mp3")
    killian "Why don’t I tell you all about my plans, Mr....[wait_05]Long, is it?"
    lloyd_ws neutral "Long is my given name.[wait_1] But I usually go by Lloyd."
    killian "Oh, is it?[wait_1] My apologies;[wait_05] I thought that I read your given name as Chen.[wait_1] Lloyd it is, then."
    killian "Now, where was I?"
    killian "Ah, yes –[wait_05] shall I tell you all about my plans, Lloyd?[wait_1] My little project to black out the minds of other psychics?"
    killian "I must admit, it feels good to be able to be open about it."
    lloyd_ws_narrating neutral "I nod and gesture for him to continue."
    lloyd_ws_narrating neutral "I’m unsure exactly what I can do to stop him –[wait_05] I haven’t acquired any hard evidence which pins him as the power behind Docherty."
    lloyd_ws_narrating neutral "Even if I had it, I doubt any authorities would recognise it.[wait_1] His control was entirely through his powers."
    lloyd_ws_narrating neutral "For now, my best bet is to hope that he slips up and gives me an opportunity."
    $ swap_sprites("killian_confident")
    killian "I’ll start by answering your question."
    killian "I first encountered Docherty when he broke into this very building.[wait_1] He was on the run, you see, after escaping from prison, and was looking for somewhere to hide."
    killian "In him, I saw an opportunity.[wait_1] By visiting the prison he had escaped from, I was able to control an administrator."
    killian "I had them enter a false record saying that he had been killed, and deleted the information about his escape.[wait_1] Hardly anything that would stand up to excess scrutiny, but enough to confuse and delay anyone should they recognise him while I sent him out."
    lloyd_ws neutral "So you used Docherty to kill since it would give you a cat’s paw.[wait_1] Someone expendable if something went awry."
    killian "Indeed.[wait_1] You are likely also wondering how you ended up on my list?"
    killian "Initially, I was unaware of your abilities.[wait_1] No doubt I would have found you given some additional time, but I first became aware of you when Docherty encountered you at that venue the other night."
    hide killian_confident
    scene venue_interior at greyscale_instant with slow_dissolve
    show docherty_neutral at greyscale_instant, center with quick_dissolve
    killian "You see, one of my psychic abilities is the power to detect the presence of psychic energy."
    killian "If I concentrate I can detect other psychics over a large area, but on getting close to you that night, I was able to detect your psychic energy."
    killian "I noticed that it was nearly identical to the energy of another of my victims –[wait_05] one I had killed just a few days earlier –[wait_05] and it piqued my interest."
    killian "Naturally, I sent Docherty after you the next night, where he encountered you and your friend at the newspaper."
    hide docherty_neutral with quick_dissolve
    scene killian_house_interior with slow_dissolve
    $ swap_sprites("killian_confident", quick_dissolve)
    lloyd_ws_narrating neutral "Killian has a handgun resting on a nearby coffee table.[wait_1] The glint from its barrel caught my eye."
    lloyd_ws_narrating neutral "If I can keep him talking, he may relax enough for me to get ahold of it."
    lloyd_ws neutral "So when you say that Docherty getting close to me enabled you to notice my energy..."
    killian "Oh, was it not obvious?[wait_1] I was controlling Docherty the entire time."
    killian "Puppeting him with my mental powers.[wait_1] Those very same mental powers which I wish to grow in strength."
    $ swap_sprites("killian_smiling")
    # Could theoretically do a CG here where we see a circle with four arrows pointing to people, showing 25%, then it changes to two people, showing 50%
    killian "You see, Lloyd –[wait_05] there is only so much psychic energy in the world."
    killian "The fewer psychics there are, the more each of us can access it –[wait_05] thus meaning that the strength of our remaining abilities grows."
    killian "Surely you’ve noticed your own abilities growing over the last few days?"
    lloyd_ws_narrating neutral "I shift my chair slightly closer to the coffee table.[wait_1] From here I could probably reach the gun if I dive towards it."
    lloyd_ws_thinking neutral "No...[wait_05]diving towards a gun will result in it going off and a bullet ending up somewhere I don’t want it to.[wait_1] I need to get closer."
    lloyd_ws neutral "And you want your abilities to grow because...?"
    $ swap_sprites("killian_confident")
    killian "Why, isn’t it obvious?[wait_1] At present I can only control a single person at a time, and the process drains my strength considerably."
    killian "As my psychic abilities gain in strength, I will be able to control more and more people, and with much less effort.[wait_1] Over time I daresay I will be able to control as many people as I want, without even having to get close to them."
    killian "And once I have achieved that state...[wait_05]I will be able to do whatever I want."
    lloyd_ws neutral "So everybody you encounter will simply do whatever you want them to?[wait_1] No free will at all?"
    lloyd_ws neutral "I can’t think of anything more selfish."
    killian "I envy you, Lloyd.[wait_1] I would have once also felt the same way, were I in your position."
    killian "I remember those days, back when I was innocent, and hadn’t seen the way in which the world truly works."
    killian "Tell me –[wait_05] before I retired, what do you think I did for a living?"
    lloyd_ws_narrating neutral "I shift my chair slightly closer to the coffee table."
    lloyd_ws_narrating neutral "I could probably reach the gun if I took a large step and stretched my arm as much as possible."
    lloyd_ws neutral "I don’t know.[wait_1] No doubt something insane."
    $ swap_sprites("killian_smiling")
    killian "I was a teacher, Lloyd.[wait_1] I believed that if I taught young minds –[wait_05] imparted some wisdom and love for humanity into them –[wait_05] then I could help to fix the world, and do some good."
    killian "I had read plenty of adult minds and knew that they regularly held nothing but twisted desires and concealed lust, but I thought that by reaching people when their minds and beliefs were still flexible, I could have them look at the bigger picture, and think of others beyond themselves."
    killian "My plan worked well enough in the beginning."
    lloyd_ws neutral "And then they grew up."
    $ swap_sprites("killian_cold")
    killian "Correct.[wait_1] They grew up, and when I reached out, or looked them up, I was constantly disappointed."
    killian "I won’t deny that some of them grew to do good in the world –[wait_05] one of my former students became a fairly prominent author with a strong body of work, and another became a local politician who successfully implemented many positive changes in their community."
    killian "Some of the seeds that I planted sprouted successfully."
    killian "The majority of them didn’t, however.[wait_1] Plenty of my students fell to all the usual vices of the world –[wait_05] drugs, alcohol, sex, greed."
    killian "Some died as young as in their teens, due to either their mistakes or those of others."
    killian "Many of them grew up and went to work for immoral companies –[wait_05] no doubt with justifications had I approached them and asked why their standards had dropped so low."
    killian "As it is, though, I don’t blame them."
    killian "It’s not their fault that the world is the way it is, encouraging everyone to be selfish and hedonistic.[wait_1] I wish that they would resist it more, but it’s difficult to fight the machine."
    lloyd_ws neutral "And so seeing generations of students fail to live up to your standards justifies your plan?"
    $ swap_sprites("killian_confident")
    killian "You’re asking the wrong question, Lloyd." 
    killian "What you should really ask yourself is:[wait_05] why shouldn’t I be selfish?"
    lloyd_ws_narrating neutral "I move a little closer to the coffee table.[wait_1] The corner of it is touching my knee."
    lloyd_ws neutral "I can’t wait to hear your reasoning for this."
    killian "Everybody is selfish, Lloyd.[wait_1] Or do you truly claim to be selfless in your goals?"
    killian "Answer me this:[wait_05] why did you come here?"
    killian "Did you hope to stop me for the sake of others?[wait_1] Or was it really, honestly, because you had something to gain from it?"
    killian "Because you wanted acclaim, or a sense of accomplishment?"
    $ play_sound("mind_read_l.mp3")
    $ swap_sprites("killian_smiling")
    killian "No...[wait_05]what’s this?[wait_1] You wanted to get a story out of it?[wait_1] To use that as leverage to get a new job?"
    killian "Well then...[wait_05]it seems as though someone doesn’t practice what he preaches."
    lloyd_ws neutral "I won’t deny that I initially investigated Docherty’s killings with the story in mind."
    lloyd_ws neutral "But that doesn’t mean that I don’t want to do good at the same time.[wait_1] I’m still helping others."
    $ swap_sprites("killian_confident")
    killian "That’s how it always starts –[wait_05] a little justification to yourself and you’ll soon be convinced that all of your actions are flawless."
    killian "At least I don’t deny that I’m selfish.[wait_1] Can you blame me?"
    killian "Trying to be selfless, and think of others –[wait_05] all that it will get you is disappointment as others exploit you."
    killian "If you embrace selfishness, and simply live according to your desires, then you’ll be much happier.[wait_1] As they say, if you can’t beat them, join them."
    lloyd_ws neutral "The world isn’t as selfish as you say."
    killian "Isn’t it?[wait_1] Look around you."
    killian "We’ve known about climate change and the harm being done to the environment for decades now.[wait_1] Yet nobody does anything about it."
    killian "Countries talk about reducing emissions, about switching to cleaner fuels, and yet they continue to open coal mines and burn carbon."
    killian "People continue to use damaging technologies and refuse to switch to more eco-friendly alternatives, simply because “it’s easier”."
    killian "How about cigarettes and the tobacco industry?[wait_1] By now the dangers of them are well known;[wait_05] nobody could claim to be ignorant about the harm they do."
    killian "Why are they not banned?[wait_1] Why do people manufacture them?[wait_1] Because they want money, and are willing to kill millions slowly to do so."
    killian "They advertise shamelessly and shove their products in peoples’ faces, then act innocent when people get sick."
    killian "On the global stage, world leaders squabble and argue over petty issues, allowing their egos to lead the decisions."
    killian "They prioritise their own countries’ needs, helping others only when it gets them something in return."
    killian "Why don’t they work together to solve world hunger?[wait_1] To initiate ceasefires and stop war?"
    killian "There are enough resources for everyone on the planet to share.[wait_1] But some have decided that it wouldn’t be enough."
    killian "Having everything would be insufficient to sate their greed, and yet they still try to have it all."
    killian "Even among the common man selfishness abides in their daily lives."
    killian "People will claim that representation matters;[wait_05] that more diversity in cultures and lifestyles are important to show in different forms of media."
    killian "But all that they ever care about is representation of their own cultures."
    killian "They rarely go out of their way to view other representations and see other viewpoints;[wait_05] all they do is view repeated variations of their existing interests and demographics.[wait_1] Even then, they’ll critique a work for not hewing exactly to their experiences."
    killian "That’s when they’re not blindly praising a work for representation without meaningfully engaging in it and acknowledging its flaws."
    killian "Consider all of that, Lloyd."
    killian "Consider how divided the world is, how unbalanced the distribution of wealth is."
    killian "Consider the problems that have been present and known for decades, if not centuries, and yet still have not been solved."
    killian "Consider the petty complaints and minor issues that people whine about, choosing to make mountains out of molehills rather than forgiving and forgetting."
    killian "Consider all of that, and then tell me:[wait_05] is the world selfish?"
    menu:
        "Yes":
            lloyd_ws neutral "You’re correct.[wait_1] The world is selfish."
            killian "Brilliant.[wait_1] It’s hard to deny, isn’t it?"
            lloyd_ws neutral "Just because it’s selfish, though, that doesn’t mean that I have to be.[wait_1] Nor do you."
            lloyd_ws neutral "To look at the state of the world and conclude that it justifies a lack of empathy will only make things worse."
            lloyd_ws neutral "If you instead focus on what you can do, rather than looking at what others are doing, you can make a change."
        "No":
            lloyd_ws neutral "You’re wrong.[wait_1] The world isn’t selfish."
            killian "All of those examples I just listed are just mild outliers, are they?"
            lloyd_ws neutral "I won’t deny that there are selfish people or that things could be better.[wait_1] But you’re ignoring the good in the world."
            lloyd_ws neutral "Charities, medical researchers, mental health professionals, social workers, environmental conservationists –[wait_05] there are many professions dedicated to helping people and fixing the world."
            lloyd_ws neutral "You’re choosing to focus on the negative examples to justify being selfish."
    $ swap_sprites("killian_cold")
    killian "Is that what you believe?[wait_1] Well then, we’ll just have to agree to disagree."
    lloyd_ws_narrating neutral "I’ve moved my chair slightly closer again.[wait_1] I can reach the gun from where I am."
    killian "Only if I let you."
    lloyd_ws_thinking worried "What?!"
    lloyd_ws_narrating worried "Killian reaches for the gun and has it in his hand before I can do anything."
    hide killian_cold
    scene cg13_0 with slow_dissolve
    killian "You really shouldn’t look so surprised, Lloyd.[wait_1] You were practically screaming your thoughts at me."
    killian "You should learn how to ward your mind.[wait_1] Or, rather, if you weren’t about to die, you should."
    lloyd_ws neutral "You’d rather shoot me than debate, huh?"
    killian "On the contrary!"
    killian "Let me tell you what we are going to do:[wait_05] I am going to fire this gun at you an unknown number of seconds after I finish talking."
    killian "If selflessness really is as important to you as you say it is, you’ll let it hit you so that I may increase my power."
    killian "If, however, you’re a hypocrite who cares only about himself, you’ll attempt to read my mind."
    killian "If you’re successful then you should find it quite easy to know where I will aim and when I will shoot, allowing you to dodge the bullet."
    lloyd_ws neutral "The odds seem quite skewed in your favour."
    killian "I suppose that I’m just being selfish."
    killian "Now, begin!"
    scene killian_house_interior
    $ swap_sprites("killian_cold", quick_dissolve)
    # TODO: add in psychic interface where if we choose mind read or mind wipe we get a game over; future sight moves us forwards; timing out also gives us a game over
    lloyd_ws_thinking neutral "...Now!"
    lloyd_ws_narrating neutral "I throw myself to the side and out of the way of the bullet.[wait_1] Killian fires the gun exactly as I saw him do with my precognition, which misses me."
    $ swap_sprites("killian_shocked")
    $ rewind_point = "branch_f_ending"
    killian "What?![wait_1] How did you do that?[wait_1] You can’t have read my mind!"
    lloyd_ws neutral "Trade secret."
    killian "..."
    $ swap_sprites("killian_smiling")
    $ current_thought = "killian_thought_03"
    $ rewind_point = ""
    killian "Well then –[wait_05] let’s see you dodge this one."
    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
    scene black_bg
    narrator "GAME OVER"
    $ MainMenu()

label branch_f_ending:
    show screen psychic_powers
    lloyd_ws_thinking worried "He’s been taken off guard –[wait_05] this might be the most vulnerable he’ll get!"
    # TODO: Set up abstract art and colours and stuff here?
    lloyd_ws_narrating neutral "My mind reaches out and touches his."
    lloyd_ws_narrating neutral "Psychic energies grapple with one another.[wait_1] Mine are victorious."
    lloyd_ws_narrating neutral "I push more power into them than I have before, needing them to be more effective than ever."
    lloyd_ws_narrating neutral "It feels like hours have passed by the time I’m done.[wait_1] I’m unsure whether I’m successful or not."
    $ swap_sprites("killian_despairing")
    $ current_thought = "killian_thought_04"
    killian "..."
    lloyd_ws neutral "...Killian?"
    lloyd_ws_narrating neutral "The gun has been dropped in the conflict.[wait_1] I’m unsure what to do about it."
    $ current_thought = "killian_thought_05"
    killian "I –[wait_05] I’m sorry, I –[wait_05] I don’t believe I know who you are."
    killian "How...[wait_05]how did you get into my house?"
    lloyd_ws_thinking neutral "His confusion seems genuine."
    lloyd_ws neutral "What’s the last thing you remember?"
    $ current_thought = "killian_thought_06"
    killian "I –[wait_05] I had a plan that I wanted to enact, but I...[wait_05]I can’t remember what it was."
    lloyd_ws_narrating neutral "Up to now I’ve been unsure about what to do with Killian.[wait_1] I don’t want to kill him."
    lloyd_ws_narrating neutral "As he speaks I finally realise the answer."
    $ current_thought = "killian_thought_07"
    lloyd_ws neutral "I know what you’re speaking of.[wait_1] It’s a plan that we made together."
    killian "It is?"
    lloyd_ws neutral "Yes.[wait_1] We’re going to use our psychic powers to improve the world."
    hide killian_despairing with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    scene bar with slow_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought_block = "mind_read_barbara"
    $ current_thought = "barbara_thought_311"
    show screen psychic_powers
    barbara "Hey, Lloyd.[wait_1] You ready to start?"
    lloyd_ws friendly "Of course, Barbara.[wait_1] Is there anything in particular that you wanted me to focus on?"
    barbara "As long as you get some good shots of the bar itself I think that’s the important thing."
    barbara "But otherwise I figured I should sit back a little and follow your lead –[wait_05] you’ll have a better eye for this than I do."
    lloyd_ws friendly "Right.[wait_1] I see no reason not to focus on the bar to begin with, in that case." 
    lloyd_ws friendly "I’ve brought a snoot in case you want to highlight anything in particular, but to start with I’ll be using a softbox to try and soften the impact of the flash."
    $ swap_sprites("barbara_thinking")
    barbara "How about you just take the photos, and then I’ll tell you what I think needs changing afterwards?[wait_1] We can work it out from there."
    lloyd_ws friendly "That makes sense.[wait_1] Could you please grab that –"
    barbara "Sorry, just one question before we start, Lloyd."
    lloyd_ws friendly "Yes?"
    barbara "It’s very generous of you to offer to take some promotional photos of the bar, and on top of that you said that you might be able to use some media contacts to get a review written up...[wait_05]not that I don’t appreciate it, but...[wait_05]why are you going so far out of your way for me?"
    lloyd_ws friendly "Why shouldn’t I?[wait_1] I’ve got the ability to help you;[wait_05] I’m sure that you’d do the same for me if the situation was reversed."
    barbara "That’s really all that it is?"
    lloyd_ws friendly "Are you disappointed by my motive?"
    $ swap_sprites("barbara_smiling")
    barbara "No.[wait_1] It’s just nice to meet someone who cares so much about others."
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    scene library_day with slow_dissolve
    $ swap_sprites("cat_neutral", quick_dissolve)
    $ current_thought_block = "mind_read_cat"
    $ current_thought = "cat_thought_216"
    show screen psychic_powers
    lloyd_ws neutral "...and that’s why it happened.[wait_1] I’m sorry that I wasn’t able to act sooner and save him."
    cat "..."
    lloyd_ws neutral "How are you feeling, Cat?"
    cat "...Not ideal." 
    cat "To tell you the truth...[wait_1]I want to hurt this Killian person.[wait_1] I want him to understand the magnitude of what he did to me...[wait_1]I want him to pay."
    lloyd_ws neutral "I understand your feelings.[wait_1] But I’d advise against it."
    cat "Why?"
    lloyd_ws neutral "You’re not the only person that’s experienced loss.[wait_1] You’re not the only person that’s been hurt."
    lloyd_ws neutral "And if you can process your emotions in a healthier way, and learn to move on, I think that would be better for the world at large, rather than adding to the endless cycle of revenge.[wait_1] Don’t you?"
    cat "...[wait_1] I’m not sure, Lloyd."
    lloyd_ws neutral "If it helps, Killian is repentant.[wait_1] He is making up for what he’s done."
    lloyd_ws neutral "I’m not asking you to forgive a selfish, arrogant killer.[wait_1] He’s no longer the man he once was."
    cat "...[wait_1]I’ll see how I feel."
    cat "I hear your words, but...[wait_1]I don’t know whether I can move on that easily."
    lloyd_ws friendly "Maybe not.[wait_1] But either way, I’ll be here for you if you need it."
    cat "Thank you, Lloyd."
    hide cat_neutral with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    scene office_interview_room with slow_dissolve
    $ swap_sprites("eddie_unimpressed", quick_dissolve)
    $ current_thought_block = "mind_read_eddie"
    $ current_thought = "eddie_thought_254"
    show screen psychic_powers
    lloyd_ws friendly "...and so by aiming to have odd-numbered groupings of items or people when you compose your photos, you’ll be able to hold your viewers’ attention more."
    lloyd_ws friendly "Even-numbered groupings subdivide into groups of equal sizing, so they homogenise somewhat and look the same at a glance."
    eddie "Hmph.[wait_1] I guess that makes sense."
    eddie "But you really don’t need to tell me this stuff, Chen.[wait_1] I already basically know it."
    lloyd_ws friendly "Do you want me to stop giving you advice on how you can improve the photos you take, Eddie?[wait_1] If you’re finding it redundant –"
    eddie "Hey, I never said I wanted you to stop.[wait_1] I’m just saying that a lot of the stuff you’re telling me is kind of obvious."
    eddie "And anyway, why do you want me to know this stuff?[wait_1] What’s in it for you?"
    lloyd_ws friendly "Nothing.[wait_1] But I can –"
    eddie "Oh, seriously?[wait_1] You expect me to believe that?"
    eddie "You’re clearly hoping that I can get you a job here, aren’t you?"
    lloyd_ws friendly "I wouldn’t say no to a recommendation."
    $ swap_sprites("eddie_arrogant")
    eddie "Ha![wait_05] I knew it –[wait_05] all you care about is yourself, Chen."
    eddie "You’re not as charitable as you think you are."
    lloyd_ws friendly "Maybe not.[wait_1] But regardless of whether or not you can assist me in finding employment, I’ll be helping you out."
    lloyd_ws friendly "If a side effect of my being selfish is doing good, is that such a bad thing?"
    $ swap_sprites("eddie_unimpressed")
    eddie "Hmph.[wait_1] Whatever."
    eddie "Just keep telling me what you think...[wait_05]maybe I’ll give my boss a heads-up next time we’re looking for some freelancers."
    lloyd_ws friendly "Thank you, Eddie."
    hide eddie_unimpressed with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    scene detective_office with slow_dissolve
    $ swap_sprites("graves_smiling", slow_dissolve)
    $ current_thought_block = "mind_read_graves"
    $ current_thought = "graves_thought_288"
    show screen psychic_powers
    graves "Lloyd![wait_1] How can I help you today, my good friend?"
    lloyd_ws friendly "Actually, Graves, I was going to ask you the same question."
    $ swap_sprites("graves_thinking")
    graves "As in...[wait_05]how could you help me?[wait_1] What exactly do you mean by that?"
    lloyd_ws friendly "Exactly as it sounds:[wait_05] is there anything that you’d like my assistance with?"
    $ swap_sprites("graves_smiling")
    graves "Lloyd![wait_1] I’m touched!"
    $ swap_sprites("graves_thinking")
    graves "I’m also a bit confused."
    graves "Not that I don’t appreciate it, but –[wait_05] can I ask what exactly has inspired this...[wait_05]philanthropy?"
    lloyd_ws friendly "I’ve been thinking about what you said the other day when I visited you."
    lloyd_ws friendly "About how we don’t need to prioritise our own needs above others’.[wait_1] About how we should help each other more, and think of others."
    lloyd_ws friendly "If I hadn’t heard you say that, I think that I would be in a very different place now...[wait_05]but even disregarding that, it’s true."
    $ swap_sprites("graves_smiling")
    graves "Glad to hear that you took my words to heart, then."
    graves "In that case, yeah –[wait_05] there is some stuff that I could use some help with.[wait_1] How much time do you have?"
    lloyd_ws friendly "At present, plenty." 
    lloyd_ws friendly "But I’m also currently unemployed, and looking for work.[wait_1] Once I get a job –"
    graves "– you won’t have as much time, yeah.[wait_1] I get you.[wait_1] But it’s all good."
    lloyd_ws friendly "Are you certain?[wait_1] It doesn’t feel good to volunteer my time when I can’t guarantee how much of it will be free in the future."
    graves "It’s more than fine.[wait_1] Every little bit makes a difference."
    graves "If more people did small things here and there –[wait_05] donating to charity, volunteering at soup kitchens and op shops, picking up rubbish –[wait_05] then I think the world would be in a much better place."
    lloyd_ws friendly "What does any of that have to do with your detective agency?"
    graves "Not a lot.[wait_1] But it’s a nice thought to have regardless, isn’t it?"
    lloyd_ws friendly "True."
    graves "Anyway, you say that you’ve got a fair bit of time right now.[wait_1] In terms of help that you can give me...[wait_05]oh, I know."
    graves "How much do you know about different blood types?"
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    scene killian_house_interior with slow_dissolve
    $ swap_sprites("killian_smiling")
    $ current_thought_block = "mind_read_killian"
    $ current_thought = "killian_thought_08"
    show screen psychic_powers
    killian "Ah, Lloyd!"
    killian "Good to see you, my friend![wait_1] How are you?"
    lloyd_ws friendly "I’m doing well, Killian.[wait_1] Are you ready?"
    killian "Indeed I am.[wait_1] Let us discuss how we can save the world."
    hide killian_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    narrator "ENDING F"
    $ MainMenu()

label branch_g_4_4:
    $ swap_sprites("killian_smiling", quick_dissolve)
    $ current_thought_block = "mind_read_killian"
    $ current_thought = "killian_thought_09"
    show screen psychic_powers
    killian "Hello, how can I –"
    $ swap_sprites("killian_shocked")
    killian "Oh.[wait_1] It’s you."
    lloyd_ws neutral "Hello.[wait_1] Can I...[wait_05]come in?"
    $ swap_sprites("killian_smiling")
    killian "Why not?[wait_1] Let’s discuss this as civilised people.[wait_1] Follow me inside."
    hide killian_smiling
    hide screen psychic_powers
    lloyd_ws_narrating neutral "I follow Killian inside."
    scene black_bg with slow_dissolve
    lloyd_ws_narrating neutral "What I find next is a complete surprise."
    scene cg14_0 with slow_dissolve
    unknown "SURPRISE!" (name="Everyone")
    lloyd_ws smiling "Aww, guys.[wait_1] How did you know that it was my birthday?"
    barbara "Jack told us![wait_1] He found all sorts of information while he was in your head."
    jack "No need to thank me or anything, Lloyd.[wait_1] I do it for the love of the game."
    lloyd_ws smiling "And you managed to get this all ready in such little time?"
    sergei "Of course![wait_1] Are we not the most magnificent group that the eyes of the world have ever gazed upon?"
    sergei "Have we not the skill, the abilities, to –"
    graves "He’s saying this now, but he was panicking more than anybody else when it looked like we were going to be –[wait_05] when it looked like we couldn’t get it set up in time."
    killian "Why is everybody standing around talking, when we could be having cake?"
    docherty "Go on, Lloyd –[wait_05] you have the first piece."
    lloyd_ws smiling "Are you sure?[wait_1] I’m happy for somebody else to –"
    cat "Go on...[wait_1]you deserve it..."
    lloyd_ws smiling "If you insist."
    eddie "Chen![wait_1] Get in close with the others, so I can show you how much better my photography is than yours!"
    eddie "...Alright, ready?"
    unknown "Ready!" (name="Everyone")
    eddie "Three...[wait_05]two...[wait_05]one..."
    unknown "CHEESE!" (name="Everyone")
    scene cg15_0 with slow_dissolve
    narrator "ENDING G"
    $ MainMenu()

    return