
#include <Servo.h>
Servo servoVer; //Vertical Servo
Servo servoHor;
Servo crawler; //Horizontal Servo
int x;
int y;
int z;
int prevX;
int prevY;
int prevz; 
void setup()
{
  Serial.begin(9600);
  servoVer.attach(10); //Attach Vertical Servo to Pin 5
  servoHor.attach(9);
  crawler.attach(6);
   //Attach Horizontal Servo to Pin 6
  servoVer.write(0);
  servoHor.write(90);
  crawler.write(90);
}
void Pos()
{
  if(prevX != x || prevY != y || prevz != z )
  {
    int servoX = map(x, 10, 600, 0, 180);
    int servoY = map(y, 10, 300, 0, 60);
    int servoz = map(y, 10, 300, 0, 90);

    servoX = min(servoX, 179);
    servoX = max(servoX, 0);
    servoY = min(servoY, 60);
    servoY = max(servoY, 0);
    servoz = min(servoz, 60);
    servoz = max(servoz, 0);
    
    
    servoHor.write(servoX);
    servoVer.write(servoY);
    crawler.write(servoz);
  }
}
void loop()
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if(Serial.read() == 'Y')
      {
        y = Serial.parseInt();
        if(Serial.read() == 'Z')
    {
      z = Serial.parseInt();
       Pos();
      }
      
    }
    while(Serial.available() > 0)
    {
      Serial.read();
    }
  }
}
}
