import cv2
import glob

img_list= glob.glob('images\*.jpg')
print(img_list)

for img in img_list:
    image= cv2.imread(img, 0)

    img_split= img.rsplit("\\")

    print(img_split[1])

    resized_img=cv2.resize(image,(100,100))

#    print(resized_img.shape)

    img_write= cv2.imwrite("resized_" +img_split[1], resized_img)
    print(img_write)

    # cv2.imshow("images",resized_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
