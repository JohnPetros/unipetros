class Pagination {
  constructor() {
    const container = document.querySelector('[data-pagination="container"]')

    if (!container) return

    this.addEventListeners()

    const observer = new MutationObserver((mutations) => {
      if (mutations[0].type === "childList") {
        this.queryParam.updateHtmxUrl()
        this.addEventListeners()
      }
    })

    observer.observe(container, { childList: true })
  }

  addEventListeners() {
    const pageButtons = document.querySelectorAll(
      '[data-pagination="page-button"]',
    )
    const input = document.querySelector('[data-pagination="input"]')

    if (!pageButtons.length || !input) return

    this.pageButtons = pageButtons
    this.input = input
    this.queryParam = new QueryParam()

    let currentPage = this.queryParam.get("page")

    if (!currentPage || currentPage === "") {
      currentPage = "1"
    }

    console.log({ currentPage })

    this.activePageButton(currentPage)

    for (const pageButton of this.pageButtons) {
      pageButton.addEventListener("click", (event) =>
        this.handlePageButtonClick(event),
      )
    }
  }

  activePageButton(pageNumber) {
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

    this.activePageButton(pageNumber)

    this.queryParam.remove("page")
    this.queryParam.append("page", pageNumber)

    this.input.value = pageNumber
    htmx.trigger(`#${this.input.id}`, "change")
  }
}

window.addEventListener("load", () => new Pagination())
