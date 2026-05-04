🚀 AquaControl SI - Sistema de Monitoramento IoT para Aquicultura

Sistema embarcado para monitoramento inteligente de tanques de tilápia, desenvolvido em MicroPython para ESP32.

📋 Sobre o Projeto

O **AquaControl SI** é uma solução IoT completa para aquicultura que monitora em tempo real:
- **Temperatura da água** (sensor DS18B20)
- **Nível de água** (sensor ultrassônico HC-SR04)
- **Controle de alimentação** (servo motor)
- **Comunicação MQTT** para envio de dados
- **Interface WiFi** para conectividade

---

🏗️ Arquitetura do Sistema

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   ESP32         │    │   Sensores      │    │   Atuadores     │
│   MicroPython   │────│ • DS18B20       │────│ • Servo Motor   │
│                 │    │ • HC-SR04       │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                    ┌─────────────────┐
                    │   Comunicação   │
                    │ • WiFi          │
                    │ • MQTT          │
                    └─────────────────┘
```

---

📁 Estrutura do Projeto

```
processoseletivoIoT/
├── src/
│   ├── main.py           # Script principal do sistema
│   ├── perifericos.py    # Controle de sensores e atuadores
│   ├── internet.py       # Gerenciamento WiFi
│   ├── comunicacao.py    # Protocolo MQTT
│   └── config.py         # Configurações e constantes
├── diagram.json          # Circuito Wokwi (ESP32 + sensores)
├── wokwi.toml           # Configuração da simulação
├── flasher_args.json     # Configuração do firmware ESP32
├── libraries.txt         # Dependências do projeto
├── fs.bin               # Sistema de arquivos MicroPython
└── README.md            # Documentação completa
```

---

🔧 Como Usar no Wokwi

Configuração Manual
1. Acesse https://wokwi.com/projects/new
2. Selecione **ESP32** como placa
3. Adicione os componentes:
   - 1x ESP32 DevKit V1
   - 1x DS18B20 (sensor temperatura)
   - 1x HC-SR04 (sensor ultrassônico)
   - 1x Servo Motor
4. Conecte conforme `diagram.json`
5. Crie os arquivos `.py` e copie o conteúdo

---

📊 Funcionalidades

🏊 Monitoramento de Temperatura
- Sensor DS18B20 no GPIO 4 (1-Wire)
- Leitura precisa de temperatura da água
- Alerta para valores fora do ideal (24-28°C)

📏 Controle de Nível
- Sensor HC-SR04 (GPIO 5/18)
- Cálculo de volume baseado na altura
- Tanque cilíndrico com raio configurável

🎯 Alimentação Automática
- Servo motor no GPIO 13 (PWM)
- Controle de porções de ração
- Temporização programável

🌐 Comunicação IoT
- Conexão WiFi automática
- Protocolo MQTT para envio de dados


---

## ⚙️ Configuração

### Pinos Utilizados
```python
PIN_TEMP = 4      # DS18B20 (Temperatura)
PIN_TRIG = 5      # HC-SR04 Trigger
PIN_ECHO = 18     # HC-SR04 Echo
PIN_SERVO = 13    # Servo Motor (PWM)
```

### Constantes do Sistema
```python
ALTURA_TANQUE = 50.0    # cm
RAIO_TANQUE = 25.0      # cm
TEMP_IDEAL_MIN = 24.0   # °C
TEMP_IDEAL_MAX = 28.0   # °C
```

---

## 🚀 Como Executar

1. **Importe o projeto** no Wokwi
2. **Inicie a simulação**
3. **Monitore o Serial Monitor**:
   ```
   ----------------------------
      AquaControl SI Online
   ----------------------------
   Conectando ao Wi-Fi...
   Conectado! IP: 192.168.1.100
   Conectando MQTT...
   MQTT conectado!
   Monitor -> Temp: 25.5C | Vol: 15.7L
   ```

---

## 📋 Dependências

### MicroPython
- `machine` - Controle de hardware
- `network` - Conectividade WiFi
- `time` - Temporização
- `onewire`, `ds18x20` - Sensor temperatura
- `math` - Cálculos geométricos

### Simulador Wokwi
- Extensão VS Code (opcional)
- Conta Wokwi (gratuita)