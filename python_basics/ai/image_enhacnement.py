""""""

import cv2
from cv2 import dnn_superres
import os


def upscale_image(input_image_path, model_path, output_dir="./output"):
    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_image_path))[0]

    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Load the super-resolution model
    try:
        sr.readModel(model_path)
    except cv2.error as e:
        print(f"Error: Failed to load model '{model_path}': {e}")
        return

    # Set the super-resolution model and scale
    try:
        sr.setModel("edsr", 3)
    except cv2.error as e:
        print(f"Error: Failed to set model 'edsr' with scale factor 3: {e}")
        return

    # Read the input image
    image = cv2.imread(input_image_path)

    if image is None:
        print(f"Error: Failed to load image from '{input_image_path}'.")
        return

    # Upscale the input image using super-resolution
    try:
        upscaled_image = sr.upsample(image)
    except cv2.error as e:
        print(f"Error: Failed to apply super-resolution: {e}")
        return

    # Construct the output image path with the desired filename
    output_image_path = os.path.join(output_dir, f"{base_filename}_upscaled.png")

    # Save the upscaled image
    cv2.imwrite(output_image_path, upscaled_image)
    print(f"Upscaled image saved as '{output_image_path}'.")

    cv2.destroyAllWindows()


# Specify the input image path and super-resolution model path
dir_path = os.path.dirname(os.path.realpath(__file__))
print("dir path", dir_path)
img_path = os.path.join(dir_path, "s1.jpeg")
# input_image_path = "./images/s1.png"
model_path = os.path.join(dir_path, "EDSR_x3.pb")

# Call the function to upscale the image
upscale_image(img_path, model_path, dir_path)
