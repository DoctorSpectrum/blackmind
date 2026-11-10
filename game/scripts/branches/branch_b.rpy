label branch_b_3_4:
    $ branch = "b"
    $ day = 3
    $ current_thought_block = "mind_read_barbara"

    lloyd_thinking thinking "Barbara said that she’d been visited by the man with the white streak the same night that he was killed."
    lloyd_thinking thinking "If I travel to her bar she should have the footage from that night for me to see."
    lloyd_thinking thinking "It might tell me something about who he is or give me an idea of why he was killed."
    lloyd_narrating neutral "Once again I take the train northwards to Barbara’s business."
    lloyd_narrating neutral "The journey is becoming familiar enough that I can recognise the order of stations that we’ll stop at and how long it will take to reach my destination."
    lloyd_narrating neutral "I cut through several alleys on the way to Barbara’s, the shortcuts making themselves more known to me as I visit more and more often."
    scene bar with slow_dissolve
    lloyd_narrating neutral "As we get further into the week Icarus is getting busier and busier."
    lloyd_narrating neutral "The sounds of laughter and exclamations surround me as I make my way up to the bar."
    lloyd_narrating neutarl "I wish that there was an unintrusive way to take some photos of the crowd and capture this atmosphere.[wait_1] It feels warm and inviting, the complete opposite of when I visited two days ago."
    lloyd_narrating neutral "Once I’m finally served I’m more surprised than I should be to see that Barbara isn’t working the bar tonight; it’s an employee of hers."
    lloyd_narrating neutral "I ask to speak to her and sit at a nearby table to wait."
    $ swap_sprites("barbara_smiling", slow_dissolve)
    $ current_thought = "barbara_thought_103"
    show screen psychic_powers
    lloyd neutral "Hello, Barbara.[wait_1] Tonight seems quite busy."
    $ current_thought = "barbara_thought_104"
    barbara "Ha, you call this busy?[wait_1] Not that I’m complaining, but this is nowhere near the numbers I’m hoping for."
    barbara "The bar’s done a lot better in the past."
    $ current_thought = "barbara_thought_105"
    lloyd neutral "It’s busier than it was earlier in the week."
    $ swap_sprites("barbara_thinking")
    barbara "True, but this is pretty usual for Thursdays.[wait_1] People get tired from the daily grind, and they’re more open to different ways to relieve the pressure."
    $ current_thought = "barbara_thought_106"
    lloyd_narrating neutral "She stares out over the crowd.[wait_1] She looks pleased enough, but I can tell that there’s some worry within her too."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_107"
    barbara "Anyway, I’m guessing you haven’t come by for a drink?"
    $ current_thought = "barbara_thought_108"
    lloyd neutral "Sorry, but I’m still here for business.[wait_1] Were you able to find the footage of the man with the white streak?"
    $ swap_sprites("barbara_thinking")
    barbara "I did, but...[wait_05]it’s weird.[wait_1] It doesn’t match up with my memories from that night."
    lloyd neutral "What do you mean?"
    barbara "I transferred the footage to my phone.[wait_1] Tell me what it looks like to you."
    hide screen psychic_powers
    lloyd_narrating neutral "Barbara passes her phone over to me and presses play on the video.[wait_1] The point of view is from above the bar."
    lloyd_narrating neutral "The footage of the video is grainy and low quality, skipping a few frames every few seconds."
    lloyd_narrating neutral "From the beginning of the footage is a man at the bar."
    lloyd_narrating neutral "He has a white streak through his hair, a small soul patch, and is wearing a dark green shirt."
    lloyd_narrating neutral "The footage isn’t detailed enough to show whether he has a gap in his teeth, but I don’t need to confirm his identity at this point."
    lloyd_narrating neutral "It’s the same man that I encountered later that night.[wait_1] It’s the victim of the man in black."
    lloyd_narrating neutral "The footage has no sound but it’s unnecessary.[wait_1] I can see the man with the white streak order a drink from Barbara, which she serves him without payment."
    lloyd_narrating neutral "He drinks it quickly, and after talking to her again receives another one.[wait_1] The process repeats multiple times."
    show screen psychic_powers
    $ current_thought = "barbara_thought_109"
    lloyd neutral "Is there a reason that you didn’t charge him?"
    barbara "That’s the thing...[wait_05]I don’t know.[wait_1] I don’t remember any of this."
    $ current_thought = "barbara_thought_110"
    lloyd neutral "What do you mean?"
    barbara "Here’s what I would have told you about that night –[wait_05] I set things up for the evening and then waited for the first few customers to come in."
    scene bar_greyscale with quick_dissolve
    barbara "Mondays are usually pretty quiet, so I wasn’t expecting to be too busy."
    show jack_smug at greyscale_instant, center with quick_dissolve
    barbara "Eventually this guy came in and started talking to me.[wait_1] He was kind of up himself, but I was looking forward to the first sale of the night, and so I put up with it."
    barbara "As he kept talking, though...[wait_05]he said that he was a reviewer, and that if I gave him a free drink he’d give me a good review."
    barbara "I was pretty tempted by the deal, but he –[wait_05] his whole demeanour had changed."
    barbara "I realised that he was –[wait_05] somehow I’d missed that he was stinking drunk."
    barbara "He clearly wasn’t a reviewer –[wait_05] just some jerk looking for a handout.[wait_1] I kicked him out then."
    barbara "I realised a bit later that we’d spoken for way longer than I’d thought, but otherwise, I didn’t think about him until you asked about him earlier today."
    scene bar with quick_dissolve
    $ swap_sprites("barbara_thinking", quick_dissolve)
    barbara "So with all of that in mind...[wait_05]why is there footage of me serving him drinks?"
    barbara "Why don’t I remember any of this?"
    barbara "It’s –[wait_05] the obvious answer would be that this is faked footage, but how would it have gotten onto my server?[wait_1] And who would benefit from it?"
    lloyd_narrating neutral "There are many questions that need to be answered."
    lloyd_narrating neutral "There are many problems with what she’s shown me in the footage."
    lloyd_narrating neutral "But there’s only one thing which I’m focusing on, one thing which has my attention."
    $ current_thought = "barbara_thought_111"
    lloyd neutral "You don’t remember any of this?"
    barbara "No, not at all."
    lloyd_thinking thinking "Just like how I forgot most of my Tuesday night."
    lloyd_thinking thinking "But that was due to my psychic powers backfiring, which –"
    $ current_thought = "barbara_thought_112"
    lloyd_narrating neutral "Psychic powers.[wait_1] They can erase memories."
    lloyd_narrating neutral "I ask to watch the footage again and take note of what the man with the white streak is doing."
    lloyd_narrating neutral "It’s obvious now what’s happening."
    lloyd_thinking thinking "He’s erasing her memories whenever he finishes his drink so that she’ll give him a new one."
    lloyd_thinking thinking "He – he has psychic powers, and is exploiting them to get alcohol for free.[wait_1] That’s what’s happening in the footage."
    $ current_thought = "barbara_thought_113"
    barbara "Do you have any ideas?"
    lloyd_narrating neutral "I’m not listening to her.[wait_1] I’m straining my memory to recall what exactly the man with the white streak said when I encountered him."
    hide screen psychic_powers
    scene cg2_0 with slow_dissolve
    dying_jack "I’m done for...but you –[wait_05] you can stop him...[wait_05]please...[wait_05]for me?"
    show screen psychic_powers
    scene bar with quick_dissolve
    $ swap_sprites("barbara_thinking", quick_dissolve)
    $ current_thought = "barbara_thought_114"
    lloyd_thinking thinking "He wanted me to use his psychic powers to stop the killer."
    lloyd_thinking thinking "He – he must have transferred them to me when he touched me."
    lloyd_thinking thinking "It was only once that happened that my headache began."
    lloyd_narrating neutral "I set out today aiming to discover who the man with the white streak was.[wait_1] I wanted to find out why he had been targeted by the man in black."
    lloyd_narrating neutral "It looks like I’ve succeeded in my goal."
    lloyd_thinking thinking "He had psychic powers.[wait_1] It’s the only significant thing that I’ve discovered about him."
    lloyd_thinking thinking "I don’t know how the man in black discovered this information, but he must have been targeted for that reason."
    lloyd_thinking thinking "My vision that I saw the other night –[wait_05] the man in black must have been eliminating another psychic."
    lloyd_thinking thinking "I wonder..."
    $ current_thought = "barbara_thought_115"
    lloyd neutral "Tell me, Barbara:[wait_05] has this ever happened before?"
    lloyd neutral "Have there been any other times that your security footage hasn’t matched your memories of a night?"
    barbara "I...[wait_05]I don’t think so." 
    barbara "But then until I looked up this footage I wouldn’t have said that it had ever happened."
    $ current_thought = "barbara_thought_116"
    lloyd_thinking thinking "It was just dumb luck that Barbara found evidence of the man with the white streak’s powers through her footage."
    lloyd_thinking thinking "But she may have been visited by other psychics in the past who similarly exploited her."
    $ current_thought = "barbara_thought_117"
    lloyd neutral "Look up more of your camera records.[wait_1] I’d like to know if this has happened before."
    barbara "I...[wait_05]like the idea of doing that, but I –[wait_05] I don’t know if I’ll have the time to."
    $ swap_sprites("barbara_sad")
    $ current_thought = "barbara_thought_118"
    barbara "Even if I did, and found something like this happening in it –[wait_05] it’s not like it’s going to get back the money that I’ve lost."
    barbara "However this person –[wait_05] and anyone else like him –[wait_05] did this, it’s –[wait_05] it’s already happened.[wait_1] It’s better to cut my losses."
    lloyd neutral "But you might discover –"
    barbara "Might isn’t the same as will, Lloyd.[wait_1] I’m glad to have found this, but it doesn’t change the past."
    barbara "The money I could have made is gone."
    lloyd_thinking thinking "I need her to look at her footage so that I can find other psychics."
    lloyd_thinking thinking "...I think I know what to do."
    $ current_thought = "barbara_thought_119"
    lloyd neutral "At the moment it’s gone, yes –[wait_05] but there’s a reason that I was asking about the man with the white streak.[wait_1] I’ve been building a case against him and his associates."
    $ swap_sprites("barbara_thinking")
    barbara "A case?[wait_1] As in –[wait_05] you’ve been preparing to prosecute him?"
    lloyd neutral "Along those lines."
    lloyd neutral "If you can go through your security footage –[wait_05] even if it’s only a few days’ worth –[wait_05] then I’ll know whether I can rely on it for evidence, or whether it can be used against me."
    lloyd neutral "Either way, I’m confident that I can get you some compensation."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_120"
    barbara "Wait –[wait_05] really?"
    lloyd neutral "I wouldn’t say so if it weren’t true."
    lloyd_thinking thinking "The lie is for a good cause.[wait_1] I’m sure that she would understand."
    $ current_thought = "barbara_thought_121"
    barbara "Wow –[wait_05] that’s amazing!"
    barbara "So you –[wait_05] you think that whatever’s happening in the footage is –[wait_05] that it’s happened here before?[wait_1] That it could have been going on for a while?"
    lloyd neutral "It’s more than likely."
    barbara "That’s –[wait_05] Lloyd, you fucking beautiful man!"
    barbara "I’ll –[wait_05] I need a bit of time to actually look through the footage I have."
    barbara "Do you want to come back here tomorrow evening and I’ll show you whatever I find?"
    lloyd neutral "That sounds like a plan to me."
    lloyd_thinking thinking "Depending upon what she finds I might have to string her along a bit further."
    lloyd_thinking thinking "But if I can find some more psychics it will all be worth it."
    $ current_thought = "barbara_thought_122"
    barbara "Well, here’s to the start of something big![wait_1] Can I get you anything to celebrate?" 
    barbara "How about a pilsner?"
    $ current_thought = "barbara_thought_123"
    lloyd neutral "Thank you, but I’d better head home.[wait_1] I have a lot to think about."
    barbara "Of course –[wait_05] I’ll see you tomorrow then.[wait_1] Don’t keep me waiting for too long!"
    hide barbara_smiling 
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    scene apartment_night with slow_dissolve
    lloyd_narrating neutral "I find myself wondering about other psychics the entire trip back to my apartment."
    lloyd_narrating neutral "Do they have any sort of community?[wait_1] Is there a way to contact them?[wait_1] How can I find them?"
    lloyd_thinking thinking "The man in black’s next victim will be another psychic."
    lloyd_thinking thinking "If Barbara can find footage of another one I’ll track them down and warn them."
    lloyd_thinking thinking "If she can’t then I’ll have to trust in my other contacts."
    lloyd_narrating neutral "It’s a problem to be solved tomorrow.[wait_1] For now there is only the quiet embrace of sleep."
    scene black_bg with slow_dissolve
    mental_jack "{size=-8}(Dammit...[wait_05]I’m too weak.){/size}"
    mental_jack "{size=-8}(I thought I could build up my strength more...[wait_05]but I can’t.[wait_1] It’s all over.){/size}"
    mental_jack "{size=-8}(At least I had a bit of fun the other night...){/size}"
    return

label branch_b_4_0:
    # Power upgrade
    $ branch = "b"
    $ day = 4
    call screen chapter_breaks("FRIDAY", "Lloyd is trying to find others with psychic abilities. He knows that the man in black is killing them and is determined to warn them.\n\nHe hasn’t considered the obvious yet.")
    scene apartment_day with slow_dissolve
    lloyd_thinking thinking "I may not have discovered anything about the man in black, but I was able to find out a little about the man with the white streak."
    lloyd_thinking thinking "He had psychic powers and was killed because of them, but managed to transfer them to me before dying."
    lloyd_thinking thinking "The man in black is killing others with psychic abilities.[wait_1] I need to find them and warn them about him."
    lloyd_thinking thinking "I’m already going to Barbara for information, but is it worth visiting my other contacts?"
    call screen map_navigation(find_locations([]))