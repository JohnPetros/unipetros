window.addEventListener('load', () => {
  function getChartOptions(professors_count) {
    return {
      series: professors_count,
      colors: ['#16BDCA', '#9061F9'],
      chart: {
        height: 320,
        width: '100%',
        type: 'donut',
      },
      stroke: {
        colors: ['transparent'],
        lineCap: '',
      },
      plotOptions: {
        pie: {
          donut: {
            labels: {
              show: true,
              name: {
                show: true,
                fontFamily: 'Poppins, sans-serif',
                offsetY: 20,
              },
              total: {
                showAlways: true,
                show: true,
                label: 'Total de professores',
                fontFamily: 'Poppins, sans-serif',
                formatter: (chart) => {
                  const sum = chart.globals.seriesTotals.reduce((a, b) => {
                    return a + b
                  }, 0)
                  return sum
                },
              },
              value: {
                show: true,
                fontFamily: 'Poppins, sans-serif',
                offsetY: -20,
              },
            },
            size: '80%',
          },
        },
      },
      grid: {
        padding: {
          top: -2,
        },
      },
      labels: ['Homens', 'Mulheres'],
      dataLabels: {
        enabled: false,
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
    '[data-professors-by-gender-and-subject-chart="container"]',
  )

  const checkboxes = document.querySelectorAll(
    '[data-professors-by-gender-and-subject-chart="checkbox"]',
  )

  if (container && checkboxes.length && typeof ApexCharts !== 'undefined') {
    const first_checkbox = checkboxes[0]

    const chart = new ApexCharts(container, getChartOptions([50, 50]))

    chart.render()

    function updateProfessorsCountBySubjectId() {
      let maleProfessorsCount = 0
      let femaleProfessorsCount = 0

      for (const checkbox of checkboxes) {
        if (checkbox.checked) {
          const professors_count = document.querySelector(
            `#${checkbox.value}[data-professors-by-gender-and-subject-chart="professor-count"]`,
          )

          if (professors_count) {
            const checkboxValues = professors_count.value.split(';').map(Number)
            maleProfessorsCount += checkboxValues[0]
            femaleProfessorsCount += checkboxValues[1]
          }
        }
      }

      chart.updateSeries([maleProfessorsCount, femaleProfessorsCount])
    }

    updateProfessorsCountBySubjectId(first_checkbox.value)

    function handleCheckboxChange(event) {
      const subject = event.target

      if (!subject) return

      updateProfessorsCountBySubjectId(subject.value)
    }

    for (const checkbox of checkboxes) {
      checkbox.addEventListener('change', handleCheckboxChange)
    }
  }
})
