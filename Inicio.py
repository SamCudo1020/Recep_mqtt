import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# --- CONFIGURACIÓN DE ESTILO PARA SUSANA ---
st.set_page_config(page_title="MQTT Control - Susana Edition", layout="centered")

# Estilo CSS para una estética orgánica y limpia
st.markdown("""
    <style>
    .stApp {
        background-color: #f1f3f0;
        background-image: linear-gradient(160deg, #f1f3f0 0%, #d4e0d4 100%);
    }
    /* Estilo de las tarjetas de control */
    .stHeader {
        color: #4a5d4a;
    }
    /* Botones con estilo orgánico */
    .stButton>button {
        background-color: #7a947a;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5d755d;
        border: none;
        color: #e8f0e8;
        transform: translateY(-2px);
    }
    /* Títulos en verde oscuro */
    h1, h2, h3 {
        color: #2f3e2f !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Slider personalizado */
    .stSlider {
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Muestra la versión de Python
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

# --- LÓGICA MQTT ---
def on_publish(client,userdata,result):
    pass

broker="157.230.214.127"
port=1883

st.title("🌿 Control de Dispositivos")
st.markdown("### Interfaz de Usuario - Susana")

# Distribución limpia
col1, col2 = st.columns(2)

with col1:
    if st.button('Activar Sistema'):
        act1="ON"
        client1= paho.Client("GIT-HUB")                           
        client1.on_publish = on_publish                          
        client1.connect(broker,port)  
        message = json.dumps({"Act1":act1})
        client1.publish("cmqtt_s", message)
        st.toast("Sistema Iniciado", icon="✅")

with col2:
    if st.button('Desactivar'):
        act1="OFF"
        client1= paho.Client("GIT-HUB")                           
        client1.on_publish = on_publish                          
        client1.connect(broker,port)  
        message = json.dumps({"Act1":act1})
        client1.publish("cmqtt_s", message)
        st.toast("Sistema en Pausa", icon="⚪")

st.markdown("---")

# Slider con feedback visual
values = st.slider('Ajuste de Intensidad', 0.0, 100.0, 50.0)
st.write(f'**Nivel seleccionado:** {values}%')

if st.button('Sincronizar Valor'):
    client1= paho.Client("GIT-HUB")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message = json.dumps({"Analog": float(values)})
    client1.publish("cmqtt_a", message)
    st.success(f"Valor {values} sincronizado")
