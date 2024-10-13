import streamlit as st
import plotly.graph_objects as go

# Parámetros del puente
st.sidebar.header("🔧 Configuración del Puente")
longitud = st.sidebar.slider("Longitud del puente (metros)", min_value=10, max_value=100, value=50, step=5)
peso = st.sidebar.slider("Peso soportado (toneladas)", min_value=10, max_value=200, value=50, step=10)

# Definir el título de la página
st.title("Simulación de un puente con distribución de peso")

# Explicación
st.write(f"Este modelo simula un puente de {longitud} metros de largo que debe soportar un peso de {peso} toneladas.")

# Crear una gráfica en 2D con Plotly para representar un puente
fig = go.Figure()

# Dibujar la carretera del puente
fig.add_trace(go.Scatter(x=[0, longitud], y=[0, 0], mode='lines', name='Plataforma', line=dict(color='black', width=3)))

# Dibujar la carga en la estructura
fig.add_trace(go.Scatter(x=[longitud/2], y=[0], mode='markers', marker=dict(size=peso/10, color='red'), name='Carga'))

# Configurar la gráfica
fig.update_layout(title='Puente con Carga (2D)', 
                  xaxis_title='Longitud del puente (metros)', 
                  yaxis_title='Altura',
                  showlegend=False)

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig)

# Mensaje de advertencia según el peso soportado
if peso > 150:
    st.error("⚠️ ¡El peso es demasiado alto! El puente puede colapsar.")
else:
    st.success("✅ El puente está en buenas condiciones para soportar el peso.")
