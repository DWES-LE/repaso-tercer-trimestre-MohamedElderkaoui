Para documentar cómo iniciar Wagtail en un archivo `readme.md`, puedes seguir estos pasos:

1. **Título y descripción**: Comienza el archivo `readme.md` con un título descriptivo y una breve descripción del proyecto.

   ```markdown
   # Proyecto Wagtail

   Este proyecto es un sitio web desarrollado utilizando el framework Wagtail.
   ```

2. **Requisitos previos**: Enumera los requisitos previos necesarios para ejecutar el proyecto. Esto puede incluir la versión de Python, la instalación de Django y Wagtail, y cualquier otra dependencia necesaria.

   ```markdown
   ## Requisitos previos
        
        -   anyascii==0.3.2
        - asgiref==3.6.0
        - beautifulsoup4==4.11.2
        - certifi==2023.5.7
        - charset-normalizer==3.1.0
        - defusedxml==0.7.1
        - Django==4.2.1
        - django-filter==22.1
        - django-modelcluster==6.0
        - django-permissionedforms==0.1
        - django-taggit==3.1.0
        - django-treebeard==4.7
        - djangorestframework==3.14.0
        - draftjs-exporter==2.1.7
        - et-xmlfile==1.1.0
        - filetype==1.2.0
        - html5lib==1.1
        - idna==3.4
        - l18n==2021.3
        - openpyxl==3.1.2
        - Pillow==9.5.0
        - pytz==2023.3
        - requests==2.30.0
        - six==1.16.0
        - soupsieve==2.4.1
        - sqlparse==0.4.4
        - telepath==0.3
        - tzdata==2023.3
        - urllib3==2.0.2
        - wagtail==5.0
        - webencodings==0.5.1
        - bakerydemo==4.0.0
        - Willow==1.5
        
   ```

