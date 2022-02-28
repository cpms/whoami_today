import hoshino
import random
import asyncio
from . import today_data
from datetime import date

sv = hoshino.Service('今天是什么少女')

@sv.on_fullmatch('今天是什么少女')
@sv.on_fullmatch('今日是什么少女')
@sv.on_fullmatch('我今天是什么少女')
@sv.on_fullmatch('我今日是什么少女')
@sv.on_fullmatch('今天我是什么少女')
@sv.on_fullmatch('今日我是什么少女')
async def today(bot, ev):
    user_id = ev.user_id
    msg = f'二次元少女的[CQ:at,qq={ev.user_id}]，长着{get_random(user_id,"kao")}，身高{get_random(user_id,"shinnchou")}，\
{get_random(user_id,"kamiiro")}色{get_random(user_id,"kami")}，{get_random(user_id,"cup")}，瞳孔{get_random(user_id,"hitomiiro")}色，\
{get_random(user_id,"zokusei1")}和{get_random(user_id,"zokusei2")}属性，是{get_random(user_id,"shokugyou")}'
    sv.logger.info(msg)
    await bot.send(ev, msg)


def get_random(user_id,today_type):
    rnd = random.Random()
    myseed = int(date.today().strftime("%y%m%d")) + int(user_id)
    rnd.seed(myseed)
    
    if today_type == 'kao':
        down = 1
        up = len(today_data.kao)
        result = today_data.kao[rnd.randint(down,up)]
    elif today_type == 'kamiiro':
        down = 301
        up = len(today_data.iro) + 300
        myseed += 1
        rnd.seed(myseed)
        result = today_data.iro[rnd.randint(down,up)]
    elif today_type == 'kami':
        down = 101
        up = len(today_data.kami) + 100
        result = today_data.kami[rnd.randint(down,up)]
    elif today_type == 'cup':
        down = 201
        up = len(today_data.cup) + 200
        result = today_data.cup[rnd.randint(down,up)]
    elif today_type == 'hitomiiro':
        down = 301
        up = len(today_data.iro) + 300
        result = today_data.iro[rnd.randint(down,up)]
    elif today_type == 'zokusei1':
        down = 401
        up = len(today_data.zokusei) + 400
        result = today_data.zokusei[rnd.randint(down,up)]
    elif today_type == 'zokusei2':
        down = 401
        up = len(today_data.zokusei) + 400
        myseed += 1
        rnd.seed(myseed)
        result = today_data.zokusei[rnd.randint(down,up)]
    elif today_type == 'shokugyou':
        down = 501
        up = len(today_data.shokugyou) + 500
        result = today_data.shokugyou[rnd.randint(down,up)]
    elif today_type == 'shinnchou':
        down = 140
        up = 180
        result = str(rnd.randint(down,up))
    return result
