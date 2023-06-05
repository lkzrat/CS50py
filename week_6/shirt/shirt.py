from PIL import Image, ImageOps
import sys

def main():
    img_transform(get_file())

def img_transform(old):
    try:
        with Image.open('shirt.png') as mask, Image.open(old[0]) as file:
            file0 = ImageOps.fit(mask, (600, 600))
            file1 = ImageOps.fit(file, (600, 600))
            file1.paste(file0, (0,0), file0)
            file1.save(f'{old[1]}')
    except FileNotFoundError:
        sys.exit('File not found')

def get_file():
    try:
        for extension in ('.jpg', '.png', '.jpeg'):
            if extension in sys.argv[1]:
                ext_0 = extension
            if extension in sys.argv[2]:
                ext_1 = extension
        try:
            if ext_0 == ext_1:
                pass
            else:
                sys.exit('Different image extensions')
        except UnboundLocalError:
            sys.exit('Invalid inputs')
        if len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        else:
            return sys.argv[1], sys.argv[2]
    except IndexError:
        sys.exit('No command-line argumntes')


if __name__ == '__main__':
    main()