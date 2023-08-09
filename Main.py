from os import system as sys
import nextcord
from nextcord.ext import commands, menus
import Config as BotC

#Importing Configs for the bot
TOKEN = BotC.MainBot["Token"]
servers = BotC.ServerBot["Servers"]
ServRules = BotC.ServerBot["Rules"]
AdminRoles = BotC.ServerBot["Admins"]
HomeInvite = BotC.PublicBot["Support_Server_Link"]
RankRoles = BotC.Ranks
bot = commands.Bot(command_prefix="###", intents=nextcord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    #sys("cls")
    print("Bouncer Bot - Online")

@bot.event
async def on_member_join(member):
    role = [x for x in await member.guild.fetch_roles() if x.id == RankRoles["Starter"]]
    role = role[0] if role else print("Role not Found.")
    await member.add_roles(role, reason="New member joined - Autorole.")

def rolecheck(interaction, roleid):
    roleowned = False
    if roleid in [x.id for x in interaction.user.roles]:
        roleowned = True
    return roleowned

def rolecheckother(user, roleid):
    roleowned = False
    if roleid in [x.id for x in user.roles]:
        roleowned = True
    return roleowned

#Important Commands
@bot.slash_command(guild_ids=servers, description="Remind yourself of the server rules!")
async def remindme(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title=f"///--- Server Rules ---///", description=f"")
    for i in range(len(ServRules)):
        embed.add_field(name=f"{i+1}. {ServRules[i]}", value="", inline=False)
    await interaction.send(embed=embed, ephemeral=True)

@bot.slash_command(guild_ids=servers, description="Get an invite to the support server!")
async def supportlink(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="///--- Support Server ---///", description="Use the link below to join this bot's support server!")
    embed.add_field(name="Invite Link:", value=f"{HomeInvite}")
    await interaction.send(embed=embed, ephemeral=True)

#Rank Command
class RankUserCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Rank - Online")
    @nextcord.slash_command(guild_ids=servers, description="Change User Ranks!")
    async def rank(self, interaction: nextcord.Interaction, user: nextcord.Member, rank: str=nextcord.SlashOption(name="rank",description="Rank to give to an user.", required=True, choices=["Level_0","Level_1","Level_2","Level_3","Level_4","Level_5","Council"])):
        if rolecheck(interaction, RankRoles["Council"]) == True or rolecheck(interaction, RankRoles["Level_5"]) == True or rolecheck(interaction, RankRoles["Level_4"]) == True:
            if rolecheckother(user, RankRoles["Council"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Council"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Level_5"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Level_5"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Level_4"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Level_4"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Level_3"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Level_3"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Level_2"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Level_2"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Level_1"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Level_1"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Level_0"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Level_0"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            if rolecheckother(user, RankRoles["Starter"]):
                role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles["Starter"]]
                role = role[0] if role else print("Role not Found.")
                await user.remove_roles(role, reason="Rank Change Through Command.")
            role = [x for x in await user.guild.fetch_roles() if x.id == RankRoles[rank]]
            role = role[0] if role else print("Role not Found.")
            await user.add_roles(role, reason="Rank Change Through Command.")
            embed = nextcord.Embed(title="///--- Rank Change ---///", description=f"User {user.mention} has been given the rank {rank}!")
        else:
            embed = nextcord.Embed(title="///--- Error ---///", description="You do not have the required permissions to use this command!")
        await interaction.send(embed=embed, ephemeral=True)

bot.add_cog(RankUserCMD(bot))

bot.run(TOKEN)
