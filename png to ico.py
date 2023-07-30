from PIL import Image

def convert_to_ico(input_path):
    try:
        img = Image.open(input_path)
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        ico_path = input_path.replace(".png", ".ico")
        img.save(ico_path, format="ICO")
        print("Conversion completed. ICO file saved at:", ico_path)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    file_path = input("Enter the image file path: ")
    convert_to_ico(file_path)
