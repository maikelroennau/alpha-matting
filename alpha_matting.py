import argparse
import cv2


def normalize(image):
    return (image - image.min()) / (image.max() - image.min())


def alpha_matte(foreground, background, alpha, output_path):
    F = normalize(cv2.imread(foreground))
    B = normalize(cv2.imread(background))
    a = normalize(cv2.imread(alpha))

    I = a * F + (1 - a) * B
    cv2.imwrite(output_path, I * 255)


def main():
    parser = argparse.ArgumentParser(description="Blend images using Laplacian Pyramids or Laplacian Sequences.")

    parser.add_argument(
        "-f",
        help="Path to the foreground image.",
        required=True,
        type=str)

    parser.add_argument(
        "-b",
        help="Path to the background image to.",
        required=True,
        type=str)

    parser.add_argument(
        "-a",
        help="Path to the alpha mask.",
        required=True,
        type=str)

    parser.add_argument(
        "-o",
        help="Path where to save the matted image.",
        default="matted.png",
        type=str)

    args = parser.parse_args()
    alpha_matte(
        foreground=args.f,
        background=args.b,
        alpha=args.a,
        output_path=args.o
    )


if __name__ == "__main__":
    main()
