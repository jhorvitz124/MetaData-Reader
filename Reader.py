from PIL import Image

def read_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img.info
            return metadata
    except Exception as e:
        print("Error:", e)
        return None

def main():
    image_path = input("Enter the path to the image file: ")
    metadata = read_image_metadata(image_path)
    if metadata:
        print("Image metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("Failed to read image metadata.")

if __name__ == "__main__":
    main()
