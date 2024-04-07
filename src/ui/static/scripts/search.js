const searchInput = document.querySelector('[data-search="input"]')

function appendSeachParam(searchValue) {
  const url = new URL(location)
  url.searchParams.set('search', searchValue)
  history.pushState({}, '', url)
}

function handleSearchInputChange(event) {
  searchValue = event.currentTarget.value
  appendSeachParam(searchValue)
}

if (searchInput) {
  searchInput.addEventListener('input', handleSearchInputChange)
}
