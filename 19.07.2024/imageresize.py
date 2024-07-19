from PIL import Image
import os

def resize_images(input_directory, output_directory, width, height):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                with Image.open(input_path) as img:
                    img = img.resize((width, height), Image.ANTIALIAS)
                    output_path = os.path.join(output_directory, filename)
                    img.save(output_path)
                    
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {input_path}: {e}")
input_directory = 'input_images'
output_directory = 'output_images'
width = 800
height = 600

resize_images(input_directory, output_directory, width, height)
