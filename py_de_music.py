import wave
import struct
import numpy as np
from pylab import *

def tone(fs):
    """do, re, mi を数値に変換
    """
    return{ \
    "do":262, "do#":277, "re":294, "re#":311, "mi":330, "fa":349, "fa#":370, "so":392, "so#":425, \
    "ra":440, "ra#":466, "si":494, "do_h":523
    }[fs]

def createWave (f0_str, length):
    """振幅A、基本周波数f0、サンプリング周波数 fs、
    長さlength秒の正弦波を作成して返す"""
    #A, fsの設定
    A = 2.0
    fs = 8000.0
    #f0_strを数値に変換
    f0 = tone(f0_str)
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):  # nはサンプルインデックス
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    for i in range(500):
        data.append(0)
#    plot(data[0:100]); show()
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data

# 波形データを保存(波形データ, サンプリング周波数, ファイル名)
def save_wave(data, filename):
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(5000)
    wf.writeframes(data)
    wf.close()


if __name__ == "__main__" :
    freqList = ["do", "do", "re", "mi"]  # ドドレミ
    datas=bytes(b"")
    for f in freqList:
        data = createWave(f, 0.5)
        datas+=data
    save_wave(datas, "test.wav")  # 波形データをwavファイルで保存
