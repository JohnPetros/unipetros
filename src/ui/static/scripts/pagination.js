class Pagination {
  constructor() {
    const pageButtons = document.querySelectorAll(
      '[data-pagination="page-button"]',
    )

    const input = document.querySelector('[data-pagination="input"]')

    if (!pageButtons.length) return

    this.pageButtons = pageButtons
    this.queryParam = new QueryParam()

    const currentPage = this.queryParam.get("page")

    this.activePageButton(currentPage ?? "1")

    for (const pageButton of pageButtons) {
      pageButton.addEventListener("click", (event) =>
        this.handlePageButtonClick(event),
      )
    }

    if (input) this.input = input
  }

  activePageButton(pageNumber) {
    const activePageButton = Array.from(this.pageButtons).find(
      (pageButton) => pageButton.value === pageNumber,
    )

    for (const pageButton of this.pageButtons) {
      if (pageButton.value === pageNumber) {
        pageButton.classList.add("bg-blue-700", "text-white")
      } else {
        pageButton.classList.remove("bg-blue-700", "text-white")
      }
    }
  }

  handlePageButtonClick(event) {
    const pageNumber = event.currentTarget.value
    this.queryParam.append("page", pageNumber)

    if (this.input) {
      this.input.value = pageNumber
      this.activePageButton(pageNumber)
      htmx.trigger(`#${this.input.id}`, "change")
    }
  }
}

window.addEventListener("load", () => new Pagination())
