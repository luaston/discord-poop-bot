# discord-poop-bot
A Discord.py bot that lets your server members eat poop. Literally.

## Overview
Poop Bot is a bot that is centred around one single command.
/eatpoop
<img src="https://files.catbox.moe/5trjdw.png">
The bot picks between a pool of random "me eating poop" GIFs, and uses a pool of custom taglines as seen in the screenshot.


# Command list:
* /eatpoop - Eat your poop!
* /addpoopmanager - A Poop Manager is a user that can add images, taglines, and add statuses (activites) to the bot. Only add people you trust!
* /removepoopmanager - Removes a user from Poop Manager
* /addtagline - Adds a tagline to the /eatpoop embed. (Poop Manager/Admin)
* /addactivity - Adds a status (activity) to the bot (Poop Manager/Admin)
* /addimage - Adds an image to the pool (Poop Manager/Admin)




## How do I add it to my server?
Poop Bot isn't publicly hosted, however you can clone Poop Bot, and add it to your own server. 

### Making the Poop Bot real.
* Go to the [Discord Developer Portal](https://discord.com/developers/home), and login.
* Create a new app, and call it whatever you please. It doesn't have to be just Poop Bot. Be creative!
* Grab the bot token in the Bot section. You may have to reset it to get it. Copy it to your clipboard and note it somewhere.
  
* Still in the bot section, scroll to Privileged Gateway Intents.
* Tick all the boxes in that section.
* Go to OAuth2, and find the URL generator.
* Tick Bot in the first box, and give it View Channels, Send Messages, Embed Links, and Attach Files.
* Copy the link at the bottom, then copy it into your browser. Add it to your server, and voila. Your bot exists.

### Making the Poop Bot alive.
Download the whole thing. main.py, all the text files, image_pool folder (it's meant to be empty), the whole thing.
* If you want to self-host it, you need to have [Python](https://www.python.org/downloads/) installed on your computer.
* First, create a .env file (I recommend getting [Visual Studio Code](https://code.visualstudio.com/) for this.
* There should be a .env.example file. Copy that into your .env file, and replace your_token_here with the token you noted down earlier.
* If you used Visual Studio Code, you should be able to open the main.py file inside of the app. If so, press the Run button at the top, and Run without debugging.

If you run the main.py file and your bot doesn't go online, make sure all your files are in the same folder as each other.

# Contact me!
If you need help, or if you want to report a bug, email me at [aaron@gamewell.xyz](mailto:aaron@gamewell.xyz)

# Happy pooping!
Warning: Updates to the bot are not promised, as this is a project for a portfolio.
  
