# -*- coding: utf-8 -*-
"""Genera el grafico de la curva de Google Trends a partir del CSV ya guardado.
NO vuelve a llamar a Google Trends (evita rate-limit): lee el CSV semanal.
"""
import matplotlib
matplotlib.use("Agg")  # backend sin ventana
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pathlib import Path

# Relativo al propio script: el repo es publico y debe ejecutarse en cualquier
# maquina (una ruta absoluta publica ademas el arbol privado de su autor).
DIR = Path(__file__).resolve().parent
df = pd.read_csv(DIR / "google_trends_skills_semanal.csv",
                 parse_dates=["date"], index_col="date")

# Excluir la ultima semana: esta en curso (dato parcial) y engaña a la baja.
df = df.iloc[:-1]

fig, ax = plt.subplots(figsize=(11, 5.5))
for col in df.columns:
    ax.plot(df.index, df[col], linewidth=2, label=col)

# Hito: lanzamiento de Agent Skills (16 oct 2025)
hito = pd.Timestamp("2025-10-16")
ax.axvline(hito, color="#999", linestyle="--", linewidth=1)
ax.annotate("Anthropic lanza\nAgent Skills (16-oct-2025)",
            xy=(hito, 95), xytext=(hito, 70),
            fontsize=9, color="#555", ha="left",
            arrowprops=dict(arrowstyle="->", color="#999"))

ax.set_title("Interes de busqueda — 'skills' de IA (Google Trends, ultimos 12 meses)",
             fontsize=13, fontweight="bold")
ax.set_ylabel("Interes relativo (0-100)")
ax.set_ylim(0, 105)
ax.legend(loc="upper left", frameon=False)
ax.grid(True, alpha=0.25)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b-%y"))
fig.autofmt_xdate()
fig.tight_layout()
fig.text(0.01, 0.01,
         "Fuente: Google Trends (interes relativo 0-100). Ultima semana en curso excluida (dato parcial).",
         fontsize=7, color="#888")

out = DIR / "grafico_tendencia_skills.png"
fig.savefig(out, dpi=150)
print(f"[OK] Grafico guardado: {out}")
