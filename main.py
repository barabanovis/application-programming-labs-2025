import argparse
import cv2
import matplotlib.pyplot as plt
import os


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
    image1 = cv2.imread('000001.jpg')
    image2 = cv2.imread('bear.jpg')

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

    cv2.imshow('Mixed Image (OpenCV)', image3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('result.jpg', image3)


if __name__ == '__main__':
    main()
