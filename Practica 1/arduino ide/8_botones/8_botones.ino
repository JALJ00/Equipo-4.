// Modificar su SSID y PASSWORD de su red antes de compilar y grabar al ESP32

#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "NOMBRE_DE_SU_RED";                    // NOTA: cambiar este parametro antes de grabar el programa en el ESP32
const char* password = "CLAVE_DE_SU_RED";                 // NOTA: cambiar este parametro antes de grabar el programa en el ESP32

const char* mqtt_server = "test.mosquitto.org";           // servidor MQTT

long lastMsg = 0;
int conta = 0;
char msg[20];
int valPot = 0;

WiFiClient espClient;                                   // creamos un objeto de la clase WiFiClient
PubSubClient client(espClient);                         // creamos un objeto de la clase PubSubClient


void setup(){
  Serial.begin(115200);                                 // iniciamos la UART a 115200
  pinMode(17, INPUT);
  pinMode(18, INPUT);
  pinMode(19, INPUT);
  pinMode(21, INPUT);
  pinMode(22, INPUT);
  pinMode(23, INPUT);
  pinMode(25, INPUT);
  pinMode(26, INPUT);                                   // GPIO17 como entrada                                  // GPIO26 como salida
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

  if(String(topic) == "esp32/led"){                     // comprobamos el topico que nos interesa
    if(msgTemp == "ON")                                 // comprobamos el mensaje (payload) si es "ON"
      digitalWrite(26, HIGH);                           // y encedemos el led conectador a la patita 22
    else if(msgTemp == "OFF")                           // si el mensaje que llego es "OFF"
      digitalWrite(26, LOW);                            // apagamos el led en la patita 22
  }
}

/* Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)*/
void reconnect(){
  while(!client.connected()){                           // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");   
    if(client.connect("ESP32_2")){                        // si el cliente ya se conecto al servidor
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
    if(digitalRead(17) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt1", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt1", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(18) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt2", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt2", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(19) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt3", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt3", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(21) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt4", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt4", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(22) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt5", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt5", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(23) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt6", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt6", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(25) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt7", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt7", "0");               // o publicamos un "1" si el boton no esta presionado
    }
    if(digitalRead(26) == 1){                           // verificamos el estado de la entrada 17
      client.publish("7c/eq4/bt8", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("7c/eq4/bt8", "0");               // o publicamos un "1" si el boton no esta presionado
    }
  client.loop();                                        // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
}