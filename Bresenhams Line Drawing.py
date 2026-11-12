import numpy as np
import cv2
import matplotlib.pyplot as plt


def bresenham_line(img, x0, y0, x1, y1, color=255):

    # Calculate differences between endpoints
    dx = x1 - x0
    dy = y1 - y0

    # Initial decision parameter
    p = 2 * dy - dx

    # Start from the first endpoint
    x, y = x0, y0

    # Process each pixel along the x-axis
    while x <= x1:

        # Set the current pixel
        img[y, x] = color

        # Move one pixel in the x direction
        x += 1

        # Decide whether to increment y
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * dy - 2 * dx

    return img


# Create blank images
height, width = 200, 200

img_bresenham = np.zeros((height, width), dtype=np.uint8) 
img_opencv = np.zeros((height, width), dtype=np.uint8)

# Define endpoints (0 <= slope <= 1)
x0, y0 = 20, 50
x1, y1 = 150, 100

# Draw using Bresenham's algorithm
bresenham_line(img_bresenham, x0, y0, x1, y1)

# Draw using OpenCV
cv2.line(
    img_opencv,
    (x0, y0),
    (x1, y1),
    255,
    thickness=1,
)

# Display both results
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(img_bresenham, cmap='gray')
ax[0].set_title("Bresenham's Algorithm")

ax[1].imshow(img_opencv, cmap='gray')
ax[1].set_title("OpenCV cv2.line()")

plt.tight_layout()
plt.show()
