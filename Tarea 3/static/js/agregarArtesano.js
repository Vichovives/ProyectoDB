//Menu de selección de tipo artesanía
let opcionesSeleccionadas = [];
function actualizarOpcionesSeleccionadas() {
    let checkboxes = [...document.querySelectorAll('#menuTipo input[type="checkbox"]:checked')];
    opcionesSeleccionadas = checkboxes.map(checkbox => checkbox.value);
}
document.getElementById('menuTipo').addEventListener('change', actualizarOpcionesSeleccionadas);

//Menú de selección de regiones y comunas
const regionesYComunas = {
    "regiones": [{
        "NombreRegion": "Arica y Parinacota",
        "comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
    },
    {
        "NombreRegion": "Tarapacá",
        "comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
    },
    {
        "NombreRegion": "Antofagasta",
        "comunas": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]
    },
    {
        "NombreRegion": "Atacama",
        "comunas": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]
    },
    {
        "NombreRegion": "Coquimbo",
        "comunas": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
    },
    {
        "NombreRegion": "Valparaíso",
        "comunas": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
    },
    {
        "NombreRegion": "Región del Libertador Gral. Bernardo O’Higgins",
        "comunas": ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
    },
    {
        "NombreRegion": "Región del Maule",
        "comunas": ["Talca", "ConsVtución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "ReVro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
    },
    {
        "NombreRegion": "Región del Biobío",
        "comunas": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío", "Chillán", "Bulnes", "Cobquecura", "Coelemu", "Coihueco", "Chillán Viejo", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"]
    },
    {
        "NombreRegion": "Región de la Araucanía",
        "comunas": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria",]
    },
    {
        "NombreRegion": "Región de Los Ríos",
        "comunas": ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
    },
    {
        "NombreRegion": "Región de Los Lagos",
        "comunas": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "FruVllar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
    },
    {
        "NombreRegion": "Región Aisén del Gral. Carlos Ibáñez del Campo",
        "comunas": ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
    },
    {
        "NombreRegion": "Región de Magallanes y de la AntárVca Chilena",
        "comunas": ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "AntárVca", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
    },
    {
        "NombreRegion": "Región Metropolitana de Santiago",
        "comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "TilVl", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
    }]
}

const menuRegiones = document.getElementById("regiones");
const menuComunas = document.getElementById("comunas");

const opcionPorDefecto = (dropdown) => {
    let porDefecto = document.createElement("option");
    porDefecto.textContent = "Elige una opción";
    porDefecto.value = "";
    porDefecto.disabled = true;
    porDefecto.selected = true;
    dropdown.appendChild(porDefecto);
}

const llenarRegiones = () => {
    opcionPorDefecto(menuRegiones);
    for (let region of regionesYComunas.regiones) {
        let opcion = document.createElement("option");
        opcion.value = region.NombreRegion;
        opcion.textContent = region.NombreRegion;
        menuRegiones.appendChild(opcion);
    }
}

const llenarComunas = () => {
    let regionSeleccionada = menuRegiones.value;
    menuComunas.innerHTML = "";
    opcionPorDefecto(menuComunas);
    let region = regionesYComunas.regiones.find(r => r.NombreRegion === regionSeleccionada);
    if (region) {
        for (let comuna of region.comunas) {
            let opcion = document.createElement("option");
            opcion.value = comuna;
            opcion.textContent = comuna;
            menuComunas.appendChild(opcion);
        }
    }
}
menuRegiones.addEventListener("change", llenarComunas);
llenarRegiones();
llenarComunas();

//Validador nombre.
const validadorNombre = (nombre) => {
    if (!nombre || nombre.length < 3 || nombre.length > 80) {
        return false;
    }
    return true;
}

//Validador correo.
const validadorCorreo = (correo) => {
    let patronCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!patronCorreo.test(correo)) {
        return false;
    }
    if (correo.length > 30) {
        return false;
    }
    return true;
}

