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

    insert_text_in_image("./image/image.png",name)

def insert_text_in_image(imagePath, nickname):
    with Image.open(imagePath) as im:
        draw    = ImageDraw.Draw(im)

        draw.text((1536//2,200),nickname,font=font,fill=(255,255,255))

        im.save("./out/image.png")
        im.show()

receive_inputs_from_terminal()
# Image size:1536,2048
