const filas = document.querySelectorAll('tbody tr');
filas.forEach(fila => {
    fila.addEventListener('click', () => {
        const href = fila.getAttribute('data-href');
        if (href) {
            window.location.href = href;
        }
    });
});

botonVolver = document.getElementById("botonRedirigir");
botonVolver.addEventListener("click", function () { window.location.href = '../index/index.html' });

