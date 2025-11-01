image studio_logo = Movie(play="videos/opening_logo.ogv")

label splashscreen:
    scene black_bg

    show studio_logo with quick_dissolve
    pause 2
    hide studio_logo with quick_dissolve

    show text "{color=#cc0000}This game was developed on land traditionally owned by the Wurundjeri people.\n\nToo Many Teeth Studios acknowledges the traditional owners of land and pays their respects to elders past, present, and emerging.{/color}" at opening_text with slow_dissolve
    pause 6
    hide text with slow_dissolve


label start:
    jump variables