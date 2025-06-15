import * as apiService from "./service/APIService.js"
import { getStatus } from "./service/TableService.js"
import { showLoading } from "./service/LoadingService.js"

window.tableCtrl = function ($scope) {
    let url = "http://192.168.0.11:8080/getdata"
    const status = getStatus()
    const statusBtn = document.querySelector("#filter-status")
    const entries = performance.getEntriesByType("navigation")

    showLoading()

    if (entries.length && entries[0].type === "reload") {
        let newUrl = new URL(url)
        newUrl.searchParams.set("cache", false)
        url = newUrl.toString()
    }

    apiService.callAPI(url).then(data => {

        $scope.cases = data
        $scope.$apply()
    }).finally(() => {

        showLoading()
    })

    $scope.statusList = status

    statusBtn.addEventListener("click", () => {
        let valueStatus = $scope.selectedStatus

        if (valueStatus == "" || valueStatus == null) return

        let newUrl = apiService.setParam(url, "status", valueStatus)

        newUrl = apiService.deleteParam(newUrl, "cache")

        showLoading()

        apiService.callAPI(newUrl).then(data => {
            console.log(data)

            $scope.cases = data
            $scope.$apply()
        }).finally(() => {

            showLoading()
        })
    })
}