from PIL import Image, ImageDraw

def create_icon():
    # Create a new image with a white background
    size = (256, 256)
    image = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(image)

    # Draw a blue rectangle
    draw.rectangle([50, 50, 206, 206], fill='#007aff')
    
    # Draw a smaller white rectangle inside
    draw.rectangle([80, 80, 176, 176], fill='white')

    # Save as ICO
    image.save('icon.ico', format='ICO', sizes=[(256, 256)])

if __name__ == '__main__':
    create_icon() 