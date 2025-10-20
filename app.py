import streamlit as st


@st.dialog("Aviso de privacidad", dismissible=True, width="medium")
def aviso_privacidad():
    st.subheader("Identidad del responsable.")
    st.text(
        "Firma Gutiérrez S.A. de C.V. con identificación social GDUH0305RJ45 es responsable del trato de sus datos de contacto, con domicilio en Av. Quien Sabe dónde, con num. no me acuerdo, colonia cerca de un Oxxo, en una de las muchísimas ciudades de Oaxaca del municipio de Shipalnopecuario con entidad federativa mexicana."
    )
    st.subheader("Datos que se recaban.")
    st.markdown(
        "Los datos que son recabados de forma directa y proporcionados por usted en el **Formulario de contacto** son: <ul><li>Nombre completo </li> <li>Correo electrónico</li> <li>Número de teléfono.</li></ul>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "Los datos que son recabados por otras fuentes al momento de su visita a nuestro sitio web por medio de 'Cookies' o 'Web Beacons' son: <ul><li>Dirección IP</li><li> Tipo de navegador </li><li> Hora y fecha de acceso </li><li> Sitio web desde donde se accede a nuestro sitio web.</li></ul>",
        unsafe_allow_html=True,
    )

    st.text(
        "Entiéndase 'Cookies' como pequeños archivos de texto que se almacenan en su navegador o dispositivo móvil al visitar nuestro sitio web, y 'Web Beacons' como imágenes invisibles que permiten monitorear la actividad en nuestro sitio web."
    )

    st.text(
        "El uso de 'Web Beacons' es únicamente para fines estadísticos y de análisis, y no recopilan información personal identificable."
    )

    st.text(
        "El no proporcionar los datos personales solicitados en el formulario de contacto puede limitar nuestra capacidad para contactarlo y ofrecerle nuestros productos y servicios relacionados con 'software'."
    )

    st.subheader("Finalidades del tratamiento de sus datos")
    """Los datos personales que recabamos de usted serán utilizados para establecer contacto con usted para la venta de nuestros productos y servicios relacionados con 'software'. Atender sus solicitudes de información o comentarios. Enviar información promocional sobre nuestros productos y servicios relacionados con 'software'."
"""

    st.subheader("Consentimiento del titular")
    st.text(
        "Al proporcionar sus datos personales en el formulario de contacto, usted otorga su consentimiento para que Firma Gutiérrez S.A. de C.V. utilice sus datos con el fin de contactarlo y ofrecerle nuestros productos y servicios relacionados con 'software'."
    )
    st.subheader(
        "Opciones y medios que el responsable ofrezca a los titulares para limitar el uso o divulgación de sus datos personales."
    )
    st.text(
        "En caso de no querer recibir información promocional de nuestros servicioso o productos, usted marque  la casilla 'Rehuso recibir información promocional'."
    )
    st.text(
        "Usted puede desactivar las 'Cookies' en la configuración de su navegador, sin embargo, esto podría limitar su acceso a ciertas funciones de nuestro sitio web."
    )
    st.text(
        "El uso de 'Web Beacons' puede ser bloqueado mediante la configuración de su navegador o utilizando software especializado para bloquear rastreadores web."
    )

    st.subheader("Derechos ARCO (Acceso, Rectificación, Cancelación y Oposición)")
    st.text(
        "Usted tiene el derecho de acceder, rectificar, cancelar u oponerse al tratamiento de sus datos personales. Para ejercer estos derechos, puede contactarnos a través del correo electrónico siempre que cuente con los mecanismos para acreditar su identidad, como su firma electrónica: firmaARCO@gmail.com."
    )

    st.text(
        "También puede marcar al mismo número que se hizo uso para su contacto para solicitar la información necesaria para ejercer sus derechos ARCO. Siempre que sea valido sus datos ingresados en el formulario de contacto para ejercer correctamente su derecho."
    )

    st.text(
        "Del mismo modo puede dirigirse a nuestro domicilio ubicado en Av. Quien Sabe dónde, con num. no me acuerdo, colonia cerca de un Oxxo, en una de las muchísimas ciudades de Oaxaca del municipio de Shipalnopecuario con entidad federativa mexicana. En caso de ser así, se le pedirá una identificación oficial para acreditar su identidad."
    )

    st.subheader("Revocación del consentimiento")
    st.text(
        "Usted puede revocar su consentimiento para el tratamiento de sus datos personales en cualquier momento, mediante una solicitud enviada al correo electrónico"
    )

    st.subheader("Transferencia de datos")
    st.text(
        "Nosotros no realizamos la transferencia de sus datos personales en ningun momento durante la ejecución de nuestras operaciones de contacto o venta de nuestro software a su marca."
    )

    st.subheader("Cambios al aviso de privacidad")
    st.text(
        "Nos reservamos el derecho de efectuar en cualquier momento modificaciones o actualizaciones al presente aviso de privacidad, para la atención de novedades legislativas o políticas internas. Estas modificaciones estarán disponibles al público a través de nuestra página web. O bien, se las haremos llegar al correo electrónico que usted nos haya proporcionado."
    )

    st.caption(
        "Hacer clic en 'He leído el **Aviso de privacidad**' señala de forma expresa y acepta lo establecido en el aviso de privacidad aquí acorde a la forma en la que sus datos serán tratados."
    )

    if st.button("**Aceptar**", type="primary"):
        st.rerun()


