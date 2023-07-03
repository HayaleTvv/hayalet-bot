# import all the packages we will need
from email import utils
from highrise import BaseBot, Highrise, Position
from highrise.models import SessionMetadata, User
from highrise import __main__
from asyncio import run as arun
from highrise import User, BaseBot
from highrise.models import User, Position
import random
import time
import aioconsole
import os
import asyncio
import eventlet


class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot Aktif")

        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(18, 0, 14, "FrontLeft")))

    async def on_user_join(self, user: User) -> None:
        
        print(f"{user.username} Sektöre Katıldı")
        giriş_mesaj = [f"\nHayaleTrnin Odasına Hoşgeldin Bot Komutları Botun Biografisinde Yazıyor \n{user.username}", f"\nDostum Hoşgeldin Destek Olmak İçin Tipse Gönlünden Ne Koparsa \n{user.username}"]
        random_word = random.choice(giriş_mesaj)
        await self.highrise.chat(f"{random_word}")
    
    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} Sektörden ayrıldı")
        await self.highrise.chat(f"Kendine İyi Bak Görürüşürüz , {user.username}!")   
    
    async def on_chat(self, user: User, message: str) -> None:
             
        if message.startswith("!yt"):
            word_list = ["\nYazı Geldi!💲\nHelal Lan", "Tura Geldi!💲\nAtatürkün yüzü yere gelmez"]
            random_word = random.choice(word_list)
            await self.highrise.chat(f"\nPara Atıldı Ve Düşüyor💸")
            await asyncio.sleep(3)
            await self.highrise.chat(f"{random_word}")
        
        if message.startswith("!dc"):
            seçim_listesi = ["\nDoğruluk geldi!\nDoğru söyle!\nYalan söylemek yasak!", "\nCesaret geldi!\nNe görev verilirse yapacaksın!\nCaymak yok düzgün oyna!"]
            random_word = random.choice(seçim_listesi)
            await self.highrise.chat(f"\nŞişe Dönüyor 🧴 Bekleyin Lütfen")
            await asyncio.sleep(3)
            await self.highrise.chat(f"{random_word}")

#burdaki komutlarda sıkıntı var çözmek gerek
        if message.startswith("!dedektif"):
            word_list = ["Elma", "Muz", "Portakal", "Üzüm", "Karpuz"]
            random_word = random.choice(word_list)
            scrambled_word = ''.join(random.sample(random_word, len(random_word)))

            await self.highrise.chat(f"Dedektif Oyununa Hoşgeldin\nÇözmen Gereken Kelime: {scrambled_word}")

            user_guess = ""

            while True:
                user_guess = await aioconsole.ainput(f"")
                if user_guess == random_word:
                    await self.highrise.chat(f"Tebrikler, {user.username}! Kelimeyi Çözdün")
                    break
                else:
                    await self.highrise.chat(f"Yanlış Cevap, {user.username}. Tekrar Dene!")
