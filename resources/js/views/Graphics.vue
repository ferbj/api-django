<template>
  <div class="container">
    <h3 class="text-center">Reporte Mundial</h3>
    <canvas id="chart"></canvas>
  </div>
</template>
<script>
import axios from "axios";
import Chart from "chart.js";
export default {
  name: "LineChartContainer",

  data() {
    return {
      chartdata: {},
      qt2018: {},
      qt2017: {}
    };
  },

  mounted() {
    this.renderChart(this.datasets, this.options);
  },
  methods: {
    renderChart(data, options) {
      const chart = document.getElementById("chart");
      let self = this;
      const url = `http://localhost:8000/api/v1.0/countries/`;
      axios
        .get(url)
        .then(response => {
          if (response.data.length != 0) {
            let countries = response.data;
            self.$data.chartdata = countries;
            let qt2018 = [];
            let lb2018 = [];
            let qt2017 = [];
            let lb2017 = [];
            let f2018 = countries.filter(country => {
              return country.date == "2018";
            });
            let f2017 = countries.filter(country => {
              return country.date == "2017";
            });
            f2017.map(function(res2017) {
              lb2017.push(res2017.name);
              qt2017.push(res2017.quantity);
              self.$data.lb2017 = lb2017;
              self.$data.qt2017 = qt2017;
            });
            f2018.map(function(res2018) {
              lb2018.push(res2018.name);
              qt2018.push(res2018.quantity);
              self.$data.lb2018 = lb2018;
              self.$data.qt2018 = qt2018;
            });

            //console.log(self.chartdata)
            function qua17() {
              return qt2017.map(function(quantity) {
                return quantity;
              });
            }
            function qua18() {
              return qt2018.map(function(quantity) {
                return quantity;
              });
            }

            new Chart(chart, {
              type: "bar",
              data: {
                labels: self.$data.lb2017,
                datasets: [
                  {
                    label: "2017",
                    backgroundColor: "blue",
                    data: qua17()
                  },
                  {
                    label: "2018",
                    backgroundColor: "green",
                    data: qua18()
                  }
                ]
              },
              options: {
                responsive: true,
                title: {
                  display: true,
                  text: "Poblacion mundial"
                },

                scales: {
                  xAxes: [
                    {
                      display: true,
                      scaleLabel: {
                        display: true,
                        labelString: "Continentes"
                      }
                    }
                  ],
                  yAxes: [
                    {
                      display: true,
                      scaleLabel: {
                        display: true,
                        labelString: "Poblacion"
                      },
                      ticks: {
                        beginAtZero: false,
                        padding: 25
                      }
                    }
                  ]
                }
              }
            });
          } else {
            let chart = document.getElementById("chart");
            let ctx = chart.getContext("2d");
            ctx.font = "28px Arial";
            ctx.fillStyle = "red";
            ctx.textAlign = "center";
            ctx.fillText("No hay datos", chart.width / 2, chart.height / 2);
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
