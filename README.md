# Pressure-Sensor-Insole
* SensorPresion.py gets the ADC measurements and streams it via WiFi to a Google Sheets. To achieve the above, the code use IFTTT to send the measurements through an HTTP request in JSON format to a Google Sheets.
* Despliegue_Presion.py gets that spreadsheet with pandas library, reorder it into an array and finally shows the result using matplotlib library.
