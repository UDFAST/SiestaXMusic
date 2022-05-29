from config import ASSISTANT_PREFIX
from Yukki import BOT_NAME, MUSIC_BOT_NAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""╔━━━━━━━━━𓆩•♡•𓆪━━━━━━━━━╗ 
✨ **مرحبا عزيزي MENTION !**\n
💭 **انا بوت استطيع تشغيل الموسيقي والفديو في محادثتك الصوتية**\n
💡 تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  » 📚 اوامر التشغيل !
╚━━━━━━━━━𓆩•♡•𓆪━━━━━━━━━╝
"""

COMMANDS_TEXT = f"""
» **قم بالضغط على الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⚡ قناة البوت @FA9SH
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 اوامر التشغيل", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📣 قناة البوت", url="https://t.me/FA9SH"
            ),
            InlineKeyboardButton(
                text="💬 جروب الدعم", url="https://t.me/S150D"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ اضف البوت الى مجموعتك ➕", url=f"https://t.me/{MUSIC_BOT_NAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 اوامر التشغيل", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="📣 قناة البوت", url="https://t.me/FA9SH"
            ),
            InlineKeyboardButton(
                text="💬 جروب الدعم", url="https://t.me/S150D"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🧙🏻 اوامر المطور", callback_data="sudo_cmd"
            ),
            InlineKeyboardButton(
                text="👷🏻 اوامر الادمنيه", callback_data="play_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="📚 اوامر اساسيه", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ رجوع", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🧙🏻 اوامر المطور", callback_data="sudo_cmd"
            ),
            InlineKeyboardButton(
                text="👷🏻 اوامر الادمنيه", callback_data="play_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="", callback_data="ggggjh_cmd"
            ),            
            InlineKeyboardButton(
                text="📚 اوامر اساسيه", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ رجوع", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ رجوع", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="", url="https://telegra.ph/SiestaXMusic-Sudo-Commands-02-08"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ رجوع", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
Here is the help for **Admin Commands:**
--**ADMIN ONLY COMMANDS WITH MANAGE VC RIGHT:**--
/pause 
- Pause the playing music on voice chat.
/resume
- Resume the paused music on voice chat.
/skip
- Skip the current playing music on voice chat
/end or /stop
- Stop the playout.
--**Authorised Users List:**--
**{BOT_NAME} has a additional feature for non-admin users who want to use admin commands**
- Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.
/auth [Username or Reply to a Message] 
- Add a user to AUTH LIST of the group.
/unauth [Username or Reply to a Message] 
- Remove a user from AUTH LIST of the group.
/authusers 
- Check AUTH LIST of the group.
"""

BOT_TEXT = """
Here is the help for **Bot Commands:**
/start 
- Start the Music Bot.
/help 
- Get Commands Helper Menu with detailed explanations of commands.
/settings 
- Get Settings dashboard of a group. You can manage Auth Users Mode. Commands Mode from here.
/ping
- Ping the Bot and check Ram, Cpu etc stats of Music Bot."""

PLAY_TEXT = """
🏮 هنا أوامر الادمنيه:
» /pause 「ايقاف التشغيل موقتآ」
» /resume 「استئناف التشغيل」
» /end「لإيقاف التشغيل」
» /vmute 「لكتم البوت」
» /vunmute 「لرفع الكتم عن البوت」
» /volume 「ضبط مستوئ الصوت」
» /reload「لتحديث البوت و قائمة المشرفين」
» /userbotjoin「لاستدعاء الحساب المساعد」
» /userbotleave「لطرد الحساب المساعد」
⚡ قناة البوت @FA9SH 
"""

SUDO_TEXT = f"""
🏮 هنا اوامر المطور:
» /gban「لحظر الشخص في الجروبات 」
» /ungban「لفك حظر الشخص في الجروبات」
» /broadcast 「للاذاعه في كل جروبات البوت」
» /update「لتحديث بوتك لاخر نسخه」
» /restart「اعاده تشغيل البوت」
» /stats「لعرض احصائيات البوت / المساعد」
» /blacklistchat「+ ايدي الجروب لحظر الجروب」
» /whitelistchat「+ ايدي الجروب لفك حظر الجروب」
⚡ قناة البوت @FA9SH 
"""

EXTRA_TEXT = """
🏮 الاوامر الاساسيه:
» /play +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
» /vplay +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
» /vstream 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» /playlist 「تظهر لك قائمة التشغيل」
» /end「لإنهاء الموسيقى / الفيديو في الكول」
» /song + 「الاسم تنزيل صوت من youtube」
»/vsong + 「الاسم  تنزيل فيديو من youtube」
» /skip「للتخطي إلى التالي」
» /ping 「إظهار حالة البوت بينغ」
» /uptime 「لعرض مده التشغيل للبوت」
» /alive「اظهار معلومات البوت(في المجموعه)」
⚡ قناة البوت @FA9SH 
"""

BASIC_TEXT = """
الدليل الأساسي لاستخدام هذا البوت:
 1 - قم [بإضافتي](https://t.me/USDDBOT?startgroup=true) لمجموعتك
 2 - قم بترقيتي مشرف في الجروب بكل الصلاحيات ما عدا الوضع الخفي
 3 - قم بإضافة @SHADOW_MUSIC0 او اكتب /play لدعوة الحساب المساعد 
 4 - قم بتشغيل المكالمه اولا قبل بدء تشغيل الفيديو/الموسيقى
اذا واجهتك اي مشكله في البوت او الحساب المساعد فيمكنك اخبار المطور [@𝑺 𝑯 𝑨 𝑫 𝑶 𝑾.❤_](https://t.me/S550D)
 💡 إذا كانت لديك اسئله  حول هذا البوت ، فيمكنك إخبارنا منن خلال جروب الدعم الخاصة بي هنا @S150D

⚡ قناة البوت @FA9SH
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ رجوع", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 طريقة التفعيل", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📚 الاوامر", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ رجوع", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)
