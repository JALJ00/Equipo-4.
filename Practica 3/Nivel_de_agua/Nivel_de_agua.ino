#if defined(ESP32)
#include <WiFi.h>
#elif defined(ARDUINO_UNOWIFIR4)
#include <WiFiS3.h>
#endif

#include <PubSubClient.h>

const char* ssid = "InstVirtual";   // NOTA: este nombre de red es solo en UTT en su casa cambiar por el nombre de su red.
const char* password = "37418601";  // NOTA: esta es la contraseña de la red en UTT en su casa cambiar por la contraseña de su red.

const char* mqtt_server = "192.168.0.102";

long lastMsg = 0;
int conta = 0;
char msg[20];
int TRIG = 17;
int ECHO = 26;

WiFiClient espClient;            // creamos un objeto de la clase WiFiClient
PubSubClient client(espClient);  // creamos un objeto de la clase PubSubClient


void setup() {
  Serial.begin(115200);
  pinMode(17, OUTPUT);                  //TRIG
  pinMode(26, INPUT);                   //ECHO
  setup_wifi();                         // iniciamos la conexion a la red WiFi
  client.setServer(mqtt_server, 1883);  // conectamos el ESP32 al serviro MQTT por el puerto 1883
  client.setCallback(callback);         // creamos una funcion callback para recibir los datos del servidor
}

void setup_wifi() {
  Serial.print("\nConectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);              // iniciamos la conexion al router
  while (WiFi.status() != WL_CONNECTED) {  // si no se ha podido conectar intentamas una reconexion medio segundo despues
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());  // imprimimos la IP que nos asigno el router
}

/* Esta funcion recibe los datos del servidor cuando un cliente publica informacion al topico. 
 *  topic: Es el topico al que se ha publicado
 *  message: Es el mensaje que el cliente publico
 *  length: Este es el tamaño del mensaje
*/
void callback(char* topic, byte* message, unsigned int length)

{
  String msgTemp;  // creamos un string donde vamos a guardar el mensaje

  for (int i = 0; i < length; i++) {  // convertimos todo los datos del mensaje de byte a char y lo concatenamos en msgTemp esta parte tambien son los datos a mandar
    msgTemp += (char)message[i];
  }
}


/* Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)*/
void reconnect() {
  while (!client.connected()) {  // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");
    if (client.connect("ESP32_Na_eq4")) {  // si el cliente ya se conecto al servidor
      Serial.println("conectado");
      // no suscribimos al topico que desamos (esto no es obligatorio si solo se va a publicar)
    } else {
      Serial.print("Fallo, rc = ");                    // si hay alguna falla en la conexion
      Serial.print(client.state());                    // desplegamos el error de conexion
      Serial.println("Reintentando en 5 segundo...");  // reintentamos una reconexion en 5 segundos
      delay(5000);
    }
  }
}


void loop() {
  if (!client.connected()) {  // checamos si el cliente esta conectado al servidor
    reconnect();              // si no esta conectado reconectamos el cliente al servidor
  }

  long varNow = millis();
  if (varNow - lastMsg > 500) {  // esperamos 500 milisegundos
    lastMsg = varNow;
    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);
    long duracion = pulseIn(ECHO, HIGH);
    if (duracion > 0){
      float distancia = duracion * 0.0343 / 2;
    if (distancia >= 1 && distancia <= 20) {
      dtostrf(distancia, 4, 1, msg);// Utilizamos dtostrf para convertir el valor float a string en vez de int
       client.publish("7c/eq4/cui", msg);
    }
    }
  }
  client.loop();  // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
}
