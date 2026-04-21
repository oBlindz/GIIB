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

def insert_text_in_image(imagePath, text):
    with Image.open(imagePath) as im:
        draw    = ImageDraw.Draw(im)
        draw.text((540//2,40),text,fill=(0,0,0))
        im.save("drawed_image.jpg")
        im.show()

#receive_inputs_from_terminal()
insert_text_in_image("./Images/image.jpg", "Hello World!")
# Image size: 540, 540
