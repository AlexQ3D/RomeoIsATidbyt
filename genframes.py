
decl = "img{0} = http.get('https://github.com/AlexQ3D/RomeoIsATidbyt/blob/main/frames/tvman{0}.jpg?raw=true').body()"

for i in range(1, 7):
    print(decl.format(i))