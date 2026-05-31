import streamlit as st
from generator import generate_test_cases
from prompts import LANG_CONFIG

st.set_page_config(
    page_title="AI Test Case Generator",
    page_icon="🧪",
    layout="centered"
)

st.title("AI Test Case Generator")
st.caption("Powered by Groq · Open Source · By José Wannan")

# - texto -
feature = st.text_area(
    "Descripción de la feature o user story",
    placeholder="Ej: El usuario puede iniciar sesión con email y contraseña. Si las credenciales son incorrectas, ve un mensaje de error.",
    height=150,
    max_chars=200
)
char_count = len(feature)
chars_remaining = 150 - char_count
exceeds_limit = char_count > 150

if exceeds_limit:
    st.error(f"Has excedido el límite por {abs(chars_remaining)} caracteres.")


# - options -
language_options = list(LANG_CONFIG.keys())

col1, col2 = st.columns(2)
with col1:
    language = st.selectbox("Idioma", language_options)
with col2:
    model = st.selectbox(
        "Modelo",
        ["qwen/qwen3-32b", "openai/gpt-oss-20b"]
    )

# - generar -
if st.button("Generar casos de prueba", type="primary",  disabled=exceeds_limit or char_count == 0):
    if not feature.strip():
        st.warning("Escribe la descripción de la feature primero.")
    else:
        with st.spinner("Generando casos de prueba..."):
            result = generate_test_cases(feature_description=feature, language=language, model=model)
        
        st.success("Casos generados")
        st.markdown(result)
        
        # Botón para descargar
        st.download_button(
            "Descargar como .txt",
            data=result,
            file_name="test_cases.txt",
            mime="text/plain"
        )