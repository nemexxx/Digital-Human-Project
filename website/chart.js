document.addEventListener('DOMContentLoaded', function () {
    // Chart Optionen
    const chartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        let label = context.label || '';
                        if (label) label += ': ';
                        if (context.parsed !== null) label += context.parsed;
                        return label;
                    }
                }
            }
        }
    };

    // Instagram Likes Chart
    const instagramCtx = document.getElementById('instagramChart').getContext('2d');
    new Chart(instagramCtx, {
        type: 'doughnut',
        data: {
            labels: ['zdfheute', 'tagesschau', 'yvonnepferrer', 'louisaschneider.info', 'grad.jetzt'],
            datasets: [{
                label: 'Likes',
                data: [161, 135, 132, 129, 113],
                backgroundColor: ['#6A0DAD', '#4A90E2', '#007BFF', '#0056b3', '#0012A8']
            }]
        },
        options: chartOptions
    });

    // Threads Likes Chart
    const threadsCtx = document.getElementById('threadsChart').getContext('2d');
    new Chart(threadsCtx, {
        type: 'doughnut',
        data: {
            labels: ['piimglueck', 'sakarilacross', 'natalie', 'withcaesare', 'cristian'],
            datasets: [{
                label: 'Likes',
                data: [9, 5, 4, 4, 4],
                backgroundColor: ['#6A0DAD', '#4A90E2', '#007BFF', '#0056b3', '#0012A8']
            }]
        },
        options: chartOptions
    });

    // Chrome Visits Chart
    const chromeCtx = document.getElementById('chromeChart').getContext('2d');
    new Chart(chromeCtx, {
        type: 'doughnut',
        data: {
            labels: ['Google Docs', 'LinkedIn', 'Ecosia', 'Wix', 'Google'],
            datasets: [{
                label: 'Visits',
                data: [5261, 1781, 756, 729, 619],
                backgroundColor: ['#6A0DAD', '#4A90E2', '#007BFF', '#0056b3', '#0012A8']
            }]
        },
        options: chartOptions
    });

    // YouTube Watched Channels Chart
    const youtubeCtx = document.getElementById('youtubeChart').getContext('2d');
    new Chart(youtubeCtx, {
        type: 'doughnut',
        data: {
            labels: ['Paluten', 'Life of Riza', 'GermanLetsPlay', 'Mady Morrison', 'Mathe by Daniel Jung'],
            datasets: [{
                label: 'Counts',
                data: [358, 323, 202, 89, 88],
                backgroundColor: ['#6A0DAD', '#4A90E2', '#007BFF', '#0056b3', '#0012A8']
            }]
        },
        options: chartOptions
    });
});