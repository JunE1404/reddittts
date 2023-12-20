from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset
from pydub import AudioSegment
import os
import video_generator as vg
import wave

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")


def create_post_audio(title, text):
    post_title = title
    post_content = text.split(".")
    
    for x, sentence in enumerate(post_content):
        
        duration = 0

        inputs = processor(text=sentence, return_tensors="pt")

        # load xvector containing speaker's voice characteristics from a dataset
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        speaker_embeddings = torch.tensor(embeddings_dataset[6450]["xvector"]).unsqueeze(0)#7200#77199

        speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

        sf.write(f"post/{x}.wav", speech.numpy(), samplerate=16000)
        
        with wave.open(f"post/{x}.wav",'r') as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                
        vg.make_clip(sentence, duration, x)
        

