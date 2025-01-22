from PIL import Image
import os
from tkinter import Tk, filedialog

# Define the density multipliers
density_multipliers = {
    "ldpi": 0.75,
    "hdpi": 1.5,
    "xhdpi": 2,
    "xxhdpi": 3,
    "xxxhdpi": 4
}

# Function to resize and save the image
def resize_image(input_image_path, base_output_dir):
    try:
        # Open the image
        with Image.open(input_image_path) as img:
            original_width, original_height = img.size

            # Get the input file name and extension
            file_name = os.path.basename(input_image_path)

            # Resize and save for each density multiplier
            for density, multiplier in density_multipliers.items():
                new_width = int(original_width * multiplier)
                new_height = int(original_height * multiplier)

                # Use LANCZOS for high-quality resampling
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Create the density folder if it doesn't exist
                density_folder = os.path.join(base_output_dir, density)
                os.makedirs(density_folder, exist_ok=True)

                # Save the resized image in the respective folder
                output_path = os.path.join(density_folder, file_name)
                resized_img.save(output_path)
                print(f"Saved {density} image at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Main script
if __name__ == "__main__":
    # Use tkinter to select the file
    Tk().withdraw()  # Hide the root window
    input_image_path = filedialog.askopenfilename(
        title="Select an Image to Resize",
        filetypes=[("Image Files", ".jpg;.jpeg;.png;.bmp;*.tiff")]
    )

    # Check if a file was selected
    if input_image_path:
        base_output_dir = filedialog.askdirectory(title="Select Output Directory")
        if base_output_dir:
            resize_image(input_image_path, base_output_dir)
        else:
            print("No output directory selected. Exiting.")
    else:
        print("No file selected. Exiting.")
