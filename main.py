import time
import perifericos
import internet
import comunicacao

def executar_aquacontrol():
    print("----------------------------")
    print("   AquaControl SI Online   ")
    print("----------------------------")
    
    if internet.conectar_wifi():
        if comunicacao.conectar_mqtt():
            while True:
                temp, volume = perifericos.ler_dados()
                
                if temp is not None:
                    print(f"Monitor -> Temp: {temp:.1f}C | Vol: {volume:.1f}L")
                    comunicacao.enviar_status(temp, volume)
                
                comunicacao.verificar_mensagens()
                time.sleep(5)
        else:
            print("Sistema parado: Erro MQTT")
    else:
        print("Sistema parado: Erro WiFi")

if __name__ == "__main__":
    executar_aquacontrol()
