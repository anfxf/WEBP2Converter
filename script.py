import os
from PIL import Image

def WEBP_TO_PNG(import_path):
    try:
        import_paths = os.listdir(import_path)
        for img in import_paths:
            image_webp = import_path + img
            name = " ".join(img.split(".")[:-1])
            ext = "".join(img.split(".")[-1])
            if (ext == "webp"):
                image_png = name + ".png"
                im = Image.open(image_webp)
                im.save("./Export/"+image_png, format="png", lossless=True)
            else:
                print(ext, "- NO NEED TO CONVERT")
    except Exception as e:
        print(e)

def WEBP_TO_JPG(import_path):
    try:
        import_paths = os.listdir(import_path)
        for img in import_paths:
            image_webp = import_path + img
            name = " ".join(img.split(".")[:-1])
            ext = "".join(img.split(".")[-1])
            if (ext == "webp"):
                image_png = name + ".jpeg"
                im = Image.open(image_webp)
                im.save("./Export/"+image_png, format="jpeg")
            else:
                print(ext, "- NO NEED TO CONVERT")

    except WindowsError as winError:
        print(winError)
        pass
    
    except Exception as e:
        print(e)

def Program():
    print("JPG OR PNG")
    choice = input(":> ").lower()
    print(choice)
    imports = input("Webp Folder Path: ")
    if(choice == "jpg"):
        WEBP_TO_JPG(imports)
    elif choice == "png":
        WEBP_TO_PNG(imports)
    else:
        print("Invalid Choice, Type Exactly 'PNG' OR 'JPG'")


if __name__ == "__main__":
    Program()