window.addEventListener('load', () => {
  function getChartOptions(maleStudentsCount, femaleStudentsCount) {
    return {
      series: [maleStudentsCount, femaleStudentsCount],
      colors: ['#16BDCA', '#9061F9'],
      chart: {
        height: 320,
        width: '100%',
        type: 'pie',
      },
      stroke: {
        colors: ['white'],
        lineCap: '',
      },
      plotOptions: {
        pie: {
          labels: {
            show: true,
          },
          size: '100%',
          dataLabels: {
            offset: -25,
          },
        },
      },
      labels: ['Masculino', 'Feminino'],
      dataLabels: {
        enabled: true,
        style: {
          fontFamily: 'Poppins, sans-serif',
        },
      },
      legend: {
        position: 'bottom',
        fontFamily: 'Poppins, sans-serif',
        fontWeight: 600,
        fontSize: 14,
      },
      xaxis: {
        axisTicks: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
      },
    }
  }

  const container = document.querySelector(
    '[data-students-by-gender-chart="container"]',
  )
  const maleStudentsCount = document.querySelector(
    '[data-students-by-gender-chart="male-students-count"]',
  )
  const femaleStudentsCount = document.querySelector(
    '[data-students-by-gender-chart="female-students-count"]',
  )

  if (container && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(
      container,
      getChartOptions(
        Number(maleStudentsCount.value),
        Number(femaleStudentsCount.value),
      ),
    )
    chart.render()
  }
})
