from time import perf_counter, perf_counter_ns
import wave
import numpy as np
import argparse
import pyaudio

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', 
                    type=str ,
                    help='Specifies a file to be opened', 
                    required=True) 
args = parser.parse_args()

file = open(args.file)

from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    import deepspeech

    model_file_path = "deepspeech-0.9.3-models.pbmm"
    beam_width = 500
    model = deepspeech.Model(model_file_path, beam_width)
    test_file = ""

    #Speech Recognition By WAV File
    w = wave.open(args.file, 'r')
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)
    #print(rate)
    #print(model.sampleRate())
    print('\n')
    print("Test: Pass a file directly into a local instance of DeepSpeech")
    timer_start = perf_counter_ns()
    type(buffer)

    data16 = np.frombuffer(buffer, dtype=np.int16)
    type(data16)

    text = model.stt(data16)
    print("End String: ", text)
    timer_end = perf_counter_ns()
    print("Test completed in ", (timer_end-timer_start) / 1000000000, " seconds")
    print('\n','\n')

    #Speech Recognition By Streaming
    print("Test: Simulate audio being processed as its coming in from the microphone")

    timer_start = perf_counter_ns()
    context = model.createStream()
    buffer_len = len(buffer)
    offset = 0
    batch_size = 16384
    text = ''

    while offset < buffer_len:
        end_offset = offset + batch_size
        chunk = buffer[offset:end_offset]
        data16 = np.frombuffer(chunk, dtype=np.int16)
        model.feedAudioContent(context, data16)
        text = model.intermediateDecode(context)
        print(text)
        offset = end_offset

    text = model.finishStream(context)
    print('\n')
    print("End String: ", text)
    print('\n')
    timer_end = perf_counter_ns()
    print("Test completed in ", (timer_end-timer_start) / 1000000000, " seconds")
    print('\n','\n')
elif platform == "darwin":
    # OS X
    None
elif platform == "win32":
    # Windows...
    #Test stream the microphone into a file and send it to the server
    timer_start = perf_counter_ns()

    # the file name output you want to record into
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 2
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(sample_rate / chunk * record_seconds)):
            data = stream.read(chunk)
            # if you want to hear your voice while recording
            # stream.write(data)
            frames.append(data)
    print("Finished recording.")
        # stop and close stream
    stream.stop_stream()
    stream.close()
        # terminate pyaudio object
    p.terminate()
        # save audio file
        # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
        # set the channels
    wf.setnchannels(channels)
        # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
        # set the sample rate
    wf.setframerate(sample_rate)
        # write the frames as bytes
    wf.writeframes(b"".join(frames))
        # close the file
    wf.close()

    data = open("recorded.wav", 'rb').read()
    response = requests.post('http://localhost:8080/stt', data)
    print("HTTP Response Code: ", response)
    print("Response Value: ", response.text)

    timer_end = perf_counter_ns()
    print("Test completed in ", (timer_end-timer_start) / 1000000000, " seconds")

#Speech recognition by server broadcast
import requests

print("Test: Broadcast audio data to local server for analysis")
timer_start = perf_counter_ns()
data = open(args.file, 'rb').read()
response = requests.post('http://localhost:8080/stt', data)
print("HTTP Response Code: ", response)
print("Response Value: ", response.text)
timer_end = perf_counter_ns()

print("Test completed in ", (timer_end-timer_start) / 1000000000, " seconds")

