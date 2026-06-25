"""
Configurazione e impostazioni di Jarvis
"""

# Lingua predefinita
DEFAULT_LANGUAGE = "it"

# Formato della mappa
MAP_CONFIG = {
    "figsize": (16, 10),
    "dpi": 100,
    "cmap": "Set3",
    "edgecolor": "black",
}

# Comandi disponibili
AVAILABLE_COMMANDS = {
    "calcola": "Esegui operazioni matematiche",
    "mostra": "Visualizza informazioni su un paese",
    "mappa": "Mostra la mappa interattiva del mondo",
    "paesi": "Elenca tutti i paesi disponibili",
    "aiuto": "Mostra l'elenco dei comandi disponibili",
    "esci": "Esci da Jarvis",
}

# Configurazione calcoli
CALCULATOR_CONFIG = {
    "max_operations": 100,
    "precision": 10,
}

# URL per dati geografici
GEO_DATA_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/10m_cultural/ne_10m_admin_0_countries.geojson"