//Validador número.
const validadorNumero = (numero) => {
    let patronNumero = /^\+(?:\d{1,3})?(?:\s*-\s*\d{1,})+$/;
    if (!numero || (numero.length > 15)) {
        if (!patronNumero.test(numero)) {
            return false;
        }
    }
    return true;
}

//Validador región
const validadorRegion = () => {
    let regiones = document.getElementById("regiones")
    if (regiones.value == "") {
        return false;
    }
    return true;
}

//Validador comuna 
const validadorComuna = () => {
    let comunas = document.getElementById("comunas");
    if (comunas.value == "") {
        return false;
    }
    return true;
}

//Validador tipos de artesanía
const validadorTipo = () => {
    if (opcionesSeleccionadas.length >= 1 && opcionesSeleccionadas.length <= 3) {
        return true;
    }
    return false;
}

//Validador fotos
const validadorFotos = (fotos) => {
    if (!fotos) {
        return false;
    }
    if (!(1 <= fotos.length && fotos.length <= 3)) {
        return false;
    }
    for (const foto of fotos) {
        let tipo = foto.type.split("/")[0];
        if (!(tipo == "image" || foto.type == "application/pdf")) {
            return false;
        }
    }
    return true;
}

//Validación y confirmación.
let formulario = document.forms["agregarArtesanoContenedorFoms"];
let botonEnviar = document.getElementById("botonEnviar");
let confirmacion = document.getElementById("confirmacion");
let botonConfirmar = document.getElementById("confirmarRegistro");
let botonCancelar = document.getElementById("cancelarRegistro");
let formEnviado = document.getElementById("formEnviado");
const validarFormulario = () => {
    let esValido = true;

    let nombre = formulario["nombre"].value;
    let validacionNombre = document.getElementById("errorNombre");
    if (!validadorNombre(nombre)) {
        esValido = false;
        validacionNombre.hidden = false;
    }
    else {
        validacionNombre.hidden = true;
    };

    let correo = formulario["correo"].value;
    let validacionCorreo = document.getElementById("errorCorreo");
    if (!validadorCorreo(correo)) {
        esValido = false;
        validacionCorreo.hidden = false;
    }
    else {
        validacionCorreo.hidden = true;
    };

    let numero = formulario["numero"].value;
    let validacionNumero = document.getElementById("errorNumero");
    if (!validadorNumero(numero)) {
        esValido = false;
        validacionNumero.hidden = false;
    }
    else {
        validacionNumero.hidden = true;
    };

    let validacionRegion = document.getElementById("errorRegion")
    if (!validadorRegion()) {
        esValido = false;
        validacionRegion.hidden = false;
    }
    else {
        validacionRegion.hidden = true;
    }

    let validacionComuna = document.getElementById("errorComuna")
    if (!validadorComuna()) {
        esValido = false;
        validacionComuna.hidden = false;
    }
    else {
        validacionComuna.hidden = true;
    }

    let validacionTipo = document.getElementById("errorTipo");
    if (!validadorTipo()) {
        esValido = false;
        validacionTipo.hidden = false;
    }
    else {
        validacionTipo.hidden = true;
    }

    let fotos = formulario["fotos"].files;
    let validacionFotos = document.getElementById("errorFotos")
    if (!validadorFotos(fotos)) {
        esValido = false;
        validacionFotos.hidden = false;
    }
    else {
        validacionFotos.hidden = true;
    }

    if (esValido) {
        formulario.style.display = "none";
        botonEnviar.style.display = "none";
        confirmacion.style.display = "block";
    };
};

const confirmarEnvio = () => {
    confirmacion.style.display = "none";
    formEnviado.style.display = "flex";
};

const cancelarEnvio = () => {
    formulario.style.display = "block";
    botonEnviar.style.display = "block";
    confirmacion.style.display = "none";
};

botonEnviar.addEventListener("click", validarFormulario);

botonConfirmar.addEventListener("click", confirmarEnvio);

botonCancelar.addEventListener("click", cancelarEnvio);

document.getElementById("confirmarRegistro").addEventListener("click", function() {
    document.getElementById("agregarArtesanoContenedorFoms").submit();
});
