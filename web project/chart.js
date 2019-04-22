Highcharts.chart('container', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Number of Users over the years'
    },
    xAxis: {
        categories: ['2009', '2010', '2011', '2012', '2013','2014'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Quantity(Rounded off)',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: 'Discord'
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 80,
        floating: true,
        borderWidth: 1,
        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
        shadow: true
    },
    credits: {
        enabled: false
    },
    series: [ {
        name: 'Discord',
        data: [4343,6544, 1538, 2745, 5434,8458]
    }]
});

