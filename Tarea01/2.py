def importar_fasta_como_texto_sin_encabezados(archivo_fasta):
    with open(archivo_fasta, 'r') as f:
        lineas = f.readlines()

    # Filtrar solo las líneas que no son encabezados
    contenido_sin_encabezados = ''.join([linea for linea in lineas if not linea.startswith('>')])

    return contenido_sin_encabezados

#importar el archivo
archivo_fasta = 'Tarea01/bicho_yellowstone.fasta'  # Reemplaza con la ruta de tu archivo FASTA
texto_fasta_sin_encabezados = importar_fasta_como_texto_sin_encabezados(archivo_fasta)

#eliminar el encabezado del archivo fasta
print(texto_fasta_sin_encabezados)

#contar los caracteres de la secuencia
cantidad_caracteres = len(texto_fasta_sin_encabezados)
print("Cantidad de caracteres:", cantidad_caracteres)