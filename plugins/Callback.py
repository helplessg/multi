from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""**HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK**.

<b><u>🛠 Sᴏᴍᴇ Fᴜɴ Cᴏᴍᴍᴀɴᴅs 🛠</u></b>

◉ send channel last message with
  forwerd tag to get the channel id 🎗

◉ /id - your tg id & info 🎗

◉ /telegraph - reply to below 5Mb media
  to get telegraph Link 🔗 

◉ /stickerid - Reply To Any Sticker to get sticker id 🎗

To Make Logo - /logo Your Name
To Make Square Logo -  /logosq Your Name

♻️ Example:
/logo Glitch
/logosq Glitch 

🌹 THANKS FOR USING ME 🌹
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🤖 Sᴏᴍᴇ Vᴇʀʏ Usᴇғᴜʟ Bᴏᴛs 🤖", callback_data="botz")
                  ],[
                  InlineKeyboardButton("🚶Bᴀᴄᴋ", callback_data="start"),
                  InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ P-Bʏ ❗ **@robo_glitch** ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : **{bot.mention}**
║┣⪼😈ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/the_glitchs>[༒Tʜᴇ Gʟɪᴛᴄʜ༒]</a>
║┣⪼📢Cʜᴀɴɴᴇʟ: <a href=https://t.me/hddubhub4u>[ʜᴅ-ᴅᴜʙ-ʜᴜʙ-ᴜ]</a>
║┣⪼🔮Oᴛʜᴇʀ Bᴏᴛs: <a href=https://t.me/futurebackups>[Fᴜᴛᴜʀᴇ Bᴀᴄᴋᴜᴘs]</a>
║┣⪼📮Sᴜᴘᴘᴏʀᴛ: <a href=https://t.me/hddubhub4uhelp>[Sᴜᴘᴘᴏʀᴛ]</a>
║┣⪼🎥Mᴏᴠɪᴇ's: <a href=https://t.me/dubbedweb>[Mᴏᴠɪᴇs-Gʀᴏᴜᴘ]</a>
║┣⪼📽Nᴇᴡ Rᴇʟᴇᴀsᴇ: <a href=https://t.me/hddubhub4u>[Nᴇᴡ-Rᴇʟᴇᴀsᴇ]</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ :<b>Pʏʀᴏɢʀᴀᴍ ᴠ {__version__}</b>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🚶Bᴀᴄᴋ", callback_data="start"),
                  InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("📮 Sᴜᴘᴘᴏʀᴛ 📮", url="https://t.me/hddubhub4uhelp"),
                  InlineKeyboardButton("🔮 Oᴛʜᴇʀ Bᴏᴛs 🔮", url="https://t.me/futurebackups")
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
                  InlineKeyboardButton("🔍 Oʟ Mᴏᴠɪᴇ's Bᴏᴛ 🎥 ", url="https://t.me/olmoviesbot"),
                  InlineKeyboardButton("📝 Mᴜʟᴛɪ Rᴇɴᴀᴍᴇʀ Bᴏᴛ ⚡", url="https://t.me/Mᴜʟᴛɪ Rᴇɴᴀᴍᴇʀ Bᴏᴛ")
                  ],[
                  InlineKeyboardButton("📊 Bᴏᴛs Lɪᴠᴇ Sᴛᴀᴛᴜs 📈", url="https://t.me/futurebackups/754"),
                  ],[
                  InlineKeyboardButton("🚶Bᴀᴄᴋ", callback_data="start"),
                  InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>🛠 Sᴏᴍᴇ Fᴜɴ Cᴏᴍᴍᴀɴᴅs 😉</u></b>

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
                 InlineKeyboardButton("🚶Bᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data="close")
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
























