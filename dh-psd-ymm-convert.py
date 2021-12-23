# /* Import library */
from psd_tools import PSDImage
from PIL import Image
import psd_tools
import numpy as np
import os
import shutil
import itertools
import re

# /*===================================================================================================*/

# /* Constant */
PATH = os.getcwd()
PSD_PATH = os.path.join(PATH, "00-full-psd")
PSD_ICO_PATH = os.path.join(PATH, "00-icon-psd")
OUTPUT_PATH = os.path.join(PATH, "00-result")
YMM3 = "-YMM3"
YMM4 = "-YMM4"

# Array
Y_VER_ARR = np.array(
    [YMM3, YMM4], dtype=object
)
Y_FOLDER_ARR = np.array(
    ["顔", "後", "口", "全", "他", "体", "髪", "眉", "目"], 
    dtype=object
)

# Dictionary
DH_DICT = {
    "感情マーク": "他",
    "汗、涙": "顔",
    "表情サンプル": "顔",
    "眉": "眉",
    "目": "目",
    "口": "口",
    "顔色": "顔",
    "体": "体",
    "その他": "他"
}
EYE_DICT_Y3 = {
    "閉じ目(下)": "00b",
    "ジト目": "00a",
    "普通目": "00"
}
EYE_DICT_Y4 = {
    "閉じ目(下)": "00.0",
    "ジト目": "00.1",
    "普通目": "00"
}
MOUTH_DICT_00_Y3 = {
    "口閉じ": "00b",
    "小口開け": "00a",
    "大口開け": "00",
}
MOUTH_DICT_00_Y4 = {
    "口閉じ": "00.0",
    "小口開け": "00.1",
    "大口開け": "00",
}
MOUTH_DICT_01_Y3 = {
    "口閉じ笑い": "01b",
    "小口笑い": "01a",
    "大口笑い": "01",
}
MOUTH_DICT_01_Y4 = {
    "口閉じ笑い": "01.0",
    "小口笑い": "01.1",
    "大口笑い": "01",
}

# /*===================================================================================================*/

# /* Def */
def change_dir(psd_name, parts_name):
    p = os.path.join(OUTPUT_PATH, psd_name)
    p = os.path.join(p, parts_name)
    os.chdir(p)

def save_psd_img(psd, layer, ver = 0):
    if layer.is_group() and ( ("目" in layer.name) or ("口" in layer.name) ):
        for l in layer:
            save_psd_layer_img(psd=psd, layer=l)
            save_psd_layer_em_img(psd=psd, layer=l, ver=ver)
    elif layer.is_group():
        for l in layer:
            save_psd_layer_img(psd=psd, layer=l)
    elif not layer.is_group():
        save_psd_layer_img(psd=psd, layer=layer)

def save_psd_layer_img(psd, layer):
    file_name = layer.name
    file_name = re.sub(r'[\\/:*?"<>|]+', '', file_name) # ファイル名に使えないものは置換
    img = Image.new('RGBA', psd.size)
    img.paste(layer.topil(), (layer.left, layer.top))
    img = img.crop(psd.bbox)
    img.save("./"+file_name+".png", quality=95)

def save_psd_layer_em_img(psd, layer, ver):
    file_name = layer.name
    file_name = re.sub(r'[\\/:*?"<>|]+', '', file_name) # ファイル名に使えないものは置換
    img = Image.new('RGBA', psd.size)
    img.paste(layer.topil(), (layer.left, layer.top))
    img = img.crop(psd.bbox)
    layer_name = re.sub('!|\*', '', layer.name)
    if ver == YMM3:
        # eye
        if layer_name in EYE_DICT_Y3:
            img.save("./"+EYE_DICT_Y3[layer_name]+".png", quality=95)
        elif layer_name in MOUTH_DICT_00_Y3:
            img.save("./"+MOUTH_DICT_00_Y3[layer_name]+".png", quality=95)
        elif layer_name in MOUTH_DICT_01_Y3:
            img.save("./"+MOUTH_DICT_01_Y3[layer_name]+".png", quality=95)
    elif ver == YMM4:
        # mouth
        if layer_name in EYE_DICT_Y4:
            img.save("./"+EYE_DICT_Y4[layer_name]+".png", quality=95)
        elif layer_name in MOUTH_DICT_00_Y4:
            img.save("./"+MOUTH_DICT_00_Y4[layer_name]+".png", quality=95)
        elif layer_name in MOUTH_DICT_01_Y4:
            img.save("./"+MOUTH_DICT_01_Y4[layer_name]+".png", quality=95)

