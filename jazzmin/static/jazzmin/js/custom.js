class AdminSetup {

  /**
   * Setup global data
   */
  constructor() {

    // Get current page without domain
    this.currrentUrl = window.location.href
    this.currentPage = this.currrentUrl.replace(window.location.origin, "")

    // Globals css selectors
    this.selectors = {
      "icon": '.field-icon > a',
      "image": '.field-image > a',
      "url": '.field-url',
    }

    // Autorun functions
    this.autorun()
  }

  /**
   * Load the base image (image, logo, icon, etc) who match with the selector
   * 
   * @param {string} selector - The css selector to find the images
   * @param {string} className - The class name to add to the image
   */
  #renderBaseImage(selector, className) {
    const images = document.querySelectorAll(selector)
    images.forEach(image_wrapper => {
      const link = image_wrapper.href
      const image_elem = document.createElement("img")
      image_elem.classList.add(className)
      image_elem.src = link
      image_wrapper.innerHTML = ""
      image_wrapper.appendChild(image_elem)
    })
  }


  /**
   * Render icon images
   */
  renderIcons() {
    this.#renderBaseImage(this.selectors.icon, "rendered-icon")
  }

  /**
   * Render regular image images
   */
  renderImages() {
    this.#renderBaseImage(this.selectors.image, "rendered-image")
  }

  /**
   * Convert the url text to a clickable link
   */
  renderUrls() {
    const urls = document.querySelectorAll(this.selectors.url)
    console.log(urls)
    urls.forEach(url_wrapper => {
      const link = url_wrapper.textContent
      const link_elem = document.createElement("a")
      link_elem.classList.add("url-link")
      link_elem.href = link
      link_elem.innerText = link
      link_elem.target = "_blank"
      url_wrapper.innerHTML = ""
      url_wrapper.appendChild(link_elem)
    })
  }

  /**
   * Run the functions for the current page
   */
  autorun() {
    // Methods to run for each page
    const methods = {
      "/admin/blog/category/": [this.renderIcons],
      "/admin/blog/group/": [this.renderIcons],
      "/admin/blog/link/": [this.renderIcons, this.renderUrls],
      "/admin/blog/post/": [this.renderImages],
    }

    // Run the methods for the current page
    if (methods[this.currentPage]) {
      for (let method of methods[this.currentPage]) {
        method.call(this)
      }
    }
  }
}

new AdminSetup()