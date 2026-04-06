import os
from PIL import Image

def convert_png_to_webp():
    # Jis folder mein script hai, wahi ke saare files check karega
    current_directory = os.getcwd()
    
    count = 0
    print("🚀 Conversion shuru ho raha hai...")

    for filename in os.listdir(current_directory):
        if filename.endswith(".png"):
            # Image open karo
            img = Image.open(filename)
            os.remove(filename)       
            
            

    print(f"\n✨ Done! Total {count} images convert ho gayi hain.")

if __name__ == "__main__":
    convert_png_to_webp()