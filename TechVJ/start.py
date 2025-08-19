from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import OWNER_ID, F_SUB
from TechVJ.db import db

@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot: Client, msg: Message):
    # Save user in DB
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id, msg.from_user.first_name)

    # Force Sub Check
    if F_SUB:
        try:
            await bot.get_chat_member(int(F_SUB), msg.from_user.id)  # ✅ user is in channel
        except:
            try:
                invite_link = await bot.create_chat_invite_link(int(F_SUB))
            except:
                await msg.reply("⚠️ Make Sure I Am Admin In Your Channel ⚠️")
                return 

            key = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🍿 Join Update Channel 🍿", url=invite_link.invite_link),
                    InlineKeyboardButton("🍀 Check Again 🍀", callback_data="chk")
                ]]
            )
            await msg.reply_text(
                "⚠️ Access Denied! ⚠️\n\nPlease Join My Update Channel To Use Me.\nIf You Already Joined, Click 'Check Again'.",
                reply_markup=key
            )
            return  # ❌ stop here if not joined

    # ✅ If joined, send main menu
    me = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""<b>𝐇𝐞𝐲 {msg.from_user.mention} 🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ.\nғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ ✅\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ 🚫\n\nMade With ❤️ By : [VJ Botz](https://t.me/VJ_Botz)</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⚡ Generate String Session ⚡", callback_data="generate")
            ],[
                InlineKeyboardButton("❣️ Support Group ❣️", url="https://t.me/VJ_Bot_Disscussion"),
                InlineKeyboardButton("🥀 Update Channel 🥀", url="https://t.me/VJ_Botz")
            ]]
        )
    )


@Client.on_callback_query(filters.regex("chk"))
async def chk(bot: Client, cb: CallbackQuery):
    try:
        await bot.get_chat_member(int(F_SUB), cb.from_user.id)  # ✅ check again
    except:
        await cb.answer("🙅‍♂️ You are not joined my channel. First join, then check again! 🙅‍♂️", show_alert=True)
        return 

    # ✅ If user joined, show main menu
    me = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=cb.from_user.id,
        text=f"""<b>𝐇𝐞𝐲 {cb.from_user.mention} 🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ.\nғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ ✅\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ 🚫\n\nMade With ❤️ By : [VJ Botz](https://t.me/VJ_Botz)</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⚡ Generate String Session ⚡", callback_data="generate")
            ],[
                InlineKeyboardButton("❣️ Support Group ❣️", url="https://t.me/VJ_Bot_Disscussion"),
                InlineKeyboardButton("🥀 Update Channel 🥀", url="https://t.me/VJ_Botz")
            ]]
        )
    )