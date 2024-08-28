### Estrutura Expandida do Código

1. Simulação de Sensores IoT (Com novos tipos de sensores)
2. Envio dos Dados para um Servidor Simulado (nuvem)
3. Processamento e Detecção de Anomalias no Servidor
4. Dashboard Simples para Visualização dos Dados

### Explicação do Código 

1. Simulação de Sensores IoT (Com novos tipos de sensores):
# Adicionamos sensores de umidade (humidity), luminosidade (light), e vibração (vibration), além dos sensores anteriores.

2. Simulação do Servidor para Processar os Dados:

# Utilizamos o Flask para simular um servidor local que atua como a "nuvem".
# O servidor possui uma rota /send_data para receber os dados dos sensores e armazená-los localmente.
# Outra rota /process_data é usada para processar esses dados, aplicando um modelo de detecção de anomalias e retornando os dados processados.

3. Processamento e Detecção de Anomalias:
# A função detect_anomalies agora processa um conjunto expandido de sensores.
# O servidor processa os dados e identifica anomalias usando o algoritmo Isolation Forest.

4. Dashboard Simples para Visualização dos Dados:
# A função plot_data foi expandida para mostrar gráficos de todos os tipos de sensores e marcar as anomalias detectadas.