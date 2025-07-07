import pandas as pa
from unidecode import unidecode

#cargar los datos
Bdatos = pa.read_csv('notas_estudiantes.csv')
print(Bdatos)

Dnuevo = Bdatos.copy()
#Limpiar la columna "Carrera" eliminar espacion en blanco,Primera leta en mayuscula y quita tildes
Dnuevo["Carrera"] = Dnuevo["Carrera"].apply(lambda x: unidecode(x.strip().title()) if isinstance(x, str)else x)
print(Dnuevo)
Dnuevo["Nombre"] = Dnuevo["Nombre"].apply(lambda x: unidecode(x.strip().title()) if isinstance(x, str) else x)
print(Dnuevo)
#eliminar filas con nombres,carreras,edad y notas vacias
Dnuevo = Dnuevo.dropna(subset=["Nombre","Carrera","Edad","Nota1","Nota2","Nota3"])
print(Dnuevo)
#cambiar tipo de dato real x entero
Dnuevo["Edad"] = Dnuevo["Edad"].astype(int)
print(Dnuevo)
#eliminar duplicados
Dnuevo = Dnuevo.drop_duplicates()
print(Dnuevo)

#Crear una nueva columna con el promedio de notas
Dnuevo["Promedio"] = Dnuevo[["Nota1","Nota2","Nota3"]].mean(axis=1)
Dnuevo["Promedio"] = Dnuevo["Promedio"].round(1)
print(Dnuevo)
#crear una funcion para el clasificar el promedio de la persona
def clasificar_promedio(prome):
    if prome >= 4.5:
        return "Excelente"
    elif prome >=3.5:
        return "Bueno"
    elif prome >=2.5:
        return "Regular"
    else:
        return "Deficiente"
#llamar la funcion y crear la nueva columna para el desempeño
Dnuevo["Desempeño"] = Dnuevo["Promedio"].apply(clasificar_promedio)  
print(Dnuevo)  
#exportar el nuevo dataframe a excel
Nuevo = Dnuevo.to_excel('notas_estudiantes_limpio.xlsx', index=False)