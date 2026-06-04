# -*- coding: utf-8 -*-
"""Curva real de Google Trends para la tendencia de las 'skills' de IA.
Parte del enjambre Analista de Audiencias (caso de estudio / demo).
Saca el interes de busqueda de los ultimos 12 meses y lo guarda en CSV.
"""
import sys

# SSL robusto en el entorno de Juan (si truststore esta disponible)
try:
    import truststore
    truststore.inject_into_ssl()
    print("[info] truststore activo")
except Exception as e:
    print(f"[info] truststore no disponible ({e}); SSL por defecto")

import pandas as pd
from pytrends.request import TrendReq

OUT_DIR = r"C:\PROYECTOS_GITHUB\TechAcces\Enjambre_Analista_Audiencias\estudio_skills"

# Terminos foco (comparables en magnitud: todos de nicho 'skills de IA')
kw_list = ["Claude skills", "agent skills", "AI agent skills"]
timeframe = "today 12-m"   # ultimos 12 meses, resolucion semanal
geo = ""                    # mundial (maximo volumen de senal)

print(f"Consultando Google Trends: {kw_list} | {timeframe} | geo='{geo or 'mundial'}'")

pytrends = TrendReq(hl="en-US", tz=0)
pytrends.build_payload(kw_list, timeframe=timeframe, geo=geo)
df = pytrends.interest_over_time()

if df is None or df.empty:
    print("[ERROR] Google Trends devolvio vacio (rate-limit o terminos sin volumen suficiente).")
    sys.exit(1)

if "isPartial" in df.columns:
    df = df.drop(columns=["isPartial"])

# Guardar serie semanal completa
df.to_csv(OUT_DIR + r"\google_trends_skills_semanal.csv", encoding="utf-8-sig")

# Resumen mensual (media)
mensual = df.resample("ME").mean().round(1)
mensual.to_csv(OUT_DIR + r"\google_trends_skills_mensual.csv", encoding="utf-8-sig")

print("\n=== Interes de busqueda — media mensual (escala 0-100) ===")
print(mensual.to_string())

print("\n=== Ultimas 8 semanas ===")
print(df.tail(8).to_string())

print("\n[OK] CSV guardados en estudio_skills/ (semanal y mensual).")
