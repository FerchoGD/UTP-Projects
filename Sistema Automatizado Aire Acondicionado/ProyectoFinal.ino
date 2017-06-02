#include <LiquidCrystal.h>
#include <stdlib.h>
#include <Fuzzy.h>
#include <FuzzyComposition.h>
#include <FuzzyInput.h>
#include <FuzzyIO.h>
#include <FuzzyOutput.h>
#include <FuzzyRule.h>
#include <FuzzyRuleAntecedent.h>
#include <FuzzyRuleConsequent.h>
#include <FuzzySet.h>
#include <FuzzyRule.h>
#include <FuzzyComposition.h>
#include <Fuzzy.h>
#include <FuzzyRuleConsequent.h>
#include <FuzzyOutput.h>
#include <FuzzyInput.h>
#include <FuzzyIO.h>
#include <FuzzySet.h>
#include <FuzzyRuleAntecedent.h>


Fuzzy* fuzzy=new Fuzzy();

LiquidCrystal lcd(12,11,5,4,3,2);
int ventil=13;

void setup() {
  // put your setup code here, to run once:

  lcd.begin(16,2);

  Serial.begin(9600); //Se inicia la comunicación serial Baudios para comunicación con PC
  //dht.begin(); //Se inicia el sensor

  //Espacio Para Iniciar los pines


  FuzzyInput* Pasajeros= new FuzzyInput(1);

  FuzzySet* Pocos= new FuzzySet(0,0,10,14);
  Pasajeros->addFuzzySet(Pocos);
  FuzzySet* Medio= new FuzzySet(12,16,18,22);
  Pasajeros->addFuzzySet(Medio);
  FuzzySet* Muchos= new FuzzySet(20,24,30,30);
  Pasajeros->addFuzzySet(Muchos);

  fuzzy->addFuzzyInput(Pasajeros);


  FuzzyInput* Temperatura= new FuzzyInput(2);

  FuzzySet* Ideal= new FuzzySet(20,20,22,25);
  Temperatura->addFuzzySet(Ideal);
  FuzzySet* Caliente= new FuzzySet(22,23,25,27);
  Temperatura->addFuzzySet(Caliente);
  FuzzySet* MuyCaliente= new FuzzySet(25,29,32,32);
  Temperatura->addFuzzySet(MuyCaliente);

  fuzzy->addFuzzyInput(Temperatura);


  FuzzyOutput* AireAcondicionado= new FuzzyOutput(1);

  FuzzySet* Baja= new FuzzySet(15,17,17,19);
  AireAcondicionado->addFuzzySet(Baja);
  FuzzySet* Media= new FuzzySet(18,20,20,22);
  AireAcondicionado->addFuzzySet(Media);
  FuzzySet* Alta= new FuzzySet(20,23,23,25);
  AireAcondicionado->addFuzzySet(Alta);
  
  fuzzy->addFuzzyOutput(AireAcondicionado);


  //#-----Regla 1 -----#

  FuzzyRuleAntecedent* CantidadPasajerosMuchoORMedio = new FuzzyRuleAntecedent();
  CantidadPasajerosMuchoORMedio->joinWithOR(Muchos,Medio);

  FuzzyRuleAntecedent* TemperaturaMuyCaliente = new FuzzyRuleAntecedent();
  TemperaturaMuyCaliente->joinSingle(MuyCaliente);

  FuzzyRuleAntecedent* IfPasajerosMuchoOrMedioANDTemperaturaMuyCaliente= new FuzzyRuleAntecedent();
  IfPasajerosMuchoOrMedioANDTemperaturaMuyCaliente->joinWithAND(CantidadPasajerosMuchoORMedio,TemperaturaMuyCaliente);

  FuzzyRuleConsequent* AireBajo= new FuzzyRuleConsequent();
  AireBajo->addOutput(Baja);

  FuzzyRule* fuzzyRule1= new FuzzyRule(1,IfPasajerosMuchoOrMedioANDTemperaturaMuyCaliente, AireBajo);
  fuzzy->addFuzzyRule(fuzzyRule1);


  //#-----Regla 2 ------#

  FuzzyRuleAntecedent* TemperaturaCaliente = new FuzzyRuleAntecedent();
  TemperaturaCaliente->joinSingle(Caliente);

  FuzzyRuleConsequent* AireMedia = new FuzzyRuleConsequent();
  AireMedia->addOutput(Media);

  FuzzyRule* fuzzyRule2= new FuzzyRule(2,TemperaturaCaliente,AireMedia);
  fuzzy->addFuzzyRule(fuzzyRule2);


  //#-----Regla 3 ------#

  FuzzyRuleAntecedent* PasajerosMuchosANDTemperaturaIdeal= new FuzzyRuleAntecedent();
  PasajerosMuchosANDTemperaturaIdeal->joinWithAND(Muchos,Ideal);

  FuzzyRule* fuzzyRule3= new FuzzyRule(3,PasajerosMuchosANDTemperaturaIdeal,AireMedia);
  fuzzy->addFuzzyRule(fuzzyRule3);
  

  //#------Regla 4------#

  FuzzyRuleAntecedent* PasajerosPocosORMedio= new FuzzyRuleAntecedent();
  PasajerosPocosORMedio->joinWithOR(Pocos,Medio);

  FuzzyRuleAntecedent* IfPasajerosPocosORMedioANDTemperaturaIdeal= new FuzzyRuleAntecedent();
  IfPasajerosPocosORMedioANDTemperaturaIdeal->joinWithAND(PasajerosPocosORMedio,Ideal);

  FuzzyRuleConsequent* AireAlta= new FuzzyRuleConsequent();
  AireAlta->addOutput(Alta);

  FuzzyRule* fuzzyRule4= new FuzzyRule(4,IfPasajerosPocosORMedioANDTemperaturaIdeal,AireAlta);
  fuzzy->addFuzzyRule(fuzzyRule4);

  //#--------Regla 5--------#
  FuzzyRuleAntecedent* PasajerosPocosANDTempMuyCaliente= new FuzzyRuleAntecedent();
  PasajerosPocosANDTempMuyCaliente->joinWithAND(Pocos,MuyCaliente);

  FuzzyRule* fuzzyRule5= new FuzzyRule(5,PasajerosPocosANDTempMuyCaliente,AireMedia);
  fuzzy->addFuzzyRule(fuzzyRule5);   

}

