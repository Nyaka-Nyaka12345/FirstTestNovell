# Вы можете расположить сценарий своей игры в этом файле.
define config.mouse = {}
define config.mouse["default"] = [ ("gui/cursor/cursor.png", 0,0) ]

# Определение персонажей игры.
define a = Character('аки', color="#FFFFFF")
define ay = Character('аяка', color="#F0FFF0")
define ak = Character('помощник',color="#FFFFFF")

init python:
    path = 'q.txt'
    if renpy.exists(path) == True:
        file = True
    else:
        file = False
init python:
    import os.path
    user = os.getlogin()
screen mousego:
    timer 0.5 action MouseMove(x=940,y=350,duration=0.2) repeat True
label splashscreen:
    scene fon with dissolve
    pause 1
    show text "WnStudio представляет" with dissolve
    pause 2
    show text "новела 'shool life' " with dissolve
    pause 2
    scene fon with dissolve
    pause 1
    return
# Игра начинается здесь:

label start:

    


    stop music fadeout 1

    scene firt_art

    show asistent_normal at left
    show screen mousego
    menu:
        "123":
            hide screen mousego
            "ewfrwef"
        "ewfw":
            hide screen mousego
            "wfwf"


    "привет [user]"
    ak "Здравствуйте, приветствуем вас в новеле 'shool life' "

    ak "вас ждет невероятная романтическая история школьника которому нравятся 3 девочки"

    ak "но кого он выберит зависит только от вас"

    ak "окунитесь в мир этой истории"

    show asistent_ul at left

    ak "желаю вам хорошей игры [user]"

    play music "audio/e.mp3"














    return
