
from PIL import Image, ImageDraw, ImageFont
import os
import asyncio
import config

class DrawScreen:

    def __init__(self):
        self.leverage_font  = ImageFont.truetype("main/fonts/Fontspring-DEMO-neuevektor-a-book.ttf",30)
        self.coin_font = ImageFont.truetype("main/fonts/DMCAPS.TTF",30)
        self.res_font = ImageFont.truetype("main/fonts/DMCAPS.TTF",95)
        self.prices = ImageFont.truetype("main/fonts/DMCAPS.TTF",35)
        self.percent = ImageFont.truetype("main/fonts/GolosText-Regular.ttf",95)
        self.srok_font = ImageFont.truetype("main/fonts/GenerischSans-SemiBold.ttf",30)
        self.green_color = (40,191,132,255)
        self.red_color = (221,77,108,255)
        self.orange_color = (212,174,9,255)
        self.sell_buy_font = ImageFont.truetype("main/fonts/FFNort-Regular.ttf",25)


    def is_int(self,str):
        try:
            int(str)
            return True
        except ValueError:
            return False
        
    def is_number(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False



    def drawscreen(self,data, chat_id):
        image = Image.open("main/images/image.png")
        drawer = ImageDraw.Draw(image)
        coin_name = data['pair']
        type = data['type']
        leverage = (data['leverage'])
        str_leverage = (data['leverage']) + 'x'
        entry = (data['entry_price'])
        take = (data['current_price'])
        
        if type == 'long': 
            res = (float(take) - float(entry)) / (float(entry) / 100) * int(leverage)

        else:
            res = (float(entry) - float(take)) / (float(entry) / 100) * int(leverage)


        if len(str(res)) > 5:
            new_res = ''
            list = []
            for i in range(5):
                list.append(str(res)[i])
            
            if list[-1] == '.':
                list.pop(-1)
                   
            for i in list:
                new_res += i 
            res = new_res

        #draw type
        if type == 'short':
            drawer.text((145, 185), "Продать", font=self.sell_buy_font, fill= self.red_color)
        elif type == 'long':
            drawer.text((145, 185), "Купить", font=self.sell_buy_font, fill= self.green_color)

        #draw leverage
        if len(str(str_leverage)) == 2:
            drawer.text((338, 182), str_leverage, font=self.leverage_font, fill='white')

        if len(str(str_leverage)) == 3:
            drawer.text((338, 182), str_leverage, font=self.leverage_font, fill='white')

        
        elif len(str(str_leverage)) == 4:
            drawer.text((334, 182), str_leverage, font=self.leverage_font, fill='white')

                
        elif len(str(str_leverage)) == 5:
            drawer.text((328, 182), str_leverage, font=self.leverage_font, fill='white')



        #draw coin_name 
        if len(str(coin_name)) == 6:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((570, 190), "Бессрочный", font=self.srok_font, fill='white')

        if len(str(coin_name)) == 7:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((590, 190), "Бессрочный", font=self.srok_font, fill='white')

        elif len(str(coin_name)) == 8:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((600, 190), "Бессрочный", font=self.srok_font, fill='white')

        elif len(str(coin_name)) == 9:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((610, 190), "Бессрочный", font=self.srok_font, fill='white')

        elif len(str(coin_name)) == 10:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((620, 190), "Бессрочный", font=self.srok_font, fill='white')

        #draw persent
        if len(str(res)) == 2:
            drawer.text((150, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((325, 215), "%", font=self.percent, fill=self.green_color) 

        elif len(str(res)) == 3:
            drawer.text((150, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((370, 215), "%", font=self.percent, fill=self.green_color) 

        elif len(str(res)) == 4:
            drawer.text((120, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((390, 215), "%", font=self.percent, fill=self.green_color) 

        elif len (str(res)) == 5:
            drawer.text((120, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((420, 215), "%", font=self.percent, fill=self.green_color) 

        #draw entry and take price
        drawer.text((410, 330), entry, font=self.prices, fill=self.orange_color) 
        drawer.text((410, 370), take, font=self.prices, fill=self.orange_color) 

        image = image.convert('RGB')
        image.save(f'main/images/{chat_id}_img.jpg')

    def delete_screen(self, chat_id):
        path = f'D:\Python\screenshotercrypto-main\main\images\{chat_id}_img.jpg' 
        os.remove(path)        