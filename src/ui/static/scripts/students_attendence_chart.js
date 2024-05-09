window.addEventListener('load', () => {
  const DATASET = 'data-students-absents-chart'

  function getChartOptions(dates, data) {
    return {
      series: [
        {
          name: 'Alunos presentes',
          data: data,
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

  function getChartData(days) {
    const dates = document.querySelector(
      `[${DATASET}="${days}-days-range-dates"]`,
    )
    const attendance = document.querySelector(
      `[${DATASET}="${days}-days-range-attendance"]`,
    )

    if (!dates || !attendance) return null

    return {
      dates: dates.value.split(';'),
      attendance: attendance.value.split(';').map(Number),
    }
  }

  function updateBalancePercentage(attendance, days) {
    const totalStudents = document.querySelector(
      `[${DATASET}="total-students"]`,
    ).value

    const balancePercentage = document.querySelector(
      `[${DATASET}="balance-percentage"]`,
    )

    if (!balancePercentage || !totalStudents) return

    const totalAttendence = attendance.reduce((total, currentAttendance) => {
      return total + currentAttendance
    })

    const percentage = (
      (totalAttendence / (Number(totalStudents) * days)) *
      100
    ).toFixed(2)

    balancePercentage.textContent = `${percentage}%`
  }

  const container = document.querySelector(`[${DATASET}="container"]`)

  const dataByDaysRange = {
    '7 days': getChartData(7),
    '30 days': getChartData(30),
    '90 days': getChartData(90),
  }

  const initialData = dataByDaysRange['7 days']

  if (container && initialData && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(
      container,
      getChartOptions(initialData.dates, initialData.attendance),
    )

    chart.render()

    updateBalancePercentage(initialData.attendance, 7)

    const select = document.querySelector('#students-absents-chart-select')

    if (select)
      select.addEventListener('change', (event) => {
        const data = dataByDaysRange[event.target.value]

        if (data) {
          chart.updateOptions(getChartOptions(data.dates, data.attendance))
          updateBalancePercentage(
            data.attendance,
            Number(event.target.value.split(' ')[0]),
          )
        }
      })
  }
})

window.addEventListener('load', () => {
  if (container && initialData && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(
      container,
      getChartOptions(initialData.dates, initialData.attendance),
    )

    chart.render()
  }
})
