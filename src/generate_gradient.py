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

def color_to_hex(color):
    """RGB値を16進数文字列に変換"""
    return f"{color[0]:02x}{color[1]:02x}{color[2]:02x}"

def main():
    if len(sys.argv) != 7:
        print("Usage: python generate_gradient.py R1 G1 B1 R2 G2 B2")
        print("Example: python generate_gradient.py 255 0 0 0 0 255")
        sys.exit(1)

    # コマンドライン引数から色を取得
    start_color = tuple(map(int, sys.argv[1:4]))
    end_color = tuple(map(int, sys.argv[4:7]))

    # 色の値を検証
    for color in [start_color, end_color]:
        for value in color:
            if not 0 <= value <= 255:
                print("Error: RGB values must be between 0 and 255")
                sys.exit(1)

    # 画像を生成
    img = create_gradient(start_color, end_color)

    # ファイル名を色コードから生成
    start_hex = color_to_hex(start_color)
    end_hex = color_to_hex(end_color)
    filename = f"gradient_{start_hex}_to_{end_hex}.png"

    # 保存先ディレクトリを作成
    output_dir = Path("images/gradations")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 画像を保存
    output_path = output_dir / filename
    img.save(output_path)
    print(f"Gradient image saved: {output_path}")

if __name__ == "__main__":
    main()
