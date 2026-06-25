# Jarvis 🤖

Un assistente intelligente multilingue con supporto per mappe interattive del mondo.

## 🎯 Caratteristiche Principali

- 🗺️ **Mappa Interattiva del Mondo** - Visualizza paesi e informazioni geografiche
- 🇮🇹 **Supporto Italiano** - Interfaccia completamente in italiano
- 🧮 **Operazioni Matematiche** - Esegui calcoli e operazioni
- 🌍 **Ricerca Paesi** - Cerca e visualizza informazioni su paesi specifici
- ⚡ **Comandi Intelligenti** - Rispondi a comandi personalizzati

## 📁 Struttura del Progetto

```
jarvis/
├── README.md
├── requirements.txt
├── main.py
├── config/
│   └── settings.py
├── core/
│   ├── __init__.py
│   ├── assistant.py
│   └── command_processor.py
├── features/
│   ├── __init__.py
│   ├── calculator.py
│   ├── translator.py
│   └── world_map.py
├── data/
│   ├── countries.json
│   └── world_map_data.json
└── tests/
    ├── __init__.py
    ├── test_calculator.py
    ├── test_world_map.py
    └── test_commands.py
```

## 🚀 Guida Rapida

### Installazione

```bash
# Clona il repository
git clone https://github.com/locapopietro28-prog/jarvis.git
cd jarvis

# Crea un ambiente virtuale
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# Installa le dipendenze
pip install -r requirements.txt
```

### Utilizzo

```bash
# Avvia Jarvis
python main.py
```

### Comandi Disponibili

- `calcola 2 + 2` - Esegui operazioni matematiche
- `mostra [paese]` - Visualizza informazioni su un paese
- `mappa` - Mostra la mappa interattiva del mondo
- `aiuto` - Mostra l'elenco dei comandi disponibili

## 📦 Dipendenze Principali

- `requests` - Per le richieste HTTP
- `matplotlib` - Per la visualizzazione di grafici e mappe
- `geopandas` - Per l'elaborazione di dati geografici
- `pandas` - Per la manipolazione di dati

## 🧪 Test

```bash
# Esegui i test
pytest tests/

# Esegui i test con coverage
pytest --cov=core --cov=features tests/
```

## 📝 Contribuire

Le contribuzioni sono benvenute! Per favore:

1. Fork il progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit i tuoi cambiamenti (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📄 Licenza

Questo progetto è open source e disponibile sotto la licenza MIT.

## 👤 Autore

**locapopietro28-prog**

## 📞 Supporto

Per problemi e domande, apri un'issue su GitHub.

---

*Jarvis - Il tuo assistente intelligente per il mondo* 🌍