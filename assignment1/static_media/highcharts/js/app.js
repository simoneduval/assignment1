$(document).ready(function() {

    var options = {
        chart: {
            renderTo: 'ath_chart',
            type: 'spline'
        },
        series: [{}]
    };

    $.getJSON('data_best.json', function(data) {
        options.series[0].data = data;
        var chart = new Highcharts.Chart(options);
    });

});



        $(function () { 
    $('#ath_chart').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Competitive Bests'
        },
        xAxis: {
            categories: ['Vault', 'Uneven Bars', 'Balance Beam', 'Floor Exercise', 'All-Around']
        },
        yAxis: {
            title: {
                text: 'Performance'
            }
        },
        series: [{
            name: 'Jane',
            data: [1, 0, 4,5, 5, 10]
        } ]
    });
});
        
 /*       
        
        function writeChart1(){
	console.log("Inside writeChart()");
	chart = new Highcharts.Chart({
            chart: {
                
                margin: [ 50, 50, 100, 80]
            },
           title: {
                text: 'Competitive Bests'
            },
            xAxis: {
                 
            categories: ['Vault', 'Uneven Bars', 'Balance Beam', 'Floor Exercise', 'All-Around'],
            
                labels: {
                    rotation: -45,
                    align: 'right',
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Geneva, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Calories'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                formatter: function() {
                    return '<b>'+ this.x +'</b><br/>'+
                        'Healthy Dessert: '+ Highcharts.numberFormat(this.y, 1) +
                        ' calories';
                }
            },
            series: [{
                name: 'Calories',
                data: [calories[4], calories[5], calories[3], calories[6], calories[1], calories[9], calories[8], calories[2], calories[7], calories[0]],
                dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    x: 4,
                    y: 10,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Geneva, sans-serif'
                    }
                }
            }]
        });



}
*/