# /* Class */
class Converter:
    def __init__(self) -> None:
        self.output_path_arr = np.array([], dtype=object)
        
    def load_psd(self):
        # Get a list of file names only
        path = PSD_PATH
        files = os.listdir(path)
        files_file = [os.path.join(path, f) for f in files if os.path.isfile(os.path.join(path, f))]
        psd_path = np.array(files_file, dtype=object)
        path = PSD_ICO_PATH
        files = os.listdir(path)
        files_file = [os.path.join(path, f) for f in files if os.path.isfile(os.path.join(path, f))]
        files_file = np.array(files_file, dtype=object)
        self.psd_paths = np.append(psd_path, files_file)
        # load psd
        psd_list = [PSDImage.open(p) for p in self.psd_paths]
        #self.psd_arr = np.array(psd_list, dtype=object)
        self.psd_arr = psd_list
        return self.psd_arr
    
    def convert(self):
        self.load_psd()
        self.create_folder()
        print("ゆっくり素材用のフォルダを作成します。")
        self.psd2png()
        print("完了！")
    
    def psd2png(self):
        for psd, name in zip(self.psd_arr, self.psd_names):
            for layer, ver in itertools.product(psd, Y_VER_ARR):
                folder_name = name+ver
                # 体
                if ( not layer.is_group() ) and ( layer.name.find("体") != -1 ):
                    print("creating [{}]...".format(folder_name))
                    change_dir(psd_name=folder_name, parts_name="体")
                    save_psd_img(psd=psd, layer=layer)
                    #layer.topil().save('./00.png')
                # 感情マーク
                elif ( layer.is_group() ) and ( layer.name.find("感情マーク") != -1 ):
                    change_dir(psd_name=folder_name, parts_name=DH_DICT["感情マーク"])
                    save_psd_img(psd=psd, layer=layer)
                # 汗、涙
                elif ( layer.is_group() ) and ( layer.name.find("汗、涙") != -1 ):
                    change_dir(psd_name=folder_name, parts_name=DH_DICT["汗、涙"])
                    save_psd_img(psd=psd, layer=layer)
                
                # 顔色
                elif ( layer.is_group() ) and ( layer.name.find("顔色") != -1 ):
                    change_dir(psd_name=folder_name, parts_name=DH_DICT["顔色"])
                    save_psd_img(psd=psd, layer=layer)
                # その他
                elif ( not layer.is_group() ):
                    change_dir(psd_name=folder_name, parts_name=DH_DICT["その他"])
                    save_psd_img(psd=psd, layer=layer)
                # 表情
                elif ( layer.is_group() ) and ( layer.name.find("表情") != -1 ):
                    for group in layer:
                        # 表情サンプル
                        if ( group.is_group() ) and ( group.name.find("表情サンプル") != -1 ):
                            change_dir(psd_name=folder_name, parts_name=DH_DICT["表情サンプル"])
                            save_psd_img(psd=psd, layer=group)
                        else:
                            for g in group:
                                # 眉
                                if ( g.is_group() ) and ( g.name.find("眉") != -1 ):
                                    change_dir(psd_name=folder_name, parts_name=DH_DICT["眉"])
                                    save_psd_img(psd=psd, layer=g, ver=ver)
                                # 目
                                elif ( g.is_group() ) and ( g.name.find("目") != -1 ):
                                    change_dir(psd_name=folder_name, parts_name=DH_DICT["目"])
                                    save_psd_img(psd=psd, layer=g, ver=ver)
                                # 口
                                elif ( g.is_group() ) and ( g.name.find("口") != -1 ):
                                    change_dir(psd_name=folder_name, parts_name=DH_DICT["口"])
                                    save_psd_img(psd=psd, layer=g, ver=ver)
    
    def create_folder(self):
        psd_names = [os.path.splitext(os.path.basename(p))[0] for p in self.psd_paths]
        psd_names = np.array(psd_names, dtype=object)
        self.psd_names = psd_names
        for folder_name, y_ver, sub_name in itertools.product(psd_names, Y_VER_ARR, Y_FOLDER_ARR):
            output_path = os.path.join(OUTPUT_PATH, folder_name)
            output_path = output_path + y_ver
            output_path = os.path.join(output_path, sub_name)
            if os.path.isdir(output_path):
                shutil.rmtree(output_path) # ディレクトリを中身ごと削除
            os.makedirs(output_path, exist_ok=True)
            self.output_path_arr = np.append(self.output_path_arr, output_path)
        return self.output_path_arr

# /*===================================================================================================*/

if __name__ == '__main__':
    converter = Converter()
    converter.convert()