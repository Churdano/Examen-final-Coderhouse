# Distribuidora LG

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
### Es una pagina para una distribuidora de ferreterias. Contiene un panel de inicio con un saludo, un panel para ver los productos, buscar, o crear. Un panel para ingresar clientes nuevos, o buscarlos en la BD. Y tambien un panel para vendedores, en donde se podran ingresar nuevos vendedores o buscarlos por apellido.