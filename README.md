THIS MIGHT GIVE A FALSE POSITIVE FROM YOUR ANTIVIRUS
Pyinstaller (the compiler I used) is known for giving false positives.

---HOW TO USE---

MAKE SURE THE .EXE IS INSIDE THE FOLDER, OR ELSE IT WILL CRASH!

This is a recreation of those Find Luigi videos that are trending on Twitter.
It's not playable, it's just for making your own versions of those videos.

The settings for the game can be controlled using the settings.json file.
Inside are a few options so you can adjust the game to your liking. 
Here is each one, and what it does:

------

"windowSize": A list with two integer values. This controls the window's width and height. Default: [250, 250]
"fps": The game's FPS as an integer. Everything runs faster (including the icons). Lowering it can improve performance. Default: 30
"images": A dictionary with a list of every image filename the game will use. Put the images in the images folder, otherwise it wont work.
"wanted": The key name of the image you want to be wanted, only one will be made.
"scale": Float of the icon's scale. Default: 1.0
"amount": The amount of icons the game generates. Default: 100
"speed": The max speed that the icons go, it is randomized. Default: 2

---CREDITS---

Here are the Twitter @s of the people who made this:

Everything: @TheOpieMonster
Beta Tester: @Xtornality
Idea: @FindLuigi

Original images were from the Super Mario 64 DS, a game by Nintendo.

------

Bugs/Suggestions: @TheOpieMonster on Twitter
Credit is optional, but would be appreciated. Mention me too if you want, I'd love to see what you guys make!
If you want you want to look inside and see how it works, the code is open source and available on my github
