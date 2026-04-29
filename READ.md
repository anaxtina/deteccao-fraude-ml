# 🛡️ Detecção de Fraude em Fintechs com Machine Learning

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

## 📖 Contexto de Negócio
Em instituições financeiras, a detecção de fraude precisa ser rápida e precisa. Este projeto utiliza **Isolation Forest** (Detecção de Anomalias) para identificar comportamentos suspeitos em transações bancárias, visando reduzir prejuízos e proteger o cliente final.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Machine Learning:** Isolation Forest (Scikit-Learn)
- **API:** Flask para servir o modelo em tempo real
- **Análise de Dados:** Pandas, Numpy, Seaborn e Matplotlib

## 📂 Estrutura do Repositório
- `api/`: Script de servidor Flask para predições.
- `data/`: Dados transacionais simulados.
- `models/`: Modelo treinado e lista de atributos (arquivos .pkl).
- `requirements.txt`: Dependências do projeto.

## 📡 Exemplo de Chamada da API (Predict)
```json
POST /predict
{
    "valor": 1250.0,
    "distancia_casa": 85.0,
    "tentativas_senha": 3,
    " hour": 2,
    "is_night": 1,
    "valor_por_tentativa": 416.6
    }