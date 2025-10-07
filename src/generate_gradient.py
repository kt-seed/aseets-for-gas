import sys
from PIL import Image
import numpy as np
from pathlib import Path

def create_gradient(start_color, end_color, width=1920, height=12):
    """
    左から右へのグラデーション画像を生成

    Args:
        start_color: 開始色 (R, G, B)
        end_color: 終了色 (R, G, B)
        width: 画像の幅
        height: 画像の高さ
    """
    # グラデーション配列を作成
    gradient = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(width):
        # 各ピクセルの位置に応じて色を補間
        ratio = i / (width - 1)
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        gradient[:, i] = [r, g, b]

    return Image.fromarray(gradient)

def hex_to_rgb(hex_color):
    """16進数カラーコードをRGBタプルに変換"""
    # '#'を削除
    hex_color = hex_color.lstrip('#')

    # 3桁の短縮形式を6桁に展開
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])

    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color: {hex_color}")

    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)
    except ValueError:
        raise ValueError(f"Invalid hex color: {hex_color}")

def color_to_hex(color):
    """RGB値を16進数文字列に変換"""
    return f"{color[0]:02x}{color[1]:02x}{color[2]:02x}"

def generate_from_colors(start_hex, end_hex):
    """指定された色でグラデーション画像を生成"""
    try:
        start_color = hex_to_rgb(start_hex)
        end_color = hex_to_rgb(end_hex)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # 画像を生成
    img = create_gradient(start_color, end_color)

    # ファイル名を色コードから生成
    start_hex_clean = color_to_hex(start_color)
    end_hex_clean = color_to_hex(end_color)
    filename = f"gradient_{start_hex_clean}_to_{end_hex_clean}.png"

    # 保存先ディレクトリを作成
    output_dir = Path("images/gradations")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 画像を保存
    output_path = output_dir / filename
    img.save(output_path)
    print(f"Gradient image saved: {output_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_gradient.py START_COLOR END_COLOR")
        print("Example: python generate_gradient.py ff0000 0000ff")
        print("Example: python generate_gradient.py #ff0000 #0000ff")
        sys.exit(1)

    generate_from_colors(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
