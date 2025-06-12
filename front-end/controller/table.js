import * as apiService from "./service/APIService.js"
import { getStatus } from "./service/TableService.js"

window.tableCtrl = function ($scope) {
    let url = "http://192.168.0.11:8080/getdata"
    const status = getStatus()
    const statusBtn = document.querySelector("#filter-status")

    // apiService.callAPI(url).then(data => {
    //     $scope.cases = data
    //     $scope.$apply()
    // })

    $scope.statusList = status

    statusBtn.addEventListener("click", () => {
        let valueStatus = $scope.selectedStatus
        console.log(valueStatus)
    })
}