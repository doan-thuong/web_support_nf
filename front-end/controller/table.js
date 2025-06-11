import * as apiService from "./service/APIService.js"

window.tableCtrl = function ($scope) {
    let url = "http://192.168.0.11:8080/getdata"

    apiService.callAPI(url).then(data => {
        $scope.cases = data
        $scope.$apply()
    })
}