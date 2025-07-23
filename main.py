from PIL import Image
import numpy as np

def turn_img_gray(image_path):
    # 1. Open the image
    img = Image.open(image_path).convert("RGB")  # ensure it is in RGB mode

    # 2. Convert the image to a NumPy array
    data = np.array(img)  # shape = (height, width, 3)

    # 3. Calculate the weighted grayscale level
    gray = (0.3 * data[:, :, 0] + 0.59 * data[:, :, 1] + 0.11 * data[:, :, 2]).astype(np.uint8)

    # 4. Stack the 3 channels R=G=B=gray to reconstruct an RGB image
    gray_rgb = np.stack((gray,) * 3, axis=-1)
    print(gray_rgb)
    # 5. Create a new image and display it
    gray_img = Image.fromarray(gray_rgb)
    gray_img.show()

# Call the function
image = "descolorir_imagem/car.jpg"
turn_img_gray(image)
