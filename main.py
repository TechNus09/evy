import os
import math
import asyncio
import discord as d
from discord.ext import commands
from discord.utils import get
import random
from datetime import date as dt
from urllib.request import Request, urlopen
import json
import nest_asyncio
import time
import aiohttp  
import pandas as pd
import numpy as np
import dataframe_image as dfi

   
nest_asyncio.apply()
     
 
event_log = {}

             
async def makelog() :
    event_log = {}
    start = time.time()
    name_list = []
    
    c_xp = ['mining_xp','woodcutting_xp']
    c_skill =['-mining', '-woodcutting']
    #sorted_lb = {}
    
    #members_sorted = []
    #unsortedl = {}
    
    
    for skill_x in range(2):
        x=0
        async with aiohttp.ClientSession() as session :
            to_do = get_tasks(session, c_skill[skill_x])
            responses = await asyncio.gather(*to_do)
            for response in responses:
                x=+1
                fdata = await response.json()
                for i in range(0,20):
                    rank = (x*i)+(i+1)
                    print(i)
                    member_temp = { 'ign' : 'name' , 'mining_xp' : 0 , 'woodcutting_xp': 0 , 'total': 0}
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]                    
                    if tag.upper() == "OWO":
                        if player_name in name_list:
                            event_log[player_name][c_xp[skill_x]]=xp
                            event_log[player_name]["total"] += xp
                        else:
                            name_list.append(player_name)
                            event_log[player_name]=member_temp
                            event_log[player_name]["ign"] = player_name
                            event_log[player_name][c_xp[skill_x]]=xp
                            event_log[player_name]["total"] += xp
    end = time.time()
    total_time = math.ceil(end - start)
    return event_log, total_time
   
 
def crt(data):
    log_file = open("data.json", "w")

    log_file = json.dump(data, log_file)
    return True     
 
def get_tasks(session,skill_name):
    tasks = []
    for k in range(0,3000):  
        url='https://www.curseofaros.com/highscores'
        tasks.append(asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k))))
    return tasks




bot = commands.Bot(command_prefix='&')

bot.remove_command("help")
bot.remove_command("date")
bot.remove_command('random')
@bot.event
async def on_ready():
    print('Logging in as {0.user}'.format(bot))
  






@bot.command()
async def log(ctx):
    await ctx.send("logging members xp ... ")
    if os.path.exists("data.json"):
        os.remove("data.json")
    
    a = asyncio.run(makelog())
    t = a[1]
    create = crt(a[0])
    if create :
        await ctx.send("logging finished \nsending log file ...")
        await ctx.channel.send('collected data!', file=d.File("data.json"))
        await ctx.send(f" time taken : {t}")

    else:
        await ctx.send("logging failed")
     

@bot.command()
async def logi(ctx):
    if os.path.exists("logs.png"):
        os.remove("logs.png")
    await ctx.send("dataframing ...")
    df = pd.DataFrame.from_dict(event_log, orient="index")
    df_styled = df.style.background_gradient()
    await ctx.send("imagification ... ")
    dfi.export(df_styled,"logs.png")
    await ctx.channel.send('imagification completed', file=d.File("logs.png"))




bot.run(os.getenv("TOKEN"))
