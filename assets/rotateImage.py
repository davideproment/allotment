from PIL.ExifTags import TAGS
from PIL import Image

image_file = "./2020-03-01/IMG_4704.jpg"
im = Image.open(image_file)
im.transpose(Image.ROTATE_270).save(image_file)


#print("exif data:")
#for tag, value in im._getexif().items():
#    tag_name = TAGS.get(tag, tag)
#    print("{}:{}".format(tag_name, value))

