import discord
from discord.ext import commands
#py
from bs4 import BeautifulSoup
import aiohttp
import random
import os
import sys

class snorfax:

  def __init__(self, bot):
   self.bot = bot
  
  @commands.command()
  async def snorfax(self):
  
  #URL, get object from whatever magic call happens
    snorfaxtxt = None
    htmlObj = None
    paragraph = None
    url = "https://en.wikipedia.org/wiki/Bulbasaur" #build the web adress
    async with aiohttp.get(url) as response:
  #The HTML Object to act on and get text from.
      htmlObj = BeautifulSoup(await response.text(), "html.parser")
      
    if ( htmlObj is not None ):
      try:
      #Snorfax
        paragraph = htmlObj.find_all('p')
        if paragraph is not None:#ew, bad temp code
          rdm = random.randint(0, len(paragraph))
          snorfaxtxt = paragraph[rdm].get_text()
        if snorfax is not None: #if fax is not bad
          await self.bot.say("Here is your Snorfax:\n\"" + snorfaxtxt + "\"")
      except ValueError:
        await self.bot.say("There's an error in Kyle's code.")

def setup(bot):
  bot.add_cog(snorfax(bot))