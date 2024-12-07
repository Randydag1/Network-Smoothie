# /backend/app.py

from flask import Flask, request, jsonify
from neural_network import NeuralNetwork
from code_generator import CodeGenerator
from code_executor import execute_code

app = Flask(__name__)

# Initialize the neural network and code generator
neural_net = NeuralNetwork()
code_generator = CodeGenerator()

@app.route("/process_input", methods=["POST"])
def process_input():
    user_input = request.json.get("input_data")
    
    # Learn from user input and generate insights
    result = neural_net.learn_from_user_input(user_input)
    
    # Generate code based on learned patterns
    generated_code = code_generator.generate_code(user_input)
    
    # Optionally, execute the generated code in a safe environment
    execution_result = execute_code(generated_code)
    
    return jsonify({
        "insight": result,
        "generated_code": generated_code,
        "execution_result": execution_result
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)/neural_ui_project
    /backend
        app.py              # Python backend server (Flask/FastAPI)
        neural_network.py   # Neural network logic (existing code)
    /frontend
        /src
            index.html      # Main HTML page
            main.js         # Frontend logic
            style.css       # Styling for the UI
    package.json           # Electron project config