import os
import random
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

current_quiz = {}

quiz_data = [
    {"question": "パンはパンでも、食べられないパンはなーんだ？", "answer": "フライパン", "hint": "キッチンで使うよ"},
    {"question": "穴がたくさん空いているのに、水をためられるものってなーんだ？", "answer": "スポンジ", "hint": "お風呂や台所で使うことが多いよ"},
    {"question": "口はあるのに、しゃべれないものってなーんだ？", "answer": "やかん", "hint": "お湯をわかすよ"},
    {"question": "目はあるのに、前が見えないものってなーんだ？", "answer": "サイコロ", "hint": "ゲームで使うことがあるよ"},
    {"question": "冷蔵庫の中にいる動物ってなーんだ？", "answer": "ゾウ", "hint": "れい『ぞう』こ"},
    {"question": "朝になると出てきて、夜になるといなくなるものってなーんだ？", "answer": "太陽", "hint": "空にあるよ"},
    {"question": "叩いても痛くないし、むしろ喜ばれるものってなーんだ？", "answer": "拍手", "hint": "パチパチするやつ"},
    {"question": "食べる前に必ず割られるものってなーんだ？", "answer": "たまご", "hint": "料理によく使う"},
    {"question": "一日中立っているのに、足がしびれないものってなーんだ？", "answer": "電柱", "hint": "道ばたにある"},
    {"question": "お風呂に入ると小さくなるものってなーんだ？", "answer": "せっけん", "hint": "体を洗うとき使う"}
]

@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")

@bot.command()
async def nazo(ctx):
    quiz = random.choice(quiz_data)
    current_quiz[ctx.guild.id] = quiz
    await ctx.send(f"🎉 なぞなぞ！\n\n{quiz['question']}\n\n答えがわかったらチャットでどうぞ！")

@bot.command()
async def hint(ctx):
    quiz = current_quiz.get(ctx.guild.id)
    if not quiz:
        await ctx.send("先に !nazo で問題を出してね！")
        return
    await ctx.send(f"💡 ヒント：{quiz['hint']}")

@bot.command()
async def answer(ctx):
    quiz = current_quiz.get(ctx.guild.id)
    if not quiz:
        await ctx.send("先に !nazo で問題を出してね！")
        return
    await ctx.send(f"✅ 答え：{quiz['answer']}")
    del current_quiz[ctx.guild.id]

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN が設定されてないよ！ RailwayのVariablesに入れてね。")

bot.run(TOKEN)
