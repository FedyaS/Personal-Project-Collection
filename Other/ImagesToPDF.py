from PIL import Image
import os

x = True


while x:
    print("No spaces please, input 'res' to restart\n")

    tinput = True
    while tinput:
        print("Enter inputs, input 'res' to restart inputs up to this point")
        directory = input("Working Directory\n")
        image = input("File name without number\n")
        extension = input("File extension\n")
        k_pdf_name = input("PDF Name\n")
        a = input("First number\n")
        z = input("Last number\n")
        new_name = input("New Name of OCR pdf\n")
        tinput = False
        klist = [directory, image, extension, k_pdf_name, a, z, new_name]
        for k in klist:
            if k == "res":
                tinput = True

    im = os.path.join(directory, image)
    pdf_name = os.path.join(directory, k_pdf_name)
    pdf_name = pdf_name + ".pdf"

    image_list = []
    image_list_final = []


    for i in range(int(a), int(z)+1):
        image_path = (im + str(i) + extension)
        image_list.append(Image.open(image_path))

    if extension == ".png":
        for image in image_list:
            image_list_final.append(image.convert(mode="RGB"))
    else:
        image_list_final = image_list

    image_list_final[0].save(pdf_name, save_all=True, quality=100, append_images=image_list_final[1:])

    name = new_name + ".pdf"
    dir_com = "cd " + directory
    command = "wsl ocrmypdf " + k_pdf_name + ".pdf" + " " + name

    print(dir_com,"\n", command)

    keep = input("More? Y/N\n")
    if keep == "n" or keep == "N":
        quit()
