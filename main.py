import argparse
import cv2
import matplotlib.pyplot as plt


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('image1_path', type=str)
    parser.add_argument('image2_path', type=str)
    parser.add_argument('save_path', type=str)
    args = parser.parse_args()
    return [args.image1_path, args.image2_path, args.save_path]


def main() -> None:
    args = argument_parsing()
    image1 = cv2.imread(args[0])
    image2 = cv2.imread(args[1])

    if (image1 is None):
        print('Error reading image1')
        raise ValueError

    if (image2 is None):
        print('Error reading image2')
        raise ValueError

    print('Shape of image 1: ', image1.shape)
    print('Shape of image 2: ', image2.shape)

    if image1.shape != image2.shape:
        image2.resize(image2, (image1.shape[0], image1.shape[1]))

    image3 = cv2.addWeighted(image1, 1.0, image2, 0.5, 0)

    fig, axes = plt.subplots(1, 3, figsize=(25, 5))

    axes[0].imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Image 1')
    axes[0].axis('off')

    axes[1].imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Image 2')
    axes[1].axis('off')

    axes[2].imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
    axes[2].set_title('Mixed Image')
    axes[2].axis('off')

    plt.show()

    cv2.imwrite(args[2], image3)


if __name__ == '__main__':
    main()
