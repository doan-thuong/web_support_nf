import * as apiService from "./service/APIService.js"
import { getStatus } from "./service/TableService.js"
import { loading } from "./service/LoadingService.js"
import * as gService from "./service/GeneralService.js"
import * as eService from "./service/ElementService.js"

window.tableCtrl = function ($scope) {
    let url = "http://192.168.0.11:8080/getdata"
    const status = getStatus()
    const statusBtn = document.querySelector("#filter-status")
    const body = document.querySelector("body")

    loading()

    url = apiService.cacheWhenReload(url)

    apiService.callAPI(url).then(data => {

        $scope.cases = data
        $scope.$apply()
    }).finally(() => {

        loading()
    })

    $scope.statusList = status
    $scope.copy = function (value) {
        gService.writeToClipboard(value)
    }

    statusBtn.addEventListener("click", () => {
        let valueStatus = $scope.selectedStatus

        if (valueStatus == "" || valueStatus == null) return

        let newUrl = apiService.setParam(url, "status", valueStatus)

        newUrl = apiService.deleteParam(newUrl, "cache")

        loading()

        apiService.callAPI(newUrl).then(data => {
            console.log(data)

            $scope.cases = data
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
}