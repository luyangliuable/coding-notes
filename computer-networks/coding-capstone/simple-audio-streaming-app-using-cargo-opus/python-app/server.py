import socket
import pyaudio

# Socket configuration
HOST = 'localhost'
PORT = 50007

# PyAudio configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

# Create a server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()
    data = conn.recv(CHUNK)

    while data != '':
        stream.write(data)
        data = conn.recv(CHUNK)

# Stop PyAudio
stream.stop_stream()
stream.close()
p.terminate()
