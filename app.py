import os
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

longitud, altura = 150, 150
modelo = './Modelo/modelo.P19'
pesos_modelo = './Modelo/pesos.P19'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    # Guardar la imagen en el servidor
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Cargar la imagen y hacer la predicción
    img = Image.open(file_path)
    x = img.resize((longitud, altura))
    x = img_to_array(x)
    x = x.reshape((1,) + x.shape)
    array = cnn.predict(x)
    result = array[0]
    answer = int(result.argmax())

    if answer == 0:
        pred = "Acaro"
        recomendacion = "Se Recomienda usar Ovicidas: (Acaristop)"
        return redirect(url_for('acaro', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 1:
        pred = "Barrenador_de_Tallo"
        recomendacion = "Se Recomienda usar Proclaim5: (Acaristop)"
        return redirect(url_for('Barrenador_de_Tallo', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 2:
        pred = "Escarabajo"
        recomendacion = "Se Recomienda usar Lexan: (Acaristop)"
        return redirect(url_for('Escarabajo', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 3:
        pred = "Gusano_Cogollero"
        recomendacion = "Se Recomienda usar Gusanol: (Acaristop)"
        return redirect(url_for('Gusano_Cogollero', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 4:
        pred = "Mosca_de_Sierra"
        recomendacion = "Se Recomienda usar Shermann: (Acaristop)"
        return redirect(url_for('Mosca_de_Sierra', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 5:
        pred = "Mosquito"
        recomendacion = "Se Recomienda usar Agroinco: (Acaristop)"
        return redirect(url_for('Mosquito', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 6:
        pred = "Pulgon"
        recomendacion = "Se Recomienda usar Aphox: (Acaristop)"
        return redirect(url_for('Pulgon', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    if answer == 7:
        pred = "Saltamones"
        recomendacion = "Se Recomienda usar Venerate: (Acaristop)"
        return redirect(url_for('Saltamones', prediction=pred, recomendacion=recomendacion, image_path=file_path))

    else:
        pred = "Cultivo en Excelente estado"
        recomendacion = ""
        return redirect(url_for('cultivo', prediction=pred, recomendacion=recomendacion, image_path=file_path))
    
    os.remove(file_path)


@app.route('/acaro')
def acaro():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('acaro.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Barrenador de Tallo')
def Barrenador_de_Tallo():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Barrenador_de_Tallo.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Escarabajo')
def Escarabajo():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Escarabajo.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Gusano_Cogollero')
def Gusano_Cogollero():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Gusano_Cogollero.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Mosca_de_Sierra')
def Mosca_de_Sierra():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Mosca_de_Sierra.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Mosquito')
def Mosquito():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Mosquito.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Pulgon')
def Pulgon():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Pulgon.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

@app.route('/Saltamones')
def Saltamones():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('Saltamones.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)


@app.route('/cultivo')
def cultivo():
    prediction = request.args.get('prediction')
    recomendacion = request.args.get('recomendacion')
    image_path = request.args.get('image_path')
    return render_template('cultivo.html', prediction=prediction, recomendacion=recomendacion, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)