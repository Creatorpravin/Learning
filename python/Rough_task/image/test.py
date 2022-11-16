from PIL import Image
import numpy as np
import pytesseract

def image_to_text(filename):    
    img1 = np.array(Image.open(filename))        
    return pytesseract.image_to_string(img1)
    
if __name__ == "__main__":    
    print(image_to_text("stack.png"))