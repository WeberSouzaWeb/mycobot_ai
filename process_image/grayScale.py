import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def process_image(input_image_path, output_image_path, num_layers=5):
    # Open the image and convert it to grayscale
    img = Image.open(input_image_path).convert('L')

    # Convert the grayscale image to a numpy array
    img_array = np.array(img)

    # Calculate the interval for each layer based on the number of layers
    layer_interval = 256 // num_layers

    # Create an empty array to store the simplified grayscale layers
    simplified_img_array = np.zeros_like(img_array)

    # Loop through each layer and assign pixel values accordingly
    for i in range(num_layers):
        # Define the range for the current layer
        lower_bound = i * layer_interval
        upper_bound = (i + 1) * layer_interval

        # Assign all pixels in this range to the middle value of the layer
        mask = (img_array >= lower_bound) & (img_array < upper_bound)
        simplified_img_array[mask] = lower_bound + layer_interval // 2

    # Convert the simplified array back to an image
    simplified_img = Image.fromarray(simplified_img_array)

    # Save the resulting image
    simplified_img.save(output_image_path)

    return simplified_img


def main(image_path):
    output_image_path = 'output_image.jpg'

    # Process the image
    processed_image = process_image(image_path, output_image_path)

    # Load the original and processed images
    original_image = Image.open(image_path)

    # Plotting original and processed images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Original image
    axs[0].imshow(original_image)
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    # Processed image
    axs[1].imshow(processed_image, cmap='gray')
    axs[1].set_title('Processed Image')
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Get the image path from the command line argument
    if len(sys.argv) != 2:
        print("Usage: python grayScale.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)
