# Image size: 1536px, 2048px
from PIL import Image, ImageDraw, ImageFont 

def receive_inputs_from_terminal():
    name        = input("Insert your nickname: ")
    kills       = int(input("Insert your kills: "))
    assists     = int(input("Insert your assistances: "))
    deaths      = int(input("Insert your deaths: "))
    rounds_win  = int(input("Insert your rounds win: "))
    rounds_lose = int(input("Insert your rounds lose: "))
    processing_match_stats(name, kills, assists, deaths, rounds_win, rounds_lose)

def processing_match_stats(name, kills, assists, deaths, rounds_win, rounds_lose):
    kdr     = round(kills/deaths,2)
    dpr     = round(deaths/(rounds_win+rounds_lose),2)
    kpr     = round(kills/(rounds_win+rounds_lose),2)
    rating  = round(((kdr*0.5)+(kpr-dpr))/(rounds_win+rounds_lose),2)

    insert_text_in_image("./image/image.png",name,kdr,kpr,dpr,rating)

def insert_text_in_image(imagePath, nickname,kdr,kpr,dpr,rtg):
    with Image.open(imagePath) as im:
        draw            = ImageDraw.Draw(im)
        nickname_font   = ImageFont.truetype("./Roboto/Roboto-VariableFont_wdth,wght.ttf",110)
        stats_font      = ImageFont.truetype("./Roboto/Roboto-VariableFont_wdth,wght.ttf",80)
        rating_font     = ImageFont.truetype("./Roboto/Roboto-VariableFont_wdth,wght.ttf",110)

        draw.text((250,250),nickname,font=nickname_font,fill=(255,255,255))
        draw.text((800,650),f"KDR: {kdr}",font=stats_font,fill=(255,255,255))
        draw.text((800,920),f"KPR: {kpr}",font=stats_font,fill=(255,255,255))
        draw.text((800,1180),f"DPR: {dpr}",font=stats_font,fill=(255,255,255))        
        draw.text((620,1750),f"RATING: {rtg}",font=rating_font,fill=(255,255,255))

        im.save("./out/image.png")
        im.show()

receive_inputs_from_terminal()
