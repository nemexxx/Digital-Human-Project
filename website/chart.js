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

    // This script is shared by every page, but only the dashboard has all the
    // canvases — skip any chart whose canvas isn't on the current page.
    function renderDoughnut(canvasId, label, labels, data) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;

        new Chart(canvas.getContext('2d'), {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: data,
                    backgroundColor: palette
                }]
            },
            options: chartOptions
        });
    }

    renderDoughnut('instagramChart', 'Likes',
        ['account_a', 'account_b', 'account_c', 'account_d', 'account_e'],
        [160, 135, 130, 120, 110]);

    renderDoughnut('threadsChart', 'Likes',
        ['account_a', 'account_b', 'account_c', 'account_d', 'account_e'],
        [9, 5, 4, 4, 4]);

    renderDoughnut('chromeChart', 'Visits',
        ['example.com', 'site-b.com', 'site-c.com', 'site-d.com', 'site-e.com'],
        [5200, 1800, 750, 700, 600]);

    renderDoughnut('youtubeChart', 'Counts',
        ['Channel A', 'Channel B', 'Channel C', 'Channel D', 'Channel E'],
        [360, 320, 200, 90, 85]);
});