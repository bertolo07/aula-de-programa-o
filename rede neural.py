import tensorflow as tf
import numpy as np
import urllib
from PIL import Image

# Função para carregar a imagem a partir de uma URL
def load_image_from_url(url):
    image = Image.open(urllib.request.urlopen(url))
    return image

# Carregar o modelo pré-treinado MobileNetV2
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Função para identificar objetos na imagem
def identify_objects(image):
    # Redimensionar a imagem para o tamanho esperado pelo modelo
    image = image.resize((224, 224))
    # Converter a imagem em um array numpy
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    # Expandir as dimensões do array para corresponder ao formato de entrada do modelo
    image_array = np.expand_dims(image_array, axis=0)
    # Pré-processamento da imagem para adequá-la ao modelo
    preprocessed_image = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
    # Fazer a previsão dos objetos na imagem
    predictions = model.predict(preprocessed_image)
    # Decodificar as previsões
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]
    # Retornar as previsões
    return decoded_predictions

# Exemplo de uso
image_url = 'URL_DA_IMAGEM'
image = load_image_from_url(image_url)
predictions = identify_objects(image)

# Exibir as previsões
for prediction in predictions:
    print(f'{prediction[1]}: {prediction[2]*100:.2f}%')


