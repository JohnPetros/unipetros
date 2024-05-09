class Select {
  constructor() {
    const select = document.querySelector('[data-select="select"]')

    if (!select) return

    this.key = select.name
    this.queryParam = new QueryParam()

    select.addEventListener("change", (event) => this.handleSelectChange(event))
  }

  handleSelectChange(event) {
    this.queryParam.append(this.key, event.currentTarget.value)
  }
}

window.addEventListener("load", () => new Select())