st.set_page_config(
    page_title="CONDA web",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded",
)

columns = st.columns([1.5, 2], gap="medium", vertical_alignment="center")

with columns[0]:
    st.title("Consolida tu conocimiento y deja a lado los problemas...")
    st.header(
        "*CONDA :violet[web]*",
        anchor="CONDA web",
    )
    st.link_button(
        "¡Haz clic para pedir **la diferencia**!",
        "#Form",
        type="primary",
        use_container_width=True,
    )

with columns[1]:
    st.image(
        "https://cdn.pixabay.com/photo/2024/10/19/07/12/man-9132119_1280.jpg", width=700
    )

st.divider()

columns = st.columns(3, gap="medium", border=True)

with columns[0]:
    st.image(
        "https://images.unsplash.com/vector-1738223599537-9eeb4dd70275?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880"
    )
    st.header("Sencillo")
    st.write(
        """
        A dos clics de convertir tu información en _:violet[conocimiento]_.
        """
    )
with columns[1]:
    st.image(
        "https://images.unsplash.com/vector-1738575604316-ceae003741a7?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880"
    )
    st.header("Simple")
    st.write(
        """
        Interfaz limpia y directa para que te enfoques en lo que realmente importa: tus _:violet[datos]_.
        """
    )

with columns[2]:
    st.image(
        "https://images.unsplash.com/vector-1738220730398-d699be1fad40?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880"
    )
    st.header("Sin rodeos")
    st.write(
        """
        Nada de curvas de aprendizaje, funciones complejas o procesos complicados. Solo arrastra y suelta tus _:violet[problemas]_.
        """
    )

column = st.columns([2, 1], gap="medium", vertical_alignment="center")

with column[0]:
    st.image(
        "https://images.unsplash.com/photo-1664575602276-acd073f104c1?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170",
        caption="¡Adiós Excel! :wave: ¡Bienvenido CONDA web!",
        width=700,
    )

with column[1]:
    st.header("¿Cansado de luchar con hojas de cálculo?")
    st.text("No eres el único...")


with st.container(
    border=True,
):

    sub_columns = st.columns([2, 1], gap="medium", vertical_alignment="center")

    with sub_columns[0]:
        st.subheader(":alarm_clock: Consolida tus datos por fecha... O como quieras")
        st.text(
            "Organiza y visualiza tus datos cronológicamente para un análisis más efectivo."
        )

    with sub_columns[1]:
        st.image(
            "https://images.unsplash.com/vector-1738569772334-e11f6975c553?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880",
            width=120,
        )

