from machine import Pin, ADC
import network
import urequests

#Inicializar InputPin
inval = ADC(Pin(34))
inval.atten(ADC.ATTN_11DB) #Rango 3.3 V
vec = []

#Inicializar Datos WiFi
ssid = 'INFINITUM5487_2.4'
password = 'JWVKXdkL9A'

api_key = 'db5zfJxvd4IQmjPpdNEbuy'

#Coneccion WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#Captura de datos
for i in range (19):
    if i > 3:
        e1 = 0
        e2 = 1
        k = i - 4
        if (k%16) > 7: a3 = 1
        else: a3 = 0

        if (k%8) > 3: a2 = 1
        else: a2 = 0

        if (k%4) > 1: a1 = 1
        else: a1 = 0

        if (k%2) == 1: a0 = 1
        else: a0 = 0
    else:
        e1 = 0
        e2 = 1
        if (i%4) > 1: b1 = 1
        else: b1 = 0

        if (i%2) == 1: b0 = 1
        else: b0 = 0

    for j in range (6):
        if (j%8) > 3: c2 = 1
        else: c2 = 0

        if (j%4) > 1: c1 = 1
        else: c1= 0

        if (j%2) == 1: c0 = 1
        else: c0 = 0

        Pin(12, Pin.OUT).value(e1)
        Pin(14, Pin.OUT).value(e2)

        Pin(27, Pin.OUT).value(a3)
        Pin(26, Pin.OUT).value(a2)
        Pin(25, Pin.OUT).value(a1)
        Pin(33, Pin.OUT).value(a0)

        Pin(15, Pin.OUT).value(b3)
        Pin(2, Pin.OUT).value(b2)
        Pin(0, Pin.OUT).value(b1)
        Pin(4, Pin.OUT).value(b0)

        Pin(16, Pin.OUT).value(c2)
        Pin(17, Pin.OUT).value(c1)
        Pin(15, Pin.OUT).value(c0)

        vec.append(inval.read())

#Envio inalambrico de datos
for i in range(len(vec)):
    sensor_read = {'value1':vec[i]}
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post(
      'http://maker.ifttt.com/trigger/Press/with/key/' + api_key,
      json=sensor_read,
      headers=request_headers)
    print(request.text)
    request.close()
