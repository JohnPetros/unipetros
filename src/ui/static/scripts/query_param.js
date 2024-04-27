class QueryParam {
  append(key, value) {
    const url = new URL(location)
    url.searchParams.set(key, value)
    history.pushState({}, "", url)
  }

  remove(key) {
    const url = new URL(window.location.href)
    url.searchParams.delete(key)
    const newUrl = url.search ? url.href : url.href.replace("?", "")
    window.history.replaceState({}, document.title, newUrl)
  }
}
