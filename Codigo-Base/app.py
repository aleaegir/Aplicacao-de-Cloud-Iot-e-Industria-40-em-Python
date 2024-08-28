import time
import random
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# 1. Simulação de Sensores IoT
def simulate_sensor_data():
    """Simula dados de sensores IoT"""
    return {
        'timestamp': pd.Timestamp.now(),
        'temperature': random.uniform(18.0, 30.0),
        'motion': random.uniform(0, 1),
        'sound': random.uniform(30, 90)
    }

# 2. Envio dos Dados para a Nuvem (Simulado Localmente)
def send_data_to_cloud(data):
    """Simula o envio de dados para a nuvem"""
    # Aqui você enviaria os dados para a nuvem, mas vamos armazená-los localmente
    cloud_storage.append(data)

# 3. Processamento e Detecção de Anomalias
def detect_anomalies(data_frame):
    """Detecta anomalias nos dados usando Isolation Forest"""
    model = IsolationForest(contamination=0.1)
    data_frame['anomaly'] = model.fit_predict(data_frame[['temperature', 'motion', 'sound']])
    return data_frame

# 4. Dashboard Simples para Visualização dos Dados
def plot_data(data_frame):
    """Gera gráficos simples para visualização dos dados e anomalias"""
    plt.figure(figsize=(14, 7))
    
    plt.subplot(3, 1, 1)
    plt.plot(data_frame['timestamp'], data_frame['temperature'], label='Temperature')
    plt.scatter(data_frame['timestamp'][data_frame['anomaly'] == -1], 
                data_frame['temperature'][data_frame['anomaly'] == -1], 
                color='red', label='Anomaly')
    plt.legend()
    plt.title('Temperature Data')

    plt.subplot(3, 1, 2)
    plt.plot(data_frame['timestamp'], data_frame['motion'], label='Motion')
    plt.scatter(data_frame['timestamp'][data_frame['anomaly'] == -1], 
                data_frame['motion'][data_frame['anomaly'] == -1], 
                color='red', label='Anomaly')
    plt.legend()
    plt.title('Motion Data')

    plt.subplot(3, 1, 3)
    plt.plot(data_frame['timestamp'], data_frame['sound'], label='Sound')
    plt.scatter(data_frame['timestamp'][data_frame['anomaly'] == -1], 
                data_frame['sound'][data_frame['anomaly'] == -1], 
                color='red', label='Anomaly')
    plt.legend()
    plt.title('Sound Data')

    plt.tight_layout()
    plt.show()

# Simulação principal
cloud_storage = []  # Simulando o armazenamento na nuvem

# Simulando coleta de dados por 100 instantes
for _ in range(100):
    sensor_data = simulate_sensor_data()
    send_data_to_cloud(sensor_data)
    time.sleep(0.1)  # Simulando intervalo de tempo entre leituras

# Convertendo os dados armazenados em um DataFrame
df = pd.DataFrame(cloud_storage)

# Detectando anomalias nos dados coletados
df = detect_anomalies(df)

# Exibindo os dados e as anomalias detectadas
plot_data(df)
