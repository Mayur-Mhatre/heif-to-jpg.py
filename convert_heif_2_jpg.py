import os
from PIL import Image
import pillow_heif
from tqdm import tqdm  # For progress bar

# Convert .heif or .heic files to .jpg
def convert_heif_to_jpg(input_dir, output_dir):
    # Ensure the export directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all HEIF/HEIC files in the input directory
    heif_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.heif', '.heic'))]
    
    # Use tqdm for a progress bar
    for filename in tqdm(heif_files, desc="Converting files", unit="file"):
        input_path = os.path.join(input_dir, filename)

        # Open the HEIF/HEIC image using pillow-heif
        heif_image = pillow_heif.open_heif(input_path)
        image = Image.frombytes(
            heif_image.mode,
            heif_image.size,
            heif_image.data
        )

        # Save as .jpg in the output directory
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_dir, output_filename)
        image.save(output_path, "JPEG")

    print(f"Conversion complete! {len(heif_files)} files converted.")

# Define the input and output directories
input_directory = './IMPORT'  # Change this to your HEIC/HEIF files directory
output_directory = './EXPORT'

# Run the conversion
convert_heif_to_jpg(input_directory, output_directory)
