from PIL import Image

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    img = Image.open(image)
    width, height = img.size

    img = img.resize((width//scale, height//scale))
    width, height = img.size

    ascii = []
    for i in range(height):
        ascii.append(["#"] * width)

    pixel = img.load()
    for i in range(height):
        for j in range(width):
            if sum(pixel[j, i]) == 0:
                ascii[i][j] = "#"
            elif sum(pixel[j, i]) in range(1,100):
                ascii[i][j] = "X"
            elif sum(pixel[j, i]) in range(100,200):
                ascii[i][j] = "%"
            elif sum(pixel[j, i]) in range(200,300):
                ascii[i][j] = "&"
            elif sum(pixel[j, i]) in range(300,400):
                ascii[i][j] = "*"
            elif sum(pixel[j, i]) in range(400,500):
                ascii[i][j] = "+"
            elif sum(pixel[j, i]) in range(500,600):
                ascii[i][j] = "/"
            elif sum(pixel[j, i]) in range(600,700):
                ascii[i][j] = "("
            elif sum(pixel[j, i]) in range(700,750):
                ascii[i][j] = "'"
            else:
                ascii[i][j] = " "
    
    art = open(saveas, "w")

    for row in ascii:
        art.write("".join(row) + "\n")

    art.close()


image = "nonnigcat.png"
# image = "Free!.jpg"
scale = 8
type = "png"
# type = "jpg"
saveas = "nonnigcat.txt"
# saveas = "Free!.txt"

asciiConvert(image, type, saveas, scale)