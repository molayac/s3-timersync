# S3 Timer Sync 

**s3-timersync** es un simple script que permite ejecutar el comando de aws s3 sync, cada *x* tiempo, durante un *y* tiempo, donde *x*, *y* son valores configurables.

Este script está desarrollado en python v3 y utiliza las librerías **argparse**, **time** y **subprocess** y puede ser modificado o personalizado sin ningún problema.

# Características!

  - Facilita la tarea de sincronizar datos de aws en un directorio local, durante cierto tiempo.
  - Perfecto para testers, que necesitan copiar los datos de un bucket especifico.
  - No utiliza credenciales directamente, porque corre el comando aws s3 sync.

# Uso

Antes de instalar o usar el script debe instalar el aws cli, desde Amazon y configurar su perfil con el comando **aws configure**.

Por último instalar este script y ejecutar:

> s3-timersync --help


## Ejemplos:
Para configurar el bucket:
```sh
$ s3-timersync -c s3://bucket -f FOLDER_LOCAL"
```

----
Configurar la sincronizacion para que a los 60 minutos se detenga el script:
```sh
$ s3-timersync -f FOLDER_LOCAL -t 60
```

---
Configurar que cada 2 segundos durante 10 minutos se ejecute el comando de sincronizacion:
```sh
$ s3-timersync -f FOLDER_LOCAL -s 2
```

##### **Tener en cuenta:** *Los tiempos por defecto son ejecución cada 60 segundos durante 10 minutos, el folder local por defecto es el actual, el bucket debe configurarse*

---
# Instalación

Como ya se mencionó, requiere tener instalado **Python V3**, y para usarlo un proyecto que ya haya sido iniciado con GIT.
Además debe realizar el siguiente proceso:
```sh
$ cd s3-timersync
$ pip install -r requirements.txt --user
$ python setup.py install --user
```

### Por Hacer

 - Modificar el campo -c por -b.
 - Modificar el tiempo de s3.
 - Agregar filtros en los parametros de entrada.
 
License
----

MIT


**Software libre!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Git Hooks]: <https://git-scm.com/book/uz/v2/Customizing-Git-Git-Hooks>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
