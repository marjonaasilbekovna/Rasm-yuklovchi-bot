import requests
# #1 - USUL------------------------------------------------------

# #rasm yuklash

print(dir(requests))
response = requests.get("https://images.wallpaperscraft.ru/image/single/bmw_iconic_lights_f82_112222_4096x2560.jpg")

print(response.status_code)
print(response.content)

if response.status_code == 200:
    content = response.content
    # png jpg svg txt mp4 mp3
    with open("car.jpg", "wb") as file:
        file.write(content)
        print("rasm yuklandi")

# # mushuklar bilan rasm
n = input("Qaysi hayvon rasmini kiritasiz dog/cat\n >>> ").lower()

if n == "cat":
    rasm = requests.get(f"https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962_square.jpg")
    print(rasm)
    if rasm.status_code == 200:
        content = rasm.content
        # png jpg svg txt mp4 mp3
        with open("cat.png", "wb") as file:
            file.write(content)
            print("rasm yuklandi")
elif n == "dog":
    rasm = requests.get(f"https://www.youriowalawyers.com/images/blog/iStock-149075263.jpg")
    print(rasm)
    if rasm.status_code == 200:
        content = rasm.content
        # png jpg svg txt mp4 mp3
        with open("dog.png", "wb") as file:
            file.write(content)
            print("rasm yuklandi")




