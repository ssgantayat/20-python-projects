from PIL import Image

def resize_image(size1, size2):
    image = Image.open('C:/Users/Chase/Desktop/python_20/image_resizer/codewithtomi-logo.jpg')

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('codewithtomi-logo-'+ str(size1) +'.jpeg')

size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2)