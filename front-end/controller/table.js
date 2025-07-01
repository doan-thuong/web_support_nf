import * as apiService from "./service/APIService.js"
import { getStatus } from "./service/TableService.js"
import { loading } from "./service/LoadingService.js"
import * as gService from "./service/GeneralService.js"
import * as eService from "./service/ElementService.js"

window.tableCtrl = function ($scope) {
    let url = "http://192.168.0.11:8080/getdata"
    let currentPage = 0
    const status = getStatus()

    const statusBtn = document.querySelector("#btn-filter")
    const refreshBtn = document.querySelector("#refresh")

    const inpCaseMin = document.querySelector("#inp-case-min")
    const inpCaseMax = document.querySelector("#inp-case-max")
    const inpDateMin = document.querySelector("#inp-date-min")
    const inpDateMax = document.querySelector("#inp-date-max")

    const body = document.querySelector("body")
    const paginationContainer = document.querySelector('.pagination')

    loading()

    url = apiService.cacheWhenReload(url)

    apiService.callAPI(url).then(res => {

        $scope.cases = res.data
        eService.generatePagination(1, res.length)

        $scope.$apply()
    }).finally(() => {

        loading()
    })

    $scope.statusList = status
    $scope.copy = function (value) {
        gService.writeToClipboard(value)
    }

    statusBtn.addEventListener("click", () => {
        let urlSearch = url
        let isSearch = false

        const searchParams = [
            { key: "status", value: $scope.selectedStatus },
            { key: "caseMin", value: inpCaseMin.value },
            { key: "caseMax", value: inpCaseMax.value },
            { key: "dateMin", value: inpDateMin.value },
            { key: "dateMax", value: inpDateMax.value },
        ]

        searchParams.forEach(param => {
            if (param.value !== undefined && param.value !== null && param.value !== "") {
                urlSearch = apiService.setParam(urlSearch, param.key, param.value)
                isSearch = true
            }
        })

        urlSearch = apiService.deleteParam(urlSearch, "cache")

        if (!isSearch) return

        loading()

        apiService.callAPI(urlSearch).then(res => {
            $scope.cases = res.data
            eService.generatePagination(1, res.length)
            $scope.$apply()

        }).finally(() => {

            loading()
        })
    })

    refreshBtn.addEventListener("click", () => {
        const params = [
            { key: "cache", value: false },
            { key: "refresh", value: true },
        ]

        let urlRefresh = url

        params.forEach(param => {
            if (param.value !== undefined && param.value !== null && param.value !== "") {
                urlSearch = apiService.setParam(urlSearch, param.key, param.value)
            }
        })

        loading()

        apiService.callAPI(urlRefresh).then(res => {
            $scope.cases = res.data
            eService.generatePagination(1, res.length)
            $scope.$apply()
        }).finally(() => {

            loading()
        })
    })

    $scope.showInfor = function (value) {
        let dataForm = [
            {
                tag: "div", id: "form-show-more", class: "show-more", tagChild: [
                    {
                        tag: "h3",
                        class: "title-show-more",
                        content: "Thông tin"
                    },
                    {
                        tag: "p",
                        class: "des-show-more",
                        content: value
                    }
                ]
            }
        ]

        let tags = eService.createForm(dataForm, body)

        let overlay = eService.createElementOverlay()

        overlay.addEventListener("click", () => {
            eService.disableElementById(overlay.id)

            tags.forEach(element => {
                eService.disableElementById(element.id)
            });
        })
    }

    paginationContainer.addEventListener('click', (event) => {
        const item = event.target;

        if (!item.classList.contains('page-item')) {
            return
        }

        let page = item.innerText

        if (page == '«') {
            page = currentPage - 1
        } else if (page == '»') {
            page = currentPage + 1
        }

        currentPage = parseInt(page)

        console.log(currentPage)
    })
}