with st.container(border=True, horizontal_alignment="center"):

    sub_columns = st.columns([1, 2], gap="small", vertical_alignment="center")

    with sub_columns[0]:
        st.image(
            "https://plus.unsplash.com/premium_vector-1721306578409-5afb80703d8a?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880",
            width=120,
        )

    with sub_columns[1]:
        st.subheader(
            ":rocket: Con soporte comprobado para más de 500 mil registros... POR ARCHIVO",
            width=550,
        )
        st.text(
            "Maneja grandes volúmenes de datos sin comprometer el rendimiento. Ideal para análisis extensos y detallados.",
            width=550,
        )

with st.container(
    border=True,
):
    sub_columns = st.columns([2, 1], gap="small", vertical_alignment="center")

    with sub_columns[0]:
        st.subheader(
            ":eyes: Ve el resultado de tu consolidación y comprueba los números",
            width=550,
        )
        st.text(
            "Visualiza los datos consolidados de manera clara y precisa para facilitar la toma de decisiones informadas.",
            width=550,
        )

    with sub_columns[1]:
        st.image(
            "https://plus.unsplash.com/premium_vector-1731632492293-c03ddda60275?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=880",
            width=120,
        )

st.divider()

st.header(
    "¡Empieza con la mejor solución hoy mismo con _CONDA :violet[web]!_ :tada:",
    anchor="Form",
)

with st.form("contact_form"):
    st.subheader("Formulario de contacto")
    nombre = st.text_input(
        "Nombre completo",
        placeholder="",
        type="default",
        help="Ingresa tu nombre completo.",
        icon="🧑‍💼",
    )
    correo = st.text_input(
        "Correo electrónico",
        placeholder="",
        type="default",
        help="Ingresa tu correo electrónico para que podamos contactarte.",
        icon="📨",
    )

    cel = st.text_input(
        "Número de teléfono",
        placeholder="",
        type="default",
        help="Ingresa tu número de teléfono para que podamos contactarte.",
        icon="📱",
    )

    st.form_submit_button(
        "Leer aviso de privacidad", type="tertiary", on_click=lambda: aviso_privacidad()
    )

    checkbox = st.checkbox(
        "Acepto que mis datos sean utilizados para contactarme respecto a CONDA web.",
        help="Al llenar y enviar el formulario, aceptas que tus datos sean utilizados exclusivamente para fines de contacto relacionados con CONDA web.",
    )

    promociones = st.checkbox(
        "Deseo recibir información promocional.",
        help="Marca esta casilla si deseas recibir información promocional sobre nuestros productos y servicios relacionados con 'software'. Puedes darte de baja en cualquier momento de acuerdo a nuestro **Aviso de privacidad**.",
    )

    if st.form_submit_button("Solicitar más información", type="primary"):
        if not correo and not nombre and not cel:
            st.error("Por favor, completa todos los campos del formulario.")
        if not checkbox:
            st.error(
                "Debes aceptar el aviso de privacidad para poder enviar el formulario."
            )
        
        if correo and nombre and cel and checkbox and not promociones:
            st.success(
                "¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto."
            )
            st.balloons()
        
        if correo and nombre and cel and checkbox and promociones:
            st.toast("¡Te has suscrito a nuestras promociones! Revisa tu bandeja de entrada, es posible que se haya caído un cupón del 56% para tu primera compra", icon="🎉", duration="long")
            st.balloons()
            st.success("¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.")
        
st.markdown(
    "<p style='font-size:12px'><i>Créditos a <a href='https://unsplash.com/es/@tashakostyuk'>Tasha Kostyuk</a> por sus ilustraciones. Landing page de uso académico</i></p>",
    unsafe_allow_html=True,
)
