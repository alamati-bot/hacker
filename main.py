import threading
import telebot
from telebot import types
import search_in_csv
import search_name
import time
import datetime
import requests
import csv
# from decouple import config
import ast
import random


BOT_TOKEN_base = "6571688882:AAF8xXbGaJi2quxm4Zpk0xKrp2AYLujAO_g"
bot_b= telebot.TeleBot(BOT_TOKEN_base)
BOT_TOKEN_shela = "6434609181:AAFs9F8mcQEaPh6elpPlJBbLmDJUBHIsXPU"
bot_sh= telebot.TeleBot(BOT_TOKEN_shela)
BOT_TOKEN_max = "6895920184:AAF7qgEouagr94QiIqK4VYxzzBN49NKGJQA"
bot_m= telebot.TeleBot(BOT_TOKEN_max)
BOT_TOKEN_prime = "6617507325:AAHMOf0lAPTGU0-YvlHtOWIW_izTUlUNr3g"
bot_p= telebot.TeleBot(BOT_TOKEN_prime)
BOT_TOKEN_contact = "6894311459:AAGbbE9Ko-WNFj7DTDe1XbpoByel3zcZPxo"
bot_c= telebot.TeleBot(BOT_TOKEN_contact)
BOT_TOKEN_admin = "6744156648:AAG8hQxAab-rTdm0cfn2g3A7WuZCs5YUuBs"
bot_ad= telebot.TeleBot(BOT_TOKEN_admin)
BOT_TOKEN_face = "6778175590:AAEDug0pSt-MPeotyXw4okhZhh4M6FVP0Po"
bot_face= telebot.TeleBot(BOT_TOKEN_face)

user_state = {}
fo = 5381170565
block = []
solo = 6038950187
admin = [6038950187,5561652878,1264230324,5366817198,5381170565,5580406193]
is_sub = [False]

def search_friend(bot, message, num, dep):
    idd = message.chat.id
    name,grades,avge = search_in_csv.search(str(num),dep)
    if name !=None:
            print(f"{num}  :  {dep}  :  {name}   ...   {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')} ...  {idd}")
            mnb = bot.send_message(idd, f"جاري البحث عن علامات {name}")
            if dep in ['physics.csv','geology.csv', 'statics.csv', 'chemistry.csv', 'biology.csv','math.csv']:
                fivty = 60
            else :
                fivty = 50
            time.sleep(1.2)
            msg = bot.edit_message_text(f"""
تم العثور على علامات للطالب :
( *{name}* )
يتم الآن جمع العلامات
       """, idd, mnb.message_id, parse_mode='Markdown')
            time.sleep(3)
            bot.edit_message_text(f"""
إن الطالب : *{name}*
قد حصل على العلامات التالية :
        """, idd, msg.message_id, parse_mode='Markdown')
            time.sleep(1.5)
            f,s,t,fo,z,avg = sort(grades,fivty)
            if f != "":
                bot.send_message(idd, f"*علامات السنة الأولى هي:*\n{f}\n\n© 2024 علامتي", parse_mode='Markdown')
                time.sleep(2)
            if s != "":
                bot.send_message(idd, f"*علامات السنة الثانية هي:*\n{s}\n\n© 2024 علامتي", parse_mode='Markdown')
                time.sleep(2)
            if t != "":
                bot.send_message(idd, f"*علامات السنة الثالثة هي:*\n{t}\n\n© 2024 علامتي", parse_mode='Markdown')
                time.sleep(2)
            if fo != "":
                bot.send_message(idd, f"*علامات السنة الرابعة هي:*\n{fo}\n\n© 2024 علامتي", parse_mode='Markdown')
                time.sleep(2)
            if z != "":
                bot.send_message(idd, f"*علامات المواد الراسبة هي:*\n{z}\n\n© 2024 علامتي", parse_mode='Markdown')
                time.sleep(2)
            if avg != None:
                time.sleep(1)
                bot.send_message(idd, f" وبمعدل قدره *{avg}*", parse_mode='Markdown')
            time.sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            dep = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')
            markup.add(dep)
            bot.send_message(idd, """شكراً لاستخدامك *بوت علاماتي*
------------------------------------------------------------------
© 2024 علامتي""", reply_markup=markup, parse_mode='Markdown')

def welcome(bot, message):
    idd = message.chat.id
    bot.send_chat_action(idd, action="typing")
    if idd in block :
                bot.send_message(message.chat.id, "عذراً لقد تم حظرك من البوت \nتواصل مع المطور @alamati_info")
    else:
        if f"{idd}_dep" in user_state:
            del user_state[f"{idd}_dep"]
        if f"{idd}_number" in user_state:
            del user_state[f"{idd}_number"]
        if f"{idd}_name" in user_state:
            del user_state[f"{idd}_name"]

        ch = "bot_alamati"
        mes = f"انت غير مشترك في القناة الخاصة بالبوت : @{ch} \nالرجاء الاشتراك للحصول على ميزات اكثر"
        url = f"https://api.telegram.org/bot{BOT_TOKEN_base}/getchatmember?chat_id=@{ch}&user_id={idd}"
        req = requests.get(url)

        markup = types.InlineKeyboardMarkup(row_width=1)
        dep = types.InlineKeyboardButton('كلية الآداب والعلوم الانسانية', callback_data='adab')
        dep1 = types.InlineKeyboardButton('كلية العلوم', callback_data='elom')
        dep2 = types.InlineKeyboardButton('الدخول بحساب ضيف', callback_data='guest')
        markup.add(dep, dep1)
        is_sub.clear()
        if bot == bot_b:
            markup.add(dep2)

            if "member" in req.text or "creator" in req.text or "administrator" in req.text :
                is_sub.append(True)
            else:
                is_sub.append(False)
                bot.send_chat_action(idd,action="typing")
                bot.send_message(message.chat.id, f"{mes}\nt.me/{ch}")
                bot.send_chat_action(idd,action="typing")
                time.sleep(4)
                bot.send_message(message.chat.id, "t.me/alamati_comments")
                time.sleep(2.5)
        else:
            is_sub.append(True)
        bot.send_chat_action(idd,action="typing")
        bot.send_message(message.chat.id, """أهلا بكم في بوت علاماتي
البوت يحتوي على علامات كلية الآداب وكلية العلوم
وقريباً سيتم اضافة علامات لكليات أخرى
-------------------------------------
اولا قم باختيار كليتك  """, reply_markup=markup)
        clear_chat(bot, message)

def clear_chat(bot, message):
    chat_id = message.chat.id
    try:
        for i in range(0,20):
                message_id = message.message_id - (20-i)
                try:
                    bot.delete_message(chat_id, message_id)
                except:
                    pass
    except Exception as e:
        pass

def sort(x,fivty=50):
    first = []
    second = []
    third = []
    forth = []
    fail = []
    marks= []
    subs =[]
    subs_f = []
    y= x.split("\n")
    for mark in y:
        if len(mark) != 0:
            item = mark.split("علامة : ")[1]
            mark = item.split(" في ")[0]
            sub1 = item.split(" في ")[1:]
            if len(sub1) >1 :
                sub2 = (" في ").join(sub1)
            else:
                sub2 = sub1[0]
            sub = sub2.split(" من السنةس")[0]
            year = sub2.split(" من السنةس")[1]
            try:
                mark = int(mark)
                if mark >= fivty:
                    marks.append(mark)
                    if int(year)==1:
                        first.append(item[:-10])
                    elif int(year)==2:
                        second.append(item[:-10])
                    elif int(year)==3:
                        third.append(item[:-10])
                    elif int(year)==4:
                        forth.append(item[:-10])
                    subs.append(sub)
                else:
                    fail.append(item)
                    subs_f.append(sub)
            except:
                fail.append(item)
                subs_f.append(sub)
    total = sum(marks)
    if len(marks)!=0:
        avg = total / len(marks)
        avg = round(avg, 2)
    else:
        avg = 0
    first = ("\n").join(first)
    second = ("\n").join(second)
    third = ("\n").join(third)
    forth = ("\n").join(forth)
    # fail = ("\n").join(fail)
    fail_s = []

    for i , item in enumerate(fail):
        if len(item) != 0:
            # item = mark.split("علامة : ")[1]
            mark = item.split(" في ")[0]
            sub1 = item.split(" في ")[1:]
            if len(sub1) >1 :
                sub2 = (" في ").join(sub1)
            else:
                sub2 = sub1[0]
            sub = sub2.split(" من السنةس")[0]
            year = sub2.split(" من السنةس")[1]
            if sub in subs :
                fail.remove(fail[i])
            else:
                fail_s.append(item)
    fail_s = ("\n").join(fail_s)

    return first,second,third,forth,fail_s,avg

