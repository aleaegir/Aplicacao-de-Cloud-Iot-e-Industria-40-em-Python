import time
import random
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify

# 1. Simulação de Sensores IoT (Com novos tipos de sensores)
def simulate_sensor_data():
    """Simula dados de múltiplos sensores IoT"""
    return {
        'timestamp': pd.Timestamp.now(),
        'temperature': random.uniform(18.0, 30.0),
        'humidity': random.uniform(30.0, 70.0),
        'motion': random.uniform(0, 1),
        'sound': random.uniform(30, 90),
        'light': random.uniform(100, 1000),
        'vibration': random.uniform(0, 1)
    }

# 2. Simulação do Servidor para Processar os Dados
app = Flask(__name__)
cloud_storage = []  # Simulando armazenamento na nuvem

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.json
    cloud_storage.append(data)
    return jsonify({"status": "data received"}), 200

@app.route('/process_data', methods=['GET'])
def process_data():
    if not cloud_storage:
        return jsonify({"status": "no data"}), 200
    
    df = pd.DataFrame(cloud_storage)
    df['anomaly'] = detect_anomalies(df)
    
    # Retorna os dados processados
    return df.to_json(orient="records"), 200

# 3. Processamento e Detecção de Anomalias
def detect_anomalies(data_frame):
    """Detecta anomalias nos dados usando Isolation Forest"""
    model = IsolationForest(contamination=0.1)
    features = ['temperature', 'humidity', 'motion', 'sound', 'light', 'vibration']
    return model.fit_predict(data_frame[features])

# 4. Dashboard Simples para Visualização dos Dados
def plot_data(data_frame):
    """Gera gráficos simples para visualização dos dados e anomalias"""
    plt.figure(figsize=(14, 14))
    
    sensors = ['temperature', 'humidity', 'motion', 'sound', 'light', 'vibration']
    for i, sensor in enumerate(sensors, 1):
        plt.subplot(3, 2, i)
        plt.plot(data_frame['timestamp'], data_frame[sensor], label=sensor.capitalize())
        plt.scatter(data_frame['timestamp'][data_frame['anomaly'] == -1], 
                    data_frame[sensor][data_frame['anomaly'] == -1], 
                    color='red', label='Anomaly')
        plt.legend()
        plt.title(f'{sensor.capitalize()} Data')
    
    plt.tight_layout()
    plt.show()

# Simulação principal
def main():
    # Simulando envio de dados para o servidor
    for _ in range(100):
        sensor_data = simulate_sensor_data()
        response = requests.post('http://127.0.0.1:5000/send_data', json=sensor_data)
        time.sleep(0.1)  # Simulando intervalo de tempo entre leituras

    # Processando os dados no servidor
    response = requests.get('http://127.0.0.1:5000/process_data')
    df = pd.read_json(response.content)
    
    # Exibindo os dados e as anomalias detectadas
    plot_data(df)

if __name__ == '__main__':
    # Primeiro, inicie o servidor Flask
    from multiprocessing import Process
    
    server = Process(target=lambda: app.run(debug=False))
    server.start()
    
    try:
        # Em seguida, execute a simulação principal
        main()
    finally:
        server.terminate()
