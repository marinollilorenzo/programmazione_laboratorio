# 🐍 Laboratorio di Introduzione alla Programmazione

Benvenuti nella repository del corso di **Laboratorio di Introduzione alla Programmazione**. 
Questo materiale fa parte del programma didattico del secondo semestre, primo anno della Laurea Triennale in **Intelligenza Artificiale e Data Analytics**.

L'obiettivo di questa repository è raccogliere tutti gli script, gli esercizi e le simulazioni d'esame affrontati durante il corso, per prepararsi al meglio sia sulla logica di programmazione pura che sull'analisi dei dati.

---

## 📚 Struttura del Progetto

Il corso e la repository sono suddivisi in due moduli principali:

### 🗂️ Modulo 1: Python Base (`lab_1`)
Questa cartella contiene tutti i fondamenti del linguaggio Python visti nella prima parte del corso. Al suo interno troverai:
* **Lezioni (1-6):** Script Python suddivisi per lezione, che coprono argomenti come tipi di base, costrutti, funzioni, Programmazione Orientata agli Oggetti (OOP), gestione dei file, eccezioni e list comprehension.
* **Esercitazioni:** File Python dedicati all'allenamento in vista della prova pratica.
* **DOCS & Data:** Vari file di testo (`.txt`) e dati (`.csv`) utilizzati per testare le operazioni di Input/Output.

### 📊 Modulo 2: Data Science (`lab_2`) - *[IN CORSO 🚧]*
Questa sezione è dedicata all'esplorazione e manipolazione dei dati tramite le principali librerie scientifiche di Python: **NumPy**, **Pandas**, **Matplotlib** e **Seaborn**.
* A differenza del Modulo 1, qui le lezioni e gli esercizi sono forniti sotto forma di **Jupyter Notebook** (`.ipynb`), che permettono un approccio interattivo perfetto per la data visualization.
* **Nota:** *Le lezioni di questo modulo sono attualmente in corso di svolgimento. La cartella verrà aggiornata progressivamente con i nuovi Notebook man mano che verranno affrontati in aula.*

---

## 🛠️ Setup dell'ambiente

Questo progetto è configurato utilizzando UV per la gestione delle dipendenze.
Le librerie necessarie (come `numpy`, `pandas`, `matplotlib`, ecc.) e le impostazioni dell'ambiente sono tracciate nei file:
* `pyproject.toml`
* `uv.lock`

Buono studio e buona programmazione! 🚀

## Struttura cartelle:

```
PROGRAMMAZIONE_LABORATORIO
├── README.md
├── lab_1
│   ├── DOCS
│   │   ├── duplicated.txt
│   │   ├── file.txt
│   │   ├── nuovo.txt
│   │   ├── shampo.csv
│   │   └── word.csv
│   ├── esercitazioni
│   │   ├── data
│   │   │   ├── GlobalLandTemperaturesByCountry.csv
│   │   │   ├── GlobalLandTemperaturesByMajorCity.csv
│   │   │   ├── GlobalTemperatures.csv
│   │   │   ├── Temperatures.csv
│   │   │   ├── Temperatures_2.csv
│   │   │   ├── data.csv
│   │   │   └── earthquakes.csv
│   │   ├── esercitazione_1.py
│   │   ├── esercitazione_2.py
│   │   ├── simulazione_esame_1.py
│   │   ├── simulazione_esame_2.py
│   │   ├── simulazione_esame_2_pythonic.py
│   │   ├── simulazione_esame_3.py
│   │   ├── simulazione_esame_4.py
│   │   └── simulazione_esame_5.py
│   ├── esercizi_dispensa
│   │   └── lst_comprehension.py
│   ├── lezione_1
│   │   ├── es1_formate_data.py
│   │   ├── es2_print_pow.py
│   │   ├── es3_pari_dispari.py
│   │   ├── es4_contains.py
│   │   ├── es5_is_prime.py
│   │   ├── es6_sum_n_numbers.py
│   │   ├── es7_factorial.py
│   │   ├── es8_triangle.py
│   │   └── es9_contains_vocals.py
│   ├── lezione_2
│   │   ├── es1.py
│   │   ├── es10.py
│   │   ├── es2.py
│   │   ├── es3.py
│   │   ├── es4.py
│   │   ├── es5.py
│   │   ├── es6.py
│   │   ├── es7.py
│   │   ├── es8.py
│   │   └── es9.py
│   ├── lezione_3
│   │   ├── coin.py
│   │   ├── csv_file.py
│   │   └── veicolo.py
│   ├── lezione_4
│   │   ├── canguro.py
│   │   ├── es_1_3
│   │   │   ├── person.py
│   │   │   ├── school.py
│   │   │   ├── student.py
│   │   │   └── teacher.py
│   │   └── poligono.py
│   ├── lezione_5
│   │   ├── date.py
│   │   ├── es6.py
│   │   └── es7.py
│   └── lezione_6
│       ├── es1.py
│       └── es_lez8.ipynb
├── lab_2
│   ├── lezione_1
│   │   ├── 1.3_NumPy.ipynb
│   │   └── 1.4_Esercizi_lez_1.ipynb
│   ├── lezione_2
│   │   ├── 2.1_NumPy2.ipynb
│   │   ├── 2.2_Esercizi_lez_2.ipynb
│   │   └── emissioni.txt
│   └── lezione_3
│       ├── 3.1_Pandas_1.ipynb
│       ├── 3.2_Pandas_2.ipynb
│       ├── 3.3_Matplotlib.ipynb
│       └── 3.4_Pandas_Plotting.ipynb
├── pyproject.toml
└── uv.lock
```