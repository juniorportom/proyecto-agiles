# Despliegue de SGRD

## Requisitos

Para realizar el despliegue de SGRD es necesario:

- Una cuenta de Heroku
- Una base de datos PostgreSQL

## Instruccioines despliegue

Utilice el botón de Heroku para crear un despliegue y configure en las variables de entorno:

1. `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` y `AWS_STORAGE_BUCKET_NAME` (por defecto en `agiles-media`)

La base de datos será automáticamente provisionada por Heroku.

## Setup adicional inicial

1. Carga las variables de entorno localmente y cree un administrador de la aplicación Django con el comando
`python manage.py createsuperuser`.

2. Entre al módulo de administación y cree algunas etiquetas.

## Listo!

Disfrute de SGRD
