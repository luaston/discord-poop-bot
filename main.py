import discord
import os
import sys
import random
import time
import logging
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
# DO NOT REMOVE ANY OF THESE, IT WILL BREAK YOUR BOT IF YOU DO.


load_dotenv()
#This is used to load the .env file.

token = os.getenv('TOKEN')
#Looks in the .env for TOKEN=[token]
#You may change it to anything you wish, as long as you entr it in your .env file as the same.

handler = logging.FileHandler(filename='poop_bot.log', encoding="UTF-8", mode='w')
#Log file handler, do not remove.

intents = discord.Intents.default()
#Do not remove either.

bot = commands.Bot(command_prefix='!', intents=intents)
#Don't remove.

pool_folder = "image_pool"



@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")
    print(f"------------------------\nLuaston Open Source Bot: Poop Bot\nBot logged in successfully.\nLogged in as {bot.user.name}.\nThank you for using my bot! - Luaston\n------------------------")
    if not status.is_running():
        status.start()

    with open("poop_activites.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                status_tags.append(line.strip())

    with open("poop_taglines.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                poop_taglines.append(line.strip())

    with open("poop_managers.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                managers.append(line.strip())

#Bot starting process (logging in terminal what bot is signed in, and if commands are synced.)

#The eat poop command.
@bot.tree.command(name="eatpoop", description="Feeling hungry? Recycling is good for the planet.")
async def poop_slashcommand(interaction: discord.Interaction):
    embed_poop = discord.Embed(title=f"{interaction.user.display_name} is eating poop!",description=random.choice(poop_taglines), color=0x8B4513)
    # All embed stuff
    embed_poop.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
    embed_poop.set_footer(text=bot.user.display_name, icon_url=bot.user.display_avatar.url)
    embed_poop.set_image(url=random.choice(poop_media))
    await interaction.response.send_message(embed=embed_poop)
    # ^^^ Sends embed into channel the command is ran in.

#Add image command, adds an image to the pool. and adds it to the image_pool txt file. This file is important as if the bot restarts, all images/gif links will be safe.
@bot.tree.command(name="addimage", description="Add a GIF or image to the pool of images/GIFs! (Needs permission)")
@app_commands.describe(file="An image/GIF file")
async def poop_add(interaction: discord.Interaction, file: discord.Attachment):
    if interaction.user in managers or interaction.permissions.administrator:
        if file.content_type and file.content_type.startswith("image/"):
            poop_media.append(file)
            file_path = os.path.join(pool_folder, file.filename)
            await file.save(file_path)
            await interaction.response.send_message(f"Your [image/GIF]({file}) has been added to the pool!", ephemeral=True)
        else:
            await interaction.response.send_message("You attached a file that isn't an image. Please try again with an image/GIF.", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to run this command. If you think this is a mistake, ask someone with Administrator permissions to add a role you have as a Poop Manager.")

#add user as a poop manager (basically means they can add images, and add stuff to the status or taglines in he embed for eating poop)
@bot.tree.command(name="addpoopmanager", description="Add a user as a Poop Manager(able to add images, taglines, etc.)")
async def poop_addManager(interaction: discord.Interaction, otheruser: discord.User):
        if interaction.permissions.administrator:
            if otheruser in managers:
                 await interaction.response.send_message("This user is already a Poop Manager.", ephemeral=True)
                 return
            managers.append(otheruser)
            with open("poop_managers.txt", "a", encoding="utf-8") as file:
                file.write(f"{otheruser}\n")
            await interaction.response.send_message(f"{otheruser} has been added as a Poop Manager!", ephemeral=True)
        else:
            await interaction.response.send_message("You don't have permission to use this command.")

@bot.tree.command(name="removepoopmanager", description="Remove a user as Poop Manager")
async def poop_removeManager(interaction: discord.Interaction, otheruser: discord.User):
        if interaction.permissions.administrator:
            if otheruser not in managers:
                 await interaction.response.send_message("This user isn't a Poop Manager.", ephemeral=True)
                 return
            managers.remove(otheruser)
            with open("poop_managers.txt", "r", encoding="utf-8") as f:
                users = f.read().splitlines()

            if otheruser in users:
                users.remove(otheruser)
                with open("poop_managers.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(users) + "\n")
            await interaction.response.send_message(f"{otheruser} has been removed from Poop Manager!", ephemeral=True)
        else:
            await interaction.response.send_message("You don't have permission to use this command.")

@bot.tree.command(name="addtagline", description="Add a tagline for embeds!")
async def poop_taglineAdd(interaction: discord.Interaction, text: str):
    if interaction.permissions.administrator or interaction.user in managers:
            with open("poop_taglines.txt", "a", encoding="utf-8") as file:
                file.write(f"{text}\n")
            poop_taglines.append(text)
            await interaction.response.send_message(f"Added '{text}' to taglines!", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to use this command.")

@bot.tree.command(name="addactivity", description="Add an activity to the bots 'Playing' activity!")
async def poop_activityAdd(interaction: discord.Interaction, text: str):
    if interaction.permissions.administrator or interaction.user in managers:
            with open("poop_activities.txt", "a", encoding="utf-8") as file:
                file.write(f"{text}\n")
            status_tags.append(text)
            await interaction.response.send_message(f"Added '{text}' to activities!", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to use this command.")

poop_media = [
    "https://static2.klipy.com/ii/2f34308bfc69e8c858753b83566e3ab4/b0/58/FPs4WD0oqkqCYuJHPtb.gif",
    "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/f3/e9/NZQKtkuCKFBtq.gif",
    "https://static2.klipy.com/ii/935d7ab9d8c6202580a668421940ec81/1c/8f/gdd5gsd2.gif"
]

poop_taglines = [
    "It's better to poop in the sink, than to sink in the poop.",
    "Leave me alone! I have a lot of shit on my plate.",
    "You haven't lived if you haven't eaten your own poop at least once.",
    "Hey, it was either gonna be smeared on the wall or eaten. And it isn't ethical to waste food.",
    "Yummy yummy in my tummy!"

]

status_tags = [
    "Feeding our server members a hearty meal!",
    "Toilet hunting, finding some food.",
    "Donate some of your feces to us today!",
    "I'm so hungry... I could eat some poop!",
    "Do you smell that? Yeah, I smell dinner.",
    "This food is crap. Not that it's bad though. I like crap.",
    "It's called recycling, sweaty ♻️💅"
]

managers = [

]

@tasks.loop(seconds=60)
async def status():
    await bot.change_presence(activity=discord.Game(name=random.choice(status_tags)))

bot.run(token, log_handler=handler, log_level=logging.DEBUG)