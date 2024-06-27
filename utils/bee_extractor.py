import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_transparent_mask(mask, rgb):
    # Create an alpha channel where the mask value is non-zero
    alpha_channel = np.where(mask > 0, 255, 0).astype(np.uint8)
    # Invert mask because of manim white background 
    mask_r = np.where(mask > 0, rgb[0], 0).astype(np.uint8)
    mask_g = np.where(mask > 0, rgb[1], 0).astype(np.uint8)
    mask_b = np.where(mask > 0, rgb[2], 0).astype(np.uint8)
    # Stack the mask to make it a 3-channel image
    rgba_mask = cv2.merge([mask_b, mask_g, mask_r, alpha_channel])
    return rgba_mask

def extract_bee(image: str) -> None:
    if not image: raise Exception("No image provided")
    
    # Obtain image from path
    image = cv2.imread(image)
    
    # Change the color space to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Yellow extraction
    lower_yellow = np.array([0, 0, 0])
    upper_yellow = np.array([35, 255, 255])

    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # Black extraction
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 135])

    black_mask = cv2.inRange(hsv_image, lower_black, upper_black)

    # White extraction
    lower_white = np.array([80, 0, 0])
    upper_white = np.array([180, 255, 255])

    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

    # Transparent wings extraction
    lower_wings = np.array([20, 0, 100])
    upper_wings = np.array([70, 50, 160])

    wings_mask = cv2.inRange(hsv_image, lower_wings, upper_wings)

    # Combine masks
    bee_mask = cv2.bitwise_or(yellow_mask, black_mask)
    bee_mask = cv2.bitwise_or(bee_mask, white_mask)
    bee_mask = cv2.bitwise_or(bee_mask, wings_mask)

    # Apply mask
    masked_image = cv2.bitwise_and(image, image, mask=bee_mask)
    masked_image[bee_mask == 0] = [255, 255, 255]

    # Green removal mask
    lower_green = np.array([0, 100, 50])
    upper_green = np.array([50, 255, 255])

    green_mask = cv2.inRange(masked_image, lower_green, upper_green)

    # Apply removal masks
    non_removed_green = masked_image.copy()
    masked_image[green_mask > 0] = [255, 255, 255]

    # Show all the images in one window 
    fig, ax = plt.subplots(2, 3, figsize=(10, 6))

    fig.suptitle('Bee Extraction')

    ax[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax[0, 0].set_title('Original Image')

    ax[0, 1].imshow(yellow_mask, cmap='gray')
    ax[0, 1].set_title('Yellow Mask')

    ax[0, 2].imshow(black_mask, cmap='gray')
    ax[0, 2].set_title('Black Mask')

    ax[1, 0].imshow(white_mask, cmap='gray')
    ax[1, 0].set_title('White Mask')

    ax[1, 1].imshow(wings_mask, cmap='gray')
    ax[1, 1].set_title('Wings Mask')

    ax[1, 2].imshow(cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB))
    ax[1, 2].set_title('Masked Image')

    for axis in ax.flatten(): axis.axis('off')

    cv2.imshow('Bee Extraction', masked_image)
    plt.show()

    return create_transparent_mask(yellow_mask, (255, 255, 30)), \
           create_transparent_mask(black_mask,   (0, 0, 0)), \
           create_transparent_mask(white_mask,   (136, 136, 136)), \
           create_transparent_mask(wings_mask,   (150, 115, 175)), \
           create_transparent_mask(green_mask,   (0, 255, 255)), \
           non_removed_green, \
           masked_image

if __name__ == '__main__':
    simple_out = extract_bee('assets/raw_bee.webp')
    simple_out_names = ['yellow_mask.png', 'black_mask.png', 'white_mask.png', 'wings_mask.png', 'green_mask.png', 'non_removed_green.jpg', 'just_bee.jpg']
    for i in range(len(simple_out)):cv2.imwrite(f'assets/{simple_out_names[i]}', simple_out[i])
    
    complex_out = extract_bee('assets/complex_image.webp')
    complex_out_names = ['new_yellow_mask.png', 'new_black_mask.png', 'new_white_mask.png', 'new_wings_mask.png',
                          'new_green_mask.png', 'new_non_removed_green.jpg', 'masked_complex_image.jpg']
    for i in range(len(complex_out)):cv2.imwrite(f'assets/{complex_out_names[i]}', complex_out[i])