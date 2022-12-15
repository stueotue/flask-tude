var graph_name = location.pathname.split("/")[3]

const title_text = {
    "speed": [  
                "Kecepatan Harian (KNOT/JAM)",
                "Kecepatan Mingguan (KNOT/JAM)",
                "Kecepatan Bulanan (KNOT/JAM)",
                "Kecepatan Tahunan (KNOT/JAM)"
            ],

    "distance": [
                    "Jarak Tempuh Harian (MILE)",
                    "Jarak Tempuh Mingguan (MILE)",
                    "Jarak Tempuh Bulanan (MILE)",
                    "Jarak Tempuh Tahunan (MILE)"
                ],

    "time": [
                "Waktu Berlayar Harian (DALAM MENIT)",
                "Waktu Berlayar Mingguan (DALAM MENIT)",
                "Waktu Berlayar Bulanan (DALAM MENIT)",
                "Waktu Berlayar Tahunan (DALAM MENIT)"
            ],

    "anchor": [
                "Waktu Jangkar Harian (DALAM MENIT)",
                "Waktu Jangkar Mingguan (DALAM MENIT)",
                "Waktu Jangkar Bulanan (DALAM MENIT)",
                "Waktu Jangkar Tahunan (DALAM MENIT)"
            ],
    "analyze": [
                "Kecepatan Harian (KNOT/JAM)",
                "Kecepatan Mingguan (KNOT/JAM)",
                "Kecepatan Bulanan (KNOT/JAM)",
                "Kecepatan Tahunan (KNOT/JAM)"
            ],
}

function setConfig(num) {

    var yValues = [14,44,36,50,55,47,63,76,87,93,123,144];
    var xValues = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"];
    return {
        type: "line",
        data: {
          labels: xValues,
          datasets: [{
            fill: false,
            lineTension: 0,
            backgroundColor: "blue",
            borderColor: "rgba(0,0,255,0.5)",
            data: yValues
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
              title: {
                  display: true,
                  text: title_text[graph_name][parseInt(num)]
              },
              legend: {
                  display: false
              }
          }
        }
      }
}

let harian = document.getElementById("harian").getContext("2d");
let mingguan = document.getElementById("mingguan").getContext("2d");

let bulanan = document.getElementById("bulanan").getContext("2d");
let tahunan = document.getElementById("tahunan").getContext("2d");

var line_harian = new Chart(harian, setConfig(0));
var line_mingguan = new Chart(mingguan, setConfig(1));
var line_bulanan = new Chart(bulanan, setConfig(2));
var line_tahunan = new Chart(tahunan, setConfig(3));