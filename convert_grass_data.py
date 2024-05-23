from PIL import Image
import os


# original_path = "/project01/cvrl/jhuang24/australia-backup/data/test/imgs"
# target_path = "/project01/cvrl/jhuang24/australia-backup/data/test/imgs_png"

original_path = "/project01/cvrl/jhuang24/australia-backup/data/test/masks"
target_path = "/project01/cvrl/jhuang24/australia-backup/data/test/masks_png"



# all_imgs = os.listdir(original_path)
#
# for one_img in all_imgs:
#     im = Image.open(os.path.join(original_path, one_img))
#     im.save(os.path.join(target_path, one_img.split(".")[0]+".png"))

im = Image.open("/project01/cvrl/jhuang24/australia-backup/data/test/imgs/2019-11-20-F6-0436_3584_3136.png")
print(im.shape)