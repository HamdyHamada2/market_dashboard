/** 
 * tradingview_clone/static/src/js/charting.js 
 */

odoo.define('tradingview_clone.charting', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.TradingChart = publicWidget.Widget.extend({
        selector: '.trading-chart-container',
        start: function () {
            const container = this.el;
            const chartDataRaw = container.dataset.chart;

            if (!chartDataRaw) {
                console.error("No OHLC data found in data-chart attribute.");
                return;
            }

            let chartData;
            try {
                chartData = JSON.parse(chartDataRaw);
            } catch (err) {
                console.error("Failed to parse OHLC chart data:", err);
                return;
            }

            const chart = LightweightCharts.createChart(container, {
                width: container.clientWidth,
                height: 500,
                layout: {
                    backgroundColor: '#ffffff',
                    textColor: '#222222',
                },
                grid: {
                    vertLines: {
                        color: '#eee',
                    },
                    horzLines: {
                        color: '#eee',
                    },
                },
                priceScale: {
                    position: 'right',
                },
                timeScale: {
                    timeVisible: true,
                    secondsVisible: false,
                },
            });

            const candleSeries = chart.addCandlestickSeries({
                upColor: '#26a69a',
                downColor: '#ef5350',
                borderVisible: false,
                wickUpColor: '#26a69a',
                wickDownColor: '#ef5350',
            });

            candleSeries.setData(chartData);
        },
    });

    return publicWidget.registry.TradingChart;
});
