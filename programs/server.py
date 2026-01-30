from flask import Flask, request
from flask_cors import CORS
import json
import pythoncom
import win32com.client

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    # Define diretório do projeto
    FOLDER_PATH = r"C:\Users\Inventor\sample"

    # Salva o JSON onde o iLogic lê
    with open(f"{FOLDER_PATH}\\programs\\myParameters.json", "w") as f:
        json.dump(data, f)

    # Abre o Inventor
    pythoncom.CoInitialize()
    inventor = win32com.client.Dispatch("Inventor.Application")
    inventor.Visible = True

    # Abre o arquivo IPT
    doc = inventor.Documents.Open(
        f"{FOLDER_PATH}\\3d-sample\\sample-object.ipt"
    )

    # Executa a regra iLogic
    iLogic = inventor.ApplicationAddIns.ItemById(
        "{3BDD8D79-2179-4B11-8A5A-257B1C0263AC}"
    ).Automation

    iLogic.RunRule(doc, "UpdateParameters")

    # Retorna status 200
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000, threaded=False)
