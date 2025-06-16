export function loading() {
    const loading = document.querySelector(".loading-view")
    const listClassLoading = loading.classList

    if (!listClassLoading.contains("active")) {
        loading.classList.add("active")
    } else if (listClassLoading.contains("active")) {
        loading.classList.remove("active")
    }
}