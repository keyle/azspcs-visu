import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon

# Function to read input from a file and parse the hex grid
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # First line is the radius (N)
    N = int(lines[0].strip())
    
    # Remaining lines are the grid rows
    numbers = []
    for line in lines[1:]:
        row = list(map(int, line.strip().split(',')))
        numbers.append(row)
    
    return N, numbers

# Function to plot a hex grid with pointy tops and a diamond shape
def plot_hex_grid(N, numbers):
    # Constants for hexagonal grid layout
    sqrt3 = np.sqrt(3)
    hex_height = 2  # Vertical distance between two points of a hexagon
    hex_width = sqrt3  # Horizontal distance between two points of a hexagon
    hex_spacing = 0.2  # Extra space between hexagons to make them disconnected

    # Adjust the figure size to ensure proper display
    fig, ax = plt.subplots(figsize=(8, 8))  # Change figure size to accommodate the grid
    ax.set_aspect('equal')

    # Calculate total height of the grid and apply an upward shift
    total_height = (len(numbers) - 1) * (hex_height * 0.75 + hex_spacing)
    vertical_shift = total_height / 2  # Move everything up by half of the grid's height

    # Plot each hexagon and its label in a diamond pattern
    for row, row_numbers in enumerate(numbers):
        y = -row * (hex_height * 0.75 + hex_spacing) + vertical_shift  # Shifted vertical distance for hex rows

        # Offset the columns depending on row number for diamond shape
        row_offset = -(len(row_numbers) - 1) / 2
        for col, num in enumerate(row_numbers):
            x = (col + row_offset) * (hex_width + hex_spacing)  # Horizontal position

            # Create hexagon with pointy top
            hexagon = RegularPolygon((x, y), numVertices=6, radius=1, orientation=0,  # Pointy top, orientation=0
                                     facecolor='white', edgecolor='black')
            ax.add_patch(hexagon)

            # Add the number if it's not zero
            if num != 0:
                ax.text(x, y, str(num), ha='center', va='center', fontsize=12)

    # Adjust plot limits to avoid cropping
    ax.set_xlim(-N * (hex_width + hex_spacing), N * (hex_width + hex_spacing))
    ax.set_ylim(-N * (hex_height + hex_spacing), N * (hex_height + hex_spacing))  # Adjust limits with padding
    ax.axis('off')

    # Show plot
    plt.tight_layout()  # Ensure the layout fits well within the figure
    plt.show()

# Main function to handle command-line arguments and run the script
if __name__ == "__main__":
    # Get the argument (e.g., "3") from the command line
    if len(sys.argv) != 2:
        print("Usage: python visu.py <radius>")
        sys.exit(1)

    # Filename based on the radius
    radius = sys.argv[1]
    filename = f"{radius}.txt"  # Assuming the file is named like "3.txt"

    # Read the input and plot the grid
    N, numbers = read_input_from_file(filename)
    plot_hex_grid(N, numbers)

