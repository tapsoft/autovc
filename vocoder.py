import os
import torch
import librosa
import pickle
import soundfile as sf
from synthesis import build_model
from synthesis import wavegen

spect_vc = pickle.load(open('results.pkl', 'rb'))
device = torch.device("cuda")
model = build_model().to(device)
checkpoint = torch.load("checkpoint_step001000000_ema.pth")
model.load_state_dict(checkpoint["state_dict"])

outputDir = './wavs'

for spect in spect_vc:
    name = spect[0]
    c = spect[1]
    print(name)
    waveform = wavegen(model, c=c)   
    #librosa.output.write_wav(name+'.wav', waveform, sr=16000)
    sf.write(os.path.join(outputDir, name+'.wav'), waveform, 16000)