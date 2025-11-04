import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_practica1 import Ui_MainWindow
import paho.mqtt.client as mqtt


class MiVentan(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLed1.clicked.connect(self.toogleLed1)
        self.btnLed2.clicked.connect(self.toogleLed2)
        self.btnLed3.clicked.connect(self.toogleLed3)
        self.btnLed4.clicked.connect(self.toogleLed4)
        self.btnLed5.clicked.connect(self.toogleLed5)
        self.btnLed6.clicked.connect(self.toogleLed6)
        self.btnLed7.clicked.connect(self.toogleLed7)
        self.btnLed8.clicked.connect(self.toogleLed8)
        self.scbPwm1.valueChanged.connect(self.PWM1)
        self.scbPwm2.valueChanged.connect(self.PWM2)


        self.cmdConectar.clicked.connect(self.conectar)
        self.cmdSalir.clicked.connect(self.salir)

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe("7c/eq4/adc1", qos=1)
        self.client.subscribe("7c/eq4/adc2", qos=1)
        self.client.subscribe("7c/eq4/adc3", qos=1)
        self.client.subscribe("7c/eq4/adc4", qos=1)
        self.client.subscribe("7c/eq4/bt1", qos=1)
        self.client.subscribe("7c/eq4/bt2", qos=1)
        self.client.subscribe("7c/eq4/bt3", qos=1)
        self.client.subscribe("7c/eq4/bt4", qos=1)
        self.client.subscribe("7c/eq4/bt5", qos=1)
        self.client.subscribe("7c/eq4/bt6", qos=1)
        self.client.subscribe("7c/eq4/bt7", qos=1)
        self.client.subscribe("7c/eq4/bt8", qos=1)

        print("Suscrito")

    def PWM1(self):
        self.lblpwm1.setText(str(self.scbPwm1.value()))
        self.client.publish("7c/eq4p1/pwm1", str(self.scbPwm1.value()))

    def PWM2(self):
        self.lblpwm2.setText(str(self.scbPwm2.value()))
        self.client.publish("7c/eq4p1/pwm2", str(self.scbPwm2.value()))
    def on_message(self, client, userdata, msg):

        if msg.topic == "7c/eq4/adc1":
            datoAdc1 = str(msg.payload.decode("utf-8"))
            datoAdc1 = int(datoAdc1)
            self.barAdc1.setValue(datoAdc1)
        elif msg.topic == "7c/eq4/adc2":
            datoAdc2 = str(msg.payload.decode("utf-8"))
            datoAdc2 = int(datoAdc2)
            self.barAdc2.setValue(datoAdc2)
        elif msg.topic == "7c/eq4/adc3":
            datoAdc3 = str(msg.payload.decode("utf-8"))
            datoAdc3 = int(datoAdc3)
            self.barAdc3.setValue(datoAdc3)
        elif msg.topic == "7c/eq4/adc4":
            datoAdc4 = str(msg.payload.decode("utf-8"))
            datoAdc4 = int(datoAdc4)
            self.barAdc4.setValue(datoAdc4)

        elif msg.topic == "7c/eq4/bt1":
            datoBoton1 = str(msg.payload.decode("utf-8"))
            self.lblBoton1.setText(datoBoton1)
        elif msg.topic == "7c/eq4/bt2":
            datoBoton2 = str(msg.payload.decode("utf-8"))
            self.lblBoton2.setText(datoBoton2)
        elif msg.topic == "7c/eq4/bt3":
            datoBoton3 = str(msg.payload.decode("utf-8"))
            self.lblBoton3.setText(datoBoton3)
        elif msg.topic == "7c/eq4/bt4":
            datoBoton4 = str(msg.payload.decode("utf-8"))
            self.lblBoton4.setText(datoBoton4)
        elif msg.topic == "7c/eq4/bt5":
            datoBoton5 = str(msg.payload.decode("utf-8"))
            self.lblBoton5.setText(datoBoton5)
        elif msg.topic == "7c/eq4/bt6":
            datoBoton6 = str(msg.payload.decode("utf-8"))
            self.lblBoton6.setText(datoBoton6)
        elif msg.topic == "7c/eq4/bt7":
            datoBoton7 = str(msg.payload.decode("utf-8"))
            self.lblBoton7.setText(datoBoton7)
        elif msg.topic == "7c/eq4/bt8":
            datoBoton8 = str(msg.payload.decode("utf-8"))
            self.lblBoton8.setText(datoBoton8)
        elif msg.topic == "7c/eq4/pwm1":
            datopwm1 = str(msg.payload.decode("utf-8"))
            datopwm1 = int(datopwm1)
            self.scbPwm1.setValue(datopwm1)
        elif msg.topic == "7c/eq4/pwm2":
            datopwm2 = str(msg.payload.decode("utf-8"))
            datopwm2 = int(datopwm2)
            self.scbPwm2.setValue(datopwm2)

    def toogleLed1(self):
        if self.btnLed1.text() == "ON":
            self.btnLed1.setText("OFF")
            self.client.publish("eq4p1/led1", "ON")
        else:
            self.btnLed1.setText("ON")
            self.client.publish("eq4p1/led1", "OFF")

    def toogleLed2(self):
        if self.btnLed2.text() == "ON":
            self.btnLed2.setText("OFF")
            self.client.publish("eq4p1/led2", "ON")
        else:
            self.btnLed2.setText("ON")
            self.client.publish("eq4p1/led2", "OFF")

    def toogleLed3(self):
        if self.btnLed3.text() == "ON":
            self.btnLed3.setText("OFF")
            self.client.publish("eq4p1/led3", "ON")
        else:
            self.btnLed3.setText("ON")
            self.client.publish("eq4p1/led3", "OFF")

    def toogleLed4(self):
        if self.btnLed4.text() == "ON":
            self.btnLed4.setText("OFF")
            self.client.publish("eq4p1/led4", "ON")
        else:
            self.btnLed4.setText("ON")
            self.client.publish("eq4p1/led4", "OFF")

    def toogleLed5(self):
        if self.btnLed5.text() == "ON":
            self.btnLed5.setText("OFF")
            self.client.publish("eq4p1/led5", "ON")
        else:
            self.btnLed5.setText("ON")
            self.client.publish("eq4p1/led5", "OFF")

    def toogleLed6(self):
        if self.btnLed6.text() == "ON":
            self.btnLed6.setText("OFF")
            self.client.publish("eq4p1/led6", "ON")
        else:
            self.btnLed6.setText("ON")
            self.client.publish("eq4p1/led6", "OFF")

    def toogleLed7(self):
        if self.btnLed7.text() == "ON":
            self.btnLed7.setText("OFF")
            self.client.publish("eq4p1/led7", "ON")
        else:
            self.btnLed7.setText("ON")
            self.client.publish("eq4p1/led7", "OFF")

    def toogleLed8(self):
        if self.btnLed8.text() == "ON":
            self.btnLed8.setText("OFF")
            self.client.publish("eq4p1/led8", "ON")
        else:
            self.btnLed8.setText("ON")
            self.client.publish("eq4p1/led8", "OFF")

    def conectar(self):
        self.client.connect(host="192.168.0.102", port=1883, keepalive=60)
        self.client.loop_start()

    def salir(self):
        try:
            self.client.unsubscribe("7c/eq4/adc1")
            self.client.unsubscribe("7c/eq4/adc2")
            self.client.unsubscribe("7c/eq4/adc3")
            self.client.unsubscribe("7c/eq4/adc4")
            self.client.unsubscribe("7c/eq4/bt1")
            self.client.unsubscribe("7c/eq4/bt2")
            self.client.unsubscribe("7c/eq4/bt3")
            self.client.unsubscribe("7c/eq4/bt4")
            self.client.unsubscribe("7c/eq4/bt5")
            self.client.unsubscribe("7c/eq4/bt6")
            self.client.unsubscribe("7c/eq4/bt7")
            self.client.unsubscribe("7c/eq4/bt8")
        except:
            print("Fallo al desconectar")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    venta = MiVentan()
    venta.show()
    sys.exit(app.exec())