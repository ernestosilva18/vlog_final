#En primer lugar, importamos las librerías necesarias para la aplicación. Streamlit es la principal, ya que nos permitirá crear la página web.
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

#Luego, creamos un menú vertical en la barra lateral para navegar entre secciones con el comando option_menu. Este menú tendrá tres opciones: Inicio, Experiencia y Gráficos, cada una con su respectivo ícono. 
with st.sidebar: 
    opciones = option_menu(None,['Inicio', 'Experiencia', 'Gráficos'] , 
        icons=['spotify','brilliance', 'battery-full'], menu_icon="non", default_index=0)

# Luego, aplico estilos globales usando markdown con HTML/CSS para la apariencia del texto dentro de la web.
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Yeseva+One&display=swap" rel="stylesheet">
    <style>
    
        /* Fondo de la app */
        [data-testid="stAppViewContainer"] {
            background-image: url("https://wallpapers.com/images/hd/christmas-teams-background-qj2j0kqebj8bpb0q.jpg");
        }

        /* h1: títulos y subtítulos en color #E50914 */
        h1, .titulo, .subtitulo,
        [data-testid="stMarkdownContainer"] h1,
        .stSubheader, .stHeader, .stMetricLabel { 
            color: #E50914 !important;
        }

        /* h2: resto del texto en blanco */
        h2,
        [data-testid="stMarkdownContainer"] h2 {
            color: #FFFFFF !important;
        }

    </style>
    """,
    unsafe_allow_html=True
)

#A continuación verificamos qué opción del menú fue seleccionada para mostrar la sección correspondiente. Esto a través de condicionales if-elif, donde cada bloque de código renderiza el contenido específico de la sección seleccionada.
if opciones == 'Inicio':
    #Luego, mostramos el título principal de la sección Inicio.
    st.markdown("<h1 style='text-align: center; font-size: 100px; color: #E50914 !important'>ENTRE PAZ Y DESGRACIA</h1>", unsafe_allow_html=True)

    #Posteriormente, organizamos el contenido en dos columnas para imagen y texto mediante el comando st.columns. Esto permite que la imagen y el texto se muestren lado a lado.
    col1, col2 = st.columns(2)

    #Luego, en la columna izquierda, cargamos y mostramos la imagen de perfil con el comando st.image. Además, establecemos un ancho específico para la imagen.
    col1.image("fotoperfil.jpeg", caption='Ernesto o Martín xd', width=300)

    #Después, en la columna derecha, definimos el texto de presentación y lo renderizamos utilizando markdown con HTML para justificarlo. Esto permite que el texto se vea más estético y legible.
    texto = """
    Mi nombre es Ernesto (o Martín) Silva, estudiante de la carrera de publicidad en la PUCP. 
    Lo que más me gusta de la carrera es la libertad que tengo para navegar y explotar mi 
    creatividad en función de crear algo que sea útil para una marca o persona. 
    Adoro escuchar música, realmente siento que no podría vivir sin la música. 
    Da igual si estoy dentro o fuera de la universidad, no puedo estar sin mis audífonos 
    escuchando música. Además, me gusta jugar videojuegos de vez en cuando. 
    Antes solía ser mucho más frecuente, pero con el tiempo fui perdiendo más y más 
    interés en ello, y ahora sólo son un pequeño pasatiempo.  
    """

    #Finalmente, renderizamos el texto utilizando markdown con HTML para justificarlo.
    col2.markdown(f"<h2 style='text-align: justify; font-size: 18px;'>{texto}</h2>", unsafe_allow_html=True)

elif opciones == 'Experiencia': #Posteriormente, si el usuario selecciona la opción Experiencia, muestro el título de la sección Experiencia mediante st.markdown con HTML para centrarlo y darle un tamaño de fuente grande. 
    #Esto permite que el título mantenga la estética de la página principal.
    st.markdown("<h1 style='text-align: center; font-size: 80px; color: #FF1515'>Ey, ¿te llama la atención programar?</h1>", unsafe_allow_html=True)

    #Luego, mostramos la sección Experiencia con su título y descripción.
    texto_2 = """
    Mi experiencia aprendiendo Python realmente se remonta a épocas de pandemia. Por allá del 2020-21, con comandos simples empleando las funciones: print, if, elif, else, comencé a familiarizarme con el lenguaje de programación. Sin embargo, luego de ello, no volví a adentrarme en algún otro lenguaje en general. Al menos eso creía, hasta que finalmente, en este 2026 volví a interactuar con el lenguaje de Python, donde aprendería muchísimo más de los conocimientos que ya tenía previamente.
    Al inicio realmente pensaba que el lenguaje era bastante simple. No obstante, conforme avanzaba en las clases me daba cuenta que también demanda mucha paciencia y mucho más conocimiento acerca de él conforme vas descubriendo nuevas funciones y/o comandos. Por ello, considero que fue muy enriquecedor ir progresando durante las semanas, pues, así pude no solo aprender a programar una página web, sino que, en general, obtuve muchísimo conocimiento para crear otro tipo de cosas. Por ejemplo, gráficos, listas, juegos, etc. Siento que esta experiencia realmente me servirá a futuro, principalmente para saber ordenar y facilitarme el manejo de datos.
    Además, quisiera dejar adjuntos algunos videos respecto a mi trayectoria dentro del curso: mis 2 PC's y la idea de mi proyecto final, al cual podrán acceder muy pronto :))).
    """

    #Posteriormente, mostramos el texto de la sección Experiencia utilizando st.markdown con HTML para justificarlo.
    st.markdown(f"<h2 style='text-align: justify; font-size: 18px;'>{texto_2}</h2>", unsafe_allow_html=True)

    #Después, incluímos subtítulos y botones que enlazan a los videos en Drive mediante st.link_button, que permiten crear enlaces dinámicos.
    st.markdown("<h3 style='color: #E50914;'>💻 Diferencias entre Strings y Listas - Google Drive</h3>", unsafe_allow_html=True) #Creamos un botón que redirige al usuario a un video alojado en Google Drive. 
    #Al hacer clic, el video se abrirá en una nueva pestaña del navegador. Esto se logra mediante el comando st.link_button, que permite crear enlaces dinámicos.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1cw9omQmLY7FFYNi6rlcmzCjqxUiL0wv_/view?usp=drive_link"
        )
    #Añadimos la descripción del primer video.
    st.markdown(
        "<h2 style='text-align: justify; font-size: 18px;'>En este video se presentan las diferencias entre los Strings y las Listas, donde, en términos sencillos, un String es como una palabra escrita con lapicero. Es decir, no puedes cambiar algo sin tener que dañar o hacer algo que interfiera con el papel. Por otro lado, las Listas son como un archivador de carpetas: puedes poner una nueva, cambiar orden, etc. Sin detallar más, dentro de este video conocerán más dieferencias entre ambas.</h2>",
        unsafe_allow_html=True
    )

    st.markdown("<h3 style='color: #E50914;'>💡Diferencias entre los bucles For y While - Google Drive</h3>", unsafe_allow_html=True)

    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1nd7dc-lQB_Imw_7h2kHjw_GC0kViXqYI/view?usp=drive_link"
        )
    #Añadimos la descripción del segundo video.
    st.markdown(
        "<h2 style='text-align: justify; font-size: 18px;'>En este video se presentan las diferencias entre los bucles for y while. Por un lado, en términos sencillos, un buble se encarga de repetir una acción para que nosotros no tengamos que escribir el mismo código una y otra vez. Por otro lado, respecto al for y el while, ambos repiten cosas, pero se usan de formas diferentes. Si te interesa conocer más acerca de estas diferencias, te invito a mirar el video completo.</h2>",
        unsafe_allow_html=True
    )

    st.markdown("<h3 style='color: #E50914;'>🎸 Proyecto Final / Concepto de Página Web - Google Drive</h3>", unsafe_allow_html=True)

    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1pyzD2s0PBpEGRAACeUSFanRkdN6OEhB9/view?usp=drive_link"
        )
    #Añadimos la descripción del tercer video.
    st.markdown(
        "<h2 style='text-align: justify; font-size: 18px;'>En este video se presenta lo que será mi proyecto final (o que quizás ya salió al público), el cual consiste en una página web interactiva dedicada a la banda Twenty One Pilots, analizando su discografía, desglosando sus canciones, conociendo el lore construido por la banda a lo largo de los años y demás cosas que, cuando estén listas, los invito cordialmente a visitarla, ya sean fans de la banda o no.</h2>",
        unsafe_allow_html=True
    )

elif opciones == 'Gráficos': #Finalmente, si el usuario selecciona la opción Gráficos, muestro el título de la sección Gráficos mediante st.markdown con HTML para centrarlo y darle un tamaño de fuente grande.
    st.markdown("<h1 style='text-align: center; font-size: 80px; color: #FF1515'>ALGUNOS GRÁFICOS HECHOS EN CLASE</h1>", unsafe_allow_html=True)

    #En esta sección, ofreceremos una selección para elegir qué mostrar a través de un selectbox, que permite al usuario elegir entre diferentes gráficos y mapas interactivos. Esto se logra mediante el comando st.selectbox, que crea un menú desplegable con las opciones disponibles.
    #Primero, definimos una lista de opciones que contiene los nombres de los gráficos y mapas interactivos que se pueden mostrar.
    graficos = ['Gráfico_1', 'Gráfico_2', 'Gráfico_3','Gráfico_4', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos) #Luego, creamos un selectbox que permite al usuario elegir entre los gráficos y mapas interactivos disponibles. El valor seleccionado se almacenará en la variable grafico_seleccionado.

    #Mostramos el contenido según la opción seleccionada mediante condicionales if-elif. Dependiendo de la opción elegida, se mostrará el título, la interpretación y la imagen correspondiente al gráfico o mapa interactivo seleccionado.
    if grafico_seleccionado == 'Gráfico_1':

        st.markdown("<h3 style='color: #E50914;'>🏃‍♂️💨 Promedio de goles anotados anotados como local por equipo</h3>", unsafe_allow_html=True)

        st.markdown(
            """
            <h2 style='text-align: justify; font-size: 20px;'>
            Este gráfico analiza principalmente el promedio de goles anotados como local por equipo respecto a las jornadas de la Liga de Francia. Como puede verse en el Gráfico, equipos como el Angers, Auxerre, Nantes, entre otros, tienen un promedio cercano a un gol por partido jugando como locales. Por otro lado, hay equipos como el Marseille y el PSG, quienes tienen casi un promedio de 2.5 goles por partido jugando como local.
            </h2>
            """,
            unsafe_allow_html=True
        )

        #Luego, centramos la imagen del gráfico mediante el uso de columnas. Creamos tres columnas con diferentes proporciones de ancho, y colocamos la imagen en la columna central para que quede centrada en la página.
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "gráfico5.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        #Mostramos el título e interpretación del segundo gráfico.
        st.markdown("<h3 style='color: #E50914;'>🟥 Promedio de Tarjetas Rojas recibidas por Equipo Local</h3>", unsafe_allow_html=True)

        #Mostramos la interpretación del gráfico.
        st.markdown(
            """
            <h2 style='text-align: justify; font-size: 20px;'>
            Este gráfico analiza principalmente el promedio de tarjetas rojas recibidas por equipo jugando como local respecto a las jornadas de LaLiga Española. Como puede verse en el Gráfico de barras. este está ordenado de mayor promedio de tarjetas rojas por equipo a menor. En este caso, el Girona se posiciona como el equipo con mayor promedio de tarjetas rojdas, seguido por el Real Madrid y el Oviedo; mientras que, por otro lado, equipos como el Celta, el Elche, Villareal, etc., se posicionan con números más bajos; además de los equipos cuyo promedio de tarjetas rojas como local es nulo, como el Barcelona y el Valencia.
            </h2>
            """,
            unsafe_allow_html=True
        )

        #Cenrtramos la imagen del gráfico mediante el uso de columnas al igual que el gráfico anterior.
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gráfico6.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_3':
        #Mostramos el título e interpretación del tercer gráfico.
        st.markdown("<h3 style='color: #E50914;'>💙❤️ Rendimiento del FCBarcelona jugando como visitante</h3>", unsafe_allow_html=True)

        #Mostramos la interpretación del gráfico.
        st.markdown(
            """
            <h2 style='text-align: justify; font-size: 20px;'>
            Este gráfico analiza principalmente el rendimiento del FCBarcelona durante LaLiga española cuando éste juega de visitante. Para ello, el gráfico de pastel está repartido principalmente en: los partidos ganados, los perdidos y los empatados. De esta manera, es posible notar que, en términos generales, al Barcelona le va relativamente bien, dentro de lo que cabe, habiendo ganado la mayoría de sus partidos, habiendo perdido menos de la mitad y habiendo empatado algunos pocos.
            </h2>
            """,
            unsafe_allow_html=True
        )

        #Cenrtramos la imagen del gráfico mediante el uso de columnas.
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gráfico7.png",
                width=800
            )
    elif grafico_seleccionado == 'Gráfico_4':
        #Mostramos el título e interpretación de la nube de palabras.
        st.markdown("<h4 style='color: #E50914;'>☁️ Nube de palabras</h4>", unsafe_allow_html=True)

        #Mostramos la interpretación de la nube.
        st.markdown(
            """
            <h2 style='text-align: justify; font-size: 20px;'>
            Esta nube de palabras fue creada a partir de un diccionario vacío inicial, utilizado para almacenar la cantidad de veces que aparece cada palabra de una lista depurada. Por ello, al imprimirlo, este nos muestra la nube de palabras, habiendo utilizado los datos del diccionario obtenido anteriormente. Además, es posible apreciar los ejes de la nube, y es posible apreciar que la palabra no es la que más se repite.
            </h2>
            """,
            unsafe_allow_html=True
        )

        #Cenrtramos la imagen de la nube.
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "gráfico8.png",
                width=800
            )

    elif grafico_seleccionado == 'Mapa_1':
        #Mostramos el título e interpretación del mapa interactivo.
        st.markdown("<h4 style='color: #E50914;'>🗺️ Mapa de los lugares donde se grabaron mis series y película favoritas</h4>", unsafe_allow_html=True)

        #Mostramos la interpretación del mapa.
        st.markdown(
            """
            <h2 style='text-align: justify; font-size: 20px;'>
            En este mapa es posible apreciar exactamente las ubicaciones en las que fueron grabadas las series y película que más han sido de mi agrado durante mi vida, las cuales son: Riverdale, Stranger Things, Spiderman No Way Home, Euphoria y Bessos, Kitty. Como es posible apreciar, cada marcador está situado en el lugar original donde se rodó cada material audiovisual.
            </h2>
            """,
            unsafe_allow_html=True
        )

        #Finalmente, cargo el HTML del mapa interactivo generado previamente con Folium y lo muestro en la aplicación web. Esto lo logramos mediante el uso de componentes.html, que permite renderizar contenido HTML directamente en la página.
        with open("mapa_interactivo.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        #Mostramos el mapa interactivo y habríamos llegado al final.
        components.html(
            html_content,
            height=600
        )
