@client.command(pass_context=False)
async def roastme(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&amp;type=txt")
        await ctx.message.author.send(format(ctx.message.author.name) + " " + format(response.content))
