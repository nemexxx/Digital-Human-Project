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

    // NOTE: The values below are placeholder sample data so the charts render
    // out of the box. Regenerate them from your own export to see real results.
    const palette = ['#6A0DAD', '#4A90E2', '#007BFF', '#0056b3', '#0012A8'];

    // Instagram Likes Chart
    const instagramCtx = document.getElementById('instagramChart').getContext('2d');
    new Chart(instagramCtx, {
        type: 'doughnut',
        data: {
            labels: ['account_a', 'account_b', 'account_c', 'account_d', 'account_e'],
            datasets: [{
                label: 'Likes',
                data: [160, 135, 130, 120, 110],
                backgroundColor: palette
            }]
        },
        options: chartOptions
    });

    // Threads Likes Chart
    const threadsCtx = document.getElementById('threadsChart').getContext('2d');
    new Chart(threadsCtx, {
        type: 'doughnut',
        data: {
            labels: ['account_a', 'account_b', 'account_c', 'account_d', 'account_e'],
            datasets: [{
                label: 'Likes',
                data: [9, 5, 4, 4, 4],
                backgroundColor: palette
            }]
        },
        options: chartOptions
    });

    // Chrome Visits Chart
    const chromeCtx = document.getElementById('chromeChart').getContext('2d');
    new Chart(chromeCtx, {
        type: 'doughnut',
        data: {
            labels: ['example.com', 'site-b.com', 'site-c.com', 'site-d.com', 'site-e.com'],
            datasets: [{
                label: 'Visits',
                data: [5200, 1800, 750, 700, 600],
                backgroundColor: palette
            }]
        },
        options: chartOptions
    });

    // YouTube Watched Channels Chart
    const youtubeCtx = document.getElementById('youtubeChart').getContext('2d');
    new Chart(youtubeCtx, {
        type: 'doughnut',
        data: {
            labels: ['Channel A', 'Channel B', 'Channel C', 'Channel D', 'Channel E'],
            datasets: [{
                label: 'Counts',
                data: [360, 320, 200, 90, 85],
                backgroundColor: palette
            }]
        },
        options: chartOptions
    });
});