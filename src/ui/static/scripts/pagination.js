class Pagination {
  constructor() {
    const pageButtons = document.querySelectorAll(
      '[data-pagination="page-button"]',
    )

    const input = document.querySelector('[data-pagination="input"]')

    if (pageButtons.length) {
      for (const pageButton of pageButtons) {
        pageButton.addEventListener('click', (event) =>
          this.handlePageButtonClick(event),
        )
        this.queryParam = new QueryParam()
      }
    }

    if (input) this.input = input
  }

  handlePageButtonClick(event) {
    const pageNumber = event.currentTarget.value
    this.queryParam.append('page', pageNumber)

    if (this.input) {
      this.input.value = pageNumber
      htmx.trigger(`#${this.input.id}`, 'change')
    }
  }
}

window.addEventListener('load', () => new Pagination())
