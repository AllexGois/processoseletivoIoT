import time

print("=== AQUACONTROL SI INICIANDO ===")

try:
    import perifericos
    import internet
    import comunicacao
    
    print("Módulos importados com sucesso!")
    
    def executar_aquacontrol():
        print("----------------------------")
        print("   AquaControl SI Online   ")
        print("----------------------------")
        
        if internet.conectar_wifi():
            print("WiFi conectado!")
            if comunicacao.conectar_mqtt():
                print("MQTT conectado!")
                contador = 0
                while contador < 3:  # Testa apenas 3 vezes
                    try:
                        temp, volume = perifericos.ler_dados()
                        print(f"Ciclo {contador}: Temp={temp}, Volume={volume}")
                        if temp is not None:
                            print(f"Monitor -> Temp: {temp:.1f}C | Vol: {volume:.1f}L")
                            comunicacao.enviar_status(temp, volume)
                        comunicacao.verificar_mensagens()
                        contador += 1
                        time.sleep(2)
                    except Exception as e:
                        print(f"Erro no loop: {e}")
                        break
            else:
                print("Sistema parado: Erro MQTT")
        else:
            print("Sistema parado: Erro WiFi")
    
    executar_aquacontrol()
    
except ImportError as e:
    print(f"Erro ao importar módulo: {e}")
except Exception as e:
    print(f"Erro geral: {e}")
