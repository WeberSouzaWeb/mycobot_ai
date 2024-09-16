import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def process_image(input_image_path, num_layers=3):
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
    
    return simplified_img

def isolate_layer(input_image_path, layer_index, num_layers=3):
    # Open the image and convert it to grayscale
    img = Image.open(input_image_path).convert('L')
    
    # Convert the grayscale image to a numpy array
    img_array = np.array(img)
    
    # Calculate the interval for each layer
    layer_interval = 256 // num_layers
    
    # Define the range for the selected layer
    lower_bound = layer_index * layer_interval
    upper_bound = (layer_index + 1) * layer_interval
    
    # Identify the pixels that belong to the selected layer
    mask = (img_array >= lower_bound) & (img_array < upper_bound)
    
    # Get the coordinates of the pixels that match the mask
    coordinates = np.argwhere(mask)
    
    return coordinates

def main(image_path, layer_index):
    # Process the image and isolate a specific layer
    layer_coords = isolate_layer(image_path, layer_index)
    
    # Print the coordinates of the selected layer
    print(f"Coordinates of pixels in layer {layer_index}:")
    for coord in layer_coords:
        print(coord)
    
    # Process the image for visualization (optional)
    processed_image = process_image(image_path)
    
    # Plot the processed image
    plt.imshow(processed_image, cmap='gray')
    plt.title(f'Processed Image with {layer_index} Layers')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <image_path> <layer_index>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    layer_index = int(sys.argv[2])
    main(image_path, layer_index)
