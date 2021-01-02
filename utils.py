import cv2
import os.path


# reads an image in gray scale, resizes it and normalizes it
def load_image(image_path):
    while not os.path.isfile(image_path):
        pass

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (350, 350))
    cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
    return img


# loads a whole set of images and returns a tuple containing:
# one list of all training images (80% of all)
# one list of all testing images (20% of all)
def load_set_of_images(folder_name, file_names):
    images = [load_image(os.path.join(folder_name, file_name)) for file_name in file_names]

    training_size = int(len(images) * 0.8)
    print("Loaded " + str(len(images)) + " images from " + folder_name + ", " + str(
        training_size) + " for training and " + str(len(images) - training_size) + " for testing.")

    return images[- training_size:], images[: - training_size or None]