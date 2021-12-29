dh-psd-ymm-converter
=====

# はじめ
* dairi＆はるか 様の [東方デフォルメ画像](https://goo.gl/3G91VJ)

dairi＆はるか 様の [東方デフォルメ画像](https://goo.gl/3G91VJ) をゆっくり動画で使用する際、口と目の画像で口パク・瞬きが実装できそうだったので、本プログラムを作りました。

一応、 [YMM3](https://manjubox.net/ymm3/) と [YMM4](https://manjubox.net/ymm4/) に対応したフォルダを作成できます。

2021/12/27: dairi＆はるか 様の [東方立ち絵](https://seiga.nicovideo.jp/seiga/im3189645) にも対応できるように改良しました。

CoC 動画で使用させていただく予定の東方立ち絵が口パク・瞬きできるぜ！
うぇっへっへっ……（きりたん風）

ダウンロードは、[Release](https://github.com/DriCro6663/dh-psd-ymm-converter/releases) から実行ファイルを zip, 7z 形式でダウンロードできます。

# 概要
本プログラムは、dairi＆はるか 様の [東方デフォルメ画像](https://goo.gl/3G91VJ) のデフォルメ psd ファイルから YMM: ゆっくりムービーメーカー に対応する画像フォルダを作成するプログラムです。

2021/12/27: dairi＆はるか 様の [東方立ち絵](https://seiga.nicovideo.jp/seiga/im3189645) にも対応できるように改良しました。

[Release](https://github.com/DriCro6663/dh-psd-ymm-converter/releases) から実行ファイルを zip, 7z 形式でダウンロードできます。

<details>
    <summary>口パク・瞬きの画像を知りたい方は、こちらをクリックしてください</summary>
    <div>　　

---

| 口パク |  YMM3  |   YMM4   | State |
| :--: | :----: |  :----:  | :---- |
| 口閉じ | 00b.png | 00.0.png | 口が閉じた状態 |
| 小口開け | 00a.png | 00.1.png | 中間フレーム |
| 大口開け | 00.png | 00.png | 口が開いた状態 |

---

| 口パク笑い |  YMM3  |   YMM4   | State |
| :--: | :----: |  :----:  | :---- |
| 口閉じ笑い | 01b.png | 01.0.png | 口が閉じた状態 |
| 小口笑い | 01a.png | 01.1.png | 中間フレーム |
| 大口笑い | 01.png | 01.png | 口が開いた状態 |

---

| 瞬き |  YMM3  |   YMM4   | State |
| :--: | :----: |  :----:  | :---- |
| 閉じ目(下) | 00b.png | 00.0.png | 目が閉じた状態 |
| ジト目 | 00a.png | 00.1.png | 中間フレーム |
| 普通目 | 00.png | 00.png | 目が開いた状態 |

---

</div></details>　　

# 使い方
1. [00-def-psd] フォルダにデフォルメ psd ファイル, [00-sta-psd] フォルダに立ち絵 psd ファイルを入れてください。

```
# Example tree
/Chara's
|-- 00-def-psd
|   |-- せいじゃ.psd
|   |-- せいじゃアイコン.psd
|-- 00-sta-psd
|   |-- 正邪.psd
|-- 01-result
|-- dist
|   |-- dh-psd-ymm-convert
|   |   |-- 00-def-psd
|   |   |-- 00-sta-psd
|   |   |-- 01-result
|   |   |-- その他のファイル・フォルダ群
|   |   |-- dh-psd-ymm-convert.exe  <= [Quick Ver.]
|-- dh-psd-ymm-convert.bat          <= [Quick Ver.]
|-- dh-psd-ymm-convert.exe          <= [OneFile Ver.]
```

2. [dh-psd-ymm-convert.exe] または [dh-psd-ymm-convert.bat] を実行してください。exe Ver. と bat Ver. の違いは以下の通りです。

* exe Ver.: 使用モジュールを含めた実行ファイル <br>
    利点：単独の実行ファイル <br>
    欠点： bat Ver. よりも実行速度が遅い
* bat Ver.: 使用モジュールと実行ファイルが分かれている <br>
    利点： exe Ver. よりも実行測度が速い <br>
    欠点：大量のファイルと関係付けられている

3. 実行後、[01-result] フォルダに YMM に対応した画像フォルダが作成されます。

```
# Example tree -exe Ver.-
/Chara's
|-- 00-def-psd
|   |-- せいじゃ.psd
|   |-- せいじゃアイコン.psd
|-- 00-sta-psd
|   |-- 正邪.psd
|-- 01-result
|   |-- せいじゃ-YMM3
|   |-- せいじゃ-YMM4
|   |-- せいじゃアイコン-YMM3
|   |-- せいじゃアイコン-YMM4
|   |-- 正邪-YMM3
|   |-- 正邪-YMM4
|-- dist
|   |-- dh-psd-ymm-convert
|   |   |-- 00-def-psd
|   |   |-- 00-sta-psd
|   |   |-- 01-result
|   |   |-- その他のファイル・フォルダ群
|   |   |-- dh-psd-ymm-convert.exe  <= [Quick Ver.]
|-- dh-psd-ymm-convert.bat          <= [Quick Ver.]
|-- dh-psd-ymm-convert.exe          <= [OneFile Ver.]

# Example tree -bat Ver.-
/Chara's
|-- 00-def-psd
|   |-- せいじゃ.psd
|   |-- せいじゃアイコン.psd
|-- 00-sta-psd
|   |-- 正邪.psd
|-- 01-result
|   |-- せいじゃ-YMM3
|   |-- せいじゃ-YMM4
|   |-- せいじゃアイコン-YMM3
|   |-- せいじゃアイコン-YMM4
|   |-- 正邪-YMM3
|   |-- 正邪-YMM4
|-- dist
|   |-- dh-psd-ymm-convert
|   |   |-- 00-def-psd
|   |   |   |-- せいじゃ.psd
|   |   |   |-- せいじゃアイコン.psd
|   |   |-- 00-sta-psd
|   |   |   |-- 正邪.psd
|   |   |-- 01-result
|   |   |   |-- せいじゃ-YMM3
|   |   |   |-- せいじゃ-YMM4
|   |   |   |-- せいじゃアイコン-YMM3
|   |   |   |-- せいじゃアイコン-YMM4
|   |   |   |-- 正邪-YMM3
|   |   |   |-- 正邪-YMM4
|   |   |-- dh-psd-ymm-convert.exe  <= [Quick Ver.]
|-- dh-psd-ymm-convert.bat          <= [Quick Ver.]
|-- dh-psd-ymm-convert.exe          <= [OneFile Ver.]
```

# 環境構築
ソースコードを編集したい方は、下記を参考に環境を構築してください。

<details>
    <summary>こちらをクリックしてください</summary>
    <div>　　

## 仮想環境構築
Anaconda Ver.
```
# create virtual env: python ver. 3.8 or higher
conda create --name exepy python=3.8
    - or -
conda create -n pyins

# Active virtual env
conda activate [venv-name]
```

## 使用モジュール

* os            : 標準ライブラリ
* re            : 標準ライブラリ
* shutil        : 標準ライブラリ
* numpy         : 計算拡張ライブラリ
* Pillow        : 画像処理ライブラリ
* psd_tools     : Photoshop: psd ファイル処理ライブラリ
* pyinstaller   : py -> exe に使用

```
conda install -y -c anaconda numpy pillow
conda install -y -c conda-forge pyinstaller
conda install -y -c auto psd-tools
    - or -
pip install numpy pyinstaller psd-tools Pillow
```

プロキシ設定が必要な方は、下記を参考に設定してください。
```
# windows
# if you need to use proxy, please set proxy setting.
set HTTP_PROXY=http://<userid>:<password>@<server-address>:<port>
set HTTPS_PROXY=http://<userid>:<password>@<server-address>:<port>

# example
set HTTP_PROXY=http://proxy.example.com:8080
set HTTPS_PROXY=http://proxy.example.com:8080

# check proxy
echo %HTTP_PROXY%
echo %HTTPS_PROXY%
```

## py -> exe
```
# Example
pyinstaller main.py --onefile

"""
    --name          : exe ファイル名の指定
    --onefile       : exe ファイルを１つにまとめる
    --noconsole     : exe 実行時にコンソールの表示を抑制
    --debug all     : デバッグ出力
    --clean         : キャッシュを削除
    --icon          : アイコンファイルのパスを指定

pyinstaller main.py --name [fileName] --onefile --icon [./img/icon.ico] --noconsole
"""
```

</div></details>　　

# 注意

* 正邪・針妙丸 以外の変換を確認しておりません。誤処理が発生した場合は、下記の開発者情報より、連絡していただくと幸いです。
* Mac / Linux 用の command / sh ファイルは用意しておりません。Mac / Linux ユーザーは bat ファイルを参考にして、それぞれのファイルを作成してください。

# 免責事項
本プログラムで生じた如何なる損失・損害も保証いたしません。

ご了承ください。

また、本プログラムは予告なく配布を終了する場合があります。

# 更新情報

* 2021/12/29: <br>
[他]フォルダのパーツが見切れた状態で出力される問題を修正
* 2021/12/28: <br>
[東方立ち絵](https://seiga.nicovideo.jp/seiga/im3189645) の -やられ Ver.- において、"体"の画像が出力されない問題を修正
* 2021/12/27: <br>
dairi＆はるか 様の [東方立ち絵](https://seiga.nicovideo.jp/seiga/im3189645) に対応
* 2021/12/23: <br>
完成・First commit

# 開発者情報

* [Github DriCro6663](https://github.com/DriCro6663)
* [Twitter Dri_Cro_6663](https://twitter.com/Dri_Cro_6663)
* [YouTube ドリクロ -DriCro-](https://www.youtube.com/channel/UCyWgav9wdiPVjYphB7jrWCQ)
* [PieceX DriCro6663](https://www.piecex.com/users/profile/DriCro6663)
* [ドリクロの備忘録](https://dri-cro-6663.jp/)
* dri.cro.6663@gmail.com

# ライセンス

[LICENSE](./LISENCE) ファイルをご確認してください。