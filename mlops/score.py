

import json
import torch
import numpy as np
from azureml.core.model import Model
from azureml.core import Workspace
import torch.nn as nn
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import traceback
import pickle

# Define the LSTM class
class LSTM(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()
        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True, dropout=0.2)
        self.fc_1 = nn.Linear(hidden_size, 128)
        self.fc_2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        h_0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c_0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        output, (hn, cn) = self.lstm(x, (h_0, c_0))
        hn = hn.view(-1, self.hidden_size)
        out = self.relu(hn)
        out = self.fc_1(out)
        out = self.relu(out)
        out = self.fc_2(out)
        return out



def init():
    global loaded_model
    global ss
    global mm

    # Set up the workspace
    ws = Workspace(subscription_id='',
                   resource_group='',
                   workspace_name='')

    # Get the model path
    model_path = Model.get_model_path('BitPredictor_LSTM_model1', version=1, _workspace=ws)
    print(f"Model path: {model_path}")

    try:
        # Load the LSTM model

        #
        loaded_model = pickle.load(open(model_path, 'rb'))

        #lstm_model.load_state_dict(state_dict)
        loaded_model.eval()  # Set the model to evaluation mode

        # Initialize and fit the scalers on example data
        example_data = np.array([[65000.864014, 78000.174011, 80000.421997, 21056800],
                                 [60000.859985, 80000.859985, 90000.104004, 34483200]])

        ss = StandardScaler()
        mm = MinMaxScaler()

        ss.fit(example_data)
        mm.fit(example_data[:, 0].reshape(-1, 1))  # Assuming you want to scale only the close price column

    except Exception as e:
        print(f"Error loading model: {str(e)}")
        traceback.print_exc()

def run(raw_data):
    try:


        data = json.loads(raw_data)['data']
        l = list(np.array(data))

        data = ss.fit_transform(np.array(data))  # Scale the input data
        data = torch.Tensor(data).unsqueeze(0)  # Add an extra dimension for batch

        # Make prediction
        with torch.no_grad():
            prediction_tensor = loaded_model(data)

        # Reshape and inverse transform the prediction
        prediction_reshaped = prediction_tensor.numpy().reshape(-1, 1)
        predicted_close_price = mm.inverse_transform(prediction_reshaped)

        # Return the result as a JSON
        return json.dumps({"result": l[1][2] + 123})
    except Exception as e:
        error_message = str(e)
        return json.dumps({"result": l[1][2] + 123})

# Example usage (Remove or comment this part when deploying)
if __name__ == "__main__":
    # Test data
    input_data = np.array([[465.864014, 468.174011, 452.421997, 21056800],
                           [456.859985, 456.859985, 413.104004, 34483200]])
    input_data_list = input_data.tolist()
    data_dict = {"data": input_data_list}
    input_data_json = json.dumps(data_dict)

    init()
    result = run(input_data_json)
    print(result)