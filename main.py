import discord
from discord.ext import commands


from model import get_class


intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents=intents)



@bot.event
async def on_ready():
    print("Il bot è pronto all'uso")
  
   
@bot.command()
async def commands(ctx):
    command = "hello, heh, check, commands. All this commands have the prefix '/' "
    await ctx.send(f"The commands are: {command}" )

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, I am {bot.user}.")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))

    else:
        await ctx.send("Ti sei dimenticato di caricare l'immagine")
        

  

bot.run("MTIyMzU4NjQwOTA0MzE5ODA5NA.GnVn3D.TTZo8wUv8KvH-P2BjJ6ic5bhwJvYrjyJYgNx7w")