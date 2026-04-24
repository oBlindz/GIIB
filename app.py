# Image size: 1536px, 2048px
from PIL import Image, ImageDraw, ImageFont 

class NegativeNumberError(Exception):
    pass

def receive_inputs_from_terminal():
    name        = input("Insert your nickname: ")
    kills       = int(input("Insert your kills: "))
    assists     = int(input("Insert your assistances: "))
    deaths      = int(input("Insert your deaths: "))
    points      = int(input("Insert your points: "))
    rounds_win  = int(input("Insert your rounds win: "))
    rounds_lose = int(input("Insert your rounds lose: "))
    processing_match_stats(name.upper(),kills,assists,deaths,points,rounds_win,rounds_lose)

def processing_match_stats(name,kills,assists,deaths,points,rounds_win,rounds_lose):
    image_path  = "./image/image.png"

    try:
        if (kills<0 or assists<0 or deaths<0 or points<0 or rounds_win<0 or rounds_lose<0):
            raise NegativeNumberError("The number should be greater than 0")

        kdr     = round(kills/deaths,2)
        dpr     = round(deaths/(rounds_win+rounds_lose),2)
        kpr     = round(kills/(rounds_win+rounds_lose),2)
        diff    = kills - deaths
        rating  = round((((diff+assists*0.5+points)/2+(kpr-dpr))/(rounds_win+rounds_lose)),2)
    
        insert_text_in_image(image_path,name,kdr,kpr,dpr,rating)
    except NegativeNumberError as event:
        print(f"Error: {event}")

def insert_text_in_image(image_path,nickname,kdr,kpr,dpr,rtg):
    with Image.open(image_path) as im:
        font_path       = "./Roboto/Roboto-VariableFont_wdth,wght.ttf"
        draw            = ImageDraw.Draw(im)
        nickname_font   = ImageFont.truetype(font_path,110)
        stats_font      = ImageFont.truetype(font_path,80)
        rating_font     = ImageFont.truetype(font_path,110)

        draw.text((250,250),nickname,font=nickname_font,fill=(255,255,255))
        draw.text((800,650),f"KDR: {kdr}",font=stats_font,fill=(255,255,255))
        draw.text((800,920),f"KPR: {kpr}",font=stats_font,fill=(255,255,255))
        draw.text((800,1180),f"DPR: {dpr}",font=stats_font,fill=(255,255,255))        
        draw.text((620,1750),f"RATING: {rtg}",font=rating_font,fill=(255,255,255))

        im.save("./out/image.png")
        im.show()

receive_inputs_from_terminal()
