from flask import Flask, jsonify
import math

app = Flask(__name__)


def calcular_factorial(n):
    """
    Calcula el factorial de un número usando la librería math.

    Args:
        n (int): Número para calcular el factorial

    Returns:
        int: Factorial del número
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    return math.factorial(n)


def es_par_o_impar(n):
    """
    Determina si un número es par o impar.

    Args:
        n (int): Número a evaluar

    Returns:
        str: "par" o "impar"
    """
    return "par" if n % 2 == 0 else "impar"


@app.route('/')
def home():
    """
    Endpoint raíz con información del servicio.
    """
    return jsonify({
        "servicio": "Calculadora de Factorial",
        "uso": "/factorial/<numero>",
        "ejemplo": "/factorial/5"
    })


@app.route('/factorial/<int:numero>', methods=['GET'])
def calcular_factorial_endpoint(numero):
    """
    Endpoint principal que recibe un número y devuelve:
    - El número recibido
    - Su factorial
    - Etiqueta "par" o "impar" del factorial

    Args:
        numero (int): Número recibido por URL

    Returns:
        JSON: Respuesta con los datos calculados
    """
    try:
        # Calcular el factorial
        factorial = calcular_factorial(numero)

        # Determinar si el factorial es par o impar
        etiqueta = es_par_o_impar(factorial)

        # Construir respuesta JSON
        respuesta = {
            "numero_recibido": numero,
            "factorial": factorial,
            "etiqueta": etiqueta,
            "mensaje": f"El factorial de {numero} es {factorial}, que es {etiqueta}"
        }

        return jsonify(respuesta), 200

    except ValueError as e:
        return jsonify({
            "error": str(e),
            "numero_recibido": numero
        }), 400

    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor",
            "detalle": str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """
    Manejador de errores 404.
    """
    return jsonify({
        "error": "Endpoint no encontrado",
        "uso_correcto": "/factorial/<numero>"
    }), 404


if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug
    app.run(debug=True, host='0.0.0.0', port=5000)