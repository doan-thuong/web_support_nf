import * as apiService from "./service/APIService.js"
import { getStatus } from "./service/TableService.js"
import { showLoading } from "./service/LoadingService.js"

window.tableCtrl = function ($scope) {
    let url = "http://192.168.0.11:8080/getdata"
    const status = getStatus()
    const statusBtn = document.querySelector("#filter-status")

    showLoading(true)

    apiService.callAPI(url).then(data => {

        $scope.cases = data
        $scope.$apply()
    }).finally(() => {

        showLoading(false)
    })

    $scope.statusList = status

    statusBtn.addEventListener("click", () => {
        let valueStatus = $scope.selectedStatus

        if (valueStatus == "" || valueStatus == null) return

        let param = `?status=${valueStatus}`

        showLoading(true)

        apiService.callAPI(url + param).then(data => {
            $scope.cases = data
            $scope.$apply()
        }).finally(() => {

            showLoading(false)
        })
    })
}