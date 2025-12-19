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
    return [parser.image1_path, parser.image2_path, parser.save_path]


def main() -> None:
    args=argument_parsing()

if __name__ == '__main__':
    main()
