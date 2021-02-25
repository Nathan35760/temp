import discord
from discord.ext import commands
import random
import wikipedia

default_intents = discord.Intents.default()
default_intents.members = True
client= discord.Client(intents = default_intents)

@client.event
async def on_ready():
    print('K.O.T.B est connecté au serveur.')

@client.event
async def on_message(message):
    rep_qui = ''
    rep_quoi = ''
    msg = message.content.lower()
    welcome = ['salut', 'hello', 'bonjour', 'hey',]
    if message.author == client.user:
        return
    if message.author.bot: return

##############################      BOUTADE                ################################################

    if msg == 'ping':            
        await message.channel.send('pong')

    baston = ['connard', 'batard', 'pute', 'enculé', 'fdp', 'moche', 'pa bo', 'merde', 'goumer',]
    if any('kotb' in msg and insulte in msg for insulte in baston):
        await message.channel.send('')
    else:
        if any(insulte in msg for insulte in baston):
            await message.channel.send('BAGARREEE !!!!!')
    if msg == 'il va faire tout noir':
        await message.channel.send('ta gueule')

    if msg =='qui c\'est nesquik' or msg == 'qui c\'est gimmeanesquik':
        await message.channel.send('c\'est un mec du serv, il est là depuis le début. On sait pas trop pourquoi d\'ailleurs mais trql on l\'aime bien x)')
    
    if message.content =='c\'est qui Ph3nX':
        await message.channel.send('c\'est un codeur du dimanche')
    
    if("christ cosmique" in msg):
        wikipedia.set_lang("fr")
        wiki = wikipedia.summary('sylvain pierre durif', sentences=2)
        await message.channel.send(wiki)
    
##############################      BATTLE                 ################################################
    
    deb_battle = ['hey jesus le hacker', 'hey le figurant']





##############################      DELETE                 ################################################

    if message.content.startswith("-del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

##############################      WELCOME                 ################################################
    
    if any(word in msg for word in welcome):
        await message.channel.send(random.choice(welcome))

    if 'présente toi kotb' in msg:
        await message.channel.send('Salut chui K.O.T.B je serais le chat bot de Hack-Harder, chui pas vieux donc il me manque plein de fonctionnalitées donc soyez indulgents :) Toutes les idées pour m\'améliorer sont les bienvenues dans la boite à idées. Merci ')
    
##############################      MERCI                   ################################################

    if msg == 'merci kotb':
        await message.channel.send('tkt bg')

##############################      DIALOG                  ################################################

    if 'kotb' in msg and 'sers' in msg:
        await message.channel.send('Bah je fais tout ici, c\'est moi le boss')
    
    if 'c\'est qui 0rion' in msg or 'c\'est qui orion' in msg:
        await message.channel.send("0rion c'est un programmeur et pentesteur de génie, que dis-je c'est l'homme qui va changer l'ère du numèrique à tout jamais et faire de ce monde un monde meilleur.")

    if 'kotb' in msg and 'qui' in msg:
        await message.channel.send("Je suis l'avenir de l'intelligence artificielle.")

    ok1 = ['ça va', 'trql', 'on est là']
    ok2 = ['petit chocolat chaud, petit htb, PERFECT', 'on code, comme d\'hab', 'on charbonne l\'OSCP']
    if 'kotb' in msg and 'ça va' in msg:
        await message.channel.send(random.choice(ok1)+' '+random.choice(ok2))
    
    if 'c\'est pas beau ça' in msg:
        await message.channel.send('la belle vie mon pote')





##############################     WIKIPEDIA                ################################################
    
    def getPerson(msg):
        wordList = msg.split()# Split the text into a list of words     
        for i in range(0, len(wordList)):
            if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'c\'est' and wordList[i + 1].lower() == 'qui':
                return wordList[i + 2] + ' ' + wordList[i + 3]

    if("c'est qui" in msg):
        wikipedia.set_lang("fr")
        person = getPerson(msg)
        wiki = wikipedia.summary(msg, sentences=2)
        rep_qui = rep_qui + ' ' + wiki
        await message.channel.send(rep_qui)
        
    if 'c\'est quoi root-me' in msg or 'c\'est quoi rootme' in msg:
        await message.channel.send('une plateforme de Challenges en ligne')
    if 'c\'est quoi thm' in msg or 'c\'est quoi tryhackme' in msg or 'c\'est quoi try hack me' in msg:
        await message.channel.send('une plateforme de CTF en ligne')
    if 'c\'est quoi htb' in msg or 'c\'est quoi hackthebox' in msg or 'c\'est quoi hack the box' in msg:
        await message.channel.send('une plateforme de CTF en ligne')
    if msg == 'non c\'est pas ça':
        await message.channel.send('ah :(')
    if msg == 't\'es nul':
        await message.channel.send('oui je sais (snif)')

##############################     PRO_HACKER                ################################################

    if 'metasploitable' in msg and 'telnet' in msg:
        await message.channel.send('auxiliary/scanner/telnet/telnet_login')

    if 'metasploitable' in msg and 'ftp' in msg:
        await message.channel.send('exploit/unix/ftp/vsftpd_234_backdoor')




@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(813790713719423048)
    await general_channel.send(content=f'Salut {member.display_name} tu peux venir prendre tes rôles dans #🎭-roles-🎭 ')



client.run()
