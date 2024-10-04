import os

print(os.getcwd())

# os.rename("pngimages/txtfile.txt", "pngimages/10.txt")

files = os.listdir("pngimages")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"pngimages/{file}", f"pngimages/{i}.png")
        i = i + 1

files = os.listdir("pngimages")
