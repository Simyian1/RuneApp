import matplotlib.pyplot as plt
import numpy as np
import os

def text_to_path_with_correct_arrow(text, line_length=100, start_point=(0, 0)):
    # Map each letter to an angle
    angle_per_letter = 360 / 26  # for 26 letters in the alphabet
    angles = {chr(65 + i): i * angle_per_letter for i in range(26)}

    # Initialize starting point
    x, y = start_point
    x_coords, y_coords = [x], [y]

    for char in text.upper():
        if char.isalpha():
            angle = angles[char]
            angle_rad = np.radians(angle)
            x += np.cos(angle_rad) * line_length
            y += np.sin(angle_rad) * line_length
        elif char == " ":  # small gap for space
            x += np.cos(angle_rad) * (line_length / 2)
            y += np.sin(angle_rad) * (line_length / 2)
        elif char == ".":  # large gap for period
            x += np.cos(angle_rad) * (line_length * 2)
            y += np.sin(angle_rad) * (line_length * 2)

        x_coords.append(x)
        y_coords.append(y)

    # Plotting with black lines
    plt.figure(figsize=(12, 6))
    plt.plot(x_coords, y_coords, marker='o', color='black')

    # Add an arrow pointing from the midpoint of the first line to the second point
    if len(x_coords) > 1:
        mid_x = (x_coords[0] + x_coords[1]) / 2
        mid_y = (y_coords[0] + y_coords[1]) / 2
        plt.arrow(mid_x, mid_y, (x_coords[1] - mid_x), (y_coords[1] - mid_y),
                  head_width=line_length/6, head_length=line_length/6, fc='black', ec='black', 
                  length_includes_head=True, zorder=5)

    # Hide axes and set transparent background
    plt.axis('off')
    plt.gca().set_position([0, 0, 1, 1])
    plt.gca().set_aspect('equal', adjustable='box')

    # Set plot limits to include space for the arrow by extending the limits
    plt.xlim(min(x_coords) - line_length, max(x_coords) + line_length)
    plt.ylim(min(y_coords) - line_length, max(y_coords) + line_length)

    # Define the directory and filename
    directory = os.path.join("J:", os.sep, "Owner", "Desktop", "MaCHiNA", "Runes")
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = f"{text}_rune.png"
    file_path = os.path.join(directory, filename)
    plt.savefig(file_path, bbox_inches='tight', pad_inches=0, transparent=True)

    # Close the plot
    plt.close()

    return file_path

# text

text = input("Text to convert to Rune: ")

# Run the function and print the file path
file_path = text_to_path_with_correct_arrow(text)
print(file_path)