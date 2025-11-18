import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, Signal, Slot
from ui_interfaz import Ui_MainWindow
import paho.mqtt.client as mqtt


# PASO 1: Crear el "Mensajero" (para comunicación segura entre threads)
class Mensajero(QObject):
    """
    Este es nuestro sistema de mensajería seguro.
    Cuando MQTT recibe datos, usa este mensajero para avisar a la ventana.
    """
    # Definimos UN SOLO mensaje que lleva: el nombre del sensor y su valor (como string)
    datos_recibidos = Signal(str, str)  # (nombre_sensor, valor_como_texto)


# PASO 2: Crear la Ventana Principal
class MiVentana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Crear nuestro mensajero
        self.mensajero = Mensajero()

        # Cuando se reciba un dato, se enviara a la funcion que muestra los datos"
        self.mensajero.datos_recibidos.connect(self.mostrar_en_pantalla)

        self.cmdConectar.clicked.connect(self.conectar)
        self.cmdSalir.clicked.connect(self.salir)

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    # FUNCIONES DE MQTT (se ejecutan en un thread aparte)
    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe("7C/Equipo4/temp1", qos=0)
        self.client.subscribe("7C/Equipo4/temp2", qos=0)
        self.client.subscribe("7C/Equipo4/temp3", qos=0)
        self.client.subscribe("7C/Equipo4/temp4", qos=0)

        self.client.subscribe("7C/Equipo4/hum1", qos=0)
        self.client.subscribe("7C/Equipo4/hum2", qos=0)

        print("Suscrito")

    def on_message(self, client, userdata, msg):
        """
        Esta función se ejecuta cada vez que llega un mensaje de MQTT.
        """
        try:
            sensor = str(msg.payload.decode("utf-8"))
            topico = msg.topic

            # El mensajero se encargará de avisar a la pantalla
            self.mensajero.datos_recibidos.emit(topico, sensor)

        except Exception as e:
            print(f"Error: No se pudo leer el mensaje del sensor: {e}")

    # FUNCIÓN DE ACTUALIZACIÓN DE PANTALLA (se ejecuta en el thread principal)
    @Slot(str, str)
    def mostrar_en_pantalla(self, topico, valor):
        """
        Esta función se ejecuta en el thread principal, por eso SÍ puede modificar la interfaz.

        Parámetros:
        - nombre_sensor: El tópico completo, ejemplo "7C/Equipo4/temp1"
        - valor: El valor que envió el sensor (como string)
        """
        try:
            if topico == "7C/Equipo4/temp1":
                temp1 = int(valor)
                self.pbTemp1.setValue(temp1)
                self.lblTemp1.setText(str(temp1))

            elif topico == "7C/Equipo4/temp2":
                temp2 = int(valor)
                self.pbTemp2.setValue(temp2)
                self.lblTemp2.setText(str(temp2))

            elif topico == "7C/Equipo4/temp3":
                temp3 = int(valor)
                self.pbTemp3.setValue(temp3)
                self.lblTemp3.setText(str(temp3))

            elif topico == "7C/Equipo4/temp4":
                temp4 = int(valor)
                self.pbTemp4.setValue(temp4)
                self.lblTemp4.setText(str(temp4))

            elif topico == "7C/Equipo4/hum1":
                hum1 = int(valor)
                self.pbHum1.setValue(hum1)
                self.lblHum1.setText(str(hum1))

            elif topico == "7C/Equipo4/hum2":
                hum2 = int(valor)
                self.pbHum2.setValue(hum2)
                self.lblHum2.setText(str(hum2))

        except ValueError:
            print(f"Error")

    def conectar(self):
        print("Conectando al broker...")
        self.client.connect(host="192.168.0.102", port=1883, keepalive=30)
        #self.client.connect(host="test.mosquitto.org", port=1883, keepalive=30)
        self.client.loop_start()

    def salir(self):
        print("Desconectando...")

        try:
            # Cancelar las suscripciones
            self.client.unsubscribe("7C/Equipo4/temp1")
            self.client.unsubscribe("7C/Equipo4/temp2")
            self.client.unsubscribe("7C/Equipo4/temp3")
            self.client.unsubscribe("7C/Equipo4/temp4")
            self.client.unsubscribe("7C/Equipo4/hum1")
            self.client.unsubscribe("7C/Equipo4/hum2")
            self.client.loop_stop()
            self.client.disconnect()
            print("Desconectado correctamente")
        except:
            print("Fallo al desconectar")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())