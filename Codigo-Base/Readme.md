 É um código básico que exemplifica a estrutura do sistema de monitoramento preditivo usando IoT e computação em nuvem. Este código incluir a simulação de sensores IoT, a coleta de dados, o envio para um serviço de nuvem (simulado localmente) e um simples modelo de machine learning para detecção de anomalias.

#### Estrutura do Código
1. Simulação de Sensores IoT
2. Envio dos Dados para a Nuvem
3. Processamento e Detecção de Anomalias
4. Dashboard Simples para Visualização dos Dados


### Como Funciona o Código
1. Simulação de Sensores IoT:
O código simula a coleta de dados de três tipos de sensores: temperatura, movimento e som.

2. Envio para a Nuvem:
Os dados são simulados como sendo enviados para um armazenamento na nuvem, mas na realidade são armazenados em uma lista (cloud_storage).

3. Processamento e Detecção de Anomalias:
Usa um modelo de Isolation Forest, que é uma técnica comum para detecção de anomalias em dados multidimensionais.

4. Dashboard Simples:
Os dados são plotados usando matplotlib, com anomalias marcadas em vermelho.