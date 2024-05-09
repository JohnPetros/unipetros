class CheckboxGroup {
  constructor() {
    const container = document.querySelector(
      "[data-checklist-group='container']",
    )

    const checkboxes = container.querySelectorAll(
      "[data-checklist-group='checkbox']",
    )

    if (checkboxes.length) {
      const checkboxesName = checkboxes[0].name

      this.key = checkboxesName.slice(0, checkboxesName.length - 2)
      this.queryParam = new QueryParam()
      this.checkboxes = checkboxes

      for (const checkbox of checkboxes) {
        checkbox.addEventListener("change", (event) =>
          this.handleCheckboxChange(event),
        )
      }
    }
  }

  handleCheckboxChange() {
    const checklistIds = []

    for (const checkbox of this.checkboxes) {
      if (!checkbox.checked) continue

      checklistIds.push(checkbox.value)
    }

    if (!checklistIds.length) {
      this.queryParam.remove(this.key)
      return
    }

    this.queryParam.append(this.key, checklistIds.join(","))
  }
}

window.addEventListener("load", () => new CheckboxGroup())
