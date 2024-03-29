[![Python package][pipeline-img]][pipeline-url]
[![codecov][codecov-img]][codecov-url]

# BGH Smart Kit

Implementación de prueba de los _webservices_ del Smart Kit en Python.

## Web services

- https://bgh-services.solidmation.com/1.0/HomeCloudService.svc/help
- https://bgh-services.solidmation.com/1.0/HomeCloudServiceAdmin.svc/help
- https://bgh-services.solidmation.com/1.0/HomeCloudCommandService.svc/help

## Información de login

En el directorio secrets hay que crear un archivo secrets.py completando los campos que aparecen en _empty_secrets.py_. El mail y el password son los que se utilizan para registrar la cuenta al instalar el software. El resto de los datos es posible obtenerlo de la base de datos SQLite3 que utiliza la aplicación u obtenerlos a través de las llamadas al servicio web.

## Motivación

La aplicación contiene un historial de temperaturas por habitación que me pareció interesante, sin embargo no era posible extraer esa información de la aplicación. Tampoco era posible consultar la información desde una computadora.

![image](https://user-images.githubusercontent.com/15602473/219908190-bbea3e90-8972-44df-9429-799fc0527759.png)

[pipeline-img]: https://github.com/rpgrca/smart_kit_sdk/actions/workflows/python.yml/badge.svg
[pipeline-url]: https://github.com/rpgrca/smart_kit_sdk/actions/workflows/python.yml
[codecov-img]: https://codecov.io/gh/rpgrca/smart_kit_sdk/branch/main/graph/badge.svg
[codecov-url]: https://codecov.io/gh/rpgrca/smart_kit_sdk
