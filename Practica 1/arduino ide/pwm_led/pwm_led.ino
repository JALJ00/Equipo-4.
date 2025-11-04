#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "InstVirtual";                    // NOTA: cambiar este parametro antes de grabar el programa en el ESP32
const char* password = "37418601";                 // NOTA: cambiar este parametro antes de grabar el programa en el ESP32

const char* mqtt_server = "192.168.0.102";           // servidor MQTT

long lastMsg = 0;
int conta = 0;
char msg[20];
int valPot = 0;

WiFiClient espClient;                                   // creamos un objeto de la clase WiFiClient
PubSubClient client(espClient);                         // creamos un objeto de la clase PubSubClient


void setup(){
  Serial.begin(115200);                                 // iniciamos la UART a 115200
  pinMode(25, OUTPUT);                                   // GPIO17 como entrada
  pinMode(26, OUTPUT);                                  // GPIO26 como salida
  setup_wifi();                                         // iniciamos la conexion a la red WiFi
  client.setServer(mqtt_server, 1883);                  // conectamos el ESP32 al serviro MQTT por el puerto 1883
  client.setCallback(callback);                         // creamos una funcion callback para recibir los datos del servidor
}

void setup_wifi(){
  Serial.print("\nConectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);                           // iniciamos la conexion al router
  while(WiFi.status() != WL_CONNECTED){                 // si no se ha podido conectar intentamas una reconexion medio segundo despues
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());                       // imprimimos la IP que nos asigno el router
}

/* Esta funcion recibe los datos del servidor cuando un cliente publica informacion al topico. 
 *  topic: Es el topico al que se ha publicado
 *  message: Es el mensaje que el cliente publico
 *  length: Este es el tamaño del mensaje
*/
void callback(char* topic, byte* message, unsigned int length){
  String msgTemp;                                       // creamos un string donde vamos a guardar el mensaje
  
  for(int i = 0; i < length; i++){                      // convertimos todo los datos del mensaje de byte a char y lo concatenamos en msgTemp
    msgTemp += (char)message[i];
  }

  if(String(topic) == "7c/eq4p1/pwm1"){     
    int valorPWM1=msgTemp.toInt();                // comprobamos el topico que nos interesa 
    analogWrite(25,valorPWM1);                              // comprobamos el mensaje (payload) si es "ON"                      // apagamos el led en la patita 22
  }
  if(String(topic) == "7c/eq4p1/pwm2"){
    int valorPWM2=msgTemp.toInt();    
    analogWrite(26,valorPWM2);
}}

/* Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)*/
void reconnect(){
  while(!client.connected()){                           // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");   
    if(client.connect("7cEquipo4_pwm")){                        // si el cliente ya se conecto al servidor
      Serial.println("conectado");
      client.subscribe("7c/eq4p1/pwm1"); 
      client.subscribe("7c/eq4p1/pwm2");                    // no suscribimos al topico que desamos (esto no es obligatorio si solo se va a publicar)
    }else{
      Serial.print("Fallo, rc = ");                     // si hay alguna falla en la conexion
      Serial.print(client.state());                     // desplegamos el error de conexion
      Serial.println("Reintentando en 5 segundo...");   // reintentamos una reconexion en 5 segundos
      delay(5000);
    }
  }
}

void loop(){
  if(!client.connected()){                              // checamos si el cliente esta conectado al servidor
    reconnect();                                        // si no esta conectado reconectamos el cliente al servidor
  }
  client.loop();                                        // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
}