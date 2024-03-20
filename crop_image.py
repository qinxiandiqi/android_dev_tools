from PIL import Image
import os
def resize_and_compress_image(input_image_path, output_image_path, size, quality=6):
    image = Image.open(input_image_path)
    resized_image = image.resize(size, Image.LANCZOS)
    resized_image.save(output_image_path, 'PNG', quality=quality)

def main():
    input_image = input("请输入PNG文件的路径：")
    input_prefix = input("请输入输出文件前缀：")
    sizes = []

    print("请输入尺寸列表，每行一个尺寸（格式：宽 高），输入'end'结束：")
    while True:
        size_input = input()
        if size_input.lower() == 'end':
            break
        elif size_input.lower() == 'default':
            sizes.clear()
            sizes.append((24, 24))
            sizes.append((26, 26))
            sizes.append((28, 28))
            sizes.append((30, 30))
            sizes.append((32, 32))
            sizes.append((34, 34))
            sizes.append((40, 40))
            sizes.append((50, 50))
            sizes.append((60, 60))
            sizes.append((80, 80))
            sizes.append((120, 120))
            break
        else:
            width, height = map(int, size_input.split(' '))
            sizes.append((width, height))

    for size in sizes:
        width, height = size
        output_image_name = f"{input_prefix}{width}.png" if width == height else f"{input_prefix}{width}_{height}.png" 
        output_image_path = os.path.join(os.path.dirname(input_image), output_image_name)
        resize_and_compress_image(input_image, output_image_path, size, 8)
        print(f"已生成尺寸为 {width}x{height} 的图片：{output_image_name}")

if __name__ == "__main__":
    main()
