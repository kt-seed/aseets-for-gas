import sys
sys.path.insert(0, 'src')
from generate_gradient import hex_to_rgb, color_to_hex, generate_from_colors

def green_brown():
    """緑から茶色へのグラデーション（左端10段階 x 右端10段階 = 100枚）"""
    base_start_hex = "#72AE2C"
    base_end_hex = "#724C2B"

    # 基準色をRGBに変換
    base_start_color = hex_to_rgb(base_start_hex)
    base_end_color = hex_to_rgb(base_end_hex)

    # 左端を10段階、右端を10段階で100枚の画像を生成
    for i in range(10):
        # 左端の明るさを10%ずつ減らす
        start_factor = 1 - (i * 0.1)

        start_r = int(base_start_color[0] * start_factor)
        start_g = int(base_start_color[1] * start_factor)
        start_b = int(base_start_color[2] * start_factor)

        start_color = (start_r, start_g, start_b)
        start_hex = f"#{color_to_hex(start_color)}"

        for j in range(10):
            # 右端の明るさを10%ずつ減らす
            end_factor = 1 - (j * 0.1)

            end_r = int(base_end_color[0] * end_factor)
            end_g = int(base_end_color[1] * end_factor)
            end_b = int(base_end_color[2] * end_factor)

            end_color = (end_r, end_g, end_b)
            end_hex = f"#{color_to_hex(end_color)}"

            print(f"Generating gradient: {start_hex} -> {end_hex} (left step {i}, right step {j})")
            generate_from_colors(start_hex, end_hex)

    print("All gradients generated successfully!")

if __name__ == "__main__":
    green_brown()
