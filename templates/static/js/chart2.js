var ctx = document.getElementById('doughnut').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Produtos adicionados', 'Produtos deletados'],

        datasets: [{
            label: 'Produtos',
            data: [1, 1],
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