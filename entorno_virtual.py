from flask import Flask
import random

app = Flask(__name__)

information = ["La dependencia de las tecnologías forma parte de las dependencias comportamentales y se caracteriza por un uso abusivo de los aparatos electrónicos, generalmente conectados a Internet, como el móvil, la tablet, el ordenador o la videoconsola.",
         "La consecuencia más directa de esta dependencia es la pérdida de control de la conducta, donde la persona trata de aliviar su malestar emocional a través de las tecnologías de forma sistemática.",
         "Se genera, por tanto, una dependencia de los elementos tecnológicos y de los estímulos que nacen de ellos (redes sociales, videojuegos, apps…), causando sentimientos de ansiedad, irritabilidad, depresión y desesperación cuando no puede hacer uso de ellos. La persona con esta dependencia necesita aumentar cada vez más el tiempo de conexión, aumentando así su tolerancia.",
         "Necesidad compulsiva de información: Las personas que presentan este tipo de dependencia, sienten una fuerte necesidad por estar informados constantemente, sobre todo en lo referente a los temas relacionados con lo que resulta interesante en su círculo social.",
         "Necesidad de aparatos tecnológicos de vanguardia:A medida que la dependencia de las nuevas tecnologías se hace más intensa, al sujeto no le basta con satisfacer su necesidad de información a través de cualquier dispositivo, sino que este necesitará de uno que le brinde los últimos avances tecnológicos para sentir que satisface su necesidad.",
         "Recursos limitados al ámbito tecnológico:A menudo las personas adictas a la tecnología convierten estos elementos en sus únicos recursos resolutivos. Es decir, estas personas suelen ser incapaces de afrontar cualquier situación en la vida sin apoyarse en aparatos tecnológicos, lo que a menudo limita su capacidad de solventar situaciones en contextos ajenos a las pantallas.",
         "Los principales signos son: - Privación del sueño por mantenerse conectado. - Descuidar actividades diarias (sociales, académicas, higiene…). - Obtener quejas de gente cercana sobre el tiempo empleado en las TIC. - Pensar constantemente en ello. - Mostrarse irritable cuando no se pueden conectar. - Intentar reducir el uso sin éxito. - Aislamiento social o cambios en sus relaciones sociales. - Sentir una alegría anómala cuando se está conectado. - Cambios en el estado de ánimo. - Cambios o sintomatología física o psicosomática."
         "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
         "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
         "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
         "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
         "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos.",
         "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.",
         "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
         "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo."
]

@app.route("/")
def hello_world():
    return '<h1>Tratamiento Psicológico para la Dependencia de la Tecnología en Madrid</h1> <a href="/random_facts">¡Ver un dato aleatorio!</a>'

@app.route("/random_facts")
def random_facts():
    return f'<p>{random.choice(information)}</p>'

@app.route("/flip_coin")
def flip_coin():
    result = random.choice(["Cara", "Cruz"])
    return f'<h1>Resultado: {result}</h1>'

app.run(debug=True)
