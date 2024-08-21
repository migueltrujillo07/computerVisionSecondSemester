import matplotlib.pyplot as plt
from mikePackage import load_image
from mikePackage import operations

image = load_image.load()

if image is not None:
    imageNegative = operations.negative(image)

    grayImage, grayHistogram = operations.gray_histogram(image)

    image_brighter = operations.brighter(image, 50)

    plt.figure(figsize=(12,6))

    plt.subplot(3, 3, 1)
    plt.imshow(image)
    plt.axis('off')
    plt.title('Original Image')

    plt.subplot(3, 3, 2)
    plt.imshow(imageNegative)
    plt.axis('off')
    plt.title('Negative Image')

    plt.subplot(3, 3, 3)
    plt.imshow(grayImage, cmap='gray')  # Specify the colormap as 'gray'
    plt.axis('off')
    plt.title('Gray Image')

    plt.subplot(3, 3, 4)
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(grayHistogram)
    plt.xlim([0, 256])

    plt.subplot(3, 3, 5)
    plt.imshow(image_brighter)
    plt.axis('off')
    plt.title('Brighter Image')

    #plt.show()

else:
    print("No image to display.")