3. **Instalación**: Proporciona instrucciones claras sobre cómo instalar y configurar el proyecto. Puedes incluir comandos de instalación de paquetes, configuración de entornos virtuales y cualquier otro paso necesario.

   ```markdown
   ## Instalación

   1. Clona el repositorio:

      ```bash
      git clone[ https://github.com/tu-usuario/proyecto-wagtail.git](https://github.com/DWES-LE/repaso-tercer-trimestre-MohamedElderkaoui)
      ```

   2. Crea y activa un entorno virtual:

      ```bash
      python3 -m venv myenv
      source myenv/bin/activate
      ```

   3. Instala las dependencias:

      ```bash
      pip install -r requirements.txt
      ```

   4. Configura la base de datos y las variables de entorno necesarias.

   5. Ejecuta las migraciones:

      ```bash
      python manage.py migrate
      ```

   6. Inicia el servidor de desarrollo:

      ```bash
      python manage.py runserver
      ```

   7. Accede al sitio web en tu navegador en `http://localhost:8000`.
   ```

4. **Estructura del proyecto**: Si es necesario, puedes proporcionar una descripción de la estructura de directorios del proyecto Wagtail y explicar cómo se organizan los archivos y las aplicaciones.

   ```markdown
   ## Estructura del proyecto

   - `proyecto-wagtail/`: Directorio principal del proyecto.
     - `manage.py`: Archivo de gestión de Django.
     - `requirements.txt`: Archivo que contiene las dependencias del proyecto.
     - Otros archivos y directorios del proyecto...

   - `miaplicacion/`: Directorio de la aplicación personalizada.
     - `models.py`: Archivo con los modelos de la aplicación.
     - `views.py`: Archivo con las vistas de la aplicación.
     - Otros archivos y directorios de la aplicación...
   ```

5. **Personalización**: Si has realizado personalizaciones específicas en el proyecto, puedes mencionarlas aquí y proporcionar cualquier información adicional necesaria.

   ```markdown
   ## Personalización

   - Se ha personalizado el modelo `Equipo` para incluir campos adicionales.
   - Se ha creado una aplicación personalizada llamada `miaplicacion` para manejar funcionalidades específicas.
   - Otros detalles de personalización...
   ```

6. **Contribución**: Si permites contribuciones al proyecto, puedes incluir instrucciones sobre cómo contribuir y cómo enviar solicitudes de extracción.

   ```markdown
   ## Contribución

   Si deseas contrib

uir a este proyecto, sigue los siguientes pasos:

   1. Haz un fork del repositorio.
   2. Crea una rama para tu contribución.
   3. Realiza los cambios y las mejoras.
   4. Envía una solicitud de extracción.
   ```

7. **Licencia**: Si el proyecto está bajo una licencia específica, menciona la licencia y proporciona un enlace al archivo de licencia.

   ```markdown
   ## Licencia

   Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más información.
   ```

Estos son solo ejemplos de secciones que puedes incluir en tu archivo `readme.md` para documentar el proyecto Wagtail. Asegúrate de adaptarlos a las necesidades y características específicas de tu proyecto.








## Proyecto de Personas en Wagtail

Este proyecto tiene como objetivo recopilar información sobre personas y mostrarla en una página web utilizando el framework Wagtail. A continuación se describen los modelos y las características principales del proyecto.

### Modelo de Persona

El modelo de Persona se utiliza para almacenar la información de cada persona en el sistema. Contiene los siguientes campos:

- `nombre`: Campo de tipo `CharField` que almacena el nombre de la persona.
- `apellidos`: Campo de tipo `CharField` que almacena los apellidos de la persona.
- `fecha_nacimiento`: Campo de tipo `DateField` que almacena la fecha de nacimiento de la persona.
- `lugar_nacimiento`: Campo de tipo `CharField` que almacena el lugar de nacimiento de la persona.
- `biografia`: Campo de tipo `RichTextField` que almacena la biografía de la persona.
- `foto`: Campo de tipo `ImageField` que almacena la foto de la persona.
- `twitter`: Campo de tipo `URLField` opcional que almacena el enlace al perfil de Twitter de la persona.
- `facebook`: Campo de tipo `URLField` opcional que almacena el enlace al perfil de Facebook de la persona.
- `instagram`: Campo de tipo `URLField` opcional que almacena el enlace al perfil de Instagram de la persona.
- `linkedin`: Campo de tipo `URLField` opcional que almacena el enlace al perfil de LinkedIn de la persona.
- `body`: Campo de tipo `RichTextField` opcional para almacenar información adicional sobre la persona.
- `into`: Campo de tipo `RichTextField` opcional para almacenar detalles importantes sobre la persona.
- `tags`: Campo de tipo `ClusterTaggableManager` que permite agregar etiquetas a la persona.

El modelo `Persona` hereda de la clase `Page` de Wagtail y tiene las siguientes propiedades:

- `template`: Propiedad que especifica la plantilla utilizada para renderizar la página de detalle de la persona.
- `search_fields`: Propiedad que define los campos utilizados para realizar búsquedas en el sitio.
- `content_panels`: Propiedad que especifica los paneles de administración para editar los campos del modelo.
- `promote_panels`: Propiedad que especifica los paneles de administración para configurar opciones de promoción del modelo.
- `Meta`: Clase que contiene metadatos del modelo, como el nombre en singular y plural.

### Página de Índice de Personas

La página de índice de personas se utiliza para mostrar un listado de personas agrupadas y ordenadas por categorías. Tiene las siguientes características:

- `intro`: Campo de tipo `RichTextField` opcional para agregar una introducción a la página.

El modelo `PersonaIndexPage` hereda de la clase `Page` de Wagtail y tiene las siguientes propiedades:

- `template`: Propiedad que especifica la plantilla utilizada para renderizar la página de índice de personas.
- `content_panels`: Propiedad que especifica los paneles de administración para editar los campos del modelo.
- `subpage_types`: Propiedad que especifica los tipos de páginas secundarias permitidas en la página de índice.
- `get_context()`: Método utilizado para obtener el contexto de la página, incluyendo la lista de personas a mostrar.

### Plantillas

El proyecto incluye plantillas para la página de detalle de personas (`persona_page.html`) y la

 página de índice de personas (`persona_list_page.html`). Estas plantillas se pueden personalizar según los requisitos de diseño del proyecto.

¡Este es el esqueleto del proyecto de personas en Wagtail! Puedes modificar y ampliar estos modelos y plantillas según tus necesidades específicas.



### Modelo de etiquetas para páginas de blog

Se ha añadido el modelo `BlogPageTag` que hereda de `TaggedItemBase`. Este modelo se utiliza para establecer una relación entre las etiquetas y las páginas de blog. Contiene un campo `content_object` que representa la clave externa a la página de blog relacionada.

### Modelo de página de blog

El modelo `BlogPage` ha sido modificado para incluir las siguientes adiciones y cambios:

- `tags`: Campo de tipo `ClusterTaggableManager` que permite agregar etiquetas a la página de blog.
- `categories`: Campo de tipo `ParentalManyToManyField` que permite agregar categorías a la página de blog.

Además, se han realizado cambios en la propiedad `content_panels` para reflejar los nuevos campos y relaciones.

### Modelo de página de índice de blog

El modelo `BlogIndexPage` ha sido modificado para incluir la propiedad `subpage_types`, que especifica los tipos de páginas secundarias permitidas en la página de índice.

### Modelo de imagen de galería para páginas de blog

Se ha añadido el modelo `BlogPageGalleryImage` que hereda de `Orderable`. Este modelo se utiliza para agregar imágenes de galería a las páginas de blog. Contiene los campos `image` para almacenar la imagen y `caption` para almacenar la descripción de la imagen.

## Página de índice de etiquetas de blog

Se ha añadido el modelo `BlogTagIndexPage`, que representa una página de índice de etiquetas de blog. Este modelo tiene el método `get_context` para filtrar las páginas de blog por etiqueta y pasarlas al contexto de la plantilla.

## Modelo de categoría de blog

Se ha añadido el modelo `BlogCategory` que representa una categoría de blog. Este modelo contiene los campos `name` para almacenar el nombre de la categoría y `icon` para almacenar la imagen de icono asociada a la categoría.

## Registro de fragmentos

El modelo `BlogCategory` se ha registrado como un fragmento utilizando el decorador `register_snippet`. Esto permite gestionar las categorías de blog como fragmentos reutilizables en el sistema de administración de Wagtail.

# Proyecto en Wagtail - Documentación

A continuación, se presenta la documentación de un proyecto en Wagtail. El proyecto consta de modelos de Django y utiliza la plataforma de administración de contenido Wagtail para crear y gestionar páginas relacionadas con un equipo de fútbol.

## Modelos de Django

### Equipo

El modelo `Equipo` representa un equipo de fútbol. Tiene los siguientes campos:

- `nombre`: campo de texto para el nombre del equipo.
- `imagen`: campo de imagen para subir una imagen del equipo.
- `contenido`: campo de texto enriquecido opcional para proporcionar información adicional sobre el equipo.
- `subpage_types`: lista de tipos de página secundarias permitidas (en este caso, `jugador` y `entrenador`).
- `template`: plantilla HTML utilizada para renderizar la página del equipo.
- `content_panels`: paneles de contenido para el administrador de Wagtail.

### Equipo_index

El modelo `Equipo_index` representa una página índice para mostrar una lista de equipos. Tiene los siguientes campos:

- `subpage_types`: lista de tipos de página secundarias permitidas (solo `Equipo` en este caso).
- `template`: plantilla HTML utilizada para renderizar la página índice del equipo.
- `save`: método personalizado para guardar la página y guardar también los equipos secundarios.

### Jugador

El modelo `Jugador` representa un jugador del equipo de fútbol. Tiene los siguientes campos:

- `nombre`: campo de texto para el nombre del jugador.
- `apellido`: campo de texto para el apellido del jugador.
- `numero`: campo numérico para el número del jugador.
- `edad`: campo numérico para la edad del jugador (con un valor predeterminado de 18).
- `sexo`: campo de selección para el género del jugador.
- `imagen`: campo de imagen para subir una imagen del jugador.
- `parent_page_types`: lista de tipos de página primarias permitidas (solo `Equipo` en este caso).
- `subpage_types`: lista de tipos de página secundarias permitidas (ninguno en este caso).
- `template`: plantilla HTML utilizada para renderizar la página del jugador.
- `content_panels`: paneles de contenido para el administrador de Wagtail.
- `save`: método personalizado para guardar la página y realizar cálculos adicionales (por ejemplo, incrementar el número del jugador).

### Jugador_index_page

El modelo `Jugador_index_page` representa una página índice para mostrar una lista de jugadores. Tiene los siguientes campos:

- `subpage_types`: lista de tipos de página secundarias permitidas (solo `jugador` en este caso).
- `template`: plantilla HTML utilizada para renderizar la página índice del jugador.

### Entrenador

El modelo `Entrenador` representa un entrenador del equipo de fútbol. Tiene los siguientes campos:

- `nombre`: campo de texto para el nombre del entrenador.
- `apellido`: campo de texto para el apellido del entrenador.
- `imagen`: campo de imagen para subir una imagen del entrenador.
- `contenido`: campo de texto enriquecido opcional para proporcionar información adicional sobre el entrenador.
- `parent_page_types`: lista de tipos de página primarias permitidas (solo `Equipo` en este caso).
- `subpage_types`: lista de tipos de página secundarias permitidas (ninguno en

 este caso).
- `template`: plantilla HTML utilizada para renderizar la página del entrenador.
- `content_panels`: paneles de contenido para el administrador de Wagtail.

### Entrenador_index_page

El modelo `Entrenador_index_page` representa una página índice para mostrar una lista de entrenadores. Tiene los siguientes campos:

- `subpage_types`: lista de tipos de página secundarias permitidas (solo `entrenador` en este caso).
- `template`: plantilla HTML utilizada para renderizar la página índice del entrenador.

### Liga_Partidos_Page

El modelo `Liga_Partidos_Page` representa una página de partidos de la liga. Tiene los siguientes campos:

- `equipo_local`: campo de clave externa para el equipo local (seleccionado entre los equipos existentes).
- `equipo_visitante`: campo de clave externa para el equipo visitante (seleccionado entre los equipos existentes).
- `fecha`: campo de fecha para la fecha del partido.
- `goles_local`: campo numérico para los goles marcados por el equipo local.
- `goles_visitante`: campo numérico para los goles marcados por el equipo visitante.
- `parent_page_types`: lista de tipos de página primarias permitidas (solo `Liga_Clasificacion_Page` en este caso).
- `subpage_types`: lista de tipos de página secundarias permitidas (ninguno en este caso).
- `template`: plantilla HTML utilizada para renderizar la página de partidos de la liga.
- `content_panels`: paneles de contenido para el administrador de Wagtail.
- `save`: método personalizado para guardar la página y realizar cálculos adicionales (por ejemplo, determinar el resultado del partido y actualizar las estadísticas de los equipos).

### Liga_Clasificacion_Page

El modelo `Liga_Clasificacion_Page` representa una página de clasificación de la liga. Tiene los siguientes campos:

- `nombre`: campo de texto para el nombre de la clasificación.
- `imagen`: campo de imagen para subir una imagen de la clasificación.
- `contenido`: campo de texto enriquecido opcional para proporcionar información adicional sobre la clasificación.
- `equipos`: campo de muchos a muchos para asociar equipos a la clasificación.
- `puntos`: campo numérico para los puntos de la clasificación.
- `partidos_jugados`: campo numérico para los partidos jugados de la clasificación.
- `partidos_ganados`: campo numérico para los partidos ganados de la clasificación.
- `partidos_empatados`: campo numérico para los partidos empatados de la clasificación.
- `partidos_perdidos`: campo numérico para los partidos perdidos de la clasificación.
- `goles_favor`: campo numérico para los goles a favor de la clasificación.
- `goles_contra`: campo numérico para los goles en contra de la clasificación.
- `subpage_types`: lista de tipos de página secundarias permitidas (solo `Equipo` en este caso).
- `template`: plantilla HTML utilizada para renderizar la página de clasificación de la liga.
- `content_panels`: paneles de contenido para el administrador de Wagtail.
- `save`: método personalizado para guardar la página y realizar cálculos adicionales (por ejemplo, actualizar las estadísticas de los equipos basándose en los partidos).

### Liga_Index_Page

El modelo

 `Liga_Index_Page` representa una página índice para la liga. Tiene los siguientes campos:

- `subpage_types`: lista de tipos de página secundarias permitidas (solo `Liga_Clasificacion_Page` en este caso).
- `template`: plantilla HTML utilizada para renderizar la página índice de la liga.

### Partido

El modelo `Partido` representa un partido entre dos equipos. Tiene los siguientes campos:

- `equipo_local`: campo de clave externa para el equipo local (seleccionado entre los equipos existentes).
- `equipo_visitante`: campo de clave externa para el equipo visitante (seleccionado entre los equipos existentes).
- `fecha`: campo de fecha para la fecha del partido.
- `goles_local`: campo numérico para los goles marcados por el equipo local.
- `goles_visitante`: campo numérico para los goles marcados por el equipo visitante.
- `parent_page_types`: lista de tipos de página primarias permitidas (solo `Equipo` en este caso).
- `subpage_types`: lista de tipos de página secundarias permitidas (ninguno en este caso).
- `template`: plantilla HTML utilizada para renderizar la página del partido.
- `content_panels`: paneles de contenido para el administrador de Wagtail.
- `save`: método personalizado para guardar la página y realizar cálculos adicionales (por ejemplo, determinar el resultado del partido).

