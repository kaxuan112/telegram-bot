import os
import telebot
from keep_alive import keep_alive
from dotenv import load_dotenv

# 载入 .env 文件
load_dotenv(8143081647:AAEv3xAGNk3pPHPZ71rJR8NzxqIuGs3aReI)

# 获取 Telegram Bot Token（从 .env 文件）
API_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# 白名单：只允许你（1133977928）使用
ALLOWED_USERS = [1133977928]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id not in ALLOWED_USERS:
        bot.reply_to(message, "❌ 无权限访问教学机器人")
        return
    bot.reply_to(message, "✅ 欢迎使用 STPM Ekonomi Bot！\n可用指令：/sem1 /soalan")

@bot.message_handler(commands=['sem1'])
def send_sem1(message):
    if message.from_user.id in ALLOWED_USERS:
        bot.reply_to(message, "📘 Sem 1 笔记下载链接：https://your-link.com")

@bot.message_handler(commands=['soalan'])
def send_soalan(message):
    if message.from_user.id in ALLOWED_USERS:
        bot.reply_to(message, "📝 Past Year Soalan 链接：https://your-pastyear.com")

# 保持运行（搭配 UptimeRobot 保持在线）
keep_alive()
bot.polling()