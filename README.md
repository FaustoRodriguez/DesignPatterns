# DesignPatterns
El alumno puede implementar un subconjunto de estos patrones o todo su conjunto dependiendo del entendimiento del problema.

Puedes construir y ejecutar tu proyecto con los comandos de docker siguientes (ubicando tu consola en la carpeta raiz del proyecto donde se ubica el Dockerfile):


Los patrones se ven en el archivo print_report.py

Y los principios se encuentran en ambos archivos agregados y refactorizados, como son el Liskov Sustitution Principle pues en ambos se utiliza codigo reemplazable por otro y el single responsability que se ve claramente en el modulo save_file.py donde solo se le da la tarea de guardar las strings de los archivos de ambos modulos web_report y print_report en archivos con sus respectivos nombres



docker image build --tag financial-report .

docker container run financial-report
