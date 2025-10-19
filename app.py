import streamlit as st

@st.dialog("Aviso de privacidad", dismissible=True, width="medium")
def aviso_privacidad():
    return 

st.set_page_config(
    page_title="CONDA web",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded",
)

columns = st.columns([1.5, 2], gap="medium", vertical_alignment="center")

with columns[0]:
    st.title("Consolida tu conocimiento y deja a lado los problemas...")
    st.header("*CONDA :violet[web]*", anchor="CONDA web", )
    st.link_button("¡Haz clic para pedir **la diferencia**!", "#Form", type="primary", use_container_width=True, )
    
with columns[1]:
    st.image("https://cdn.pixabay.com/photo/2024/10/19/07/12/man-9132119_1280.jpg", width=700)
    
st.divider()

columns = st.columns(3, gap="medium", border=True)

with columns[0]:
    st.image("https://images.unsplash.com/vector-1738223599537-9eeb4dd70275?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880")
    st.header("Sencillo")
    st.write(
        """
        A dos clics de convertir tu información en _:violet[conocimiento]_.
        """
    )
with columns[1]:
    st.image("https://images.unsplash.com/vector-1738575604316-ceae003741a7?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880")
    st.header("Simple")
    st.write(
        """
        Interfaz limpia y directa para que te enfoques en lo que realmente importa: tus _:violet[datos]_.
        """
    )

with columns[2]:
    st.image("https://images.unsplash.com/vector-1738220730398-d699be1fad40?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880")
    st.header("Sin rodeos")
    st.write(
        """
        Nada de curvas de aprendizaje, funciones complejas o procesos complicados. Solo arrastra y suelta tus _:violet[problemas]_.
        """
    )

column = st.columns([2, 1], gap="medium", vertical_alignment="center")

with column[0]:
    st.image("https://images.unsplash.com/photo-1664575602276-acd073f104c1?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170", caption="¡Adiós Excel! :wave: ¡Bienvenido CONDA web!" , width=700)
    
with column[1]:
    st.header("¿Cansado de luchar con hojas de cálculo?")
    st.text("No eres el único...")
    

with st.container(border=True, ):
    
    sub_columns = st.columns([2, 1], gap="medium", vertical_alignment="center")
    
    with sub_columns[0]:
        st.subheader(":alarm_clock: Consolida tus datos por fecha... O como quieras")
        st.text("Organiza y visualiza tus datos cronológicamente para un análisis más efectivo.")
    
    with sub_columns[1]:
        st.image("https://images.unsplash.com/vector-1738569772334-e11f6975c553?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880", width=120)

with st.container(border=True, horizontal_alignment="center"):
    
    sub_columns = st.columns([1, 2], gap="small", vertical_alignment="center")
    
    with sub_columns[0]:
        st.image("https://plus.unsplash.com/premium_vector-1721306578409-5afb80703d8a?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880", width=120)
    
    with sub_columns[1]:
        st.subheader(":rocket: Con soporte comprobado para más de 500 mil registros... POR ARCHIVO", width=550)
        st.text("Maneja grandes volúmenes de datos sin comprometer el rendimiento. Ideal para análisis extensos y detallados.", width=550)

with st.container(border=True, ):
    sub_columns = st.columns([2, 1], gap="small", vertical_alignment="center")
    
    with sub_columns[0]:
        st.subheader(":eyes: Ve el resultado de tu consolidación y comprueba los números", width=550)
        st.text("Visualiza los datos consolidados de manera clara y precisa para facilitar la toma de decisiones informadas.", width=550)
        
    with sub_columns[1]:
        st.image("https://plus.unsplash.com/premium_vector-1731632492293-c03ddda60275?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880", width=120)

st.divider()

st.header("¡Empieza con la mejor solución hoy mismo con _CONDA :violet[web]!_ :tada:", anchor="Form")

with st.form("contact_form"):
        correo = st.text_input("Correo electrónico", placeholder="", type="default", help="Ingresa tu correo electrónico para que podamos contactarte.", icon="📨")
        
        cel = st.text_input("Número de teléfono", placeholder="", type="default", help="Ingresa tu número de teléfono para que podamos contactarte.", icon="📱")
        
        st.form_submit_button("Leer aviso de privacidad", type="tertiary", on_click=lambda: aviso_privacidad())
        
        checkbox = st.checkbox("He leído el **Aviso de privacidad** y acepto que mis datos sean utilizados para contactarme respecto a CONDA web.", value=False, help="Al marcar esta casilla, aceptas que tus datos sean utilizados exclusivamente para fines de contacto relacionados con CONDA web.")
        
        st.form_submit_button("¡Haz clic para pedir **la diferencia**!", type="primary")

st.markdown("<p style='font-size:12px'><i>Créditos a <a href='https://unsplash.com/es/@tashakostyuk'>Tasha Kostyuk</a> por sus ilustraciones. Landing page de uso académico</i></p>", unsafe_allow_html=True)