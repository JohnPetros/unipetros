window.addEventListener('load', () => {
  function calculatePercentage(count, totalCount) {
    return (count / totalCount) * 100
  }

  function capitalizeFirstLetter(text) {
    return text.charAt(0).toUpperCase() + text.substring(1)
  }

  function getChartOptions(categories, postsCounts, totalCount) {
    return {
      series: postsCounts.map((postCount) =>
        calculatePercentage(postCount, totalCount),
      ),
      colors: ['#1C64F2', '#16BDCA', '#FDBA8C'],
      chart: {
        height: '380px',
        width: '100%',
        type: 'radialBar',
        sparkline: {
          enabled: true,
        },
      },
      plotOptions: {
        radialBar: {
          track: {
            background: '#E5E7EB',
          },
          dataLabels: {
            show: true,
            name: {
              show: true,
              fontSize: '16px',
              fontFamily: 'Poppins, sans-serif',
              fontWeight: 600,
              offsetY: 0,
            },
            value: {
              show: true,
              fontSize: '16px',
              fontFamily: undefined,
              fontWeight: 600,
              color: '#6B7D7D',
              offsetY: 8,
            },
            total: {
              show: true,
              label: 'Total',
              fontSize: 20,
              fontFamily: 'Poppins, sans-serif',
              color: '#32908F',
              formatter: () => totalCount,
            },
          },
          hollow: {
            margin: 12,
            size: '32%',
          },
        },
      },
      grid: {
        show: true,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
          top: -23,
          bottom: -20,
        },
      },
      labels: categories.map(capitalizeFirstLetter),
      legend: {
        show: true,
        position: 'bottom',
        fontFamily: 'Poppins, sans-serif',
        fontSize: '14px',
        fontWeight: 600,
      },
      stroke: {
        show: true,
        curve: 'smooth',
        lineCap: 'round',
        colors: undefined,
        width: 2,
        dashArray: 0,
      },
      tooltip: {
        enabled: false,
        x: {
          show: false,
        },
      },
      yaxis: {
        show: false,
      },
    }
  }

  const container = document.querySelector(
    '[data-post-by-category-chart="container"]',
  )
  const categories = document.querySelector(
    '[data-post-by-category-chart="categories"]',
  )
  const postsCounts = document.querySelector(
    '[data-post-by-category-chart="posts-counts"]',
  )
  const totalCount = document.querySelector(
    '[data-post-by-category-chart="total-count"]',
  )

  if (container && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(
      container,
      getChartOptions(
        categories.value.split(';'),
        postsCounts.value.split(';').map(Number),
        Number(totalCount.value),
      ),
    )
    chart.render()
  }
})
