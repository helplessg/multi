from pyrogram import Client, filters, idle
import pyrogram
from pyrogram.errors import FloodWait
from helper.ban import BanChek
from helper.motor_db import db
from helper.utils import not_subscribed
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from helper.database import insert, getid
from variables import STAT_STICK, PICS, ADMIN, DELAY, LOG_CHANNEL
from plugins.logo_maker import generate_logo
import asyncio
import random

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**📢 Yᴏᴜ ᴅɪᴅɴ'ᴛ Jᴏɪɴᴇᴅ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Jᴏɪɴ ɴᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ᴀɢᴀɪɴ ❤**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="📢 Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ 📢", url=client.invitelink)
           ],[
           InlineKeyboardButton("🔄 Tʀʏ ᴀɢᴀɪɴ 🔄", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
       kikked = await BanChek(bot, message)
       if kikked == 400:
           return
       insert(int(message.chat.id))
       await message.reply_chat_action("Typing")    
       m=await message.reply_sticker(STAT_STICK)
       await asyncio.sleep(DELAY)
       await m.delete()             
       await message.reply_photo(
           photo=random.choice(PICS),
           caption=f"ʜᴇʟʟᴏ <b>{message.from_user.mention}</b> 🌹\n**ɪ'ᴀᴍ ᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ʙᴏᴛ ʙᴏᴛ ᴡɪᴛʜ ᴍᴀɴʏ ᴜsᴇꜰᴜʟʟ ꜰᴇᴀᴛᴜʀᴇS** 🔱.\n**ᴇɢ:- ᴛᴇʟᴇɢᴀʀᴘʜ, ᴄʜᴀɴɴᴇʟ ɪᴅ, ᴜsᴇʀ ɪᴅ, ꜰᴜɴ, ɢʀᴏᴜᴘ ɪᴅ sᴛɪᴄᴋᴇʀ ɪᴅ ᴇᴛᴄ...\nʏᴏᴜ ᴄᴀɴ sᴇᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴜsɪɴɢ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs**...🛠 \n\n◉** Sɪᴍᴘʟʏ sᴇɴᴅ ᴄʜᴀɴɴᴇʟ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ꜰᴏʀᴡᴇʀᴅ ᴛᴀɢ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ** 🎗\n**ᴘᴏᴡᴇʀᴇᴅ ʙʏ** ❗ **@robo_glitch**",               
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("📮 Sᴜᴘᴘᴏʀᴛ 📮", url="https://t.me/hddubhub4uhelp"),
               InlineKeyboardButton("🔮 Oᴛʜᴇʀ Bᴏᴛs 🔮", url="https://t.me/futurebackups")
               ],[            
               InlineKeyboardButton("ℹ️ Hᴇʟᴘ ℹ️ ", callback_data="help"),
               InlineKeyboardButton("🤣 Fᴜɴ 🤣", callback_data="fun")
               ],[
               InlineKeyboardButton("😈 Dᴇᴠᴇʟᴏᴘᴇʀ 😈", callback_data="devs"),
               InlineKeyboardButton("🌹 Aʙᴏᴜᴛ 🌹", callback_data="about")
               ]]
               )
           )
       if not await db.is_user_exist(message.from_user.id):
          await db.add_user(message.from_user.id)
          await bot.send_message(LOG_CHANNEL, text=f"""<i>
<u>👁️‍🗨️ USER DETAILS </u>

○ 🎗 ID : <code>{message.from_user.id}</code>
○ 🎭 DC : <code>{message.from_user.dc_id}</code>
○ 🎀 First Name : <code>{message.from_user.first_name}<code>
○ 💡 UserName : @{message.from_user.username}

By = {bot. mention}</i>""")     


         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return
    await message.reply_text(
    text = f"""<i>
<u>👁️‍🗨️ YOUR DETAILS </u>

○ 🎗 ID : <code>{message.from_user.id}</code>
○ 🎭 DC : <code>{message.from_user.dc_id}</code>
○ 🎀 First Name : <code>{message.from_user.first_name}<code>
○ 💡 UserName : @{message.from_user.username}
○ 🔗 Link : <code>https://t.me/{message.from_user.username}</code>

🌹**Thank You For Using Me❣️\nPᴏᴡᴇʀᴇᴅ Bʏ ❗ @robo_glitch**</i>""")


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message): 
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    if message.reply_to_message.sticker:
       await message.reply(f"**🎗 Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n **🎭 Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("😳 Oops !! Not a sticker file 📁")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
      ms = await message.reply_text("Geting All ids from database ...........")
      ids = getid()
      tot = len(ids)
      await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
      for id in ids:
        try:
     	   await message.reply_to_message.copy(id)
        except:
     	   pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(bot, message):    
    msg = await bot.send_message(chat_id=message.chat.id, text="<b>Processing ...</b>")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")


@Client.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logosq(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return
    try:
      text = message.text.replace("logosq","").replace("/","").replace(" Pᴏᴡᴇʀᴇᴅ Bʏ ❗ @robo_glitch ","").strip().upper()
      
      if text == "":
        return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo Glitch\n/logosq Glitch")
  
      x = await message.reply_text("`⚡ Generating Logo For You...⌛`")  
      logo = await generate_logo(text,True)
  
      if "telegra.ph" not in logo:
        return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot")
        
      if "error" in logo:
        return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot\n\n`{logo}`")
        
      await x.edit("`🔄 Done Generated... Now Sending You ⌛`")
      
      logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
      
      await message.reply_photo(logo,caption="**🖼 Logo Generated By @robo_glitch**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
    except FloodWait:
      pass
    except Exception as e:
      try:
        await x.delete()
      except:
        pass
      return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot")

@Client.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logo(bot, message):
  kikked = await BanChek(bot, message)
  if kikked == 400:
      return
  try:
    text = message.text.replace("logo","").replace("/","").replace("@GlitchLogoMakerBot","").strip().upper()
    
    if text == "":
      return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo Glitch\n/logosq glitch")

    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot")
      
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")

    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption="**🖼 Logo Generated By @robo_glitch**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot")


@Client.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By robo_glitch**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @glichassistantbot\n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()






