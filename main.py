from PIL import Image, ImageDraw, ImageFont
x = input("введите номер задания:")

#8.1
def f1():
    filename = 'hb.jpg'
    with Image.open(filename) as img:
        img.load()

    crop_img = img.crop((150, 80, 850, 310))
    crop_img.save(('crop_hb.jpg'))
if x==1:
    f1()

#8.2
def f2():
    p = {'день рождения': 'db.jpg', 'новый год': 'ny.jpg', '8 марта': '8.jpg', '23 февраля': '23.jpg'}
    q = input('Какой праздник?')
    f = p.get(q)
    with Image.open(f) as img:
        img.load()
    img.show()
if x==2:
    f2()

#8.3
def f3():
    img = Image.open('hb.jpg')
    n = input('Кого поздравить?')
    s = 'Happy birthday, ' + n + "!<3"
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype('/Users/Запасной/Desktop/прога/Laba8IAN/ofont.ru_Maki Sans', size=30)
    d.text((100, 100), s, (0, 255, 255), font=f)
    img.save('r.png')
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")
