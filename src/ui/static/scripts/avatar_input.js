const avatar = document.querySelector("[data-avatar-input='avatar']")
const input = document.querySelector("[data-avatar-input='input']")

function handleInputChange(event) {
  const file = event.target.files[0]
  const fileReader = new FileReader()

  if (file) {
    fileReader.onload = (fileReaderEvent) => {
      avatar.src = fileReaderEvent.target.result
    }

    fileReader.readAsDataURL(file)
  }
}

if (input) input.addEventListener('change', handleInputChange)
