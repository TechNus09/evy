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
              
async def makelog() :
    event_log = {}
    #start = time.time()
    name_list = []
    
    c_xp = ['mining_xp','woodcutting_xp']
    c_skill =['-mining', '-woodcutting']
    #sorted_lb = {}
    
    #members_sorted = []
    #unsortedl = {}
    
    
    for skill_x in range(2):
        async with aiohttp.ClientSession() as session :
            to_do = get_tasks(session, c_skill[skill_x])
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20):
                    member_temp = { 'mining_xp' : 0 , 'woodcutting_xp': 0}
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split(" ")[0]                    
                    if tag.upper() == "OWO":
                        if player in name_list:
                            event_log[player_name][c_xp[skill_x]]=xp
                            event_log[player_name]["total"]=+xp
                        else:
                            name_list.append(player_name)
                            event_log[player_name]=member_temp
                            event_log[player_name][c_xp[skill_x]]=xp
                            event_log[player_name]["total"]=+xp
    return event_log
   
 
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











@bot.command(name='cooking',aliases=['cook','food'])
async def cooking(ctx):
    await ctx.send("logging members xp ... ")
    loging = makelog()
    a = asyncio.run(loging)
    if create = crt(a):
        await ctx.send("logging finished \nsending log file ...")
    else:
        await ctx.send("logging failed")
     
bot.run(os.getenv("TOKEN"))
