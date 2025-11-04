// Modificar su SSID y PASSWORD de su red antes de compilar y grabar al ESP32

// Modificar su SSID y PASSWORD de su red antes de compilar y grabar al ESP32

#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "InstVirtual";                    // NOTA: cambiar este parametro antes de grabar el programa en el ESP32
const char* password = "37418601";                 // NOTA: cambiar este parametro antes de grabar el programa en el ESP32

const char* mqtt_server = "192.168.0.102";           // servidor MQTT

long lastMsg = 0;
int conta = 0;
char msg[20];
int valPot1 = 0;
int valPot2 = 0;
int valPot3 = 0;
int valPot4 = 0;

WiFiClient espClient;                                   // creamos un objeto de la clase WiFiClient
PubSubClient client(espClient);                         // creamos un objeto de la clase PubSubClient


void setup(){
  Serial.begin(115200);                                 // iniciamos la UART a 115200
  pinMode(32, INPUT);                                   // GPIO17 como entrada
  pinMode(36, INPUT);
  pinMode(34, INPUT);
  pinMode(35, INPUT);                                  // GPIO26 como salida
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

                
}

/* Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)*/
void reconnect(){
  while(!client.connected()){                           // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");   
    if(client.connect("ESP32_2_pwm")){                        // si el cliente ya se conecto al servidor
      Serial.println("conectado");
      client.subscribe("esp32/led");                    // no suscribimos al topico que desamos (esto no es obligatorio si solo se va a publicar)
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
  
  long varNow = millis();
  if(varNow - lastMsg > 500){                           // esperamos 500 milisegundos
    lastMsg = varNow;
    valPot1 = analogRead(32);
    delay(10);
    sprintf(msg,"%d", valPot1);
    client.publish("7c/eq4/adc1", msg);
    
    
    valPot2 = analogRead(36);
    delay(10);
    sprintf(msg,"%d", valPot2);
    client.publish("7c/eq4/adc2", msg);
    
    valPot3 = analogRead(34);
    delay(10);
    sprintf(msg,"%d", valPot3);
    client.publish("7c/eq4/adc3", msg);
    
    valPot4 = analogRead(35);
    delay(10);
    sprintf(msg,"%d", valPot4);
    client.publish("7c/eq4/adc4", msg);
    
  }
  client.loop();                                        // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
}