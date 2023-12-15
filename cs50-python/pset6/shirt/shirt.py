import sys
from os.path import splitext

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    if splitext(output_filename)[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    if splitext(input_filename)[1] != splitext(output_filename)[1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open("shirt.png") as shirt_img, Image.open(
            input_filename
        ) as input_img:
            input_img = ImageOps.fit(input_img, shirt_img.size)
            input_img.paste(shirt_img, mask=shirt_img)
            input_img.save(output_filename)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
