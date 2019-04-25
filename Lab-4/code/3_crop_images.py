import cv2
import os


def crop_img(img):
    scale = 1.0
    center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
    width_scaled, height_scaled = img.shape[1] * scale, img.shape[0] * scale
    left_x, right_x = center_x - width_scaled / 2, center_x + width_scaled / 2
    top_y, bottom_y = center_y - height_scaled / 2, center_y + img.shape[0] * 0.65 / 2
    img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
    return img_cropped


dataset_numbers = []
for dataset_number in os.listdir("data/image_frames"):
    dataset_numbers.append(dataset_number)

for dataset_number in dataset_numbers:
    for image in os.listdir("data/image_frames/" + dataset_number):
        img = cv2.imread("data/image_frames/" + dataset_number + "/" + image)
        img_cropped = crop_img(img)
        cv2.imwrite("data/image_frames/" + dataset_number + "/" + image, img_cropped)
        cv2.waitKey(0)
