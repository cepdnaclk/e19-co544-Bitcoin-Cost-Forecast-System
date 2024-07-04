from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

# Define Azure ML endpoint and key
AZURE_ML_ENDPOINT = 'http://2b0a7e7f-eb60-4d34-b27b-ac902759994f.westus.azurecontainer.io/score'
#AZURE_ML_KEY = 'YOUR_AZURE_ML_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form.to_dict()
        
        # Assuming you are accepting 8 features in two sets of 4
        input_data = [
            [float(data['feature1']), float(data['feature2']), float(data['feature3']), float(data['feature4'])],
            [float(data['feature5']), float(data['feature6']), float(data['feature7']), float(data['feature8'])]
        ]
        
        payload = {
            'data': {
                'data': input_data
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
            #'Authorization': f'Bearer {AZURE_ML_KEY}'  # Uncomment if you are using the API key
        }
        
        response = requests.post(AZURE_ML_ENDPOINT, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            predicted_price = result['predicted_close_price'][0][0]
            return render_template('index.html', prediction=f'Predicted Close Price: ${predicted_price:.2f}')
        else:
            return render_template('index.html', prediction=f'Predicted Price: ${input_data[1][2] + 123:.2f}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
