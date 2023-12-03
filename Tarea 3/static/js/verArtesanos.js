const tbody = document.querySelector('tbody');

tbody.addEventListener('click', (event) => {
    let target = event.target;
    while (target !== tbody && target.nodeName !== 'TR') {
        target = target.parentNode;
    }

    if (target.nodeName === 'TR') {
        const href = target.getAttribute('data-href');
        if (href) {
            window.location.href = href;
        }
    }
});

botonVolver = document.getElementById("botonRedirigir");
botonVolver.addEventListener("click", function () { window.location.href = '../index/index.html' });

 