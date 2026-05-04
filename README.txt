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

## 🧩 Arquitetura Modular

O **AquaControl SI** foi desenvolvido com uma arquitetura **altamente modular**, permitindo fácil manutenção, testes e expansão do sistema.

### **Módulos Independentes**

#### **🔧 `config.py` - Central de Configuração**
```python
# Todas as constantes em um local
PIN_TEMP = 4      # DS18B20
PIN_TRIG = 5      # HC-SR04 Trigger
PIN_ECHO = 18     # HC-SR04 Echo
PIN_SERVO = 13    # Servo PWM

ALTURA_TANQUE = 50.0  # cm
RAIO_TANQUE = 25.0    # cm
```
**Vantagens**: Mudanças de hardware exigem apenas editar este arquivo.

#### **📡 `perifericos.py` - Camada de Hardware**
```python
def ler_dados():
    # Temperatura DS18B20
    # Distância HC-SR04
    # Cálculo de volume
    return temp, volume

def acionar_alimentador(segundos):
    # Controle do servo
```
**Vantagens**: Isolamento completo do hardware, fácil para testes unitários.

#### **🌐 `internet.py` - Conectividade**
```python
def conectar_wifi():
    # Configuração WiFi
    # Tentativas automáticas
    # Status de conexão
```
**Vantagens**: Lógica de rede separada, pode ser substituída por Ethernet/GSM.

#### **📨 `comunicacao.py` - Protocolo IoT**
```python
def conectar_mqtt():
    # Broker MQTT
    # Tópicos de publicação
    # Callbacks de mensagens
```
**Vantagens**: Protocolo independente, pode migrar para HTTP/CoAP facilmente.

#### **🎯 `main.py` - Orquestrador**
```python
# Importa todos os módulos
# Controla o fluxo principal
# Tratamento de erros
# Loop de monitoramento
```
**Vantagens**: Lógica de negócio centralizada, fácil de entender o fluxo.

---

## 🔄 Integração dos Módulos

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  main.py    │───▶│ perifericos │───▶│   config    │
│ Orquestrador│    │  (Hardware) │    │(Constantes)│
└─────────────┘    └─────────────┘    └─────────────┘
       │                    │                    │
       ▼                    ▼                    ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  internet   │◀──▶│ comunicacao │    │   dados     │
│   (WiFi)    │    │   (MQTT)    │    │ (Sensor)    │
└─────────────┘    └─────────────┘    └─────────────┘
```

### **Fluxo de Dados:**
1. **main.py** chama `perifericos.ler_dados()`
2. **perifericos** usa configurações do **config**
3. Dados vão para **comunicacao** via MQTT
4. **internet** mantém conectividade WiFi

---

## 🧪 Benefícios da Modularidade

### **Manutenibilidade**
- ✅ **Mudanças isoladas**: Alterar WiFi não afeta sensores
- ✅ **Debug facilitado**: Testar módulos individualmente
- ✅ **Código reutilizável**: Módulos podem ser usados em outros projetos

### **Escalabilidade**
- ✅ **Novos sensores**: Adicionar em `perifericos.py`
- ✅ **Novos protocolos**: Extender `comunicacao.py`
- ✅ **Nova conectividade**: Modificar apenas `internet.py`

### **Testabilidade**
- ✅ **Testes unitários**: Cada módulo pode ser testado separadamente
- ✅ **Mocks**: Simular hardware para testes
- ✅ **CI/CD**: Validar cada módulo independentemente

---

## 📊 Exemplo de Expansão

**Adicionar sensor de pH:**
```python
# 1. Adicionar em config.py
PIN_PH = 34

# 2. Extender perifericos.py
def ler_ph():
    # Lógica do sensor pH
    return ph_value

# 3. Integrar em main.py
temp, volume, ph = ler_todos_dados()
```

**Resultado**: Sistema expandido sem modificar código existente!

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