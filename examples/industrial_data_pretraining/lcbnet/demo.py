#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright FunASR (https://github.com/alibaba-damo-academy/FunASR). All Rights Reserved.
#  MIT License  (https://opensource.org/licenses/MIT)

from funasr import AutoModel

model = AutoModel(model="iic/LCB-NET",
                  model_revision="v1.0.0")


# example1
res = model.generate(input=("https://www.modelscope.cn/api/v1/models/iic/LCB-NET/repo?Revision=master&FilePath=example/asr_example.wav","https://www.modelscope.cn/api/v1/models/iic/LCB-NET/repo?Revision=master&FilePath=example/ocr.txt"),data_type=("sound", "text"))

print(res)


'''
# tensor or numpy as input
# example2
import torchaudio
import os
wav_file = os.path.join(model.model_path, "example/asr_example.wav")
input_tensor, sample_rate = torchaudio.load(wav_file)
input_tensor = input_tensor.mean(0)
res = model.generate(input=[input_tensor], batch_size_s=300, is_final=True)


# example3
import soundfile

wav_file = os.path.join(model.model_path, "example/asr_example.wav")
speech, sample_rate = soundfile.read(wav_file)
res = model.generate(input=[speech], batch_size_s=300, is_final=True)
'''
