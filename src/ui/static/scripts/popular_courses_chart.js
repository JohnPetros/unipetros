window.addEventListener('load', () => {
  function getChartOptions(coursesNames, studentsCounts) {
    const colors = ['#7D84B2', '#57C4E5', '#D9DBF1', '#B4CEB3']
    const series = []

    for (let i = 0; i < colors.length; i++) {
      series.push({
        name: coursesNames[i],
        data: [studentsCounts[i]],
        color: colors[i],
      })
    }

    return {
      series: series,
      chart: {
        type: 'bar',
        width: '100%',
        height: 180,
        sparkline: {
          enabled: false,
        },
      },
      plotOptions: {
        bar: {
          borderRadius: 4,
          horizontal: true,
          barHeight: '100%',
          columnWidth: '100%',
        },
      },
      stroke: {
        colors: ['transparent'],
        width: 12,
      },
      dataLabels: {
        enabled: true,
        textAnchor: 'start',
        background: {
          enabled: true,
          foreColor: '#212738',
          borderRadius: 2,
          borderWidth: 1,
          opacity: 0.9,
          dropShadow: {
            enabled: false,
            top: 1,
            left: 1,
            blur: 1,
            color: '#212738',
            opacity: 0.45,
          },
        },
      },

      legend: {
        show: true,
        position: 'left',
        horizontalAlign: 'center',
        floating: false,
        fontSize: '12px',
        fontFamily: 'Poppins, Arial',
        fontWeight: 600,
        markers: {
          width: 12,
          height: 12,
          strokeWidth: 0,
          strokeColor: '#fff',
          fillColors: undefined,
          radius: 12,
          customHTML: undefined,
          onClick: undefined,
          offsetX: 0,
          offsetY: 2,
        },
        itemMargin: {
          horizontal: 0,
          vertical: 8,
        },
      },
      tooltip: {
        x: {
          show: false,
        },
        y: {
          title: {
            formatter: (seriesName) => seriesName,
          },
        },
      },
      xaxis: {
        show: false,
        labels: {
          show: false,
        },
      },
      yaxis: {
        show: false,
        showAlways: false,
        style: {
          cssClass: 'text-transparent',
        },
      },
      grid: {
        show: true,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
        },
      },
    }
  }

  const container = document.querySelector(
    '[data-popular-courses-chart="container"]',
  )
  const coursesNames = document.querySelector(
    '[data-popular-courses-chart="courses-names"]',
  )
  const studentsCounts = document.querySelector(
    '[data-popular-courses-chart="students-counts"]',
  )

  if (
    container &&
    coursesNames &&
    studentsCounts &&
    typeof ApexCharts !== 'undefined'
  ) {
    const chart = new ApexCharts(
      container,
      getChartOptions(
        coursesNames.value.split(';'),
        studentsCounts.value.split(';').map(Number),
      ),
    )
    chart.render()
  }
})
