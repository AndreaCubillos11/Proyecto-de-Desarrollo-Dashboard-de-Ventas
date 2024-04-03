from django.shortcuts import render
from Ventas.models import Venta
import plotly.express as px
import pandas as pd

def ventaControlador(request):
    ventas = Venta.objects.all()

    df = pd.DataFrame(ventas.values())

    # Calcular el promedio de ventas por mes en cada barrio
    promedio_ventas = df.groupby(['Barrio', 'Mes']).size().reset_index(name='Ventas')
    promedio_ventas = promedio_ventas.groupby(['Barrio', 'Mes'])['Ventas'].mean().reset_index()

    # Graficar el promedio de ventas por mes para cada barrio con color diferenciado por barrio
    grafico = px.bar(promedio_ventas, x="Mes", y="Ventas", color="Barrio",
                     title="Promedio de ventas por mes en cada barrio",
                     )


    fig = px.pie(promedio_ventas, values='Ventas', names='Mes', hole=.3,
                 title="Análisis de las ventas por mes")

    fig2 = px.pie(promedio_ventas, values='Ventas', names='Barrio', hole=.3,
                 title="Análisis de las ventas por barrio")
    
    fig3 = px.scatter_matrix(promedio_ventas, dimensions=["Ventas", "Mes"], color="Barrio")
    
     
    grafico.update_layout(title_font_family="Arial")
    fig.update_layout(title_font_family="Arial")
    fig2.update_layout(title_font_family="Arial")
    fig3.update_layout(title_font_family="Arial")
    
    mihtml = grafico.to_html(full_html=False)
    mihtml2 = fig.to_html(full_html=False)
    mihtml3 = fig2.to_html(full_html=False)
    mihtml4 = fig3.to_html(full_html=False)

    context = {
        "nombre": "Ivonne",
        "ventas": ventas,
        "grafico": mihtml,
        "fig": mihtml2,
        "fig2": mihtml3,
        "fig3": mihtml4
    }
    return render(request, "Ventas/index.html", context)




