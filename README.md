# Form-visualizer

## Setup instrukcijas

1. Uzinstalējam bibliotēkas

```
pip install streamlit wordcloud peewee plotly pandas
```

**NOTE**: Tagad vairs nav obligāti jālaiž katrs skripts atsevišķi. Tie izpildās automātiski līdz ko tiek uploadots jauns survey fails

2. Palaid datubāzes setup skriptu (es izmantoju python3.9)

```python scripts/init_database.py```

3. Palaid (sample) datu importēšanas skriptu

```python scripts/import_data.py```

4. Pārbaudi, ka dati ir datubāzē

```python scripts/check_data.py```

## WEB app palaišana

Streamlit oficiāli var palaist šādi:

```
streamlit run app.py
```

Ja tas neiet un sūdzās, ka "'streamlit' is not recognized as the name of a cmdlet, function, script file, or operable program", tad pamēģini palaist šādi:

```
python -m streamlit run app.py
```

After that browserī vajadzētu visam būt.

Iziet var ar CTRL+C