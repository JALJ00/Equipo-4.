// Modificar su SSID y PASSWORD de su red antes de compilar y grabar al ESP32

#if defined(ESP32)
#include <WiFi.h>
#elif defined(ARDUINO_UNOWIFIR4)
#include <WiFiS3.h>
#endif
#include <PubSubClient.h>

const char* ssid = "InstVirtual";   // NOTA: este nombre de red es solo en UTT en su casa cambiar por el nombre de su red.
const char* password = "37418601";  // NOTA: esta es la contraseña de la red en UTT en su casa cambiar por la contraseña de su red.

const char* mqtt_server = "192.168.0.102";             // servidor MQTT local (en UTT)
//const char* mqtt_server = "test.mosquitto.org";  // servidor MQTT en la nube (en su casa)

long lastMsg = 0;
int conta = 0;
char msg[20];
int valPot = 0;

WiFiClient espClient;            // creamos un objeto de la clase WiFiClient
PubSubClient client(espClient);  // creamos un objeto de la clase PubSubClient


void setup() {
  Serial.begin(115200);  // iniciamos la UART a 115200
  pinMode(17, OUTPUT);   // GPIO17 como entrada
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(21, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);

  setup_wifi();                         // GPIO26 como salida
  client.setServer(mqtt_server, 1883);  // conectamos el ESP32 al serviro MQTT por el puerto 1883
  client.setCallback(callback);

  digitalWrite(17, LOW);
  digitalWrite(18, LOW);
  digitalWrite(19, LOW);
  digitalWrite(21, LOW);
  digitalWrite(22, LOW);
  digitalWrite(23, LOW);
  digitalWrite(25, LOW);
  digitalWrite(26, LOW);  // creamos una funcion callback para recibir los datos del servidor
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
void callback(char* topic, byte* message, unsigned int length) {
  String msgTemp;  // creamos un string donde vamos a guardar el mensaje

  for (int i = 0; i < length; i++) {  // convertimos todo los datos del mensaje de byte a char y lo concatenamos en msgTemp
    msgTemp += (char)message[i];
  }

  if (String(topic) == "eq4p1/led1") {  //LED 1
    if (msgTemp == "ON")
      digitalWrite(17, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(17, LOW);
  }
  if (String(topic) == "eq4p1/led2") {  //LED 2
    if (msgTemp == "ON")
      digitalWrite(18, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(18, LOW);
  }
  if (String(topic) == "eq4p1/led3") {
    if (msgTemp == "ON")
      digitalWrite(19, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(19, LOW);
  }
  if (String(topic) == "eq4p1/led4") {
    if (msgTemp == "ON")
      digitalWrite(21, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(21, LOW);
  }
  if (String(topic) == "eq4p1/led5") {
    if (msgTemp == "ON")
      digitalWrite(22, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(22, LOW);
  }
  if (String(topic) == "eq4p1/led6") {
    if (msgTemp == "ON")
      digitalWrite(23, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(23, LOW);
  }
  if (String(topic) == "eq4p1/led7") {
    if (msgTemp == "ON")
      digitalWrite(25, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(25, LOW);
  }
  if (String(topic) == "eq4p1/led8") {
    if (msgTemp == "ON")
      digitalWrite(26, HIGH);
    else if (msgTemp == "OFF")
      digitalWrite(26, LOW);
  }
}
/* Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)*/
void reconnect() {
  while (!client.connected()) {  // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");
    if (client.connect("ESP32_eq4p1")) {  // si el cliente ya se conecto al servidor
      Serial.println("conectado");
      client.subscribe("eq4p1/led1");
      client.subscribe("eq4p1/led2");
      client.subscribe("eq4p1/led3");
      client.subscribe("eq4p1/led4");
      client.subscribe("eq4p1/led5");
      client.subscribe("eq4p1/led6");
      client.subscribe("eq4p1/led7");
      client.subscribe("eq4p1/led8");  // no suscribimos al topico que desamos (esto no es obligatorio si solo se va a publicar)
    } else {
      Serial.print("Fallo, rc = ");                    // si hay alguna falla en la conexion
      Serial.print(client.state());                    // desplegamos el error de conexion
      Serial.println("Reintentando en 5 segundo...");  // reintentamos una reconexion en 5 segundos
      delay(10000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();  // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
}