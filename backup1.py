import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon


# Function to plot a hex grid with pointy tops and a diamond shape
def plot_hex_grid(N, numbers):
    # Constants for hexagonal grid layout
    sqrt3 = np.sqrt(3)
    hex_height = 2  # Vertical distance between two points of a hexagon
    hex_width = sqrt3  # Horizontal distance between two points of a hexagon
    hex_spacing = 0.1  # Extra space between hexagons to make them disconnected

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Plot each hexagon and its label in a diamond pattern
    for row, row_numbers in enumerate(numbers):
        y = -row * (hex_height * 0.75 + hex_spacing
                    )  # Vertical distance for hex rows

        # Offset the columns depending on row number for diamond shape
        row_offset = -(len(row_numbers) - 1) / 2
        for col, num in enumerate(row_numbers):
            x = (col + row_offset) * (hex_width + hex_spacing
                                      )  # Horizontal position

            # Create hexagon with pointy top
            hexagon = RegularPolygon(
                (x, y),
                numVertices=6,
                radius=1,
                orientation=0,  # Pointy top, orientation=0
                facecolor='white',
                edgecolor='black')
            ax.add_patch(hexagon)

            # Add the number if it's not zero
            if num != 0:
                ax.text(x, y, str(num), ha='center', va='center', fontsize=12)

    # Set plot limits and hide axes
    ax.set_xlim(-N * (hex_width + hex_spacing), N * (hex_width + hex_spacing))
    ax.set_ylim(-N * (hex_height + hex_spacing),
                N * (hex_height + hex_spacing))
    ax.axis('off')

    # Show plot
    plt.show()


# Input data with "0" representing an empty hexagon in the second row
numbers = [[2, 6, 1], [9, 17, 0, 5], [16, 10, 13, 18, 7], [12, 4, 15, 3],
           [14, 8, 11]]

# Call the function to plot the hex grid
plot_hex_grid(5, numbers)