def mine(bot, message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                num = row[1]
                name = row[2]
                dep = row[3]
                if row[6] != datetime.datetime.now().strftime('%Y-%m-%d'):
                    name,grades,avge = search_in_csv.search(str(num),dep)
                    if name !=None:
                        user_state[f"{idd}_num"] = message.text
                        if dep in ['physics.csv','geology.csv', 'statics.csv', 'chemistry.csv', 'biology.csv','math.csv']:
                            fivty = 60
                        else :
                            fivty = 50
                        bot.send_chat_action(idd, action="typing")
                        msg = bot.edit_message_text(f"""
أهلا بك : ( *{name}* )
يتم الآن البحث عن علاماتك وجمعها
شكراً لانتظارك   """, idd, message.message_id, parse_mode='Markdown')
                        bot.send_chat_action(idd, action="typing")
                        time.sleep(1.5)
                        f,s,t,fo,z,avg = sort(grades,fivty)
                        if f != "":
                            bot.send_chat_action(idd, action="typing")
                            bot.send_message(idd, f"*علامات السنة الأولى هي:*\n{f}\n\n© 2024 علامتي", parse_mode='Markdown')
                            time.sleep(2)
                        if s != "":
                            bot.send_chat_action(idd, action="typing")
                            bot.send_message(idd, f"*علامات السنة الثانية هي:*\n{s}\n\n© 2024 علامتي", parse_mode='Markdown')
                            time.sleep(2)
                        if t != "":
                            bot.send_chat_action(idd, action="typing")
                            bot.send_message(idd, f"*علامات السنة الثالثة هي:*\n{t}\n\n© 2024 علامتي", parse_mode='Markdown')
                            time.sleep(2)
                        if fo != "":
                            bot.send_chat_action(idd, action="typing")
                            bot.send_message(idd, f"*علامات السنة الرابعة هي:*\n{fo}\n\n© 2024 علامتي", parse_mode='Markdown')
                            time.sleep(2)
                        if z != "":
                            bot.send_chat_action(idd, action="typing")
                            bot.send_message(idd, f"*علامات المواد الراسبة هي:*\n{z}", parse_mode='Markdown')
                            time.sleep(2)
                        if avg != None:
                            bot.send_chat_action(idd, action="typing")
                            time.sleep(0.5)
                            bot.send_message(idd, f" وبمعدل قدره *{avg}*", parse_mode='Markdown')
                        bot.send_chat_action(idd, action="typing")
                        time.sleep(2)
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        dep = types.InlineKeyboardButton(' تواصل مع المطور ', url="https://t.me/alamati_comments")
                        start = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')

                        markup.add(dep,start)
                        bot.send_message(idd, """شكراً لاستخدامك *بوت علاماتي*""", reply_markup=markup, parse_mode='Markdown')
                else:
                        try:
                            bot.delete_message(idd, message.message_id)
                        except:
                            pass
                        mark_up = types.InlineKeyboardMarkup(row_width=1)
                        de = types.InlineKeyboardButton(' الاشتراك من هنا ', url="https://t.me/alamati_contact_bot")
                        sta = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')
                        mark_up.add(de,sta)
                        bot.send_message(idd, """لقد قمت بالبحث عن علاماتك هذا اليوم
 لا يمكنك البحث مرتين في نفس اليوم  ❌
يجب الانتظار حتى يوم الغد
-------------------------------------------------------
اذا كنت تريد البحث اكثر من مرة والبحث عن علامات أصدقائك يمكنك *الاشتراك* من هنا""", reply_markup=mark_up, parse_mode='Markdown')
                if bot == bot_b:
                    row[6] = datetime.datetime.now().strftime('%Y-%m-%d')
                    with open('db.csv', 'w', newline='', encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerows(data)
                    f.close()
                break


def him(bot, message):
    idd = message.chat.id
    if bot ==bot_b:
        bot.send_chat_action(idd, action="typing")
        bot.send_chat_action(idd, action="typing")
        mark_up = types.InlineKeyboardMarkup(row_width=1)
        de = types.InlineKeyboardButton(' الاشتراك من هنا ', url="https://t.me/alamati_contact_bot")
        sta = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')
        mark_up.add(de,sta)
        bot.send_message(idd, """*انت لا تملك اشتراك*  ❌
إن ميزة البحث عن علامات الآخرين تحتاج الى الاشتراك
-------------------------------------------------------
اذا كنت تريد البحث عن علامات أصدقائك يمكنك *الاشتراك* من هنا
https://t.me/alamati\_contact\_bot""", reply_markup=mark_up, parse_mode='Markdown')

def him_sh(message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()
    markup = types.InlineKeyboardMarkup(row_width=1)
    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                if len(row) >= 9:
                    row[8] = ast.literal_eval(row[8])
                    for i, fri in enumerate(row[8]):
                        btn = types.InlineKeyboardButton(f"{fri[1]}", callback_data=f"friend{i}")
                        markup.add(btn)
                    if len(row[8]) <= 4:
                        dep = types.InlineKeyboardButton(f"اضافة صديق آخر      (متبقي {5-len(row[8])})", callback_data="new_friend")
                        markup.add(dep)
                    bot_sh.send_message(idd, """شكراً لاستخدامك *بوت علاماتي*
------------------------------------------------------------------
يمكنك البحث عن علامات اصدقائك من هنا
اضغط على اسم الصديق من القائمة""", reply_markup=markup, parse_mode='Markdown')
                    break
                else:
                    welcome(bot_sh,message)
                    break

def him_m(message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()
    markup = types.InlineKeyboardMarkup(row_width=1)
    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                if len(row) >= 9:
                    row[8] = ast.literal_eval(row[8])
                    for i, fri in enumerate(row[8]):
                        btn = types.InlineKeyboardButton(f"{fri[1]}", callback_data=f"friend{i}")
                        markup.add(btn)
                    if len(row[8]) <= 14:
                        dep = types.InlineKeyboardButton(f"اضافة صديق آخر      (متبقي {15-len(row[8])})", callback_data="new_friend")
                        markup.add(dep)
                    bot_m.send_message(idd, """شكراً لاستخدامك *بوت علاماتي*
------------------------------------------------------------------
يمكنك البحث عن علامات اصدقائك من هنا
اضغط على اسم الصديق من القائمة""", reply_markup=markup, parse_mode='Markdown')
                else:
                    welcome(bot_m,message)
                    break

def him_p(message):
    idd = message.chat.id
    welcome(bot_p, message)

friend = []

def add_sh(message):
    idd = message.chat.id
    msg = bot_sh.send_message(idd, "يتم الآن اضافة صديقك الى قائمة الاصدقاء")
    found = False
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    if friend != []:
        for row in data:
            if len(row) != 0:
                if int(idd) == int(row[0]):
                    if len(row) >= 9:
                        row[8] = ast.literal_eval(row[8])

                        if len(row[8]) <= 4:
                            for fri in row[8]:
                                if fri == friend:
                                    bot_sh.send_chat_action(idd, action="typing")
                                    time.sleep(2)
                                    try:
                                        bot_sh.delete_message(idd,msg.message_id)
                                    except:
                                        pass
                                    bot_sh.send_message(idd, f"إن {friend[1]} موجود مسبقاً بقائمة أصدقائك\nولا يمكن اضافته مرة أخرى")
                                    found = True
                                    break
                            if not found:
                                row[8].append(friend)
                                bot_sh.send_chat_action(idd, action="typing")
                                time.sleep(1)
                                try:
                                    bot_sh.delete_message(idd,msg.message_id)
                                except:
                                    pass
                                bot_sh.send_message(idd, "تم اضافة صديقك بنجاح")
                        else:
                            bot_sh.send_chat_action(idd, action="typing")
                            time.sleep(0.5)
                            try:
                                bot_sh.delete_message(idd,msg.message_id)
                            except:
                                pass
                            bot_sh.send_message(idd, "عذراً لديك 5 أصدقاء مسبقاً \nلا يمكنك اضافة المزيد من الاصدقاء")
                    else:
                        row.append([friend])
                        bot_sh.send_chat_action(idd, action="typing")
                        time.sleep(1)
                        try:
                            bot_sh.delete_message(idd,msg.message_id)
                        except:
                            pass
                        bot_sh.send_message(idd, "تم اضافة صديقك بنجاح")

                    with open('db.csv', 'w', newline='', encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerows(data)
                    f.close()
                    friend.clear()
                    him_sh(message)
                    break

def add_m(message):
    idd = message.chat.id
    msg = bot_m.send_message(idd, "يتم الآن اضافة صديقك الى قائمة الاصدقاء")
    found = False
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    if friend != []:
        for row in data:
            if len(row) != 0:
                if int(idd) == int(row[0]):
                    if len(row) >= 9:
                        row[8] = ast.literal_eval(row[8])

                        if len(row[8]) <= 14:
                            for fri in row[8]:
                                if fri == friend:
                                    bot_m.send_chat_action(idd, action="typing")
                                    time.sleep(2)
                                    try:
                                        bot_m.delete_message(idd,msg.message_id)
                                    except:
                                        pass
                                    bot_m.send_message(idd, f"إن {friend[1]} موجود مسبقاً بقائمة أصدقائك\nولا يمكن اضافته مرة أخرى")
                                    found = True
                                    break
                            if not found:
                                row[8].append(friend)
                                bot_m.send_chat_action(idd, action="typing")
                                time.sleep(1)
                                try:
                                    bot_m.delete_message(idd,msg.message_id)
                                except:
                                    pass
                                bot_m.send_message(idd, "تم اضافة صديقك بنجاح")
                        else:
                            bot_m.send_chat_action(idd, action="typing")
                            time.sleep(0.5)
                            try:
                                bot_m.delete_message(idd,msg.message_id)
                            except:
                                pass
                            bot_m.send_message(idd, "عذراً لديك 15 صديق مسبقاً \nلا يمكنك اضافة المزيد من الاصدقاء")
                    else:
                        row.append([friend])
                        bot_m.send_chat_action(idd, action="typing")
                        time.sleep(1)
                        try:
                            bot_m.delete_message(idd,msg.message_id)
                        except:
                            pass
                        bot_m.send_message(idd, "تم اضافة صديقك بنجاح")

                    with open('db.csv', 'w', newline='', encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerows(data)
                    f.close()
                    friend.clear()
                    him_m(message)
                    break

def append(x):
    with open('db.csv', '+a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(x)
        print(f"adding {x[0]} and {x[1]} to data base in {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')}")
    f.close()

def new_member(message, num ,name, dep):
    idd = message.chat.id
    new =[idd, num, name, dep, "no_sub","no_notification", "never",datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')]
    append(new)
    start_b(message)

def welcome_back(bot, message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                num = row[1]
                name = row[2]
                sub = row [4]
                break

    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('البحث عن علاماتي', callback_data='mine')
    dep1 = types.InlineKeyboardButton('البحث عن علامة شخص آخر', callback_data='him')
    dep2 = types.InlineKeyboardButton('قناة البوت', url="https://t.me/bot_alamati")
    dep3 = types.InlineKeyboardButton('التواصل مع المطور', url="https://t.me/alamati_comments")
    dep4 = types.InlineKeyboardButton('الاشتراكات والشكاوي', url="https://t.me/alamati_contact_bot")
    markup.add(dep, dep1, dep2, dep3, dep4)
    if sub == "no_sub":
        if bot != bot_b:
            bot.send_message(idd, f"أهلا بك : *{name}*\nانت *لا تملك اشتراك* في هذا البوت\nيمكنك استخدام البوت التالي:\nhttps://t.me/alamati\_base\_bot", parse_mode='Markdown')
        else:
            bot.send_message(idd, f"أهلا بك : *{name}*", reply_markup=markup, parse_mode='Markdown')
    elif sub == "shela":
        if bot != bot_sh:
            bot.send_message(idd, f"أهلا بك : *{name}*\nانت *تملك اشتراك في بوت آخر *\nيمكنك استخدام البوت التالي:\nhttps://t.me/alamati\_shela\_bot", parse_mode='Markdown')
        else:
            bot.send_message(idd, f"أهلا بك : *{name}*", reply_markup=markup, parse_mode='Markdown')
    elif sub == "max":
        if bot != bot_m:
            bot.send_message(idd, f"أهلا بك : *{name}*\nانت *تملك اشتراك في بوت آخر *\nيمكنك استخدام البوت التالي:\nhttps://t.me/alamati\_max\_bot", parse_mode='Markdown')
        else:
            bot.send_message(idd, f"أهلا بك : *{name}*", reply_markup=markup, parse_mode='Markdown')
    elif sub == "prime":
        if bot != bot_p:
            bot.send_message(idd, f"أهلا بك : *{name}*\nانت *تملك اشتراك في بوت آخر *\nيمكنك استخدام البوت التالي:\nhttps://t.me/alamati\_prime\_bot", parse_mode='Markdown')
        else:
            bot.send_message(idd, f"أهلا بك : *{name}*", reply_markup=markup, parse_mode='Markdown')

@bot_ad.message_handler(commands=["start"])
def start_ad(message):
    idd = message.chat.id
    if idd in admin :
        bot_ad.send_message(idd, "Welcome To Your Bot")
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['view'])
def view(message):
    found = False
    idd = message.chat.id
    if idd in admin :
        text = message.text.split()
        if len(text) > 1:
            num = text[1]
            with open("db.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            f.close()

            for row in data:
                if len(row) != 0:
                    if (num) == (row[1]) or (num) == (row[0]):
                        bot_ad.send_message(idd, f"{row}")
                        found = True

            if not found:
                bot_ad.reply_to(message, f'The number ==> {num} <== is not found')
        else:
            bot_ad.reply_to(message, 'please enter the number after the command')
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['view_all'])
def view_all(message):
    idd = message.chat.id
    if idd in admin :
        with open("db.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
        f.close()
        rows = []
        for row in data:
            if len(row) != 0:
                rows.append(row)
                if len(rows) >= 50:
                    rows_text = "\n".join(rows)
                    bot_ad.send_message(idd, f"{rows_text}")
                    rows.clear()
        if len(rows) != 0:
            rows_text = "\n".join(rows)
            bot_ad.send_message(idd, f"{rows_text}")

    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['view_sub'])
def view_sub(message):
    idd = message.chat.id
    if idd in admin :
        with open("sub.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
        f.close()
        rows = []
        for row in data:
            if len(row) != 0:
                rows.append(row)
                if len(rows) >= 50:
                    rows_text = "\n".join(rows)
                    bot_ad.send_message(idd, f"{rows_text}")
                    rows.clear()
        if len(rows) != 0:
            rows_text = "\n".join(rows)
            bot_ad.send_message(idd, f"{rows_text}")
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")


@bot_ad.message_handler(commands=['send_to_all'])
def send_to_all(message):
    found = False
    idd = message.chat.id
    if idd in admin:
        text = message.text.split()
        if len(text) > 1:
            split = text[1:]
            msg = " ".join(split)
            with open("db.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            f.close()
            errors = []
            for row in data:
                if len(row) != 0:
                    try:
                        if row[4] == "no_sub":
                            bot_b.send_message(row[0],msg, parse_mode="Markdown")
                        elif row[4] == "shela":
                            bot_sh.send_message(row[0],msg, parse_mode="Markdown")
                        elif row[4] == "max":
                            bot_m.send_message(row[0],msg, parse_mode="Markdown")
                        elif row[4] == "prime":
                            bot_p.send_message(row[0],msg, parse_mode="Markdown")
                    except Exception as e :
                        errors.append([row[0],e])
            if len (errors) >1:
                error_mes = "\n\n".join([str(i)+ "  :  "+ str(j) for i, j in errors])
                bot_ad.send_message(idd,"Errors:\n"+error_mes)
            elif len(errors) == 1:
                bot_ad.send_message(idd,f"Message is not sent to {errors[0][0]} \nError:{errors[0][1]}")
            elif len(errors) == 0 :
                bot_ad.send_message(idd, "Message has been successfully sent!")
        else:
            bot_ad.reply_to(message, 'please enter the message after the command')
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['send_to_me'])
def send_to_me(message):
    found = False
    idd = message.chat.id
    if idd in admin:
        text = message.text.split()
        if len(text) > 1:
            split = text[1:]
            msg = " ".join(split)
            try:
                    bot_b.send_message(idd,msg, parse_mode="Markdown")
                    bot_ad.send_message(idd, "Message has been successfully sent!")
            except Exception as e :
                bot_ad.send_message(idd,f"Message is not sent to {idd} \nError:{e}")
        else:
            bot_ad.reply_to(message, 'please enter the message after the command')
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['subscribe'])
def subscribe(message):
    found =False
    idd = message.chat.id
    if idd in admin:
        text = message.text.split()
        if len(text) > 1:
            if len(text) > 2:
                num = text[1]
                sub = text[2]
                with open("db.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    data = list(reader)
                f.close()

                for row in data:
                    if len(row) != 0:
                        if (num) == (row[1]) or num == row[0]:
                            row[4] = sub
                            with open('db.csv', 'w', newline='', encoding="utf-8") as f:
                                writer = csv.writer(f)
                                writer.writerows(data)
                            f.close()
                            new = row[0:6]
                            new[5] = datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')
                            with open('sub.csv', 'a', encoding="utf-8") as s:
                                writer = csv.writer(s)
                                writer.writerow(new)
                            s.close()
                            found = True
                            bot_ad.send_message(idd, f"{num}  :  {row[2]}  \nhas updated successfully")
                            bot_ad.send_message(idd, f"{row}")
                            break
                if not found:
                    bot_ad.reply_to(message, f'The number ==> {num} <== is not found')
            else:
                bot_ad.reply_to(message, 'please enter the subscription after the number')
        else:
            bot_ad.reply_to(message, 'please enter the number after the command')
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['refresh'])
def refresh(message):
    idd = message.chat.id
    if idd in admin:
        text = message.text.split()
        if len(text) > 1:
                found = False
                num = text[1]
                with open("db.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    data = list(reader)
                f.close()

                for row in data:
                    if len(row) != 0:
                        if (num) == (row[1]):
                            row[6] = "no"
                            with open('db.csv', 'w', newline='', encoding="utf-8") as f:
                                writer = csv.writer(f)
                                writer.writerows(data)
                            f.close()
                            bot_ad.send_message(idd, f"{num}  :  {row[2]}  \nhas refreshed successfully")
                            found = True
                            break
                if not found:
                    bot_ad.reply_to(message, f'The number ==> {num} <== is not found')
        else:
            bot_ad.reply_to(message, 'please enter the number after the command')
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.message_handler(commands=['add'])
def add(message):
    idd = message.chat.id
    if idd in admin:
            text = message.text.split()
            for i,x in enumerate(text):
                text [i] = x.replace("#", " ")
            if len(text) > 1:
                    found = False
                    num = text[1]
                    item = text[1:]
                    with open("db.csv", "r", encoding="utf-8") as f:
                        reader = csv.reader(f)
                        data = list(reader)
                    f.close()

                    for row in data:
                        if len(row) != 0:
                            if (num) == (row[0]):
                                found = True
                                bot_ad.reply_to(message, f'The number ==> {num} <== is found')
                                break
                    if not found:
                        with open('db.csv', '+a', encoding="utf-8") as f:
                            writer = csv.writer(f)
                            item.extend(["no_sub","no_notification", "never", datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')])
                            writer.writerow(item)
                            print(f"adding {item[0]} and {item[1]} to data base in {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')}")
                        f.close()
                        bot_ad.reply_to(message, f'adding {item[0]} and {item[1]} to data base in {datetime.datetime.now().strftime("%Y-%m-%d || %H:%M:%S")}')
            else:
                bot_ad.reply_to(message, 'please enter the number after the command')
    else:
        bot_ad.reply_to(message,"ليس لديك صلاحية لاستخدام هذا البوت\nسيتم حظرك من جميع البوتات اذا حاولت استخدام هذا البوت مرة ثانية")

@bot_ad.callback_query_handler(func=lambda call:True)
def answer_ad(callback):
    if callback.message:
        idd = callback.message.chat.id

        if callback.data == 'restart':
            try:
                bot_b.delete_message(idd,callback.message.message_id)
            except:
                pass
            start_ad(callback.message)


@bot_b.message_handler(commands=["start"])
def start_b(message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                welcome_back(bot_b,message)
                clear_chat(bot_b, message)
                break
    else:
        welcome(bot_b, message)
        clear_chat(bot_b, message)

@bot_b.callback_query_handler(func=lambda call:True)
def answer_b(callback):
    if callback.message:
        idd = callback.message.chat.id
        department = user_state.get(f"{idd}_dep", {})
        if department == 'اللغة العربية':
            dep = "arabic.csv"
        elif department == 'اللغة الانكليزية':
            dep = "english.csv"
        elif department == 'اللغة الفرنسية':
            dep = "french.csv"
        elif department == 'الجغرافية':
            dep = "geography.csv"
        elif department == 'التاريخ':
            dep = "history.csv"
        elif department == 'الفلسفة':
            dep = "philosophy.csv"
        elif department == 'الآثار':
            dep = "archeology.csv"
        elif department == 'علم الاجتماع':
            dep = "sociology.csv"
        elif department == 'علم الحياة':
            dep = "biology.csv"
        elif department == 'الرياضيات':
            dep = "math.csv"
        elif department == 'الكيمياء':
            dep = "chemistry.csv"
        elif department == 'الفيزياء':
            dep = "physics.csv"
        elif department == 'الجيلوجيا':
            dep = "geology.csv"
        elif department == 'الاحصاء الرياضي':
            dep = "statics.csv"

        if callback.data == 'adab':
            adab(bot_b, callback)

        if callback.data == 'elom':
            alom(bot_b, callback)

        elif callback.data == 'guest':
            try:
                bot_b.delete_message(idd,callback.message.message_id)
            except:
                pass
            new_member (callback.message, "00000", "حساب ضيف", "english.csv")

        elif callback.data == 'restart':
            try:
                bot_b.delete_message(idd,callback.message.message_id)
            except:
                pass
            start_b(callback.message)

        elif callback.data in ['اللغة العربية', 'اللغة الانكليزية','الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات', 'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة', 'الآثار'] :
            idd = callback.message.chat.id
            user_state[f"{idd}_dep"] = callback.data
            markup = types.InlineKeyboardMarkup(row_width=1)
            name = types.InlineKeyboardButton('البحث عن طريق الاسم', callback_data='name')
            number = types.InlineKeyboardButton('البحث عن طريق الرقم', callback_data='number')
            start = types.InlineKeyboardButton('اختيار قسم جديد', callback_data='restart')

            markup.add(number, start)
            try:
                bot_b.edit_message_text(chat_id=idd, message_id=callback.message.message_id
                                  , text=f"لقد اخترت : {callback.data}\nهل تريد البحث عن طريق الاسم أم الرقم الجامعي \nعلماً ان علمية البحث عن الاسم قد لا تكون دقيقة دائماً ", reply_markup=markup)
            except Exception as e:
                    print(e)
                    bot_b.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_b, callback.message)
            except:
                    print("error")

        elif callback.data == "mine":
            mine(bot_b, callback.message)

        elif callback.data == "him":
            try:
                bot_b.delete_message(idd,callback.message.message_id)
            except:
                pass
            him(bot_b, callback.message)

        elif callback.data == "number":
            try:
                msg = bot_b.edit_message_text(chat_id=callback.message.chat.id, text="ادخل رقمك الجامعي\nالرجاء كتابة الارقام باللغة الانكليزية (1234567890)", message_id=callback.message.message_id)
                bot_b.register_next_step_handler(msg, process_number_step, bot_b)
            except Exception as e:
                    bot_b.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_b, callback.message)

@bot_sh.message_handler(commands=["start"])
def start_sh(message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                welcome_back(bot_sh,message)
                clear_chat(bot_sh, message)
                break
    else:
        bot_sh.send_message(idd, "انت غير مسجل بالبوت انتقل الى الرابط التالي للتسجيل    \nhttps://t.me/alamati_base_bot")
        welcome(bot_b, message)

@bot_sh.callback_query_handler(func=lambda call:True)
def answer_sh(callback):
    if callback.message:
        idd = callback.message.chat.id
        if callback.data == "new_friend":
            try:
                bot_sh.delete_message(idd,callback.message.message_id)
            except:
                pass
            welcome(bot_sh,callback.message)


        department = user_state.get(f"{idd}_dep", {})
        if department == 'اللغة العربية':
            dep = "arabic.csv"
        elif department == 'اللغة الانكليزية':
            dep = "english.csv"
        elif department == 'اللغة الفرنسية':
            dep = "french.csv"
        elif department == 'الجغرافية':
            dep = "geography.csv"
        elif department == 'التاريخ':
            dep = "history.csv"
        elif department == 'الفلسفة':
            dep = "philosophy.csv"
        elif department == 'الآثار':
            dep = "archeology.csv"
        elif department == 'علم الاجتماع':
            dep = "sociology.csv"
        elif department == 'علم الحياة':
            dep = "biology.csv"
        elif department == 'الرياضيات':
            dep = "math.csv"
        elif department == 'الكيمياء':
            dep = "chemistry.csv"
        elif department == 'الفيزياء':
            dep = "physics.csv"
        elif department == 'الجيلوجيا':
            dep = "geology.csv"
        elif department == 'الاحصاء الرياضي':
            dep = "statics.csv"

        if callback.data == 'adab':
            adab(bot_sh, callback)

        elif callback.data == 'elom':
            alom(bot_sh, callback)

        elif callback.data == 'add':
            try:
                bot_sh.delete_message(idd,callback.message.message_id)
            except:
                pass
            add_sh(callback.message)

        elif callback.data == 'restart':
            try:
                bot_sh.delete_message(idd,callback.message.message_id)
            except:
                pass
            start_sh(callback.message)

        elif callback.data == "mine":
            mine(bot_sh, callback.message)
        elif callback.data == "him":
            try:
                bot_sh.delete_message(idd,callback.message.message_id)
            except:
                pass
            him_sh(callback.message)

        elif callback.data in ['اللغة العربية', 'اللغة الانكليزية','الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات', 'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة', 'الآثار'] :
            idd = callback.message.chat.id
            user_state[f"{idd}_dep"] = callback.data
            markup = types.InlineKeyboardMarkup(row_width=1)
            name = types.InlineKeyboardButton('البحث عن طريق الاسم', callback_data='name')
            number = types.InlineKeyboardButton('البحث عن طريق الرقم', callback_data='number')
            start = types.InlineKeyboardButton('اختيار قسم جديد', callback_data='restart')

            markup.add(number, start)
            try:
                bot_sh.edit_message_text(chat_id=idd, message_id=callback.message.message_id
                                  , text=f"لقد اخترت : {callback.data}\nهل تريد البحث عن طريق الاسم أم الرقم الجامعي \nعلماً ان علمية البحث عن الاسم قد لا تكون دقيقة دائماً ", reply_markup=markup)
            except Exception as e:
                    print(e)
                    bot_sh.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_sh, callback.message)

        elif callback.data == "number":
            try:
                msg = bot_sh.edit_message_text(chat_id=callback.message.chat.id, text="ادخل رقمك الجامعي\nالرجاء كتابة الارقام باللغة الانكليزية (1234567890)", message_id=callback.message.message_id)
                bot_sh.register_next_step_handler(msg, process_number_step, bot_sh)
            except Exception as e:
                    bot_sh.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    try:
                        bot_sh.delete_message(idd,callback.message.message_id)
                    except:
                        pass
                    welcome(bot_sh, callback.message)

        else :
            with open("db.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            f.close()
            for row in data:
                if len(row) != 0:
                    if int(idd) == int(row[0]):
                        if len(row) >= 9:
                            row[8] = ast.literal_eval(row[8])
                            for i, fri in enumerate(row[8]):
                                if callback.data == f"friend{i}":
                                    try:
                                        bot_sh.delete_message(idd,callback.message.message_id)
                                    except:
                                        pass
                                    search_friend(bot_sh, callback.message, row[8][i][0], row[8][i][2])

@bot_m.message_handler(commands=["start"])
def start_m(message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                welcome_back(bot_m,message)
                clear_chat(bot_m, message)
                break
    else:
        bot_m.send_message(idd, "انت غير مسجل بالبوت انتقل الى الرابط التالي للتسجيل    \nhttps://t.me/alamati_base_bot")

@bot_m.callback_query_handler(func=lambda call:True)
def answer_m(callback):
    if callback.message:
        idd = callback.message.chat.id
        department = user_state.get(f"{idd}_dep", {})
        if department == 'اللغة العربية':
            dep = "arabic.csv"
        elif department == 'اللغة الانكليزية':
            dep = "english.csv"
        elif department == 'اللغة الفرنسية':
            dep = "french.csv"
        elif department == 'الجغرافية':
            dep = "geography.csv"
        elif department == 'التاريخ':
            dep = "history.csv"
        elif department == 'الفلسفة':
            dep = "philosophy.csv"
        elif department == 'الآثار':
            dep = "archeology.csv"
        elif department == 'علم الاجتماع':
            dep = "sociology.csv"
        elif department == 'علم الحياة':
            dep = "biology.csv"
        elif department == 'الرياضيات':
            dep = "math.csv"
        elif department == 'الكيمياء':
            dep = "chemistry.csv"
        elif department == 'الفيزياء':
            dep = "physics.csv"
        elif department == 'الجيلوجيا':
            dep = "geology.csv"
        elif department == 'الاحصاء الرياضي':
            dep = "statics.csv"

        if callback.data == "new_friend":
            try:
                bot_m.delete_message(idd,callback.message.message_id)
            except:
                pass
            welcome(bot_m,callback.message)

        elif callback.data == 'adab':
            adab(bot_m, callback)

        elif callback.data == 'elom':
            alom(bot_m, callback)

        elif callback.data == 'add':
            add_m(callback.message)

        elif callback.data == 'restart':
            try:
                bot_m.delete_message(idd,callback.message.message_id)
            except:
                pass
            start_m(callback.message)

        elif callback.data == "mine":
            mine(bot_m, callback.message)
        elif callback.data == "him":
            him_m(callback.message)

        elif callback.data in ['اللغة العربية', 'اللغة الانكليزية','الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات', 'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة', 'الآثار'] :
            idd = callback.message.chat.id
            user_state[f"{idd}_dep"] = callback.data
            markup = types.InlineKeyboardMarkup(row_width=1)
            name = types.InlineKeyboardButton('البحث عن طريق الاسم', callback_data='name')
            number = types.InlineKeyboardButton('البحث عن طريق الرقم', callback_data='number')
            start = types.InlineKeyboardButton('اختيار قسم جديد', callback_data='restart')

            markup.add(number, start)
            try:
                bot_m.edit_message_text(chat_id=idd, message_id=callback.message.message_id
                                  , text=f"لقد اخترت : {callback.data}\nهل تريد البحث عن طريق الاسم أم الرقم الجامعي \nعلماً ان علمية البحث عن الاسم قد لا تكون دقيقة دائماً ", reply_markup=markup)
            except Exception as e:
                    bot_m.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_m, callback.message)

        elif callback.data == "number":
            try:
                msg = bot_m.edit_message_text(chat_id=callback.message.chat.id, text="ادخل رقمك الجامعي\nالرجاء كتابة الارقام باللغة الانكليزية (1234567890)", message_id=callback.message.message_id)
                bot_m.register_next_step_handler(msg, process_number_step, bot_m)
            except Exception as e:
                    bot_m.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_m, callback.message)

        else :
            with open("db.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            f.close()
            for row in data:
                if len(row) != 0:
                    if int(idd) == int(row[0]):
                        if len(row) >= 9:
                            row[8] = ast.literal_eval(row[8])
                            for i, fri in enumerate(row[8]):
                                if callback.data == f"friend{i}":
                                    try:
                                        bot_m.delete_message(idd,callback.message.message_id)
                                    except:
                                        pass
                                    search_friend(bot_m, callback.message, row[8][i][0], row[8][i][2])


@bot_p.message_handler(commands=["start"])
def start_p(message):
    idd = message.chat.id
    with open("db.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    for row in data:
        if len(row) != 0:
            if int(idd) == int(row[0]):
                welcome_back(bot_p,message)
                clear_chat(bot_p, message)
                break
    else:
        bot_p.send_message(idd, "انت غير مسجل بالبوت انتقل الى الرابط التالي للتسجيل    \nhttps://t.me/alamati_base_bot")

@bot_p.callback_query_handler(func=lambda call:True)
def answer_p(callback):
    if callback.message:
        idd = callback.message.chat.id
        department = user_state.get(f"{idd}_dep", {})
        if department == 'اللغة العربية':
            dep = "arabic.csv"
        elif department == 'اللغة الانكليزية':
            dep = "english.csv"
        elif department == 'اللغة الفرنسية':
            dep = "french.csv"
        elif department == 'الجغرافية':
            dep = "geography.csv"
        elif department == 'التاريخ':
            dep = "history.csv"
        elif department == 'الفلسفة':
            dep = "philosophy.csv"
        elif department == 'الآثار':
            dep = "archeology.csv"
        elif department == 'علم الاجتماع':
            dep = "sociology.csv"
        elif department == 'علم الحياة':
            dep = "biology.csv"
        elif department == 'الرياضيات':
            dep = "math.csv"
        elif department == 'الكيمياء':
            dep = "chemistry.csv"
        elif department == 'الفيزياء':
            dep = "physics.csv"
        elif department == 'الجيلوجيا':
            dep = "geology.csv"
        elif department == 'الاحصاء الرياضي':
            dep = "statics.csv"


        if callback.data == 'adab':
            adab(bot_p, callback)

        if callback.data == 'elom':
            alom(bot_p, callback)


        elif callback.data == 'restart':
            try:
                bot_p.delete_message(idd,callback.message.message_id)
            except:
                pass
            start_p(callback.message)


        elif callback.data == "mine":
            mine(bot_p, callback.message)
        elif callback.data == "him":
            him_p( callback.message)

        elif callback.data in ['اللغة العربية', 'اللغة الانكليزية','الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات', 'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة', 'الآثار'] :
            idd = callback.message.chat.id
            user_state[f"{idd}_dep"] = callback.data
            markup = types.InlineKeyboardMarkup(row_width=1)
            name = types.InlineKeyboardButton('البحث عن طريق الاسم', callback_data='name')
            number = types.InlineKeyboardButton('البحث عن طريق الرقم', callback_data='number')
            start = types.InlineKeyboardButton('اختيار قسم جديد', callback_data='restart')

            markup.add(number, start)
            try:
                bot_p.edit_message_text(chat_id=idd, message_id=callback.message.message_id
                                  , text=f"لقد اخترت : {callback.data}\nهل تريد البحث عن طريق الاسم أم الرقم الجامعي \nعلماً ان علمية البحث عن الاسم قد لا تكون دقيقة دائماً ", reply_markup=markup)
            except Exception as e:
                    print(e)
                    bot_p.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_p, callback.message)

        elif callback.data == "number":
            try:
                msg = bot_p.edit_message_text(chat_id=callback.message.chat.id, text="ادخل رقمك الجامعي\nالرجاء كتابة الارقام باللغة الانكليزية (1234567890)", message_id=callback.message.message_id)
                bot_p.register_next_step_handler(msg, process_number_step, bot_p)
            except Exception as e:
                    bot_p.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
                    welcome(bot_p, callback.message)

def process_number_step(message, bot):
    idd = message.chat.id
    if user_state.get(f"{idd}_dep", {}) in ['اللغة العربية', 'اللغة الانكليزية','الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات', 'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة', 'الآثار']:
        x= message.text
        department = user_state.get(f"{idd}_dep", {})
        if department == 'اللغة العربية':
            dep = "arabic.csv"
        elif department == 'اللغة الانكليزية':
            dep = "english.csv"
        elif department == 'اللغة الفرنسية':
            dep = "french.csv"
        elif department == 'الجغرافية':
            dep = "geography.csv"
        elif department == 'التاريخ':
            dep = "history.csv"
        elif department == 'الفلسفة':
            dep = "philosophy.csv"
        elif department == 'الآثار':
            dep = "archeology.csv"
        elif department == 'علم الاجتماع':
            dep = "sociology.csv"
        elif department == 'علم الحياة':
            dep = "biology.csv"
        elif department == 'الرياضيات':
            dep = "math.csv"
        elif department == 'الكيمياء':
            dep = "chemistry.csv"
        elif department == 'الفيزياء':
            dep = "physics.csv"
        elif department == 'الجيلوجيا':
            dep = "geology.csv"
        elif department == 'الاحصاء الرياضي':
            dep = "statics.csv"

        try:
            x = message.text
            x = int(x)
            name,grades,avge = search_in_csv.search(str(x),dep)
            if name !=None:
                user_state[f"{idd}_num"] = message.text
                if bot == bot_b:
                    new_member(message, x, name, dep)
                elif bot == bot_p:
                    print(f"{x}  :  {dep}  :  {name}   ...   {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')} ...  {idd}")
                    mnb = bot.send_message(idd, f"جاري البحث عن الرقم ( {x} )")
                    if department in ['الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات']:
                        fivty = 60
                    else :
                        fivty = 50
                    time.sleep(1.2)
                    msg = bot.edit_message_text(f"""
تم العثور على علامات للطالب :
    ( *{name}* )
يتم الآن جمع العلامات
شكراً لانتظارك        """, idd, mnb.message_id, parse_mode='Markdown')
                    time.sleep(3)
                    bot.edit_message_text(f"""
إن الطالب : *{name}*
قد حصل على العلامات التالية :
                """, idd, msg.message_id, parse_mode='Markdown')
                    time.sleep(1.5)
                    f,s,t,fo,z,avg = sort(grades,fivty)
                    if f != "":
                        bot.send_message(idd, f"*علامات السنة الأولى هي:*\n{f}", parse_mode='Markdown')
                        time.sleep(2)
                    if s != "":
                        bot.send_message(idd, f"*علامات السنة الثانية هي:*\n{s}", parse_mode='Markdown')
                        time.sleep(2)
                    if t != "":
                        bot.send_message(idd, f"*علامات السنة الثالثة هي:*\n{t}", parse_mode='Markdown')
                        time.sleep(2)
                    if fo != "":
                        bot.send_message(idd, f"*علامات السنة الرابعة هي:*\n{fo}", parse_mode='Markdown')
                        time.sleep(2)
                    if z != "":
                        bot.send_message(idd, f"*علامات المواد الراسبة هي:*\n{z}", parse_mode='Markdown')
                        time.sleep(2)
                    if avg != None:
                        time.sleep(1)
                        bot.send_message(idd, f" وبمعدل قدره *{avg}*", parse_mode='Markdown')
                    time.sleep(2)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    dep = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')
                    markup.add(dep)
                    bot.send_message(idd, """شكراً لاستخدامك *بوت علاماتي*
------------------------------------------------------------------
يمكنك البحث عن رقم جديد من هنا """, reply_markup=markup, parse_mode='Markdown')
                else:
                    mnb = bot.send_message(idd, f"جاري البحث عن الرقم ( {x} )")
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    arabic = types.InlineKeyboardButton('اضافة الى قائمة الاصدقاء', callback_data='add')
                    english = types.InlineKeyboardButton('البحث عن رقم جديد', callback_data='him')
                    french = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')
                    markup.add(arabic,english,french)
                    friend.append(x)
                    friend.append(name)
                    friend.append(dep)
                    msg = bot.edit_message_text(f"""
تم العثور على علامات للطالب :
    ( *{name}* )
هل تريد اضافته الى قائمة أصدقائك؟       """, idd, mnb.message_id, parse_mode='Markdown', reply_markup=markup)

            elif name == None  :
                markup = types.InlineKeyboardMarkup(row_width=2)
                aric = types.InlineKeyboardButton('العودة الى صفحة البداية', callback_data='restart')
                markup.add(aric)
                bot.send_message(idd, f"الرقم ({x}) غير موجود", reply_markup=markup)



            else:
                msg = bot.send_message(idd, f"الرقم ({x}) غير موجود")
                bot.send_message(idd,"اضغط   /start    للبدء من جديد")
        except ValueError:
            msg = bot.reply_to(message, 'هذا ليس رقمًا صالحًا. الرجاء إدخال ارقام فقط')
            bot.register_next_step_handler(msg, process_number_step)
        except Exception as e:
            bot.reply_to(message, f'حدث خطأ ما\nفي حال تكرر الخطأ تواصل مع المطور\nالخطأ: {e} ')
            print(f"{e} ... {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')}  ...  {idd}")
    else:
        bot.send_message(idd, "من فضلك اختر قسمًا أولاً.\nاضغط   /start    للبدء من جديد")

def alom(bot, callback):
    idd = callback.message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    arabic = types.InlineKeyboardButton('علم الحياة', callback_data='علم الحياة')
    english = types.InlineKeyboardButton('الرياضيات', callback_data='الرياضيات')
    frensh = types.InlineKeyboardButton('الكيمياء', callback_data='الكيمياء')
    geography = types.InlineKeyboardButton('الفيزياء', callback_data='الفيزياء')
    history = types.InlineKeyboardButton('الجيلوجيا', callback_data='الجيلوجيا')
    philosophy = types.InlineKeyboardButton('الاحصاء الرياضي', callback_data='الاحصاء الرياضي')

    markup.add(arabic,english,frensh,geography,history,philosophy)

    try:
        bot.edit_message_text(chat_id=idd, message_id=callback.message.message_id
                        , text="البوت يحتوي على علامات كلية العلوم \nللعام 2022/2023 فقط\n----------------------------------------------\nما هو قسمك؟", reply_markup=markup)
    except Exception as e:
        bot.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
        welcome(bot, callback.message)
    except:
        print("error")

def adab(bot, callback):
    idd = callback.message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    arabic = types.InlineKeyboardButton('اللغة العربية', callback_data='اللغة العربية')
    english = types.InlineKeyboardButton('اللغة الانكليزية', callback_data='اللغة الانكليزية')
    frensh = types.InlineKeyboardButton('اللغة الفرنسية', callback_data='اللغة الفرنسية')
    geography = types.InlineKeyboardButton('الجغرافية', callback_data='الجغرافية')
    history = types.InlineKeyboardButton('التاريخ', callback_data='التاريخ')
    socology = types.InlineKeyboardButton('علم الاجتماع', callback_data='علم الاجتماع')
    philosophy = types.InlineKeyboardButton('الفلسفة', callback_data='الفلسفة')
    arch = types.InlineKeyboardButton('الآثار', callback_data='الآثار')

    markup.add(arabic,english,frensh,geography,history,socology,philosophy,arch)

    try:
        bot.edit_message_text(chat_id=idd, message_id=callback.message.message_id
                        , text="البوت يحتوي على علامات كلية الآداب منذ 2018\n----------------------------------------------\nما هو قسمك؟", reply_markup=markup)
    except Exception as e:
        bot.send_message(idd, f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد")
        welcome(bot, callback.message)
    except:
        print("error")

@bot_c.message_handler(commands=["start"])
def welcome_contact(message):
    idd = message.chat.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    bot_c.send_chat_action(idd,action="typing")
    ch = "bot_alamati"
    mes = f"انت غير مشترك في القناة الخاصة بالبوت : @{ch} \nالرجاء الاشتراك للحصول على ميزات اكثر"
    url = f"https://api.telegram.org/bot{BOT_TOKEN_contact}/getchatmember?chat_id=@{ch}&user_id={idd}"
    req = requests.get(url)
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('تقديم اقتراح لتحسين البوت', callback_data='sug')
    dep1 = types.InlineKeyboardButton('تقديم شكوى عن مشكلة حدثت معك', callback_data='pro')
    dep2 = types.InlineKeyboardButton('الاشتراك بالبوت', callback_data='sub')
    dep3 = types.InlineKeyboardButton('العودة الى البوت', url="https://t.me/alamai00bot")
    markup.add(dep,dep1,dep2,dep3)
    is_sub.clear()
    if "member" in req.text or "creator" in req.text or "administrator" in req.text:
        is_sub.append(True)
    else:
        is_sub.append(False)
        bot_c.send_message(message.chat.id, f"{mes}\nt.me/{ch}")
        bot_c.send_chat_action(idd,action="typing")
        time.sleep(2.5)
    bot_c.send_chat_action(idd,action="typing")
    bot_c.send_message(message.chat.id, """أهلا بكم في بوت التواصل الخاص
لماذا تريد التواصل مع مطور البوت
""", reply_markup=markup)

@bot_c.message_handler(commands=["help"])
def help(message):
    idd = message.chat.id
    bot_c.send_message(idd, "قريباً سيتم نشر الشروحات الخاصة بالبوت")

@bot_c.callback_query_handler(func=lambda call:True)
def answer_c(callback):
    if callback.message:
        idd = callback.message.chat.id
        if callback.data == 'pro':
                markup = types.InlineKeyboardMarkup(row_width=1)
                arabic = types.InlineKeyboardButton('البوت لا يقوم بالرد على الرسائل', callback_data='no_res')
                english = types.InlineKeyboardButton('لا استطيع البحث عن طريق الاسم', callback_data='no_name')
                frensh = types.InlineKeyboardButton('رقمي الجامعي غير موجود', callback_data='no_num')
                geography = types.InlineKeyboardButton('خطأ في العلامات', callback_data='mark_error')
                history = types.InlineKeyboardButton('غير ذلك', callback_data='else')
                markup.add(arabic,english,frensh,geography,history)
                bot_c.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id
                                  , text="ما هي المشكلة التي تواجهها؟", reply_markup=markup)

        elif callback.data == 'restart':
            welcome_contact(callback.message)

        elif callback.data == 'sub':
            subscribe(callback.message)
            try:
                bot_c.delete_message(idd, callback.message.message_id)
            except:
                pass

        elif callback.data == 'confirm':
            found = False
            found1 = False
            with open("sub.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            f.close()
            for row in data:
                if len(row) != 0:
                    if str(idd) == (row[0]):
                        if row[4] == "wait":
                            found = True
                            bot_c.send_message(idd, "لديك طلب اشتراك سابق\nيرجى الانتظار حتى الانتهاء من معالجة طلبك السابق")
            if not found:
                with open("db.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    data1 = list(reader)
                f.close()
                for row in data1:
                    if len(row) != 0:
                        if str(idd) == str(row[0]) :
                            found1 = True
                            new = row[0:4]
                            new.extend(["wait",datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')])
                            with open('sub.csv', 'a', encoding="utf-8") as s:
                                writer = csv.writer(s)
                                writer.writerow(new)
                            s.close()
                            msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="الرجاء ادخال اسمك ورقمك وقسمك ورقم جوالك\(اختياري\) مع نوع الاشتراك ومدته *في رسالة واحدة* \nعلماً انه سيتم تحويل اول رسالة فقط الى المسؤول", message_id=callback.message.message_id,parse_mode="MarkdownV2")
                            bot_c.send_message(idd, """الاسم:
الرقم الجامعي:
القسم:
رقم الجوال:
نوع الاشتراك:
مدي الاشتراك: """)
                            bot_c.register_next_step_handler(msg, process_else)
            if not found1:
                bot_c.answer_callback_query(callback.id, text='بياناتك غير موجودة بالبوت')
                bot_c.send_message(idd, "انت غير مسجل بالبوت \nانتقل الى الرابط التالي للتسجيل\nhttps://t.me/alamati_base_bot")
        elif callback.data in ["first", "year"]:
            sub_now(callback.message)
            try:
                bot_c.delete_message(idd, callback.message.message_id)
            except:
                pass

        elif callback.data == 'shela':
            shela(callback.message)
            try:
                bot_c.delete_message(idd, callback.message.message_id)
            except:
                pass

        elif callback.data == 'shela_max':
            shela_max(callback.message)
            try:
                bot_c.delete_message(idd, callback.message.message_id)
            except:
                pass

        elif callback.data == 'prime':
            prime(callback.message)
            try:
                bot_c.delete_message(idd, callback.message.message_id)
            except:
                pass

        elif callback.data == 'msg':
            m_msg(callback.message)
            try:
                bot_c.delete_message(idd, callback.message.message_id)
            except:
                pass

        elif callback.data == "sug":
            markup = types.InlineKeyboardMarkup(row_width=1)
            name = types.InlineKeyboardButton('اضافة علامات من سنوات قبل 2018', callback_data='old')
            number = types.InlineKeyboardButton('اضافة علامات من كليات اخرى', callback_data='other')
            start = types.InlineKeyboardButton('غير ذلك', callback_data='else')
            markup.add(name, number, start)
            bot_c.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id
                                  , text=f"ما هو اقتراحك لتحسين البوت؟", reply_markup=markup)

        elif callback.data == "else":
            if is_sub[0] == True:
                msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="الرجاء ادخال مشكلتك في رسالة واحدة \nعلماً انه سيتم تحويل اول رسالة فقط الى المسؤول", message_id=callback.message.message_id)
                bot_c.register_next_step_handler(msg, process_else)
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                dep2 = types.InlineKeyboardButton('الاشتراك من هنا', url="https://t.me/bot_alamati")
                markup.add(dep2)
                bot_c.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id
                                  , text=f"عذراً انت غير مشترك في قناة البوت\nوهذه الميزة حصرية للمشتركين\nيمكنك الاشتراك ثم المحاولة مرة ثانية\nhttps://t.me/bot_alamati", reply_markup=markup)

        elif callback.data == "back_bot":
            print("back")

        elif callback.data == "no_name":
            if is_sub[0] == True:
                msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="ادخل اسمك وقسمك ورقمك الجامعي (اذا وجد) \nادخل جميع المعلومات في رسالة واحدة", message_id=callback.message.message_id)
                bot_c.register_next_step_handler(msg, process_else)
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                dep2 = types.InlineKeyboardButton('الاشتراك من هنا', url="https://t.me/bot_alamati")
                markup.add(dep2)
                bot_c.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id
                                  , text=f"عذراً انت غير مشترك في قناة البوت\nوهذه الميزة حصرية للمشتركين\nيمكنك الاشتراك ثم المحاولة مرة ثانية\nhttps://t.me/bot_alamati", reply_markup=markup)

        elif callback.data == "no_num":
            msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="قد تكون المشكلة انك تدخل الارقام باللغة العربية \nيرجى ادخال الارقام الانكليزية (0123456789) فقط \nادخل اسمك ورقمك الجامعي مع القسم \nادخل جميع المعلومات في رسالة واحدة", message_id=callback.message.message_id)
            bot_c.register_next_step_handler(msg, process_else)

        elif callback.data == "other":
            if is_sub[0] == True:
                msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="ادخل اسمك واسم كليتك مع القسم \nادخل جميع المعلومات في رسالة واحدة", message_id=callback.message.message_id)
                bot_c.register_next_step_handler(msg, process_else)
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                dep2 = types.InlineKeyboardButton('الاشتراك من هنا', url="https://t.me/bot_alamati")
                markup.add(dep2)
                bot_c.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id
                                  , text=f"عذراً انت غير مشترك في قناة البوت\nوهذه الميزة حصرية للمشتركين\nيمكنك الاشتراك ثم المحاولة مرة ثانية\nhttps://t.me/bot_alamati", reply_markup=markup)

        elif callback.data == "old":
            msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="تم تسجيل طلبك لاضافة سنوات قبل ال 2018", message_id=callback.message.message_id)
            bot_c.send_message(solo, f"from: {idd}\nproblem: old")

        elif callback.data == "no_res":
            msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="تم ارسال الخطأ الى المطور\nعلماً أن الخطأ يكون بسبب أن البوت في النسخة التجريبية\nويمكن ان تحدث مثل هذه الأخطاء", message_id=callback.message.message_id)
            bot_c.send_message(idd, "يمكنك استعمال الرابط التالي لاعادة تشغيل البوت\n")
            bot_c.send_message(solo, f"from: {idd}\nproblem: no_res")

        elif callback.data == "edit":
                msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="يمكنك تغير الرسالة\nعلماً انه سيتم ارسال اول رسالة فقط", message_id=callback.message.message_id)
                bot_c.register_next_step_handler(msg, process_else)

        elif callback.data == "send":
            try:
                bot_c.forward_message(solo,callback.message.chat.id,f"{forward[1]}\n{forward[2]}")
                bot_c.delete_message(callback.message.chat.id,callback.message.message_id)
                bot_c.send_message(callback.message.chat.id,"تم تحويل رسالتك الى المطور\n        شكراً لك")
                bot_c.send_message(solo, f"from: {idd}\n{forward[2]}")
                # bot_c.edit_message_text(callback.message.id,"تم ارسال رسالتك الى المطور\nشكراً لك",message_id=callback.message.message_id)
            except Exception as e:
                print(e)
                bot_c.send_message(callback.message.chat.id,f"لقد حصل الخطأ التالي:\n {e}")

        elif callback.data == "mark_error":
            if is_sub[0] == True:
                msg = bot_c.edit_message_text(chat_id=callback.message.chat.id, text="الرجاء ادخال مشكلتك في رسالة واحدة \nعلماً انه سيتم تحويل اول رسالة فقط الى المسؤول", message_id=callback.message.message_id)
                bot_c.register_next_step_handler(msg, process_else)
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                dep2 = types.InlineKeyboardButton('الاشتراك من هنا', url="https://t.me/bot_alamati")
                markup.add(dep2)
                bot_c.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id
                                  , text=f"عذراً انت غير مشترك في قناة البوت\nوهذه الميزة حصرية للمشتركين\nيمكنك الاشتراك ثم المحاولة مرة ثانية\nhttps://t.me/bot_alamati", reply_markup=markup)

@bot_c.message_handler(content_types=['document', 'photo'])
def echo_p(message):
    if message.content_type == 'photo':
        if message.reply_to_message and message.reply_to_message.forward_from:
            bot_c.send_photo(message.reply_to_message.forward_from.id, message.photo[-1].file_id)

    elif message.content_type == 'document':
        if message.reply_to_message and message.reply_to_message.forward_from:
            bot_c.send_document(message.reply_to_message.forward_from.id, message.document.file_id)

@bot_c.message_handler(func=lambda message: True)
def echo_all(message):
    if message.reply_to_message and message.reply_to_message.forward_from:
        if message.chat.id == solo :
            try:
                bot_c.send_message(message.reply_to_message.forward_from.id,
                             f" *لديك رسالة من المطور:*  \n{message.text}",
                             parse_mode='Markdown')
            except Exception as e:
                bot_c.send_message(solo, f"{e}")
        else:
            bot_c.send_message(message.chat.id, "لا يمكنك التواصل مع المطور بهذه الطريقة\nاضغط على /start واتبع الخطوات")
    else:
        bot_c.send_message(message.chat.id, "لا يمكنك التواصل مع المطور بهذه الطريقة\nاضغط على /start واتبع الخطوات")

forward = []
def process_else(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    mes_to = message.id
    forward.clear()
    forward.append(idd)
    forward.append(mes_to)
    forward.append(message.text)
    markup = types.InlineKeyboardMarkup(row_width=2)
    dep1 = types.InlineKeyboardButton('تعديل الرسالة', callback_data="edit")
    dep2 = types.InlineKeyboardButton('ارسال الرسالة', callback_data="send")
    markup.add(dep1, dep2)
    bot_c.reply_to(message ,text="ستم تحويل هذه الرسالة فقط\nيمكنك تعديلها او ارسالها من الازرار",reply_markup=markup)

def sub_now(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('تسجيل طلب الاشتراك', callback_data='confirm')
    dep1 = types.InlineKeyboardButton('باقة علامات الشلة ماكس', callback_data='')
    dep2 = types.InlineKeyboardButton('العودة', callback_data='sub')
    markup.add(dep,dep2)
    bot_c.send_message(idd, "لتسجيل طلب الاشتراك اضغط الزر في الاسفل\nوقم بتفعيل صوت الاشعارات لانه سيتم التواصل معك هنا لاحقاً\n\n\n*ملاحظة:*\nاذا قمت بتسجيل طلب اشتراك ولم تقم باكمال طلبك فسيتم حظرك من استخدام البوت الى الأبد", reply_markup=markup,parse_mode="MarkdownV2")

def subscribe(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('باقة علامات الشلة ', callback_data='shela')
    dep1 = types.InlineKeyboardButton('باقة علامات الشلة ماكس', callback_data='shela_max')
    dep2 = types.InlineKeyboardButton('باقة المشترك المميز', callback_data='prime')
    dep3 = types.InlineKeyboardButton('باقة علامتي برسالة', callback_data='msg')
    markup.add(dep,dep1,dep2,dep3)
    bot_c.send_message(idd, "يمكنك الاشتراك باحدى الباقات التالية:\nاضغط على الباقة التي تريدها لمعرفة جميع التفاصيل", reply_markup=markup)

def shela(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('الاشتراك في الفصل الأول', callback_data='first')
    dep1 = types.InlineKeyboardButton('الاشتراك في العام كامل', callback_data='year')
    dep2 = types.InlineKeyboardButton('العودة', callback_data='sub')
    markup.add(dep,dep1,dep2)
    bot_c.send_message(idd, """*باقة علامات الشلة*:
تمكنك الباقة من البحث عن علامات 5 من أصدقائك في الوقت الذي ترغب علماً انه يمكنك البحث بعدد مرات غير منتهية حتى نهاية اشتراكك
وإن سعر الاشتراك في هذه الخدمة يكون على الشكل التالي:
1     *الفصل الأول* : يبدأ من 1/1/2024 وينتهي ب 1/4/2024
بسعر \(لفترة محدودة\) 5000 ل س بدلاً من ~8000~
2     *الفصل الثاني* : يبدأ من 1/4/2024 وينتهي ب 1/10/2024
بسعر \(لفترة محدودة\) 5000 ل س بدلاً من ~8000~
3     *الفصل التكميلي* : يبدأ من 1/10/2024 وينتهي ب 1/1/2025
بسعر \(لفترة محدودة\) 2000 ل س بدلاً من ~5000~
4     * العام كامل* : يبدأ من 1/1/2024 وينتهي ب 1/1/2025
بسعر \(لفترة محدودة\) 10000 ل س بدلاً من ~15000~
يمكن الآن من الاشتراك في باقات الفصل الأول او العام كامل""", reply_markup=markup, parse_mode="MarkdownV2")

def shela_max(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('الاشتراك في الفصل الأول', callback_data='first')
    dep1 = types.InlineKeyboardButton('الاشتراك في العام كامل', callback_data='year')
    dep2 = types.InlineKeyboardButton('العودة', callback_data='sub')
    markup.add(dep,dep1,dep2)
    bot_c.send_message(idd, """*باقة علامات الشلة ماكس*:
تمكنك الباقة من البحث عن علامات 15 من أصدقائك في الوقت الذي ترغب علماً انه يمكنك البحث بعدد مرات غير منتهية حتى نهاية اشتراكك
وإن سعر الاشتراك في هذه الخدمة يكون على الشكل التالي:
1     *الفصل الأول* : يبدأ من 1/1/2024 وينتهي ب 1/4/2024
بسعر \(لفترة محدودة\) 12000 ل س بدلاً من ~20000~
2     *الفصل الثاني* : يبدأ من 1/4/2024 وينتهي ب 1/10/2024
بسعر \(لفترة محدودة\) 12000 ل س بدلاً من ~20000~
3     *الفصل التكميلي* : يبدأ من 1/10/2024 وينتهي ب 1/1/2025
بسعر \(لفترة محدودة\) 5000 ل س بدلاً من ~10000~
4     * العام كامل* : يبدأ من 1/1/2024 وينتهي ب 1/1/2025
بسعر \(لفترة محدودة\) 20000 ل س بدلاً من ~30000~
يمكن الآن من الاشتراك في باقات الفصل الأول او العام كامل""", reply_markup=markup, parse_mode="MarkdownV2")

def prime(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('الاشتراك في الفصل الأول', callback_data='first')
    dep1 = types.InlineKeyboardButton('الاشتراك في العام كامل', callback_data='year')
    dep2 = types.InlineKeyboardButton('العودة', callback_data='sub')
    markup.add(dep,dep1,dep2)
    bot_c.send_message(idd, """*باقة المشترك المميز*:
تمكنك الباقة من البحث عن علامات *أي شخص تريده بدون حدود*
بالاضافة الى ميزة *البحث عن طريق الاسم*
كما يحصل على خصم على كل المميزات التي سوف تصدر في البوت
علماً انه يمكنك البحث بعدد مرات غير منتهية حتى نهاية اشتراكك
وإن سعر الاشتراك في هذه الخدمة يكون على الشكل التالي:
1     *الفصل الأول* : يبدأ من 1/1/2024 وينتهي ب 1/4/2024
بسعر \(لفترة محدودة\) 30000 ل س بدلاً من ~55000~
2     *الفصل الثاني* : يبدأ من 1/4/2024 وينتهي ب 1/10/2024
بسعر \(لفترة محدودة\) 40000 ل س بدلاً من ~65000~
3     *الفصل التكميلي* : يبدأ من 1/10/2024 وينتهي ب 1/1/2025
بسعر \(لفترة محدودة\) 15000 ل س بدلاً من ~25000~
4     * العام كامل* : يبدأ من 1/1/2024 وينتهي ب 1/1/2025
بسعر \(لفترة محدودة جداً\) 50000 ل س بدلاً من ~100000~
يمكن الآن من الاشتراك في باقات الفصل الأول او العام كامل""", reply_markup=markup, parse_mode="MarkdownV2")

def m_msg(message):
    idd = message.chat.id
    bot_c.send_chat_action(idd,action="typing")
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('الاشتراك في الفصل الأول', callback_data='first')
    dep1 = types.InlineKeyboardButton('الاشتراك في العام كامل', callback_data='year')
    dep2 = types.InlineKeyboardButton('العودة', callback_data='sub')
    markup.add(dep2)
    bot_c.send_message(idd, """*باقة علامتي برسالة*:
تمكنك الباقة من الحصول على علاماتك برسالة فور صدورها
\-\-\-\-\-\-\-\-\-\-\-\- لم يتم تفعيل الباقة بعد \-\-\-\-\-\-\-\-\-\-\-\-""", reply_markup=markup, parse_mode="MarkdownV2")

BOT_TOKEN = "6945336020:AAGBKrRJtzH3vK-bWpnOp9hpr3bdiD_ZMIc"
bot3= telebot.TeleBot(BOT_TOKEN)
user_state = {}

@bot3.message_handler(commands=["start"])
def welcome_3(message):
    idd = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('التواصل مع المطور من هنا', url="t.me/alamati_comments")
    dfp = types.InlineKeyboardButton('الذهاب الى القناة من هنا', url="https://t.me/bot_alamati")
    markup.add(dep, dfp)
    bot3.send_message(idd, """ البوت في فترة صيانة
--------------------------------------------------
لمعرفة موعد التشغيل يرجى الاشتراك في قناة البوت
ويمكنك التواصل مع المطور""", reply_markup=markup)
    marup = types.InlineKeyboardMarkup(row_width=1)
    page = types.InlineKeyboardButton('صفحة الفيس بوك هنا', url="https://facebook.com/mymarks.bot")
    marup.add(page)
    time.sleep(2)
    bot3.send_message(idd, """
رابط صفحة الفيس بوك الخاصة بالبوت
في الصفحة يمكن أن تعرف علاماتك أثناء صيانة البوت
            """, reply_markup=marup)

@bot3.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        welcome_3(callback.message)
@bot3.message_handler(func=lambda m:True)
def reply(message):
        welcome_3(message)



#######

def zkr(bot, idd):
  azkar=[
    "الحمد لله",
    "سبحان الله",
    "لا اله الا الله",
    "الله اكبر",
    "سبحانك اللهم وبحمدك استغفرك واتوب اليك",
    "استغفر الله وأتوب اليه",
    "لا حول ولا قوة الا بالله",
    "لا اله الا الله وحده لا شريك له، له الملك وله الحمد، وهو على كل شيء قدير",
    "لا اله الا الله وحده لا شريك له، له الملك وله الحمد، يحيي ويميت وهو على كل شيء قدير",
    "اللهم اني اسألك علماً نافعاً، ورزقاً طيباً، وعملاً متقبلاً",
    "اللهم أعني على ذكرك وشكرك وحسن عبادتك"
  ]
  link = [
    "رابط قناة البوت\nhttps://t.me/bot_alamati",
    "رابط المجموعة الخاصة بالبوت على تلغرام\nhttps://t.me/alamati_comments",

  ]
  try:
    zkr = f"*لا تنسى ذكر الله*\n{(azkar[random.randint(0,15)])}"
  except:
    links =[
      "رابط صفحة البوت على الفيس بوك\nhttps://www.facebook.com/mymarks.bot/",
      "رابط صفحة البوت على الفيس بوك\nhttps://www.facebook.com/mymarks.bot/",
      "رابط صفحة البوت على الفيس بوك\nhttps://www.facebook.com/mymarks.bot/",
      "رابط قناة تنشر اقتباسات وعبارات حلوة وأشياء مميزة تجدوها بالقناة\nhttps://t.me/hopeforall87",
      "رابط قناة تنشر اقتباسات وعبارات حلوة وأشياء مميزة تجدوها بالقناة\nhttps://t.me/hopeforall87"
    ]
    zkr = (links[random.randint(0,3)])
  bot.send_message(idd,(link[random.randint(0,2)]))
  time.sleep(1)
  bot.send_message(idd,zkr,parse_mode="Markdown")

@bot_face.message_handler(commands=["start"])
def welcome_face(message):
  idd = message.chat.id
  if idd in block:
    bot_face.send_message(
        message.chat.id,
        "عذراً لقد تم حظرك من البوت \nتواصل مع المطور @alamati_info")
  elif idd in admin:
    if idd == fo:
      bot_face.send_message(message.chat.id, "أهلا بحبيبة قلب حسن 😍")
    if f"{idd}_dep" in user_state:
      del user_state[f"{idd}_dep"]
    if f"{idd}_number" in user_state:
      del user_state[f"{idd}_number"]
    if f"{idd}_name" in user_state:
      del user_state[f"{idd}_name"]
    markup = types.InlineKeyboardMarkup(row_width=1)
    dep = types.InlineKeyboardButton('كلية الآداب والعلوم الانسانية',
                                     callback_data='adab')
    dep1 = types.InlineKeyboardButton('كلية العلوم', callback_data='elom')
    markup.add(dep, dep1)
    is_sub.clear()
    is_sub.append(True)
    bot_face.send_message(message.chat.id,
                     """أهلا بكم في بوت علاماتي
البوت يحتوي على علامات كلية الآداب وكلية العلوم
وقريباً سيتم اضافة علامات لكليات أخرى
-------------------------------------
اولا قم باختيار كليك  """,
                     reply_markup=markup)
    clear_chat(bot_face,message)
  else:
    bot_face.send_message(idd,"عذراً غير مسموح لك باستخدام البوت")

nams = []


@bot_face.callback_query_handler(func=lambda call: True)
def answer(callback):
  if callback.message:
    idd = callback.message.chat.id
    department = user_state.get(f"{idd}_dep", {})
    if department == 'اللغة العربية':
      dep = "arabic.csv"
    elif department == 'اللغة الانكليزية':
      dep = "english.csv"
    elif department == 'اللغة الفرنسية':
      dep = "french.csv"
    elif department == 'الجغرافية':
      dep = "geography.csv"
    elif department == 'التاريخ':
      dep = "history.csv"
    elif department == 'الفلسفة':
      dep = "philosophy.csv"
    elif department == 'الآثار':
      dep = "archeology.csv"
    elif department == 'علم الاجتماع':
      dep = "sociology.csv"
    elif department == 'علم الحياة':
      dep = "biology.csv"
    elif department == 'الرياضيات':
      dep = "math.csv"
    elif department == 'الكيمياء':
      dep = "chemistry.csv"
    elif department == 'الفيزياء':
      dep = "physics.csv"
    elif department == 'الجيلوجيا':
      dep = "geology.csv"
    elif department == 'الاحصاء الرياضي':
      dep = "statics.csv"

    if callback.data == 'adab':
      markup = types.InlineKeyboardMarkup(row_width=2)
      arabic = types.InlineKeyboardButton('اللغة العربية',
                                          callback_data='اللغة العربية')
      english = types.InlineKeyboardButton('اللغة الانكليزية',
                                           callback_data='اللغة الانكليزية')
      frensh = types.InlineKeyboardButton('اللغة الفرنسية',
                                          callback_data='اللغة الفرنسية')
      geography = types.InlineKeyboardButton('الجغرافية',
                                             callback_data='الجغرافية')
      history = types.InlineKeyboardButton('التاريخ', callback_data='التاريخ')
      socology = types.InlineKeyboardButton('علم الاجتماع',
                                            callback_data='علم الاجتماع')
      philosophy = types.InlineKeyboardButton('الفلسفة',
                                              callback_data='الفلسفة')
      arch = types.InlineKeyboardButton('الآثار', callback_data='الآثار')

      markup.add(arabic, english, frensh, geography, history, socology,
                 philosophy, arch)

      try:
        bot_face.edit_message_text(
            chat_id=idd,
            message_id=callback.message.message_id,
            text=
            "البوت يحتوي على علامات كلية الآداب منذ 2018\n----------------------------------------------\nما هو قسمك؟",
            reply_markup=markup)
      except Exception as e:
        bot_face.send_message(
            idd,
            "لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد"
        )
        welcome_face(callback.message)
      except:
        print("error")
    if callback.data == 'elom':
      markup = types.InlineKeyboardMarkup(row_width=2)
      arabic = types.InlineKeyboardButton('علم الحياة',
                                          callback_data='علم الحياة')
      english = types.InlineKeyboardButton('الرياضيات',
                                           callback_data='الرياضيات')
      frensh = types.InlineKeyboardButton('الكيمياء', callback_data='الكيمياء')
      geography = types.InlineKeyboardButton('الفيزياء',
                                             callback_data='الفيزياء')
      history = types.InlineKeyboardButton('الجيلوجيا',
                                           callback_data='الجيلوجيا')
      philosophy = types.InlineKeyboardButton('الاحصاء الرياضي',
                                              callback_data='الاحصاء الرياضي')

      markup.add(arabic, english, frensh, geography, history, philosophy)

      try:
        bot_face.edit_message_text(
            chat_id=idd,
            message_id=callback.message.message_id,
            text=
            "البوت يحتوي على علامات كلية العلوم \nللعام 2022/2023 فقط\n----------------------------------------------\nما هو قسمك؟",
            reply_markup=markup)
      except Exception as e:
        bot_face.send_message(
            idd,
            "لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد"
        )
        welcome_face(callback.message)
      except:
        print("error")

    elif callback.data == 'restart':
      try:
        bot_face.delete_message(idd, callback.message.message_id)
      except:
        pass
      welcome_face(callback.message)

    elif callback.data in [
        'اللغة العربية', 'اللغة الانكليزية', 'الفيزياء', 'الجيلوجيا',
        'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة', 'الرياضيات',
        'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة',
        'الآثار'
    ]:
      idd = callback.message.chat.id
      user_state[f"{idd}_dep"] = callback.data
      markup = types.InlineKeyboardMarkup(row_width=1)
      name = types.InlineKeyboardButton('البحث عن طريق الاسم',
                                        callback_data='name')
      number = types.InlineKeyboardButton('البحث عن طريق الرقم',
                                          callback_data='number')
      start = types.InlineKeyboardButton('اختيار قسم جديد',
                                         callback_data='restart')

      markup.add(name, number, start)
      try:
        bot_face.edit_message_text(
            chat_id=idd,
            message_id=callback.message.message_id,
            text=
            f"لقد اخترت : {callback.data}\nهل تريد البحث عن طريق الاسم أم الرقم الجامعي \nعلماً ان علمية البحث عن الاسم قد لا تكون دقيقة دائماً ",
            reply_markup=markup)
      # bot_face.delete_message(chat_id="", message_id = "")
      except Exception as e:
        bot_face.send_message(
            idd,
            f"لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد"
        )
        welcome_face(callback.message)
      except:
        print("error")
    elif callback.data == "number":
      try:
        msg = bot_face.edit_message_text(
            chat_id=callback.message.chat.id,
            text=
            "ادخل رقمك الجامعي\nالرجاء كتابة الارقام باللغة الانكليزية (1234567890)",
            message_id=callback.message.message_id)
        bot_face.register_next_step_handler(msg, process_number)
      except Exception as e:
        bot_face.send_message(
            idd,
            "لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد"
        )
        welcome_face(callback.message)
      except:
        print("error")
    elif callback.data == "name":
      if is_sub[0] == True:
        try:
          msg = bot_face.edit_message_text(chat_id=callback.message.chat.id,
                                      text="ادخل اسمك",
                                      message_id=callback.message.message_id)
          bot_face.register_next_step_handler(msg, process_name)
        except Exception as e:
          bot_face.send_message(
              idd,
              "لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد"
          )
          welcome_face(callback.message)
        except:
          print("error")
      else:
        try:
          msg = bot_face.edit_message_text(
              chat_id=callback.message.chat.id,
              text=
              "انت غير مشترك في القناة @bot_alamati\nوهذه الميزة مخصصة فقط للمشكتركين في القناة\nالرجاء الاشتراك والمحاولة ثانيةً\nt.me/bot_alamati",
              message_id=callback.message.message_id)
        except Exception as e:
          bot_face.send_message(
              idd,
              "لقد حدث الخطأ التالي \n{e}\nفي حال تكرار الخطأ ابعث الخطأ الى المطور\nسيتم الآن البدأ من جديد"
          )
          welcome_face(callback.message)
        except:
          print("error")

    elif callback.data == "name1":
      try:
        name_ch = nams[0][0]
      except Exception as e:
        print(e)
    elif callback.data == "name2":
      try:
        name_ch = nams[0][1]
      except Exception as e:
        print(e)
    elif callback.data == "name3":
      try:
        name_ch = nams[0][2]
      except Exception as e:
        print(e)
    elif callback.data == "name4":
      try:
        name_ch = nams[0][3]
      except Exception as e:
        print(e)
    elif callback.data == "name5":
      try:
        name_ch = nams[0][4]
      except Exception as e:
        print(e)
    if callback.data in ["name1", "name2", "name3", "name4", "name5"]:
      try:
        bot_face.delete_message(chat_id=idd, message_id=callback.message.message_id)
      except:
        pass
      try:
        num, grades, avge = search_name.search(f"{name_ch}", dep)
        print(
            f"{name_ch}  :  {dep}  :  {num}   ...   {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')} ...  {idd}"
        )
        user_state[f"{idd}_name"] = name_ch
        if department in ['الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات']:
          fivty = 60
        else:
          fivty = 50
        mnb = bot_face.send_message(idd,
                               f"""
أهلا بك : ( *{name_ch}* ) رقمك (*{num}*)
يتم الآن البحث عن علاماتك وجمعها
شكراً لانتظارك        """,
                               parse_mode='Markdown')
        time.sleep(2.5)
        bot_face.edit_message_text(f"""
إن الطالب : *{name_ch}* والرقم الجامعي (*{num}*)
قد حصل على العلامات التالية :
            """,
                              idd,
                              mnb.message_id,
                              parse_mode='Markdown')
        time.sleep(1.5)
        f, s, t, fo, z, avg = sort(grades,fivty)
        if f != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الأولى هي:*\n{f}",
                           parse_mode='Markdown')
          time.sleep(2)
        if s != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الثانية هي:*\n{s}",
                           parse_mode='Markdown')
          time.sleep(2)
        if t != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الثالثة هي:*\n{t}",
                           parse_mode='Markdown')
          time.sleep(2)
        if fo != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الرابعة هي:*\n{fo}",
                           parse_mode='Markdown')
          time.sleep(2)
        if z != "":
          bot_face.send_message(idd,
                           f"*علامات المواد الراسبة هي:*\n{z}",
                           parse_mode='Markdown')
          time.sleep(2)
        # bot_face.send_message(idd, f"{grades}\n تم الانتهاء من جمع العلامات")
        if avg != None:
          time.sleep(1)
          bot_face.send_message(idd, f" وبمعدل قدره {avg}")
        time.sleep(2)
        try:
          zkr(bot_face, idd)
          time.sleep(2)
        except:
          pass
        markup = types.InlineKeyboardMarkup(row_width=1)
        dep = types.InlineKeyboardButton('اختيار اسم جديد',
                                         callback_data='restart')
        markup.add(dep)
        bot_face.send_message(idd,
                         """شكراً لاستخدامك بوت علاماتي
------------------------------------------------------------------
يمكنك البحث عن اسم جديد من هنا """,
                         reply_markup=markup)
      except Exception as e:
        markup = types.InlineKeyboardMarkup(row_width=1)
        dep = types.InlineKeyboardButton('اختيار اسم جديد',
                                         callback_data='restart')
        markup.add(dep)
        bot_face.send_message(
            idd,
            f"""حدث خطأ في البحث \nيرجى التواصل مع المسؤول وارفاق الخطأ التالي\n{e}
------------------------------------------------------------------
يمكنك البحث عن اسم جديد من هنا """,
            reply_markup=markup)


def process_name(message):
  idd = message.chat.id
  if user_state.get(f"{idd}_dep", {}) in [
      'اللغة العربية', 'اللغة الانكليزية', 'الفيزياء', 'الجيلوجيا',
      'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة', 'الرياضيات',
      'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة',
      'الآثار'
  ]:
    x = message.text

    department = user_state.get(f"{idd}_dep", {})
    if department == 'اللغة العربية':
      dep = "arabic.csv"
    elif department == 'اللغة الانكليزية':
      dep = "english.csv"
    elif department == 'اللغة الفرنسية':
      dep = "french.csv"
    elif department == 'الجغرافية':
      dep = "geography.csv"
    elif department == 'التاريخ':
      dep = "history.csv"
    elif department == 'الفلسفة':
      dep = "philosophy.csv"
    elif department == 'الآثار':
      dep = "archeology.csv"
    elif department == 'علم الاجتماع':
      dep = "sociology.csv"
    elif department == 'علم الحياة':
      dep = "biology.csv"
    elif department == 'الرياضيات':
      dep = "math.csv"
    elif department == 'الكيمياء':
      dep = "chemistry.csv"
    elif department == 'الفيزياء':
      dep = "physics.csv"
    elif department == 'الجيلوجيا':
      dep = "geology.csv"
    elif department == 'الاحصاء الرياضي':
      dep = "statics.csv"

    x = message.text
    names = search_name.search_names(x, dep)
    nams.clear()
    nams.append(names)
    i = 0
    mark_up = types.InlineKeyboardMarkup(row_width=1)
    for name in names:
      i += 1
      btn = types.InlineKeyboardButton(f"{name}", callback_data=f"name{i}")
      mark_up.add(btn)
    mnb = bot_face.send_message(
        idd,
        f"ان عملية البحث عن الاسم  قد لا تكون دقيقة جداً\nاليك بعض الخيارات الممكنة",
        reply_markup=mark_up)
    time.sleep(3.5)
    try:
       bot_face.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
      print(e)

def process_number(message):
  idd = message.chat.id
  if user_state.get(f"{idd}_dep", {}) in [
      'اللغة العربية', 'اللغة الانكليزية', 'الفيزياء', 'الجيلوجيا',
      'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة', 'الرياضيات',
      'اللغة الفرنسية', 'الجغرافية', 'التاريخ', 'علم الاجتماع', 'الفلسفة',
      'الآثار'
  ]:
    x = message.text
    department = user_state.get(f"{idd}_dep", {})
    if department == 'اللغة العربية':
      dep = "arabic.csv"
    elif department == 'اللغة الانكليزية':
      dep = "english.csv"
    elif department == 'اللغة الفرنسية':
      dep = "french.csv"
    elif department == 'الجغرافية':
      dep = "geography.csv"
    elif department == 'التاريخ':
      dep = "history.csv"
    elif department == 'الفلسفة':
      dep = "philosophy.csv"
    elif department == 'الآثار':
      dep = "archeology.csv"
    elif department == 'علم الاجتماع':
      dep = "sociology.csv"
    elif department == 'علم الحياة':
      dep = "biology.csv"
    elif department == 'الرياضيات':
      dep = "math.csv"
    elif department == 'الكيمياء':
      dep = "chemistry.csv"
    elif department == 'الفيزياء':
      dep = "physics.csv"
    elif department == 'الجيلوجيا':
      dep = "geology.csv"
    elif department == 'الاحصاء الرياضي':
      dep = "statics.csv"

    try:
      x = message.text
      x = int(x)
      name, grades, avge = search_in_csv.search(str(x), dep)
      if name != None:
        print(
            f"{x}  :  {dep}  :  {name}   ...   {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')} ...  {idd}"
        )
        user_state[f"{idd}_num"] = message.text
        mnb = bot_face.send_message(idd, f"جاري البحث عن الرقم ( {x} )")
        time.sleep(1.2)
        msg = bot_face.edit_message_text(f"""
أهلا بك : ( *{name}* )
يتم الآن البحث عن علاماتك وجمعها
شكراً لانتظارك        """,
                                    idd,
                                    mnb.message_id,
                                    parse_mode='Markdown')
        time.sleep(2.5)
        bot_face.edit_message_text(f"""
إن الطالب : *{name}*
قد حصل على العلامات التالية :
            """,
                              idd,
                              msg.message_id,
                              parse_mode='Markdown')
        time.sleep(1.5)
        time.sleep(1.5)
        if department in ['الفيزياء','الجيلوجيا', 'الاحصاء الرياضي', 'الكيمياء', 'علم الحياة','الرياضيات']:
          fivty = 60
        else:
          fivty = 50
        f, s, t, fo, z, avg = sort(grades,fivty)
        if f != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الأولى هي:*\n{f}",
                           parse_mode='Markdown')
          time.sleep(2)
        if s != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الثانية هي:*\n{s}",
                           parse_mode='Markdown')
          time.sleep(2)
        if t != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الثالثة هي:*\n{t}",
                           parse_mode='Markdown')
          time.sleep(2)
        if fo != "":
          bot_face.send_message(idd,
                           f"*علامات السنة الرابعة هي:*\n{fo}",
                           parse_mode='Markdown')
          time.sleep(2)
        if z != "":
          bot_face.send_message(idd,
                           f"*علامات المواد الراسبة هي:*\n{z}",
                           parse_mode='Markdown')
          time.sleep(2)
        if avg != None:
          time.sleep(1)
          bot_face.send_message(idd, f" وبمعدل قدره *{avg}*", parse_mode='Markdown')
        time.sleep(2)
        try:
          zkr(bot_face, idd)
          time.sleep(2)
        except:
          pass
        markup = types.InlineKeyboardMarkup(row_width=1)
        dep = types.InlineKeyboardButton('اختيار رقم جديد',
                                         callback_data='restart')
        markup.add(dep)
        bot_face.send_message(idd,
                         """شكراً لاستخدامك *بوت علاماتي*
------------------------------------------------------------------
يمكنك البحث عن رقم جديد من هنا """,
                         reply_markup=markup,
                         parse_mode='Markdown')
      elif name == None:
        msg = bot_face.send_message(idd, f"الرقم ({x}) غير موجود")
        bot_face.register_next_step_handler(msg, process_number)
      else:
        msg = bot_face.send_message(idd, f"الرقم ({x}) غير موجود")

    except ValueError:
      msg = bot_face.reply_to(message,
                         'هذا ليس رقمًا صالحًا. الرجاء إدخال ارقام فقط')
      bot_face.register_next_step_handler(msg, process_number)
    except Exception as e:
      bot_face.reply_to(
          message,
          f'حدث خطأ ما\nفي حال تكرر الخطأ تواصل مع المطور\nالخطأ: {e} ')
      print(
          f"{e} ... {datetime.datetime.now().strftime('%Y-%m-%d || %H:%M:%S')}  ...  {idd}"
      )
  else:
    bot_face.send_message(idd, "من فضلك اختر قسمًا أولاً.")


thread_b = threading.Thread(target=bot_b.polling)
thread_sh = threading.Thread(target=bot_sh.polling)
thread_m = threading.Thread(target=bot_m.polling)
thread_p = threading.Thread(target=bot_p.polling)
thread_c = threading.Thread(target=bot_c.polling)
thread_ad = threading.Thread(target=bot_ad.polling)
thread_3 = threading.Thread(target=bot3.polling)
thread_face = threading.Thread(target=bot_face.polling)

# print("run_b")
# thread_b.start()
# print("run_sh")
# thread_sh.start()
# print("run_m")
# thread_m.start()
# print("run_P")
# thread_p.start()
# print("run_c")
# thread_c.start()
# print("run_ad")
# thread_ad.start()
# print("run_3")
# thread_3.start()
# print("run_face")
# thread_face.start()

# print("run_b")
# bot_b.polling()
# print("run_ad")
# bot_ad.polling()
try:
    print("run_b")
    thread_b.start()
except:
    try:
        print("run_b")
        thread_b.start()
    except:
        try:
            print("run_b")
            thread_b.start()
        except:
            try:
                print("run_b")
                thread_b.start()
            except:
                try:
                    print("run_b")
                    thread_b.start()
                except:
                    try:
                        print("run_b")
                        thread_b.start()
                    except:
                        print("run_b")
                        thread_b.start()

try:
    print("run_sh")
    thread_sh.start()
except:
    try:
        print("run_sh")
        thread_sh.start()
    except:
        try:
            print("run_sh")
            thread_sh.start()
        except:
            try:
                print("run_sh")
                thread_sh.start()
            except:
                try:
                    print("run_sh")
                    thread_sh.start()
                except:
                    try:
                        print("run_sh")
                        thread_sh.start()
                    except:
                        print("run_sh")
                        thread_sh.start()

try:
    print("run_m")
    thread_m.start()
except:
    try:
        print("run_m")
        thread_m.start()
    except:
        try:
            print("run_m")
            thread_m.start()
        except:
            try:
                print("run_m")
                thread_m.start()
            except:
                try:
                    print("run_m")
                    thread_m.start()
                except:
                    try:
                        print("run_m")
                        thread_m.start()
                    except:
                        print("run_m")
                        thread_m.start()

try:
    print("run_p")
    thread_p.start()
except:
    try:
        print("run_p")
        thread_p.start()
    except:
        try:
            print("run_p")
            thread_p.start()
        except:
            try:
                print("run_p")
                thread_p.start()
            except:
                try:
                    print("run_p")
                    thread_p.start()
                except:
                    try:
                        print("run_p")
                        thread_p.start()
                    except:
                        print("run_p")
                        thread_p.start()

try:
    print("run_ad")
    thread_ad.start()
except:
    try:
        print("run_ad")
        thread_ad.start()
    except:
        try:
            print("run_ad")
            thread_ad.start()
        except:
            try:
                print("run_ad")
                thread_ad.start()
            except:
                try:
                    print("run_ad")
                    thread_ad.start()
                except:
                    try:
                        print("run_ad")
                        thread_ad.start()
                    except:
                        print("run_ad")
                        thread_ad.start()

try:
    print("run_c")
    thread_c.start()
except:
    try:
        print("run_c")
        thread_c.start()
    except:
        try:
            print("run_c")
            thread_c.start()
        except:
            try:
                print("run_c")
                thread_c.start()
            except:
                try:
                    print("run_c")
                    thread_c.start()
                except:
                    try:
                        print("run_c")
                        thread_c.start()
                    except:
                        print("run_c")
                        thread_c.start()
try:
    print("run_face")
    thread_face.start()
except:
    try:
        print("run_face")
        thread_face.start()
    except:
        try:
            print("run_face")
            thread_face.start()
        except:
            try:
                print("run_face")
                thread_face.start()
            except:
                try:
                    print("run_face")
                    thread_face.start()
                except:
                    try:
                        print("run_face")
                        thread_face.start()
                    except:
                        print("run_face")
                        thread_face.start()
try:
    print("run_3")
    thread_3.start()
except:
    try:
        print("run_3")
        thread_3.start()
    except:
        try:
            print("run_3")
            thread_3.start()
        except:
            try:
                print("run_3")
                thread_3.start()
            except:
                try:
                    print("run_3")
                    thread_3.start()
                except:
                    try:
                        print("run_3")
                        thread_3.start()
                    except:
                        print("run_3")
                        thread_3.start()


            