import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import schedule
import time
import threading
from datetime import datetime

fly auth login

#计算天数
def count_day():
    today = datetime.today()
    spm_day = datetime(2024,12,1)
    days_difference = (spm_day - today).days
    return (days_difference)


#API
API_TOKEN = '7193488836:AAGk0hPhA1HjGZWFs3ixGOQ4KEFsDRpGgLY'


#initialize bot
bot = telegram.Bot(token=API_TOKEN)


def send_message(chat_id,message):
    bot.send_message(chat_id=chat_id,text=message)


def job():
    days = count_day()
    chat_id = '1651618788'
    message = f'今天离spm还有{days}天哦小宝\^o^/ \n 记得读书少玩电话啊( •̀ ω •́ )✧ 哇哈哈哈哈'
    send_message(chat_id,message)


#set time
schedule.every().day.at("0:00").do(job())


#start the set time
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    updater = Updater(API_TOKEN, use_context=True)


    # 启动调度器
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()


    # 启动机器人
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()