window.addEventListener('load', () => {
  function getChartOptions(dates, count) {
    return {
      series: [
        {
          name: 'Alunos presentes',
          data: count,
          color: '#7E3BF2',
        },
      ],
      chart: {
        height: 220,
        maxWidth: '100%',
        type: 'area',
        fontFamily: 'Poppins, sans-serif',
        dropShadow: {
          enabled: false,
        },
        toolbar: {
          show: false,
        },
      },
      tooltip: {
        enabled: true,
        x: {
          show: false,
        },
      },
      legend: {
        show: false,
      },
      fill: {
        type: 'gradient',
        gradient: {
          opacityFrom: 0.55,
          opacityTo: 0,
          shade: '#1C64F2',
          gradientToColors: ['#1C64F2'],
        },
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        width: 6,
      },
      grid: {
        show: true,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
          top: 0,
        },
      },
      xaxis: {
        categories: dates,
        labels: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
        axisTicks: {
          show: false,
        },
        tooltip: {
          enabled: true,
          offsetY: 12,
          style: {
            fontSize: 12,
            fontFamily: 'Poppins, sans-serif',
          },
        },
      },
      yaxis: {
        show: false,
      },
    }
  }

  function splitData(data) {
    return data.split(';')
  }

  const container = document.querySelector(
    '[data-students-absents-chart="container"]',
  )

  const sevenDaysRangeDates = document.querySelector(
    '[data-students-absents-chart="7-days-range-dates"]',
  )
  const sevenDaysRangeCount = document.querySelector(
    '[data-students-absents-chart="7-days-range-count"]',
  )

  const thirtyDaysRangeDates = document.querySelector(
    '[data-students-absents-chart="30-days-range-dates"]',
  )
  const thirtyDaysRangeCount = document.querySelector(
    '[data-students-absents-chart="30-days-range-count"]',
  )

  const ninetyDaysRangeDates = document.querySelector(
    '[data-students-absents-chart="90-days-range-dates"]',
  )
  const ninetyDaysRangeCount = document.querySelector(
    '[data-students-absents-chart="90-days-range-count"]',
  )

  const select = document.querySelector('#students-absents-chart-select')

  if (container && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(
      container,
      getChartOptions(
        splitData(sevenDaysRangeDates.value),
        splitData(sevenDaysRangeCount.value).map(Number),
      ),
    )
    chart.render()

    if (select)
      select.addEventListener('change', (event) => {
        switch (event.currentTarget.value) {
          case '7 days':
            chart.updateOptions(
              getChartOptions(
                splitData(sevenDaysRangeDates.value),
                splitData(sevenDaysRangeCount.value).map(Number),
              ),
            )
            break
          case '30 days':
            chart.updateOptions(
              getChartOptions(
                splitData(thirtyDaysRangeDates.value),
                splitData(thirtyDaysRangeCount.value).map(Number),
              ),
            )
            break
          case '90 days':
            chart.updateOptions(
              getChartOptions(
                splitData(ninetyDaysRangeDates.value),
                splitData(ninetyDaysRangeCount.value).map(Number),
              ),
            )
            break
          default:
            chart.updateOptions(
              getChartOptions(
                splitData(sevenDaysRangeDates.value),
                splitData(sevenDaysRangeCount.value).map(Number),
              ),
            )
        }
      })
  }
})
