# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define witcher = Character('Геральт', color="#b50c0f")
define yen = Character('Йеннифер', color="#53304a")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene landscape_1
    with fade

    "Однажды встретились Ведьмак и Чародейка в баре"
    
    
    show geralt
    with dissolve
    

    witcher " Любовь и кровь. В них могучая сила. Маги и учёные не первый год ломают себе над этим головы, но поняли только одно…"

    witcher "Любовь должна быть истинной."

    show geralt at left

    show yen at right
    with dissolve

    yen "Ему больше не наливать"

    return
