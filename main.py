import nextcord
from nextcord.ext import commands
from flask import Flask, render_template
import threading

# Initialize Flask app
app = Flask(__name__)

# Initialize bot
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@app.route('/')
def home():
    return render_template('index.html')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member: nextcord.Member):
    channel = nextcord.utils.get(member.guild.text_channels, name="👋➧𝙅𝙤𝙞𝙣𝙨")
    if channel:
        welcome_message = f"Welcome to the Team Singe Discord server, {member.mention}!"
        await channel.send(welcome_message)

        dm_message = "Type `/teamsingeverify` in the appropriate channel to get verified.   https://discord.com/channels/1255016293262692454/1255392049885220894"
        try:
            await member.send(dm_message)
        except nextcord.Forbidden:
            await channel.send(f"Could not send a private message to {member.mention}. They might have DMs disabled.")

# Slash command to share the YouTube link
@bot.slash_command(name="youtubeinfo", description="Get the YouTube channel link")
async def youtubeinfo(interaction: nextcord.Interaction):
    youtube_message = (
        "This is the owner of team Singe YouTube go subscribe to them! "
        "https://www.youtube.com/@ggaoi1?si=oow6fH-iopzo6WNR"
    )
    await interaction.response.send_message(youtube_message)

# Slash command to share the Instagram link
@bot.slash_command(name="insta", description="Get the Instagram link")
async def insta(interaction: nextcord.Interaction):
    insta_message = (
        "This is the official team Singe Instagram, go follow for posts! "
        "https://www.instagram.com/teamsingegg?igsh=Z3g1bm4zNGFqcTIz"
    )
    await interaction.response.send_message(insta_message)

# Slash command to verify and assign the role
@bot.slash_command(name="verifyteamsinge", description="Assign the verified role to the user")
async def verifyteamsinge(interaction: nextcord.Interaction):
    guild = interaction.guild
    role = nextcord.utils.get(guild.roles, name="verified")
    member = interaction.user

    if role:
        await member.add_roles(role)
        await interaction.response.send_message("You have been verified and assigned the 'verified' role!")
    else:
        await interaction.response.send_message("The 'verified' role does not exist.")

# Function to run Flask app
def run_flask():
    app.run(host="0.0.0.0", port=80)

# Run Flask app in a separate thread
if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    bot.run('MTIxMjIzOTcyNDk5NjIwMjU2Ng.Get7ml.RFQBapGAICIt93uE4cbjtrPP_BzQ28l9mSCRjQ')
