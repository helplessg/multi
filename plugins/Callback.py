from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.

<b><u>COMMANDS</u></b>

◉ send channel last message with
  forwerd tag to get the channel id 💯

◉ /id - your tg id & info

◉ /telegraph - reply to below 5Mb media
  to get telegraph link💯

◉ /stickerid - Reply To Any Sticker to get sticker id

To Make Logo - /logo Your Name
To Make Square Logo -  /logosq Your Name

♻️ Example:
/logo Glitch
/logosq Glitch mkv

🤩THANKS FOR USING ME😍
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🤖 𝐌𝐘 𝐁𝐎𝐓𝐒", callback_data="botz")
                  ],[
                  InlineKeyboardButton("💚 Start", callback_data="start"),
                  InlineKeyboardButton("🔒 Close", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ Pᴏᴡᴇʀᴇᴅ Bʏ ❗ @robo_glitch ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {bot.mention}
║┣⪼👦ᴅᴇᴠ 1 : <a href=https://t.me/the_glitchs</a>
║┣⪼📢Cʜᴀɴɴᴇʟ: <a href=https://t.me/hddubhub4u>HD DUB HUB 4 U</a>
║┣⪼🔮Oᴛʜᴇʀ Bᴏᴛs: <a href=https://github.com/Jeolpaul/futurebackups>Future Backups</a>
║┣⪼📮Support: <a href=https://t.me/hddubhub4uhelp>Feadbacks</a>
║┣⪼🎥Movies: <a href=https://t.me/dubbedweb>Group</a>
║┣⪼📽New Release: <a href=https://github.com/hddubhub4u>Movies</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : Pyrogram v{__version__}  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("💚 Start", callback_data="start"),
                  InlineKeyboardButton("🔒 Close", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("📮 Support 📮", url="https://t.me/BETA_BOTSUPPORT"),
                  InlineKeyboardButton("🔮 Oᴛʜᴇʀ Bᴏᴛs 🔮", url="https://t.me/BETA_UPDATES")
                  ],[            
                  InlineKeyboardButton("ℹ️ Hᴇʟᴘ ℹ️", callback_data="help"),
                  InlineKeyboardButton("🤣 Fᴜɴ 🤣", callback_data="fun")
                  ],[
                  InlineKeyboardButton("😈Dᴇᴠᴇʟᴏᴘᴇʀ 😈", callback_data="devs"),
                  InlineKeyboardButton("🌹 Aʙᴏᴜᴛ 🌹", callback_data="about")
                  ]]
                  )
             )
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @the_glitcs & @robo_glitch ",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🔍 Movies Bot 🎥 ", url="https://t.me/JP_Jeol_org"),
                  InlineKeyboardButton("⚡ Rename Bot ⚡", url="https://t.me/mr_MKN")
                  ],[
                  InlineKeyboardButton("📍 Bots Staus 📍", url="https://github.com/Jeolpaul/TG-MULTI-BOT"),
                  ],[
                  InlineKeyboardButton("↩️ Back", callback_data="start"),
                  InlineKeyboardButton("🔒 Close", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUS TEST THIS COMMANDS 😉</u></b>

◉ /runs         
◉ /ikka      
◉ /dice     
◉ /arrow    
◉ /goal    
◉ /luck    
◉ /throw     
◉ /bowling  
◉ /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("↩️ Back", callback_data="start"),
                 InlineKeyboardButton("🔒 Close", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="🤖 This is My botz 😁",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("😉 Get Download link Bot", url="https://t.me/GeorgeMalarobot"),
                     InlineKeyboardButton("🛠Channel Bot", url="https://t.me/SK_MUSIC_ROBOT")
                     ],[
                     InlineKeyboardButton("🎖️ Group Manger Bot 🎖️", url="https://t.me/MKN_GROUPMANAGEROBOT")
                     ],[                   
                     InlineKeyboardButton("↩️ Back ", callback_data="start"),
                     InlineKeyboardButton("🔒 Close", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























