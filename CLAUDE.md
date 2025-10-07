# Claude開発メモ

このプロジェクトのClaudeとの対話履歴および開発メモ。

プロジェクトの詳細については [README.md](README.md) を参照してください。

## 開発履歴

### 初期セットアップ

1. グラデーション画像生成スクリプトの作成
   - 1920x12pxの横長グラデーション画像を生成
   - RGB値を指定して左から右へのグラデーション
   - ファイル名は色コードから自動生成（例: `gradient_ff0000_to_0000ff.png`）
   - 保存先: `images/gradations/`

2. uvによるパッケージ管理
   - プロジェクト名: `gas-sozai` (ディレクトリ名に日本語が含まれるため)
   - 依存パッケージ: Pillow, numpy

3. Git設定
   - `.gitignore`作成（images/は除外しない - GitHub Pages公開のため）

## 技術メモ

- パッケージ管理: uv
- Python: 3.12+
- 画像は上書き保存される仕様
- GitHub Pagesで公開し、GASから画像をURL参照する想定
