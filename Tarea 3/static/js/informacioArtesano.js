let botonVolver = document.getElementById("botonVolver");
botonVolver.addEventListener("click", function () { window.location.href = "../ver-artesanos/ver-artesanos.html" });

let imagen1 = document.getElementById("imagen1");
let imagen2 = document.getElementById("imagen2");

const agrandarImagen = (imagen) => {
    imagen.height = 1280;
    imagen.width = 1024;
}

imagen1.addEventListener("click", () => agrandarImagen(imagen1));
imagen2.addEventListener("click", () => agrandarImagen(imagen2));

