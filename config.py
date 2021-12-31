import discord
from discord.ext import commands
import os, sqlite3

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@bot.event # Когда бот успешно запускается без ошибок, это пишется в командной строке.
async def on_ready():
	print('Бот успешно запустился.')

	global base, cur
	base = sqlite3.connect('Databasebot.db') # База данных, которая потребуется.
	cur = base.cursor()
	if base:
		print('Успешно было подключено к DataBase c:')

@bot.event # Бот приветствует нового участника сервера в личные сообщение.
async def on_member_join(member):
	await member.send('Добро пожаловать на сервер whats happening! я рад, что ты с нами.')

@bot.command() # Проверка бота в дискорде. .bon
async def bon(ctx):
	await ctx.send('Раскуриться бы, раскумариться.')

@bot.command() # Что-то типо хелпа, потом переделаю красивее.
async def b(ctx, arg=None):
	author = ctx.message.author
	if arg == None:
		await ctx.send(f'🌸{author.mention} введите:\n!b bot\n!b comm\n!b version')
	elif arg == 'bot':
		await ctx.send(f'{author.mention} Наше вам здравствуйте! я бот который будет наказывать по правилам, если не хочешь поймать маслину, будь аккуратен.')
	elif arg == 'comm':
		await ctx.send(f'{author.mention} команды бота:\n.bon - проверка бота в сети.\n')
	elif arg == 'version':
		await ctx.send(f'{author.mention} ```Версия бота: 1.0.0.\nБот создан:30.12.2021```')
	elif arg == 'hackstalcraft':
		await ctx.send(f'{author.mention} ты шо дурак?')
	else:
		await ctx.send(f'{author.mention} такой команды нет.')

async def on_message(message): # Когда участник присылает пункт - бот ему присылает правила как не странно.
	if '1.1' in message.content.lower():
		await message.channel.send('```· Запрещено рекламировать посторонние Discord сервера без согласии администрации.```')
	if '1.2' in message.content.lower():
		await message.channel.send('```· Запрещено использовать другую учетную запись чтобы избежать наказаниe.```')
	if '1.3' in message.content.lower():
		await message.channel.send('```· Запрещено распространять личную информацию участников сервера.```')
	if '1.4' in message.content.lower():
		await message.channel.send('```· Запрещен флуд/спам во всех каналах кроме #flood. Также запрещено использовать капс.```')
	if '1.5' in message.content.lower():
		await message.channel.send('```· Запрещено "тегать" роли сервера/саппортов/администраторов без смысловой нагрузки.```')
	if '1.6' in message.content.lower():
		await message.channel.send('```· Запрещено всячески оскорблять участников сервера(вне) а также оскорблять родных.```')
	if '1.7' in message.content.lower():
		await message.channel.send('```· Запрещено разжигание национальной розни, дискриминация, враждебность к религиям и людям с ограниченными возможностями.```')
	if '1.8' in message.content.lower():
		await message.channel.send('```· Запрещена пропаганда наркотиков также терроризма либо материал содержащий сексуальный характер.```')
	if '1.9' in message.content.lower():
		await message.channel.send('```· Запрещена неконструктивная критика по отношению к серверу, призыв покинуть сервер, критика к администрации либо оскорбление самого сервера.```')
	if '2.0' in message.content.lower():
		await message.channel.send('```· Запрещено использовать музыкальные команды во всех каналах кроме #❍🧬commands-dj.```')
	if '2.1' in message.content.lower():
		await message.channel.send('```· Запрещено использовать посторонние ПО для изменение своего голоса.```')
	if '2.2' in message.content.lower():
		await message.channel.send('```· Запрещено использовать ненастроенный микрофон, перед тем как вы зашли на сервер и хотите общаться, удостоверьтесь, правильно ли настроен ваш микрофон.```')
	if '2.3' in message.content.lower():
		await message.channel.send('```· Запрещено намеренное усиление чувствительности своего микрофона с помощью посторонних ПО/усиление чувствительности дБ ради вреда других участников.```')
	if '2.4' in message.content.lower():
		await message.channel.send('```· Запрещено флудить словами в голосовых категориях т.е всячески мешать геймплею.```')
	await bot.process_commands(message)

@bot.command(pass_context = True) # Система очистки сообщений.
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 500):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'{ctx.author.mention}, было удалено {amount} сообщений.')

@bot.command(pass_context=True) # Система киков.
@commands.has_permissions(administrator = True)
async def kick(ctx,member:discord.Member,*,reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'{ctx.author.mention}, участник успешно выгнан.')

@bot.command(pass_context=True) # Система банов.
@commands.has_permissions(administrator = True)
async def ban(ctx,member:discord.Member,*,reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'{ctx.author.mention}, участник успешно забанен.')

bot.run(os.getenv('TOKEN'))