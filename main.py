import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from keep_alive import keep_alive

# ===== 获取 Telegram Bot Token =====
API_TOKEN = "8143081647:AAEv3xAGNk3pPHPZ71rJR8NzxqIuGs3aReI"

if API_TOKEN is None:
    print("Error: TELEGRAM_TOKEN environment variable not set.")
    exit()  # Exit the program if the token is not found
print("Loaded Token:", API_TOKEN)
bot = telebot.TeleBot(API_TOKEN)
print("Bot Token 已加载:", API_TOKEN)

# ===== 用户权限表 =====
USER_PERMISSIONS = {
    1133977928: ['S1jun_recordings', 'S1jul_recordings', 'S3jul_recordings','S1aug_recordings'],  # 你本人，所有权限
    1812568625: ['S3jul_recordings'],  # 学生 A，只能看 Sem 3 七月
    # 更多用户可在此添加，例如：
    # 1122334455: ['S1jun_recordings']
    1821940215:['S3jul_recordings'],  # shunwen
    1542377582:['S3jul_recordings'],  #meiqi
    1687569236:['S3jul_recordings'],  #rachel
    7123068204:['S3jul_recordings'],  #ruien
    1546769481:['S3jul_recordings'],  #yixuan
    1514480552:['S3jul_recordings'],  #yangling
    1316252749:['S3jul_recordings'],  #jingqi
    1237294924:['S1jun_recordings', 'S1jul_recordings','S1aug_recordings'],  #S1ruijie
    1579236248:['S1jun_recordings', 'S1jul_recordings','S1aug_recordings'],  #S1amber
    7503610132:['S1jun_recordings', 'S1jul_recordings','S1aug_recordings'],  #S1wenxuan
    1000428594:['S1jun_recordings', 'S1jul_recordings', 'S1aug_recordings'], #S1shimei
    5506885279:['S3jul_recordings'],  #S3zixuan
    1202445284:['S1jul_recordings'],
}

# ===== 权限检查函数 =====
def has_permission(user_id, folder):
    return user_id in USER_PERMISSIONS and folder in USER_PERMISSIONS[user_id]

# ===== /start 和帮助指令 =====
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 欢迎使用 STPM Ekonomi Bot！\n\n"
        "可用指令：\n"
        "📘 /sem1recording - Semester 1 录课\n"
        "📕 /sem3recording - Semester 3 录课\n"
    )

# ===== /sem1recording 指令 =====
@bot.message_handler(commands=['sem1recording'])
def sem1_recording(message):
    user_id = message.from_user.id
    markup = InlineKeyboardMarkup()

    if has_permission(user_id, 'S1jun_recordings'):
        markup.add(InlineKeyboardButton("🎧 SEM 1 六月录课", callback_data="S1jun_recordings"))
    if has_permission(user_id, 'S1jul_recordings'):
        markup.add(InlineKeyboardButton("🎧 SEM 1 七月录课", callback_data="S1jul_recordings"))
    if has_permission(user_id, 'S1aug_recordings'):
        markup.add(InlineKeyboardButton("🎧 SEM 1 八月录课", callback_data="S1aug_recordings"))

    if len(markup.keyboard) > 0:
        bot.send_message(message.chat.id, "请选择要查看的 <b>Semester 1 录课</b>：", reply_markup=markup, parse_mode="HTML")
    else:
        bot.reply_to(message, "❌ 你没有权限查看 Semester 1 的录课。")

# ===== /sem3recording 指令 =====
@bot.message_handler(commands=['sem3recording'])
def sem3_recording(message):
    user_id = message.from_user.id
    markup = InlineKeyboardMarkup()

    if has_permission(user_id, 'S3jul_recordings'):
        markup.add(InlineKeyboardButton("🎧 SEM 3 七月录课", callback_data="S3jul_recordings"))

    if len(markup.keyboard) > 0:
        bot.send_message(message.chat.id, "请选择要查看的 <b>Semester 3 录课</b>：", reply_markup=markup, parse_mode="HTML")
    else:
        bot.reply_to(message, "❌ 你没有权限查看 Semester 3 的录课。")

# ===== Inline Keyboard 回调处理 =====
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id

    # === SEM 1 六月 ===
    if call.data == "S1jun_recordings":
        if has_permission(user_id, "S1jun_recordings"):
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("📅 14/6", url="https://drive.google.com/file/d/1PcF-MxcFKFicI4obBOqWT9qB1MitGjoc/view?usp=drivesdk"),
                InlineKeyboardButton("📅 21/6", url="https://drive.google.com/file/d/10ba6gx-vrVbX3-aZbPKBKmbRc-W3fTiO/view?usp=drivesdk"),
                InlineKeyboardButton("📅 28/6", url="https://drive.google.com/file/d/18XKvyFJ2HlTPOJfKOszI-mVAcZqpV6wk/view?usp=drivesdk")
            )
            bot.send_message(call.message.chat.id, "✅ <b>SEM 1 六月录课</b>：", reply_markup=markup, parse_mode="HTML")
        else:
            bot.send_message(call.message.chat.id, "❌ 你没有权限查看 SEM 1 六月录课。")

# === SEM 1 七月 ===
    elif call.data == "S1jul_recordings":
        if has_permission(user_id, "S1jul_recordings"):
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("📅 5/7", url="https://drive.google.com/file/d/1Qb5ZV_TanQxWPx6jJToSW4SuXMcF4i1j/view?usp=drivesdk"),
                InlineKeyboardButton("📅 12/7", url="https://drive.google.com/file/d/15yXB8cOu-vCUcnBKS4j2C7ZHgbT3toRP/view?usp=drivesdk"),
                InlineKeyboardButton("📅 19/7", url="https://drive.google.com/file/d/1rhcOC2iBqm4cRDGGq5YT3qqWSZyYo-We/view?usp=drivesdk")
            )
            bot.send_message(call.message.chat.id, "✅ <b>SEM 1 七月录课</b>：", reply_markup=markup, parse_mode="HTML")
        else:
            bot.send_message(call.message.chat.id, "❌ 你没有权限查看 SEM 1 七月录课。")

    # === SEM 1 八月 ===
    elif call.data == "S1aug_recordings":
        if has_permission(user_id, "S1aug_recordings"):
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("📅 2/8", url="https://drive.google.com/file/d/1cXGGUMpUIoxYMDuFQkplDmJl8N4iJrnE/view?usp=drivesdk")
            )
            bot.send_message(call.message.chat.id, "✅ <b>SEM 1 八月录课</b>: ", reply_markup=markup, parse_mode="HTML")
        else:
            bot.send_message(call.message.chat.id, "❌ 你没有权限查看 SEM 1 八月录课。")
            
    # === SEM 3 七月 ===
    elif call.data == "S3jul_recordings":
        if has_permission(user_id, "S3jul_recordings"):
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("📅 20/7 补课", url="https://drive.google.com/file/d/1aoK14DIGW5JYJaAmwh1rQV3w4sFAkzZ6/view?usp=drivesdk"),
                InlineKeyboardButton("📅 23/7", url="https://drive.google.com/file/d/1_qwy0qBWSzfyKG2zRAHMRYe815Usq6CI/view?usp=drivesdk")
            )
            bot.send_message(call.message.chat.id, "✅ <b>SEM 3 七月录课</b>：", reply_markup=markup, parse_mode="HTML")
        else:
            bot.send_message(call.message.chat.id, "❌ 你没有权限查看 SEM 3 七月录课。")

# ===== 保持运行 (Replit + UptimeRobot) =====
keep_alive()
bot.polling()


