import struct
import numpy as np
import time
from PyQt5 import QtCore
from app.processing.pipeline import ProcessingPipeline


class DataReceiverThread(QtCore.QThread):
    data_received = QtCore.pyqtSignal(np.ndarray)
    status_update = QtCore.pyqtSignal(str)

    def __init__(self, device, client_socket, tracks):
        super().__init__()
        self.device = device
        self.client_socket = client_socket
        self.tracks = tracks
        self.running = True
        self.packet_count = 0
        self.last_time = time.time()
        self.fps = 0
        self.processor = ProcessingPipeline()

    def run(self):
        packet_bytes = self.device.nchannels * 2 * (self.device.frequency // 16)

        while self.running:
            try:
                data = self.client_socket.recv(packet_bytes)
                if not data:
                    break

                unpacked = struct.unpack(f'>{len(data)//2}h', data)
                reshaped = np.array(unpacked).reshape((-1, self.device.nchannels)).T
                processed = self.processor.run(reshaped)

                idx = 0
                for track in self.tracks:
                    track.feed(processed[idx:idx + track.num_channels])
                    idx += track.num_channels

                self.data_received.emit(processed)

                self.packet_count += 1
                if self.packet_count % 100 == 0:
                    now = time.time()
                    elapsed = now - self.last_time
                    self.fps = 100 / elapsed if elapsed else 0
                    self.last_time = now
                    self.status_update.emit(f"Data rate: {self.fps:.1f} packets/s")

            except Exception as e:
                print(f"Receiver error: {e}")
                break

    def stop(self):
        self.running = False
