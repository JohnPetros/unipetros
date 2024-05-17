class AvatarInput {
  constructor() {
    const avatar = document.querySelector("[data-avatar-input='avatar']")
    const input = document.querySelector("[data-avatar-input='input']")

    if (!avatar || !input) return

    this.avatar = avatar
    input.addEventListener("change", (event) => this.handleInputChange(event))
  }

  handleInputChange(event) {
    const file = event.target.files[0]
    const fileReader = new FileReader()

    if (file) {
      fileReader.onload = (fileReaderEvent) => {
        this.avatar.src = fileReaderEvent.target.result
      }

      fileReader.readAsDataURL(file)
    }
  }
}

window.addEventListener("load", () => new AvatarInput())
