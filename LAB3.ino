#include "DHT.h"

DHT dht;
int vccPin;
int dataPin;

/*  Seleciona modelo do arduino
 *  0 = UNO, MEGA ou LEONARDO
 *  1 = NANO
 */
int arduino = 0;


void setup()
{
  Serial.begin(9600);
  Serial.println();
  Serial.println("Status\tHumidity (%)\tTemperature (C)\t(F)");

  if(arduino == 0) {
    vccPin = 11;
    dataPin = 12;
  } else {
    vccPin = 4;
    dataPin = 3;
  }

  pinMode(vccPin, OUTPUT);
  digitalWrite(vccPin, HIGH);
  dht.setup(dataPin); // data pin 2
}

void loop()
{
  delay(15000); // taxa de amostragem minima thingspeak

  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();

  Serial.print(temperature);
  Serial.print(" ");
  Serial.println(humidity);
}
