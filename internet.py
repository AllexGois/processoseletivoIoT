import network
import time

def conectar_wifi():
    print("Conectando ao Wi-Fi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    
    # No Wokwi, use estas credenciais:
    sta_if.connect('Wokwi-GUEST', '')
    
    tentativas = 0
    while not sta_if.isconnected() and tentativas < 15:
        print(".", end="")
        time.sleep(1)
        tentativas += 1
        
    if sta_if.isconnected():
        print("\nConectado!")
        print("IP:", sta_if.ifconfig()[0])
        return True
    else:
        print("\nFalha na conexão.")
        return False
