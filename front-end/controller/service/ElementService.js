import * as gService from "./GeneralService.js"

export function CreateElementInfor() {
    const infor = document.createElement("i")

    infor.classList("bx bx-info-octagon")
    infor.title = "Thêm thông tin"

    return infor
}

export function createElementOverlay() {
    const getOverlay = document.querySelectorAll(".overlay")

    if (getOverlay.length > 0) {
        let getClassList = getOverlay[0].classList

        if (getClassList.contains("disable")) {
            getOverlay[0].classList.remove("disable")
        } else if (getOverlay[0].style.display == "none") {
            getOverlay[0].style.display == "block"
        }
        return getOverlay[0]
    }

    const overlay = document.createElement("div")
    const body = document.querySelector("body")

    let getClassList = overlay.classList

    if (!getClassList.contains("overlay")) {
        overlay.classList.add("overlay")
    }

    overlay.id = gService.generateUUID()

    body.appendChild(overlay)

    return overlay
}

export function createForm(dataForm, parentEle) {
    if (dataForm.length < 1) return

    let listTag = []

    dataForm.forEach(element => {
        let tag = document.querySelector(`#${element["id"]}`)

        if (tag) {
            if (tag.classList.contains("disable")) {

                tag.classList.remove("disable")
            } else if (tag.style.display == "none") {

                tag.classList.add("enable")
            }

            listTag.push(tag)
        } else {
            tag = document.createElement(`${element["tag"]}`)

            parentEle.appendChild(tag)

            tag.id = element["id"]

            const classTag = element["class"]

            if (Array.isArray(classTag)) {
                classTag.forEach(eleClass => {
                    if (eleClass) tag.classList.add(eleClass)
                })
            } else {
                tag.classList.add(classTag)
            }

        }
        listTag.push(tag)

        const tagChild = element["tagChild"]
        if (!tagChild || !Array.isArray(tagChild)) return

        tag.innerHTML = "";

        tagChild.forEach(child => {
            const childTag = document.createElement(child["tag"]);
            tag.appendChild(childTag);

            const classTag = child["class"];
            if (Array.isArray(classTag)) {
                classTag.forEach(eleClass => {
                    if (eleClass) childTag.classList.add(eleClass);
                });
            } else if (classTag) {
                childTag.classList.add(classTag);
            }

            try {
                const content = child["content"];
                if (content !== undefined) {
                    childTag.innerHTML = content;
                }
            } catch (error) {
                console.log("Not content");
            }
        });
    })

    return listTag
}

export function enableElementById(id) {
    const ele = document.querySelector(id)
    ele.classList.remove("disable")
}

export function disableElementById(id) {
    if (!id || typeof id !== "string") {
        console.warn("Invalid ID provided.");
        return;
    }

    try {
        const ele = document.querySelector(`#${id}`);
        if (ele) {
            ele.classList.add("disable");
        } else {
            console.warn(`Element with ID "${id}" not found.`);
        }
    } catch (error) {
        console.error(`Error in disableElementById for ID "${id}":`, error);
    }
}

export function removeElementById(ele) {
    const element = document.querySelector(`#${ele}`)

    if (element) {
        element.remove()
    }
}

function createPageItem(page, text = page, isDisabled = false, isActive = false) {
    return `<li class="page-item ${isDisabled ? 'disabled' : ''} ${isActive ? 'active-page' : ''}">
                ${text}
            </li>`
}

export function generatePagination(currentPage, totalPages) {
    const paginationContainer = document.getElementById('pagination')

    paginationContainer.innerHTML = ''
    if (totalPages <= 1) {
        return
    }

    if (!paginationContainer.innerHTML) {

        paginationContainer.innerHTML += createPageItem('prev', '&laquo', currentPage === 1)
        paginationContainer.innerHTML += createPageItem(1, 1, false, currentPage === 1)

        if (currentPage > 3) paginationContainer.innerHTML += createPageItem('dots', '...', true)

        for (let i = Math.max(2, currentPage - 1); i <= Math.min(totalPages - 1, currentPage + 1); i++) {
            paginationContainer.innerHTML += createPageItem(i, i, false, i === currentPage)
        }

        if (currentPage < totalPages - 2) paginationContainer.innerHTML += createPageItem('dots', '...', true)

        paginationContainer.innerHTML += createPageItem(totalPages, totalPages, false, currentPage === totalPages)

        paginationContainer.innerHTML += createPageItem('next', '&raquo', currentPage === totalPages)
    } else {
        const prevItem = paginationContainer.querySelector('.page-item:first-child')
        prevItem.classList.toggle('disabled', currentPage === 1)

        const pageItems = paginationContainer.querySelectorAll('.page-item')
        pageItems.forEach(item => {
            const page = parseInt(item.textContent)
            if (!isNaN(page)) {
                item.classList.toggle('active-page', page === currentPage)
            }
        })

        const nextItem = paginationContainer.querySelector('.page-item:last-child')
        nextItem.classList.toggle('disabled', currentPage === totalPages)
    }
}