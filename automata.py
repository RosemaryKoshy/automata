"""Cellular automata
Compute cellular automata and print then to terminal or write to .png file.
I recommend editing the resulting images using GIMP.
Note that large files >=4096px may not display.
"""

import numpy as np
from PIL import Image  # pip install Pillow


def seq(i):
    """Return ith term of the Thue-Morse sequence."""
    return bin(i).count('1') % 2


def initialize_colors(arr):
    """Initialize the array of colors."""
    for i in range(len(arr)):
        arr[i] = np.array([seq(i) * 255, seq(i + 1) * 255, seq(i + 2) * 255])


def display_colors(arr):
    """Display colors using 24-bit xterm colors."""
    for cell in arr:
        print(f"\033[48;2;{cell[0]};{cell[1]};{cell[2]}m \033[0m", end="")
    print()


def edit_colors(arr):
    """Apply cellular automaton rule to generate next_row(color array)."""
    next_row = np.zeros((len(arr), 3), dtype=int)
    for i in range(len(arr)):
        next_row[i] = (arr[i - 1] + arr[(i + 1) % len(arr)]) % 256
    return next_row


if __name__ == "__main__":
    # LENGTH must be a power of two for np.sum(colors) to zero-out
    LENGTH = 2 ** int(input("Enter exponent: "))
    colors = np.zeros((LENGTH, 3), dtype=int)
    img = []
    initialize_colors(colors)
    while np.sum(colors):  # stop when empty (black) row
        # display_colors(colors)  # for terminal
        img.append(colors)
        colors = edit_colors(colors)

    img = np.array(img)
    pil_img = Image.fromarray(img.astype(np.uint8), 'RGB')
    pil_img.save(f"seq{LENGTH}.png")
