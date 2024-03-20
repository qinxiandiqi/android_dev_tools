from PIL import Image, ImageDraw
import os

def make_rounded_rectangle(image, radius, fill_color):
    """Create a rounded rectangle and paste the image into it."""
    width, height = image.size
    rounded_rectangle = Image.new('L', (width, height), 0)
    drawing = ImageDraw.Draw(rounded_rectangle)
    # Calculate the coordinates of the rounded rectangle
    corner_radius = min(radius, width//2, height//2)
    box = [0, 0, width, height]
    drawing.rounded_rectangle(box, corner_radius, fill=255)
    # Paste the original image onto the rounded rectangle
    mask = rounded_rectangle.convert("L").point(lambda i: i * 1 if i > 0 else 0, mode='1')
    image.putalpha(mask)
    rounded_rectangle.paste(image, (0, 0), image)
    return rounded_rectangle

def resize_and_make_rounded(input_image_path, output_image_path, size, radius, fill_color=(255, 255, 255, 0)):
    """Resize the image and make it rounded."""
    image = Image.open(input_image_path)
    resized_image = image.resize((size, size), Image.LANCZOS)
    # rounded_image = make_rounded_rectangle(resized_image, radius, fill_color)
    resized_image.save(output_image_path, 'PNG', quality=9)

def main():
    input_image = input("请输入PNG文件的路径：")
    launcher_file_name = input("请输入输出文件名：")
    sizes = []

    sizes.append(("mdpi", 48))
    sizes.append(("hdpi", 72))
    sizes.append(("xhdpi", 96))
    sizes.append(("xxhdpi", 144))
    sizes.append(("xxxhdpi", 192))

    input_dir = os.path.dirname(input_image)
    launcher_dir = f"{input_dir}/launcher"
    os.makedirs(launcher_dir, exist_ok=True)

    for size in sizes:
        dpi, s = size
        
        dpi_dir = f"{launcher_dir}/mipmap-{dpi}"
        os.makedirs(dpi_dir, exist_ok=True)
        output_image_path = os.path.join(dpi_dir, f"{launcher_file_name}.png")
        resize_and_make_rounded(input_image, output_image_path, s, 10)
        print(f"已生成尺寸为 {dpi}x{s} 的图片：{output_image_path}")

if __name__ == "__main__":
    main()