#burdaki komutlarda sıkıntı var çözmek gerek

        if message.startswith("!t-ç"):
            word_list = ["1 TEK", "2 ÇİFT", "3 TEK", "4 ÇİFT", "5 TEK", "6 ÇİFT", "7 TEK", "8 ÇİFT", "9 TEK", "10 ÇİFT", "11 TEK", "12 ÇİFT", "13 TEK", "14 ÇİFT", "15 TEK"]
            random_word = random.choice(word_list)
            await self.highrise.chat(f"\nZar 🎲Dönüyor Lütfen Bekleyin")
            await asyncio.sleep(3)

            await self.highrise.chat(f"{random_word}")
                    
        if message.lower().startswith("!tkm"):
            choices = ['taş', 'kağıt', 'makas']
            client_chosen = random.choice(choices)
            option = message[5:].strip().lower()

            text_to_emoji = {"taş": "✊", "kağıt": "✋", "makas": "✌️"}
            if option not in choices:
                response = f"Invalid command usage:\nExample: !tkm <{client_chosen}>\nAvailable Options:\n{', '.join(choices)}"
                await self.highrise.send_whisper(user.id, response)
                return
            elif option == client_chosen:
                response = "Hiçkimse Kazanamadı Beraberlik 🤝"
            elif (option == "taş" and client_chosen == "makas") or (option == "kağıt" and client_chosen == "taş") or (option == "makas" and client_chosen == "kağıt"):
                response = f"\nHelal lan Kazandın! 🎉\nSen: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"
            else:
                response = f"\nKaybettin 😢\nSen: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"

            await self.highrise.chat(response)
        
        #Burdan Sonrası Konuşma Metin Ekleme Kısımı


        if message.startswith("!31"):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-laughing", roomUser.id)

        if message.startswith("!ağla"):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sad", roomUser.id)

        print(f"{user.username} said: {message}")
        if message.startswith("!kumar"):
            await self.highrise.chat(f"Kumar İçin Tipse Min50 Max500 Gold Atacaksın Tek Çift Diye Seçim Yapacağız Kazanırsan 2Katı Senindir! {user.username}")
        if message.startswith("Sa"):
            await self.highrise.chat(f"Aleyküm Selam Cano")
        if message.startswith("sa"):
            await self.highrise.chat(f"Aleyküm Selam Cano")
        if message.startswith("mik"):
            await self.highrise.chat(f"Önce selam ver sonra yaşını söyle ona göre mikrafon verelim")
        if message.startswith("Mik"):
            await self.highrise.chat(f"Önce selam ver sonra yaşını söyle ona göre mikrafon verelim")
        if message.startswith("!tips"):
            await self.highrise.chat(f"Tipse 3 5 Bişe Atında Gönlümüz Hoş Olsun")
        if message.startswith("!play"):
            await self.highrise.chat(f"If Tips For Gambling, You Will Throw Min50 Max500 Gold. We Will Choose One Pair If You Win, Double Yours!")
        if message.startswith("!bot-com"):
            await self.highrise.chat(f"Bot Komutları Biografimde Mevcut")
        
        
        

        #Burdan Sonrası Tekli Emotlar İçin
        if message.startswith("?float"):
            await self.highrise.send_emote("emote-float", user.id)
        if message.startswith("?snowangel"):
            await self.highrise.send_emote("emote-snowangel", user.id)
        if message.startswith("?teleporting"):
            await self.highrise.send_emote("emote-teleporting", user.id)
        if message.startswith("?swordfight"):
            await self.highrise.send_emote("emote-swordfight", user.id)
        if message.startswith("?pose3"):
            await self.highrise.send_emote("emote-pose3", user.id)
        if message.startswith("?energyball"):
            await self.highrise.send_emote("emote-energyball", user.id)
        if message.startswith("?cute"):
            await self.highrise.send_emote("emote-cute", user.id)
        if message.startswith("?shoppingcart"):
            await self.highrise.send_emote("dance-shoppingcart", user.id)
        if message.startswith("?singing"):
            await self.highrise.send_emote("idle_singing", user.id)
        if message.startswith("?lust"):
            await self.highrise.send_emote("emote-lust", user.id)
        if message.startswith("?pose7"):
            await self.highrise.send_emote("emote-pose7", user.id)
        if message.startswith("?tiktok9"):
            await self.highrise.send_emote("dance-tiktok9", user.id)
        if message.startswith("?telekinesis"):
            await self.highrise.send_emote("emote-telekinesis", user.id)
        if message.startswith("?curtsy"):
            await self.highrise.send_emote("emote-curtsy", user.id)
        if message.startswith("?superpose"):
            await self.highrise.send_emote("emote-superpose", user.id)
        if message.startswith("?model"):
            await self.highrise.send_emote("emote-model", user.id)
        if message.startswith("?pose1"):
            await self.highrise.send_emote("emote-pose1", user.id)
        if message.startswith("?tiktok8"):      
            await self.highrise.send_emote("dance-tiktok8", user.id)
        if message.startswith("?tiktok2"):
            await self.highrise.send_emote("dance-tiktok2", user.id)
        if message.startswith("?tiktok10"):
            await self.highrise.send_emote("dance-tiktok10", user.id)
        if message.startswith("?pose5"):
            await self.highrise.send_emote("emote-pose5", user.id)
        if message.startswith("?pose8"):
            await self.highrise.send_emote("emote-pose8", user.id)
        if message.startswith("?flex"):
            await self.highrise.send_emote("emoji-flex", user.id)
        if message.startswith("?curtsy"):
            await self.highrise.send_emote("emote-curtsy", user.id)
        if message.startswith("?greedy"):
            await self.highrise.send_emote("emote-greedy", user.id)
        if message.startswith("?snake"):
            await self.highrise.send_emote("emote-snake", user.id)
        if message.startswith("?russian"):
            await self.highrise.send_emote("dance-russian", user.id)
        if message.startswith("?charging"):
            await self.highrise.send_emote("emote-charging", user.id)
        if message.startswith("?pennywise"):
            await self.highrise.send_emote("dance-pennywise", user.id)
        if message.startswith("?snowball"):
            await self.highrise.send_emote("emote-snowball", user.id)
        if message.startswith("?bow"):
            await self.highrise.send_emote("emote-bow", user.id)
        if message.startswith("?hot"):
            await self.highrise.send_emote("emote-hot", user.id)
        if message.startswith("?weird"):
            await self.highrise.send_emote("dance-weird", user.id)
        if message.startswith("?gagging"):
            await self.highrise.send_emote("emoji-gagging", user.id)
        if message.startswith("?blackpink"):
            await self.highrise.send_emote("dance-blackpink", user.id)
        if message.startswith("?ateş"):
            await self.highrise.send_emote("idle-enthusiastic", user.id)
        if message.startswith("?frog"):
            await self.highrise.send_emote("emote-frog", user.id)
        if message.startswith("?casual"):
            await self.highrise.send_emote("idle-dance-casual", user.id)
        if message.startswith("?thumbsup"):
            await self.highrise.send_emote("emoji-thumbsup", user.id)
        if message.startswith("?zombi"):
            await self.highrise.send_emote("emote-zombierun", user.id)
        if message.startswith("?maniac"):
            await self.highrise.send_emote("emote-maniac", user.id)
        if message.startswith("?blackpink"):
            await self.highrise.send_emote("dance-blackpink", user.id)
      
        #Tepkiler Burdan Aşşağıya
        
        if message.startswith("❤"):
            await self.highrise.react("heart", user.id)
        if message.startswith("Sa"):
            await self.highrise.react("wave", user.id)
        if message.startswith("👏"):
            await self.highrise.react("clap", user.id)
        if message.startswith("👍"):
            await self.highrise.react("thumbs", user.id)
        if message.startswith("😉"):
            await self.highrise.react("wink", user.id)
        
        #Yetkiler Burdan Aşşağıya
        if message.startswith("Cüzdan"):
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"Cebimde Şuan {wallet[0].amount} {wallet[0].type} Var")          
            
    async def run(self, room_id, token) -> None:
        await __main__.main(self, room_id, token)
    
if __name__ == "__main__":
    room_id = "62745c19de27dba803bbb515"
    token = "e218cb211bd00aeb42983138c15fefd80bc52142fc728374ce58008881cf49ec"
    arun(Bot().run(room_id, token))