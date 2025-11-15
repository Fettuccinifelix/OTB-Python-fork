from PyQt5 import QtWidgets
import pyqtgraph as pg

from app.device import SessantaquattroPlus
from app.window import SoundtrackWindow


def main():
    app = QtWidgets.QApplication([])
    pg.setConfigOptions(antialias=True)
    
    '''
    # Configure device with specific parameters
    FSAMP = 0  # 2000 Hz
    NCH = 0    # 64 channels
    MODE = 0   # Standard mode
    HRES = 0   # Normal resolution
    HPF = 0    # High-pass filter enabled
    EXTEN = 0  # External trigger disabled
    TRIG = 0   # Trigger mode disabled
    REC = 0    # Recording disabled
    GO = 0     # Start acquisition
    '''

    device = SessantaquattroPlus()
    device.create_command(FSAMP=0, NCH=0, MODE=0, HRES=0, HPF=0, EXTEN=0, TRIG=0, REC=0, GO=0)
    device.start_server()

    window = SoundtrackWindow(device, device.client_socket)
    window.show()

    app.exec_()


if __name__ == "__main__":
    main()
