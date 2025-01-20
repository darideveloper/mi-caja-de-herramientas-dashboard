class AdminSetup {

  /**
   * Setup global data
   */
  constructor() {

    // Get current page without domain
    this.currentPage = document.querySelector("h1").textContent.toLowerCase().trim()
    console.log("Current page:", this.currentPage)

    // Globals css selectors
    this.selectors = {
      "icon": '.field-icon a',
      "image": '.field-image a',
      "url": 'td.field-url',
      "video": '.field-video a',
      "audio": '.field-audio a',
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
  #renderBaseImage(imageWrapper, className) {
    // Get link
    const link = imageWrapper.href

    // Create image tag
    const imageElem = document.createElement("img")
    imageElem.classList.add(className)
    imageElem.classList.add("rendered-media")
    imageElem.src = link

    // Append element to the wrapper
    imageWrapper.innerHTML = ""
    imageWrapper.appendChild(imageElem)
  }

  #renderBaseAudioVideo(mediaWrapper, isVideo) {
    // Get link
    const link = mediaWrapper.href

    // Create audio or video tag
    const mediaElem = isVideo ? document.createElement("video") : document.createElement("audio")
    mediaElem.classList.add("rendered-media")
    mediaElem.classList.add(isVideo ? "rendered-video" : "rendered-audio")
    mediaElem.controls = true

    // Create source tag
    const sourceElem = document.createElement("source")
    sourceElem.src = link
    sourceElem.type = isVideo ? "video/mp4" : "audio/mp3"

    // Append elements to the wrappers
    mediaElem.appendChild(sourceElem)
    mediaWrapper.innerHTML = ""
    mediaWrapper.appendChild(mediaElem)
  }


  /**
   * Render icon images
   */
  renderIcons() {
    const icons = document.querySelectorAll(this.selectors.icon)
    icons.forEach(iconWrapper => {
      this.#renderBaseImage(iconWrapper, "rendered-icon")
    })
  }

  /**
   * Render regular image images
   */
  renderImages() {
    const images = document.querySelectorAll(this.selectors.image)
    images.forEach(imageWrapper => {
      this.#renderBaseImage(imageWrapper, "rendered-image")
    })
  }

  /**
   * Render videos
   */
  renderVideos() {
    const videos = document.querySelectorAll(this.selectors.video)
    videos.forEach(videoWrapper => {
      this.#renderBaseAudioVideo(videoWrapper, true)
    })
  }

  renderAudios() {
    const audios = document.querySelectorAll(this.selectors.audio)
    audios.forEach(audioWrapper => {
      this.#renderBaseAudioVideo(audioWrapper, false)
    })
  }

  /**
   * Convert the url text to a clickable link
   */
  renderUrls() {
    const urls = document.querySelectorAll(this.selectors.url)
    console.log(urls)
    urls.forEach(urlWrapper => {
      const link = urlWrapper.textContent
      const linkElem = document.createElement("a")
      linkElem.classList.add("url-link")
      linkElem.href = link
      linkElem.innerText = link
      linkElem.target = "_blank"
      urlWrapper.innerHTML = ""
      urlWrapper.appendChild(linkElem)
    })
  }

  /**
   * Run the functions for the current page
   */
  autorun() {
    // Methods to run for each page
    const methods = {
      "categorías": [this.renderIcons],
      "grupos": [this.renderIcons],
      "links": [this.renderIcons, this.renderUrls],
      "posts": [this.renderImages, this.renderVideos, this.renderAudios],
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