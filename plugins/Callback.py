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

<b><u>ð  Sá´á´á´ Fá´É´ Cá´á´á´á´É´á´s ð </u></b>

â send channel last message with
  forwerd tag to get the channel id ð

â /id - your tg id & info ð

â /telegraph - reply to below 5Mb media
  to get telegraph Link ð 

â /stickerid - Reply To Any Sticker to get sticker id ð

To Make Logo - /logo Your Name
To Make Square Logo -  /logosq Your Name

â»ï¸ Example:
/logo Glitch
/logosq Glitch 

ð¹ THANKS FOR USING ME ð¹
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("ð¤ Sá´á´á´ Vá´ÊÊ Usá´Òá´Ê Bá´á´s ð¤", callback_data="botz")
                  ],[
                  InlineKeyboardButton("ð¶Bá´á´á´", callback_data="start"),
                  InlineKeyboardButton("ð CÊá´sá´", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
ââââââ° P-BÊ â **@robo_glitch** â±ââ
ââ­ââââââââââââââââ£
ââ£âª¼ð¤á´Ê É´á´á´á´ : **{bot.mention}**
ââ£âª¼ðá´á´á´ á´Êá´á´á´Ê : <a href=https://t.me/the_glitchs>[à¼TÊá´ GÊÉªá´á´Êà¼]</a>
ââ£âª¼ð¢CÊá´É´É´á´Ê: <a href=https://t.me/hddubhub4u>[Êá´-á´á´Ê-Êá´Ê-á´]</a>
ââ£âª¼ð®Oá´Êá´Ê Bá´á´s: <a href=https://t.me/futurebackups>[Fá´á´á´Êá´ Bá´á´á´á´á´s]</a>
ââ£âª¼ð®Sá´á´á´á´Êá´: <a href=https://t.me/hddubhub4uhelp>[Sá´á´á´á´Êá´]</a>
ââ£âª¼ð¥Má´á´ Éªá´'s: <a href=https://t.me/dubbedweb>[Má´á´ Éªá´s-GÊá´á´á´]</a>
ââ£âª¼ð½Ná´á´¡ Rá´Êá´á´sá´: <a href=https://t.me/hddubhub4u>[Ná´á´¡-Rá´Êá´á´sá´]</a> 
ââ£âª¼ðï¸á´ á´ÊsÉªá´É´ :<b>PÊÊá´É¢Êá´á´ á´  {__version__}</b>
ââ°ââââââââââââââââ£
ââââââââââââââââââââ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("ð¶Bá´á´á´", callback_data="start"),
                  InlineKeyboardButton("ð CÊá´sá´", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}ðð»\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\nâ send channel last message with forwerd tag to get the channel id ð¯",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("ð® Sá´á´á´á´Êá´ ð®", url="https://t.me/hddubhub4uhelp"),
                  InlineKeyboardButton("ð® Oá´Êá´Ê Bá´á´s ð®", url="https://t.me/futurebackups")
                  ],[            
                  InlineKeyboardButton("â¹ï¸ Há´Êá´ â¹ï¸", callback_data="help"),
                  InlineKeyboardButton("ð¤£ Fá´É´ ð¤£", callback_data="fun")
                  ],[
                  InlineKeyboardButton("ð Dá´á´ á´Êá´á´á´Ê ð", callback_data="devs"),
                  InlineKeyboardButton("ð¹ AÊá´á´á´ ð¹", callback_data="about")
                  ]]
                  )
             )
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @the_glitcs & @robo_glitch ",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("ð OÊ Má´á´ Éªá´'s Bá´á´ ð¥ ", url="https://t.me/olmoviesbot"),
                  InlineKeyboardButton("ð Má´Êá´Éª Rá´É´á´á´á´Ê Bá´á´ â¡", url="https://t.me/MultiRenamerBot")
                  ],[
                  InlineKeyboardButton("ð Bá´á´s LÉªá´ á´ Sá´á´á´á´s ð", url="https://t.me/futurebackups/754"),
                  ],[
                  InlineKeyboardButton("ð¶Bá´á´á´", callback_data="start"),
                  InlineKeyboardButton("ð CÊá´sá´", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>ð  Sá´á´á´ Fá´É´ Cá´á´á´á´É´á´s ð</u></b>

â /runs         
â /ikka      
â /dice     
â /arrow    
â /goal    
â /luck    
â /throw     
â /bowling  
â /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("ð¶Bá´á´á´", callback_data="start"),
                 InlineKeyboardButton("ð CÊá´sá´", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="ð¤ TÊá´sá´ á´Êá´ Sá´á´á´ OÒ Há´Êá´Òá´Ê Bá´á´ Yá´á´ Cá´É´ AÊsá´ Usá´ ð",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("ð á´á´á´á´ á´á´á´á´Éªá´É´ Êá´á´ ð", url="https://t.me/GlitchAutoCaptionBot"),
                     InlineKeyboardButton("ð½OTT Má´á´ Éªá´/Sá´ÊÉªá´s Bá´á´ð½", url="https://t.me/Ott_MoviesBot")
                     ],[
                     InlineKeyboardButton("ðá´á´á´¡É´ ÊÉªÉ´á´ É¢á´É´á´Êá´á´á´Ê Êá´á´ð", url="https://t.me/DownLinkGeneratorBot")
                     ],[                   
                     InlineKeyboardButton("ð¶Bá´á´á´ ", callback_data="start"),
                     InlineKeyboardButton("ð CÊá´sá´", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























