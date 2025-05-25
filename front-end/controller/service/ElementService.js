export function CreateElementInfor() {
    const infor = document.createElement("i")

    infor.classList("bx bx-info-octagon")
    infor.title = "Thêm thông tin"

    return infor
}

export function createElementOverlay() {
    const overlay = document.createElement("div")

    overlay.className("overlay")
}

export function removeElementById(ele) {
    const element = document.querySelector(`#${ele}`)

    if (element) {
        element.remove()
    }
}