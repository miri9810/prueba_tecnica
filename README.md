# PRUEBA TÉCNICA ARKON DATA

### Desarrollo de la prueba
Me gustaría empezar diciendo como fue el desarrollo e implementación de la prueba, la primera parte fue leer, comprender y entender de que trata la prueba. 

1. La primera parte fue diseñar las funciones en una tabla para poder desarrollarlo, es decir, una serie de instrucciones
![alt text](/img1.jpg)

2. Lo siguiente fue proseguir al diseño del modelo de la base de datos, y aunque no me apegué al mismo, dejo una prueba de lo que en un inicio quería hacer
![alt text](/img2.jpg)

3. Por consecuencia, lo que hice fue desarrollar el proyecto, pero me encontré con el inconveniente del contador para los boletos, por lo que tuve que modificar mis modelos para las peticiones y poder seguir con el conteo. 

4. Los siguientes pasos fueron para hacer las pruebas y agregar los test para analizar la información, pero seguí con otro inconveniente, que aunque funciona, al hacer los registros las fechas no coinciden y aunque no me da un error por terminal, si comente el error de registrar eventos con fechas de tiempo atrás. 

5. A continuación muestro lo que hice y como hacer funcionar el proyecto. 

    - Crear la carpeta dónde se va alojar el proyecto

    - Instalar el entorno virtual con el siguiente comando:
    ´python -m venv env´

    - Activar el entorno:
    ´.\env\Scripts\activate´

    -Lo siguiente fue instalar las librerías y guardarlas en el archivo **requirements.txt**
    ![alt text](/img3.jpg)

    - Después inicié el proyecto con el comando :
    ´django-admin startproject arkondata´
    
    - Lo siguiente fue abrir el proyecto en VSCode
    ![alt text](/img4.jpg)

    - Por consiguiente, lo que viene es escribir el código para que funcione el proyecto:
    **Modelos, Serializers, Views, Urls y Tests**

    ![alt text](/img5.jpg)

    - A las pruebas me remito para decir que el registro de los eventos con fechas equivocadas lo guarda cuando no debería hacerlo, aún con los condicionales que escribí en el serializador
    ![alt text](/img6.jpg)

    - Realicé los test unitarios, aunque solo fue para revisar el metódo **POST**, y vaya que si funciona sin problemas
    ![alt text](/img7.jpg)
    ![alt text](/img8.jpg)
