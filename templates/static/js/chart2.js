var ctx = document.getElementById('doughnut').getContext('2d');
var media_valor = document.getElementById('media-valores').value
var total_em_estoque = document.getElementById('em-estoque').value
if (! media_valor) {
    media_valor = 1
    total_em_estoque = 1
}

var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Media dos valores de cada produto', 'Total de produtos em estoque'],

        datasets: [{
            label: 'Produtos',
            data: [media_valor, total_em_estoque],
            backgroundColor: [
                'rgba(83, 53, 249, 1)',
                'rgba(176, 115, 236, 1)',
    

            ],
            borderColor: [
                'rgba(83, 53, 249, 1)',
                'rgba(176, 115, 236, 1)',


            ],
            borderWidth: 1
        }]

    },
    options: {
        responsive: true
    }
});