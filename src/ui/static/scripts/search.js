class Search {
  constructor() {
    const searchInput = document.querySelector(
      '[data-search="input"]',
      (event) => this.handleSearchInputChange(event),
    )

    if (searchInput) {
      searchInput.addEventListener("input", (event) =>
        this.handleSearchInputChange(event),
      )
      this.queryParam = new QueryParam()
    }
  }

  handleSearchInputChange(event) {
    const searchValue = event.currentTarget.value
    this.queryParam.append("search", searchValue)
  }
}

window.addEventListener("load", () => new Search())
