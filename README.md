# Pyxel Game

このリポジトリは GitHub Pages で公開されています。

## アクセス

https://chihiro723.github.io/pyxel-game/

## ⚠️ 重要な注意事項

現在の HTML ファイルは**ブラウザで正常に動作しません**。
Pyxel の WebAssembly 実装に技術的な制限があるため、ブラウザで実行するとエラーが発生します。

## ローカルで遊ぶ方法

### 必要なもの

- Python 3.6 以上
- Pyxel

### インストール

```bash
pip install pyxel
```

### 実行

```bash
# .pyxappファイルを実行
pyxel play game.pyxapp

# または、Pythonファイルから実行
python info2_App.py
```

## 操作方法

- **スペース**: ジャンプ
- **← →**: 左右移動
- **ゲームオーバー時**: スペースで選択、上下矢印で選択変更

## ファイル構成

- `index.html` - ブラウザ用 HTML ファイル（現在動作しません）
- `game.pyxapp` - Pyxel アプリファイル
- `info2_App.py` - メインアプリケーション
- `info2_Game.py` - ゲームロジック
- `info2_Player.py` - プレイヤー
- `info2_Home.py` - ホーム画面
- `character.pyxres` - キャラクターリソース

## 開発方法

```bash
# パッケージ化
pyxel package . info2_App.py

# HTMLに変換（ブラウザで動作しません）
pyxel app2html game.pyxapp
```
