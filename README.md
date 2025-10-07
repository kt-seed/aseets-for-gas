# GAS素材プロジェクト

Google Apps Script (GAS) から参照するための画像素材を生成し、GitHub Pagesで公開するプロジェクト。

## プロジェクト概要

このプロジェクトは、GASで使用する画像素材（主にグラデーション画像）をPythonで生成し、GitHub Pagesを通じて公開することで、GASから直接URLで参照できるようにします。

## セットアップ

### 必要なツール

- Python 3.12+
- uv (Pythonパッケージマネージャー)

### 依存パッケージのインストール

```bash
uv sync
```

## 使い方

### グラデーション画像の生成

1920x12pxの横長グラデーション画像を生成します。

```bash
uv run src/generate_gradient.py R1 G1 B1 R2 G2 B2
```

**パラメータ:**
- R1 G1 B1: 開始色のRGB値 (0-255)
- R2 G2 B2: 終了色のRGB値 (0-255)

**例:**

```bash
# 赤から青へのグラデーション
uv run src/generate_gradient.py 255 0 0 0 0 255
```

**出力:**
- ファイル名: `gradient_{開始色16進数}_to_{終了色16進数}.png`
- 保存先: `images/gradations/`
- 例: `images/gradations/gradient_ff0000_to_0000ff.png`

## GitHub Pagesでの公開

`images/`ディレクトリ配下のファイルはGitHub Pagesで公開され、GASから以下のようなURLで参照できます:

```
https://{username}.github.io/{repository}/images/gradations/gradient_ff0000_to_0000ff.png
```

## ディレクトリ構成

```
.
├── src/
│   └── generate_gradient.py    # グラデーション画像生成スクリプト
├── images/
│   └── gradations/             # 生成されたグラデーション画像
├── pyproject.toml              # uvプロジェクト設定
├── .gitignore                  # Git除外設定
└── README.md                   # このファイル
```

## ライセンス

このプロジェクトで生成された画像素材は自由に使用できます。
