# Sistema de Monitoramento IoT com Análise Preditiva

Este projeto é uma simulação de um sistema de monitoramento em tempo real baseado em IoT que utiliza computação em nuvem e machine learning para análise preditiva. O sistema é projetado para detectar anomalias em diversos dados ambientais coletados por sensores, ajudando a melhorar a segurança e o monitoramento em um ambiente comunitário.

## Índice

- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Visão Geral do Projeto

O Sistema de Monitoramento IoT simula o uso de múltiplos sensores (temperatura, umidade, movimento, som, luminosidade e vibração) para coletar dados em tempo real. Esses dados são enviados para um servidor simulado na nuvem, onde são processados para detectar anomalias usando um modelo de machine learning. O sistema tem como objetivo prever possíveis incidentes de segurança, identificando padrões anormais nos dados.

## Funcionalidades

- **Simulação de Dados de Múltiplos Sensores**: Simula dados de seis tipos diferentes de sensores.
- **Processamento de Dados na Nuvem**: Simula o envio de dados para um servidor na nuvem para processamento.
- **Detecção de Anomalias**: Usa Isolation Forest para identificar anomalias nos dados.
- **Visualização em Tempo Real**: Plota os dados dos sensores e marca as anomalias detectadas.

## Tecnologias Utilizadas

- **Python**: A principal linguagem de programação usada no projeto.
- **Flask**: Para simular o servidor na nuvem.
- **pandas**: Para manipulação e processamento de dados.
- **scikit-learn**: Para implementar o modelo de machine learning.
- **matplotlib**: Para visualização dos dados.
- **Git**: Sistema de controle de versão.

## Instalação

Para configurar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/SEU_NOME_DE_USUARIO/Sistema-Monitoramento-IoT.git
   cd Sistema-Monitoramento-IoT
