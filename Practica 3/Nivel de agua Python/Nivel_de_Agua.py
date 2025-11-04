import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Nivel_de_agua import Ui_MainWindow
import paho.mqtt.client as mqtt

class MiVentan(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        #self.client.subscribe("esp32/adc", qos=1)
        '''recibes datos del topico'''
        print("Suscrito")

    def on_message(self, client, userdata, msg):
        if msg.topic == "7c/eq4/cui":
            progressBar = str(msg.payload.decode("utf-8"))
            progressBar = int(progressBar)
            self.ProBar.setValue(progressBar)

    def conectar(self):
        #self.client.connect(host="test.mosquitto.org", port=1883, keepalive=60)    # broker en la nube usar cuando esten en su casa
        self.client.connect(host="192.168.0.102", port=1883, keepalive=60)         # broker local usar cuando esten en UTT
        self.client.loop_start()

    def salir(self):
        try:
            self.client.unsubscribe("7c/eq4/cui")
        except:
            print("Fallo al desconectar")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    venta = MiVentan()
    venta.show()

    sys.exit(app.exec())