
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregando o modelo e a lista de features que salvamos no Passo 8
model = joblib.load('models/fraud_detector_model.pkl')
features_list = joblib.load('models/features_list.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df_input = pd.DataFrame([data])
        
        # O Isolation Forest retorna -1 para anomalia (fraude) e 1 para normal
        prediction = model.predict(df_input[features_list])
        
        resultado = "ALERTA: Fraude Detectada" if prediction[0] == -1 else "Transação Normal"
        
        return jsonify({
            'status': resultado,
            'prediction_code': int(prediction[0]),
            'mensagem': 'Análise concluída com sucesso'
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
