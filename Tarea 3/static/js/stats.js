const graficoArtesanos = Highcharts.chart('graficoArtesano', {
    chart: {
        type: 'pie',
        backgroundColor: 'rgb(4, 112, 254)'
    },
    title: {
        text: 'Número de artesanos que trabajan cierto tipo de artesanía',
        style: {
            color: '#f2f2f2'
        }
    },
    series: [{
        name: 'Artesanos',
        colorByPoint: true,
        data: [],
        dataLabels: {
            style: {
                color: 'white',
                textOutline: '0.2px white',
                fontSize: '15px' 
            }
        }
    }],
});

const graficoHinchas = Highcharts.chart('graficoHincha', {
    chart: {
        type: 'pie',
        backgroundColor: 'rgb(4, 112, 254)'
    },
    title: {
        text: 'Número de hinchas que apoyan cierto deporte',
        style: {
            color: '#f2f2f2'
        }
    },
    series: [{
        name: 'Hinchas',
        colorByPoint: true,
        data: [],
        dataLabels: {
            style: {
                color: 'white',
                textOutline: '0.2px white',
                fontSize: '15px' 
            }
        }
    }],
});

fetch("http://127.0.0.1:5000/get_stats_data")
    .then((response) => response.json())
    .then((data) => {
        const datosArtesanos = Object.keys(data.artesanos)
            .map((tipo) => ({ name: tipo, y: data.artesanos[tipo] }))
            .filter(item => item.y > 0);

        const datosHinchas = Object.keys(data.hinchas)
            .map((deporte) => ({ name: deporte, y: data.hinchas[deporte] }))
            .filter(item => item.y > 0);

        graficoArtesanos.series[0].setData(datosArtesanos);

        graficoHinchas.series[0].setData(datosHinchas);
    })
    .catch((error) => console.error("Error:", error));

