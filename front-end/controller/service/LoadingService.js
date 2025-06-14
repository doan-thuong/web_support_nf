export function showLoading(isShow) {
    const loading = document.querySelector(".loading-view")

    if (isShow == true) {
        loading.classList.add("active")
    } else if (isShow == false && loading.classList.contains("active")) {
        loading.classList.remove("active")
    }
}