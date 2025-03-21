from PIL import Image
import csv

# Config
input_image = 'input.png'
output_csv = 'tilemap.csv'

# Colors
color_map = {
    (255, 0, 0): 1,    # Pure red -> tile 1
    (0, 255, 0): 2,    # Pure green -> tile 2
    (0, 0, 255): 3,    # Pure blue -> tile 3
    # Add more colors as needed
}

default_tile_id = 0  # Default tile ID for unlisted colors

# Image
img = Image.open(input_image).convert('RGB')
width, height = img.size

# Build Tilemap
tilemap_data = []
for y in range(height):
    row = []
    for x in range(width):
        pixel = img.getpixel((x, y))
        tile_id = color_map.get(pixel, default_tile_id)
        row.append(tile_id)
    tilemap_data.append(row)

# Export
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(tilemap_data)

print(f"Tilemap CSV saved to {output_csv}")
