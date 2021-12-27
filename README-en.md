dh-psd-ymm-converter
=====

# Introduction

I'm not good at English. There may be parts that are difficult to understand. In that case, please feel free to ask me questions.

* [Touhou deformed image](https://goo.gl/3G91VJ) by dairi & Haruka.

I made this program because I thought it would be possible to implement mouth clicks and blinks when using dairi & Haruka's [Touhou Deformed Image](https://goo.gl/3G91VJ) in a Yukkuri's video.

In the meantime, you can create folders for [YMM3](https://manjubox.net/ymm3/) and [YMM4](https://manjubox.net/ymm4/).

2021/12/27: Modified to support dairi & Haruka's [Touhou Standing Pictures](https://seiga.nicovideo.jp/seiga/im3189645).

I can blink and talk in the CoC video!
Heh heh heh ...... (Kiritan style)

You can download the executable file in zip and 7z format from [Release](https://github.com/DriCro6663/dh-psd-ymm-converter/releases).

# Overview
This program creates an image folder for YMM: Yukkuri Movie Maker from a deformed psd file of [Touhou Deformed Images](https://goo.gl/3G91VJ) by dairi & Haruka.

2021/12/27: Modified to support dairi & Haruka's [Touhou Standing Pictures](https://seiga.nicovideo.jp/seiga/im3189645).

You can download the executable file in zip and 7z format from [Release](https://github.com/DriCro6663/dh-psd-ymm-converter/releases).

<details>
    <summary>If you want to know the image of mouthing and blinking, click here.</summary>
    <div>　　

---

| Lip-sync 00 |  YMM3  |   YMM4   | State |
| :--- | :----: |  :----:  | :---- |
| 口閉じ: Mouth closed | 00b.png | 00.0.png | Mouth closed |
| 小口開け: Small mouth open | 00a.png | 00.1.png | Intermediate |
| 大口開け: Large mouth open | 00.png | 00.png | Mouth open |

---

| Lip-sync 01 |  YMM3  |   YMM4   | State |
| :--- | :----: |  :----:  | :---- |
| 口閉じ笑い: Closed-mouth laughter | 01b.png | 01.0.png | Mouth closed |
| 小口笑い: Small smile | 01a.png | 01.1.png | Intermediate |
| 大口笑い: Smile | 01.png | 01.png | Mouth open |

---

| Blink |  YMM3  |   YMM4   | State |
| :--- | :----: |  :----:  | :---- |
| 閉じ目(下): Closed eyes (bottom) | 00b.png | 00.0.png | Eyes closed |
| ジト目: disgusted eyes | 00a.png | 00.1.png | Intermediate |
| 普通目: Normal eyes | 00.png | 00.png | Eyes open |

---

</div></details>　　


# Usage

1. put the deformed psd file in the [00-def-psd] folder and the standing psd file in the [00-sta-psd] folder.

```
# Example tree
/Chara's
|-- 00-def-psd
|   |-- Seija.psd
|   |-- Seija-icon.psd
|-- 00-sta-psd
|   |-- SEIJA.psd
|-- 01-result
|-- dist
|   |-- dh-psd-ymm-convert
|   |   |-- 00-def-psd
|   |   |-- 00-sta-psd
|   |   |-- 01-result
|   |   |-- Other files and folders
|   |   |-- dh-psd-ymm-convert.exe  <= [Quick Ver.]
|-- dh-psd-ymm-convert.bat          <= [Quick Ver.]
|-- dh-psd-ymm-convert.exe          <= [OneFile Ver.]
```

2. Please execute [dh-psd-ymm-convert.exe] or [dh-psd-ymm-convert.bat]. The differences between exe Ver. and bat Ver. are as follows.

* exe: An executable file that includes the modules used. <br>
    Merit: A single executable file. <br>
    Demerit: Execution speed is slower than bat Ver.
* bat: Separate modules and executables for use. <br>
    Merit: Faster execution than exe Ver. <br>
    Demerit: It is associated with a large number of files.

3. After execution, an image folder corresponding to YMM will be created in the [01-result] folder.

```
# Example tree -exe Ver.-
/Chara's
|-- 00-def-psd
|   |-- Seija.psd
|   |-- Seija-icon.psd
|-- 00-sta-psd
|   |-- SEIJA.psd
|-- 01-result
|   |-- Seija-YMM3
|   |-- Seija-YMM4
|   |-- Seija-icon-YMM3
|   |-- Seija-icon-YMM4
|   |-- SEIJA-YMM3
|   |-- SEIJA-YMM4
|-- dist
|   |-- dh-psd-ymm-convert
|   |   |-- 00-def-psd
|   |   |-- 00-sta-psd
|   |   |-- 01-result
|   |   |-- Other files and folders
|   |   |-- dh-psd-ymm-convert.exe  <= [Quick Ver.]
|-- dh-psd-ymm-convert.bat          <= [Quick Ver.]
|-- dh-psd-ymm-convert.exe          <= [OneFile Ver.]

# Example tree -bat Ver.-
/Chara's
|-- 00-def-psd
|   |-- Seija.psd
|   |-- Seija-icon.psd
|-- 00-sta-psd
|   |-- SEIJA.psd
|-- 01-result
|   |-- Seija-YMM3
|   |-- Seija-YMM4
|   |-- Seija-icon-YMM3
|   |-- Seija-icon-YMM4
|   |-- SEIJA-YMM3
|   |-- SEIJA-YMM4
|-- dist
|   |-- dh-psd-ymm-convert
|   |   |-- 00-def-psd
|   |   |   |-- Seija.psd
|   |   |   |-- Seija-icon.psd
|   |   |-- 00-sta-psd
|   |   |   |-- SEIJA.psd
|   |   |-- 01-result
|   |   |   |-- Seija-YMM3
|   |   |   |-- Seija-YMM4
|   |   |   |-- Seija-icon-YMM3
|   |   |   |-- Seija-icon-YMM4
|   |   |   |-- SEIJA-YMM3
|   |   |   |-- SEIJA-YMM4
|   |   |-- dh-psd-ymm-convert.exe  <= [Quick Ver.]
|-- dh-psd-ymm-convert.bat          <= [Quick Ver.]
|-- dh-psd-ymm-convert.exe          <= [OneFile Ver.]
```

# BuildTheEnvironment
If you want to edit the source code, please refer to the following to build the environment.

<details>
    <summary>Click here</summary>
    <div>　　

## Virtual environment construction
Anaconda Ver.
```
# create virtual env: python ver. 3.8 or higher
conda create --name exepy python=3.8
    - or -
conda create -n pyins

# Active virtual env
conda activate [venv-name]
```

## Required modules

* os            : Standard library
* re            : Standard library
* shutil        : Standard library
* numpy         : Computational Extension Library
* Pillow        : Image Processing Library
* psd_tools     : Photoshop: psd file processing library
* pyinstaller   : py -> exe

```
conda install -y -c anaconda numpy pillow
conda install -y -c conda-forge pyinstaller
conda install -y -c auto psd-tools
    - or -
pip install numpy pyinstaller psd-tools Pillow
```

If you need to set up a proxy, please refer to the following.
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
    --name          : Specify the name of the exe file
    --onefile       : Combine all exe files into one
    --noconsole     : Suppress console display when running exe
    --debug all     : Debug output
    --clean         : Delete the cache
    --icon          : Specify the path of the icon file

pyinstaller main.py --name [fileName] --onefile --icon [./img/icon.ico] --noconsole
"""
```

</div></details>　　

# Note

* I have not confirmed any conversions other than Seija and Shinmyoumaru. If you encounter any mishandling, I would appreciate it if you could contact us via the developer information below.
* I don't provide command / sh files for Mac / Linux. Mac / Linux users should refer to the bat file to create their own files.

# Disclaimer
I don't guarantee any loss or damage caused by this program.

Please be aware of this.

The distribution of this program may be terminated without notice.

# Updates

* 2021/12/27: <br>
Modified to support dairi & Haruka's [Touhou Standing Pictures](https://seiga.nicovideo.jp/seiga/im3189645).
* 2021/12/23: <br>
Completed / First commit

# Developer Information

* [Github DriCro6663](https://github.com/DriCro6663)
* [Twitter Dri_Cro_6663](https://twitter.com/Dri_Cro_6663)
* [YouTube -DriCro-](https://www.youtube.com/channel/UCyWgav9wdiPVjYphB7jrWCQ)
* [PieceX DriCro6663](https://www.piecex.com/users/profile/DriCro6663)
* [Dri-Cro's Memorandum](https://dri-cro-6663.jp/)
* dri.cro.6663@gmail.com

# License

Please check the [LICENSE](./LICENSE) file.