"""
Autor: Tatiana Gutierrez Rodriguez
Fecha: 20 de agosto de 2024
Descripción: Script del dogma central, este script convierte ADN a ARN y luego traduce ARN a proteínas.
"""

import tkinter as tk
from tkinter import ttk

class TranscripcionADN:
    def __init__(self, secuencia_adn):
        self.secuencia_adn = secuencia_adn.upper()
        self.secuencia_arn = ""
        self.proceso_transcripcion = []

    def validar_secuencia(self):
        caracteres_validos = {'A', 'T', 'C', 'G'}
        return all(c in caracteres_validos for c in self.secuencia_adn)

    def iniciar_transcripcion(self):
        self.proceso_transcripcion.append(
            "Iniciación de la transcripción: La ARN polimerasa se une al promotor y abre la doble hélice de ADN. \n"
        )

    def elongar_transcripcion(self):
        if not self.validar_secuencia():
            raise ValueError("La secuencia de ADN contiene caracteres no válidos. Solo se permiten A, T, C y G.")
        
        self.proceso_transcripcion.append(
            "Elongación de la transcripción: La ARN polimerasa sintetiza ARN complementario a la cadena molde. \n"
        )
        for nucleotido in self.secuencia_adn:
            if nucleotido == 'A':
                self.secuencia_arn += 'U'
            elif nucleotido == 'T':
                self.secuencia_arn += 'A'
            elif nucleotido == 'C':
                self.secuencia_arn += 'G'
            elif nucleotido == 'G':
                self.secuencia_arn += 'C'
            self.proceso_transcripcion.append(
                f"Nucleótido {nucleotido} en ADN se transcribe a {self.secuencia_arn[-1]} en ARN."
            )

    def terminar_transcripcion(self):
        self.proceso_transcripcion.append(
            "\nTerminación de la transcripción: Se libera el ARN transcrito y la ARN polimerasa se separa del ADN.\n"
        )

    def transcribir(self):
        self.iniciar_transcripcion()
        self.elongar_transcripcion()
        self.terminar_transcripcion()

class TraduccionARN:
    tabla_codones = {
        'AUG': 'Metionina', 'UUU': 'Fenilalanina', 'UUC': 'Fenilalanina',
        'UUA': 'Leucina', 'UUG': 'Leucina', 'UCU': 'Serina',
        'UCC': 'Serina', 'UCA': 'Serina', 'UCG': 'Serina',
        'UAU': 'Tirosina', 'UAC': 'Tirosina', 'UGU': 'Cisteína',
        'UGC': 'Cisteína', 'UGG': 'Triptófano', 'CUU': 'Leucina',
        'CUC': 'Leucina', 'CUA': 'Leucina', 'CUG': 'Leucina',
        'AUU': 'Isoleucina', 'AUC': 'Isoleucina', 'AUA': 'Isoleucina',
        'GUU': 'Valina', 'GUC': 'Valina', 'GUA': 'Valina', 'GUG': 'Valina',
        'CCU': 'Prolina', 'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina',
        'ACU': 'Treonina', 'ACC': 'Treonina', 'ACA': 'Treonina', 'ACG': 'Treonina',
        'GCU': 'Alanina', 'GCC': 'Alanina', 'GCA': 'Alanina', 'GCG': 'Alanina',
        'UAA': 'Parada', 'UAG': 'Parada', 'UGA': 'Parada',
        'CAU': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina',
        'AAU': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina',
        'GAU': 'Ácido aspártico', 'GAC': 'Ácido aspártico', 'GAA': 'Ácido glutámico', 'GAG': 'Ácido glutámico',
        'CGU': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina',
        'AGU': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina',
        'GGU': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina'
    }

    def __init__(self, secuencia_arn):
        self.secuencia_arn = secuencia_arn.upper()
        self.proceso_traduccion = []
        self.proteinas = []

    def traducir(self):
        self.proceso_traduccion.append(
            "Proceso de Traducción: Traduciendo la secuencia de ARN a proteínas...\n"
        )
        for i in range(0, len(self.secuencia_arn) - 2, 3):
            codon = self.secuencia_arn[i:i+3]
            aminoacido = self.tabla_codones.get(codon, 'Desconocido')
            if aminoacido == 'Parada':
                break
            self.proteinas.append((codon, aminoacido))
            self.proceso_traduccion.append(
                f"Codón {codon} se traduce a {aminoacido}."
            )
        return self.proteinas

