import discord
from discord.ext import commands
#py
from bs4 import BeautifulSoup
import re
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
    url = "https://en.wikipedia.org/wiki/Snorlax" #build the web address
    async with aiohttp.get(url) as response:
  #The HTML Object to act on and get text from.
      htmlObj = BeautifulSoup(await response.text(), "html.parser")
      
    if ( htmlObj is not None ):
      try:
      #Snorfax
        paragraph = htmlObj.find_all('p')
        if paragraph is not None and len(paragraph) != 0:#ew, bad temp code
          # Get random paragraph
          rdmp = random.randint(0, len(paragraph)-1)
          paragraphtxt = paragraph[rdmp].get_text()
          
          #Split the paragraph by sentence
          ssplit = paragraphtxt.split(".")
          rdms = random.randint(0, len(ssplit)-1)
          snorfaxtxt = ssplit[rdms].strip()
          snorfaxtxt = re.sub(r'\[\d+\]+', '', snorfaxtxt)
          
        else:
          await self.bot.say("Paragraph probs too short.")
          
        if snorfaxtxt is not None and len(snorfaxtxt) != 0: #if fax is not bad
          await self.bot.say("Here is your Snorfax:\n\"" + snorfaxtxt + "\"")
          
        else:
          await self.bot.say("\\:snorfax: \\:snorfax:264215284758347776 \:snorfax:264215284758347776 :heart: \r")
          
      except ValueError:
        await self.bot.say("There's an error in Kyle's code.")

def setup(bot):
  bot.add_cog(snorfax(bot))