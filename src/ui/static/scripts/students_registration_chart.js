window.addEventListener('load', () => {
  const DATASET = 'data-students-registration-chart'
  const ENROLLMENT_COLOR = '#31C48D'
  const DISMISSAL_COLOR = '#F05252'

  function getChartOptions(dates, enrollmentsData, dismissalsData) {
    const enrollments = dates.map((date, index) => ({
      x: date,
      y: enrollmentsData[index],
    }))
    const dismissals = dates.map((date, index) => ({
      x: date,
      y: dismissalsData[index],
    }))

    return {
      colors: [ENROLLMENT_COLOR, DISMISSAL_COLOR],
      series: [
        {
          name: 'Matrículas efetuadas',
          color: '#31C48D',
          data: enrollments,
        },
        {
          name: 'Matrículas desativadas',
          color: DISMISSAL_COLOR,
          data: dismissals,
        },
      ],
      chart: {
        type: 'bar',
        height: '320px',
        fontFamily: 'Poppins, sans-serif',
        toolbar: {
          show: false,
        },
      },
      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: '70%',
          borderRadiusApplication: 'end',
          borderRadius: 8,
        },
      },
      tooltip: {
        shared: true,
        intersect: false,
        style: {
          fontFamily: 'Poppins, sans-serif',
        },
      },
      states: {
        hover: {
          filter: {
            type: 'darken',
            value: 1,
          },
        },
      },
      stroke: {
        show: true,
        width: 0,
        colors: ['transparent'],
      },
      grid: {
        show: false,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
          top: -14,
        },
      },
      dataLabels: {
        enabled: false,
      },
      legend: {
        show: false,
      },
      xaxis: {
        show: false,
        labels: {
          show: false,
        },
      },
      yaxis: {
        show: false,
      },
      fill: {
        opacity: 1,
      },
    }
  }

  function getChartData(days) {
    const dates = document.querySelector(
      `[${DATASET}="${days}-days-range-dates"]`,
    )
    const enrollmentsCount = document.querySelector(
      `[${DATASET}="${days}-days-range-enrollments-count"]`,
    )
    const dismissalsCount = document.querySelector(
      `[${DATASET}="${days}-days-range-dismissals-count"]`,
    )

    if (!dates || !enrollmentsCount || !dismissalsCount) return null

    return {
      dates: dates.value.split(';'),
      enrollmentsCount: enrollmentsCount.value.split(';').map(Number),
      dismissalsCount: dismissalsCount.value.split(';').map(Number),
    }
  }

  function calculateTotalCount(data) {
    return data.reduce((total, currentCount) => {
      return total + currentCount
    })
  }

  function updateTotalCount(data) {
    const totalEnrollmentsCount = document.querySelector(
      `[${DATASET}="total-enrollments-count"]`,
    )
    const totalDismissalsCount = document.querySelector(
      `[${DATASET}="total-dismissals-count"]`,
    )

    totalEnrollmentsCount.textContent = calculateTotalCount(
      data.enrollmentsCount,
    )
    totalDismissalsCount.textContent = calculateTotalCount(data.dismissalsCount)
  }

  function calculateBalancePercentage(data) {
    const enrollmentsCount = calculateTotalCount(data.enrollmentsCount)
    const dismissalsCount = calculateTotalCount(data.dismissalsCount)

    const total = enrollmentsCount + dismissalsCount
    return (enrollmentsCount / total) * 100
  }

  function updateBalancePercentage(data) {
    const balancePercentage = document.querySelector(
      `[${DATASET}="balance-percentage"]`,
    )

    if (!balancePercentage) return

    const percentage = calculateBalancePercentage(data)

    balancePercentage.textContent = `${percentage}%`
  }

  const container = document.querySelector(`[${DATASET}="container"]`)

  const rangeDaysData = {
    '7 days': getChartData(7),
    '30 days': getChartData(30),
    '90 days': getChartData(90),
  }

  const data = rangeDaysData['7 days']

  if (container && data && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(
      container,
      getChartOptions(data.dates, data.enrollmentsCount, data.dismissalsCount),
    )

    chart.render()

    updateTotalCount(data)
    updateBalancePercentage(data)

    const select = document.querySelector('#students-registration-select')

    if (select)
      select.addEventListener('change', (event) => {
        const data = rangeDaysData[event.currentTarget.value]

        if (data) {
          chart.updateOptions(
            getChartOptions(
              data.dates,
              data.enrollmentsCount,
              data.dismissalsCount,
            ),
          )

          updateTotalCount(data)
        }
      })
  }
})
