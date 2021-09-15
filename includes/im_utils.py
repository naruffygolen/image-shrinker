# coding : utf-8


if __name__ == '__main__':
    print('this module must be imported')
else:
    from PIL import Image
    import os
    import includes.common as common


    def display_help(cause: str = None) -> None:
        if cause is None:
            __display_default_help__()
        elif cause == "parameters":
            print("wrong parameter the module should be used as follow : ")
            __display_default_help__()


    def __display_default_help__():
        print("""This is a mini image file shrinker, it helps you reduce the  size of your images 
        by reducing its resolution but keeps the aspect ratio the result shrinked 
        file is then stored in an output folder usage is : shrinker.py -f file_path [-r factor] [-o output_path] [-h] file_path : path to image factor : max pixels per side
                                             output_path : path to output file""")


    def shrink_image(rimage_path: str = None, rfactor: int = 500, routput: str = None, rverbose: str = None) -> None:
        if rimage_path is None:
            raise ValueError
        image = Image.open(rimage_path)

        img_height, img_width = image.size
        if rverbose is not None:
            print('precalculation size : height = {}, width = {}'.format(img_height, img_width))
        if common.xor(img_width > rfactor, img_height > rfactor):
            if img_width > rfactor:
                ratio: float = rfactor / img_width
            elif img_height > rfactor:
                ratio: float = rfactor / img_height
        elif img_height > rfactor and img_height > rfactor:
            # img_height is the bigger value we calculate depending on it

            if img_height > img_width:
                ratio: float = rfactor / img_height
            else:
                ratio: float = rfactor / img_width
        else:
            ratio = 1

        img_width *= ratio
        img_height *= ratio
        img_width = int(img_width)
        img_height = int(img_height)
        image = image.resize((img_height, img_width), Image.ANTIALIAS)

        if routput is not None:
            if os.path.exists(os.path.dirname(routput)):
                image.save(os.path.abspath(routput), quality=95)
            else:
                image.save(os.getcwd().join(routput), quality=95)
        else:
            if not os.path.exists('output'):
                os.mkdir('output')
            image.save(os.path.abspath('output/{}'.format(os.path.basename(rimage_path))), quality=95)

        if rverbose is not None:
            print(f'post calculating shapes : width = {img_width}, height = {img_height}, ratio = {ratio}')