class Aplicacion:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Transcripción y Traducción de ADN")
        self.raiz.geometry("600x500")
        self.raiz.config(bg="#e6f7ff")  # Color de fondo suave

        self.titulo = tk.Label(raiz, text="Transcripción y Traducción de ADN", font=("Arial", 18, "bold"), bg="#e6f7ff")
        self.titulo.pack(pady=10)

        #Entrada de secuencia de ADN
        self.label_adn = tk.Label(raiz, text="Introduce la secuencia de ADN:", font=("Arial", 14), bg="#e6f7ff")
        self.label_adn.pack(pady=5)
        self.entrada_adn = tk.Entry(raiz, width=50, font=("Arial", 12))
        self.entrada_adn.pack(pady=5)

        #Botón para transcribir y traducir
        self.boton_transcribir = tk.Button(raiz, text="Transcribir y Traducir", command=self.transcribir_y_traducir, font=("Arial", 12, "bold"), bg="#ff5457", fg="white")
        self.boton_transcribir.pack(pady=20)  # Aumentar el espacio

        #Sección de resultados
        self.label_resultados = tk.Label(raiz, text="RESULTADOS", font=("Arial", 16, "bold"), bg="#e6f7ff")
        self.label_resultados.pack(pady=15)  # Aumentar el espacio

        #Contenedor para los botones
        self.frame_botones = tk.Frame(raiz, bg="#e6f7ff")
        self.frame_botones.pack(pady=5)

        #Botones de opciones
        self.boton_elongacion = tk.Button(self.frame_botones, text="Elongación", command=self.mostrar_elongacion, font=("Arial", 12), bg="#7e75f8", fg="white")
        self.boton_elongacion.grid(row=0, column=0, padx=5)
        self.boton_secuencia = tk.Button(self.frame_botones, text="Secuencia resultante", command=self.mostrar_secuencia, font=("Arial", 12), bg="#dd57d3", fg="white")
        self.boton_secuencia.grid(row=0, column=1, padx=5)
        self.boton_proteinas = tk.Button(self.frame_botones, text="Proteínas", command=self.mostrar_proteinas, font=("Arial", 12), bg="#ff3f98", fg="white")
        self.boton_proteinas.grid(row=0, column=2, padx=5)
        self.boton_todo = tk.Button(self.frame_botones, text="Proceso completo", command=self.mostrar_todo, font=("Arial", 12), bg="#ff6935", fg="white")
        self.boton_todo.grid(row=0, column=3, padx=5)

        #Cuadro de texto para mostrar resultados
        self.cuadro_texto = tk.Text(raiz, height=15, width=70, wrap=tk.WORD, font=("Arial", 12))
        self.cuadro_texto.pack(pady=10)

    def transcribir_y_traducir(self):
        secuencia_adn = self.entrada_adn.get()
        if not secuencia_adn:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "Error: La secuencia de ADN no puede estar vacía.\n")
            return
        
        try:
            #Realizar la transcripción
            transcripcion = TranscripcionADN(secuencia_adn)
            transcripcion.transcribir()
            self.secuencia_arn = transcripcion.secuencia_arn
            self.proceso_transcripcion = transcripcion.proceso_transcripcion
            
            #Realizar la traducción
            traduccion = TraduccionARN(self.secuencia_arn)
            self.proteinas = traduccion.traducir()
            self.proceso_traduccion = traduccion.proceso_traduccion
            
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "Proceso completo, para ver los resultados da clic en el botón que desees.\n")

        except ValueError as ve:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, f"Error: {ve}\n")
        except Exception as e:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, f"Error inesperado: {e}\n")

    def mostrar_elongacion(self):
        if hasattr(self, 'proceso_transcripcion'):
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "\n".join(self.proceso_transcripcion) + "\n")
        else:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "Error: No se ha realizado la transcripción aún.\n")

    def mostrar_secuencia(self):
        if hasattr(self, 'secuencia_arn'):
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, f"Secuencia de ARN: {self.secuencia_arn}\n")
        else:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "Error: No se ha realizado la transcripción aún.\n")

    def mostrar_proteinas(self):
        if hasattr(self, 'proteinas'):
            self.cuadro_texto.delete(1.0, tk.END)
            if self.proteinas:
                for codon, aminoacido in self.proteinas:
                    self.cuadro_texto.insert(tk.END, f"Codón {codon} se traduce a {aminoacido}.\n")
            else:
                self.cuadro_texto.insert(tk.END, "No se tradujeron proteínas (posiblemente se encontró un codón de parada).\n")
        else:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "Error: No se ha realizado la traducción aún.\n")

    def mostrar_todo(self):
        if hasattr(self, 'proceso_transcripcion') and hasattr(self, 'secuencia_arn') and hasattr(self, 'proteinas'):
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "\n".join(self.proceso_transcripcion) + "\n")
            self.cuadro_texto.insert(tk.END, f"Secuencia de ARN: {self.secuencia_arn}\n")
            if self.proteinas:
                for codon, aminoacido in self.proteinas:
                    self.cuadro_texto.insert(tk.END, f"Codón {codon} se traduce a {aminoacido}.\n")
            else:
                self.cuadro_texto.insert(tk.END, "No se tradujeron proteínas (posiblemente se encontró un codón de parada).\n")
        else:
            self.cuadro_texto.delete(1.0, tk.END)
            self.cuadro_texto.insert(tk.END, "Error: No se ha realizado la transcripción o traducción aún.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
