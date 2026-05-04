import machine, onewire, ds18x20, time, math
import config

# Inicialização Temperatura
ds_pin = machine.Pin(config.PIN_TEMP)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Inicialização Nível
trig = machine.Pin(config.PIN_TRIG, machine.Pin.OUT)
echo = machine.Pin(config.PIN_ECHO, machine.Pin.IN)

# Inicialização Servo
servo = machine.PWM(machine.Pin(config.PIN_SERVO), freq=50)

def ler_dados():
    # Temperatura
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    temp = ds_sensor.read_temp(roms[0]) if roms else None
    
    # Distância e Volume
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    duracao = machine.time_pulse_us(echo, 1, 30000)
    distancia = (duracao * 0.0343) / 2 if duracao > 0 else None
    
    volume = 0
    if distancia is not None:
        altura_agua = config.ALTURA_TANQUE - distancia
        area_base = math.pi * (config.RAIO_TANQUE ** 2)
        volume = (area_base * altura_agua) / 1000
        
    return temp, volume

def acionar_alimentador(segundos=2):
    print(f"Acionando alimentador por {segundos}s")
    servo.duty(75) # Aprox 90 graus
    time.sleep(segundos)
    servo.duty(26) # Aprox 0 graus