void loop() {
  // put your main code here, to run repeatedly:

  randomSeed(analogRead(0));
  int pasajeros= random(0,30);
  //float temperatura= random(20,32);
  
 
/*
  //Configurando el teclado matricial

  byte Pins_Filas[] = {39,41,43,45};     //Pines Arduino para las filas.
  byte Pins_Cols[] = { 47,49,51,53};     // Pines Arduino para las columnas.

  char Teclas [ 4 ][ 4 ] =
    {
        {'1','2','3','A'},
        {'4','5','6','B'},
        {'7','8','9','C'},
        {'*','0','#','D'}
     };


  Keypad Teclado = Keypad(makeKeymap(Teclas), Pins_Filas, Pins_Cols, 4, 4);


  char pulsacion = Teclado.getKey() ;
*/

  

  //Capturando lectura del sensor LM35
  int value = analogRead(A0);
  float celsius = (value*500.0) /1023; 
  fuzzy->setInput(1,pasajeros);
  fuzzy->setInput(2,celsius);
  fuzzy->fuzzify();
  float aire=fuzzy->defuzzify(1);
  float ventilador=map(aire,15,25,255,0);
  analogWrite(ventil,ventilador);


  lcd.setCursor(0,0);
  lcd.print("P:");
  lcd.print(pasajeros);
  lcd.print(" ");
  lcd.setCursor(6,0);
  lcd.print("T:");
  lcd.print(celsius);
  lcd.print("C");
  lcd.print((char)223);
  lcd.setCursor(0,1);
  lcd.print("T.Ambiente:");
  lcd.print(aire);
  lcd.setCursor(0,0);
  Serial.println(pasajeros);
  Serial.print(celsius);
  Serial.println(" C° ");
  Serial.println(aire);
  delay(10000);
}
