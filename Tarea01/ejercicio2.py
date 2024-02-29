def importar_fasta_como_texto_sin_encabezados(archivo_fasta):
    with open(archivo_fasta, 'r') as f:
        lineas = f.readlines()

    # Filtrar solo las líneas que no son encabezados
    contenido_sin_encabezados = ''.join([linea for linea in lineas if not linea.startswith('>')])

    return contenido_sin_encabezados

def traducir_codones(texto_fasta_sin_encabezados):
    translation = ""
    
    codon_translation = {
        "UAA": "", "UAG": "", "UGA": "",  # Stop codons
        "AUG": "M",  # Start codon
        "UUU": "F", "UUC": "F",
        "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y",
        "UGU": "C", "UGC": "C",
        "UGG": "W",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    for i in range(0, cantidad_caracteres, 3):
        codon = texto_fasta_sin_encabezados[i:i+3]
        if codon in codon_translation:
            translation += codon_translation[codon]

    return translation

def replicacion_adn(texto_fasta_sin_encabezados):
    # Replicación
    replicacion_adn = ""
    for i in range(cantidad_caracteres):
        if texto_fasta_sin_encabezados[i] == "A":
            replicacion_adn += "T"
        elif texto_fasta_sin_encabezados[i] == "T":
            replicacion_adn += "A"
        elif texto_fasta_sin_encabezados[i] == "C":
            replicacion_adn += "G"
        elif texto_fasta_sin_encabezados[i] == "G":
            replicacion_adn += "C"
    return replicacion_adn

def transcripcion_adn(cadena_adn):
    cadena_adn = cadena_adn.replace("T", "U")
    return cadena_adn

def traduccion_adn(cadena_adn):
    cadena_adn = traducir_codones(cadena_adn)
    return cadena_adn

#importar el archivo
archivo_fasta = 'Tarea01/bicho_yellowstone.fasta'  
texto_fasta_sin_encabezados  = importar_fasta_como_texto_sin_encabezados(archivo_fasta)

cantidad_caracteres = len(texto_fasta_sin_encabezados)

replicacion_adn = replicacion_adn(texto_fasta_sin_encabezados)
transcripcion_adn = transcripcion_adn(replicacion_adn)
traduccion = traduccion_adn(transcripcion_adn)


#print(traduccion)
print("Cantidad de caracteres: ")
print(cantidad_caracteres)

print("Cantidad de T (Timina) en la secuencia: ")
print(texto_fasta_sin_encabezados.count("T"))

print("Longitud de la cadena de ADN: ")
print(len(texto_fasta_sin_encabezados))

print("Longitud de la cadena de replicación: ")
print(len(replicacion_adn))

print("Longitud de la cadena de transcripción ARNm: ")
print(len(transcripcion_adn))

print("Longitud de la cadena de traducción: ")
print(len(traduccion))

# Crear un archivo de texto con la cadena de traducción
with open('Tarea01/traduccion.txt', 'w') as f:
    f.write(traduccion)