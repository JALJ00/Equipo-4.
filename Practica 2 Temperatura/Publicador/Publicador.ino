#include <DHT.h>
#include <DHT_U.h>

// Modificar su SSID y PASSWORD de su red antes de compilar y grabar al ESP32

#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ARDUINO_UNOWIFIR4)
  #include <WiFiS3.h>
#endif
#include <PubSubClient.h>
//inicializamos el pin del primer dht 11 
#define DHTPIN1 4
#define DHTTYPE DHT11
DHT dht1(DHTPIN1, DHTTYPE);
//inicializamos el pin del segundo dht 11 
#define DHTPIN2 5
#define DHTTYPE DHT11
DHT dht2(DHTPIN2, DHTTYPE);
//Creamos las variables que recibiran los datos del dht11 float para despues convertirla a int
float temp1=0;
float temp2=0;
float hum1=0;
float hum2=0;
int tempi1=0, tempi2=0, humi1=0, humi2=0;

//definimos los pines de los lm35
#define lm351 15
#define lm352 16
//variables que recibiran el valor de las entradas analogicas
int lectura1;
int lectura2;
//variables que almacenarian las temperaturas
int temp3=0;
int temp4=0;

//const char* ssid = "Totalplay-B0A5";                  
//const char* password = "B0A5E065b9DMfKr5";  
const char* ssid = "InstVirtual";                  
const char* password = "37418601";            

//const char* mqtt_server = "test.mosquitto.org";             
const char* mqtt_server = "192.168.0.102";                 

long lastMsg = 0;
char msg[20];


WiFiClient espClient;                                 
PubSubClient client(espClient);                         


void setup(){
  Serial.begin(115200);  
  dht1.begin();  
  dht2.begin();     
  #if defined(ESP32)
  WiFi.setSleep(false);
  #endif                       
  setup_wifi();                                        
  client.setServer(mqtt_server, 1883);    
  client.setKeepAlive(20);              
  //client.setCallback(callback);                         
}

void setup_wifi(){
  Serial.print("\nConectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);                          
  while(WiFi.status() != WL_CONNECTED){                
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());                       
}


 //Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)
void reconnect(){
  while(!client.connected()){                          
    Serial.print("\nReconectando servidor MQTT...");   
    if(client.connect("7CEquipo4_ESP32")){                        
      Serial.println("conectado");
      //client.subscribe("7C/Equipo4/led");                   
    }else{
      Serial.print("Fallo, rc = ");                     
      Serial.print(client.state());                     
      Serial.println("Reintentando en 5 segundo...");  
      delay(3000);
    }
  }
}

void loop(){
  if(!client.connected()){                             
    reconnect();                                        
  }
  client.loop();
  
  long varNow = millis();
  if(varNow - lastMsg > 450){                          
    lastMsg = varNow;
    //recibe los valores de los lm35
    lectura1= analogRead(lm351);
    lectura2= analogRead(lm352);
    //recibe los datos de los dht em float por que es en el tipo de dato que devuelve la funcion
    temp1 = dht1.readTemperature(); 
    temp2 = dht2.readTemperature();
    hum1 = dht1.readHumidity();
    hum2=dht2.readHumidity();
    //convierte los datos recibidos a int
    //No afecta los datos porque el dht11 devuelve datos enteros
    tempi1 = (int)temp1;  
    tempi2 = (int)temp2; 
    humi1= (int)hum1;
    humi2=(int)hum2;
  
    //convierte los datos a temperatura (lm35)
    temp3=(int)((lectura1*3300.0/4095.0)/10.0);
    temp4=(int)((lectura2*3300.0/4095.0)/10.0);
    //convierte los datos a string y los envia
    sprintf(msg,"%d", tempi1);
    client.publish("7C/Equipo4/temp1", msg,false);
    sprintf(msg,"%d", tempi2);
    client.publish("7C/Equipo4/temp2", msg,false); 
    sprintf(msg,"%d", temp3);
    client.publish("7C/Equipo4/temp3", msg, false); 
    sprintf(msg,"%d", temp4);
    client.publish("7C/Equipo4/temp4", msg, false); 
    sprintf(msg,"%d", humi1);
    client.publish("7C/Equipo4/hum1", msg, false); 
    sprintf(msg,"%d", humi2);
    client.publish("7C/Equipo4/hum2", msg, false); 
  }        
  }
                                      // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
