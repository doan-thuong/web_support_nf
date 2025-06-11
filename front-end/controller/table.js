import * as apiService from "./service/APIService.js"

window.tableCtrl = function ($scope) {
    const dataJson = [
        {
            case: 100,
            id: "8650e99945b74051af23985bebcb025e",
            content: "I bought Starter Pack 3 (Nightfall: Kingdom Frontier TD) king crown, payment was successful but the item has not been given to me",
            link: "https://drive.google.com/open?id=1UxNJsFl_LOTJRtZYfWT2HqX0Z4oxXU63",
            answer: "xin id hóa đơn và báo logout",
            status: 0
        },
        {
            case: 101,
            id: "8650e99945b74051af23985bebcb025e",
            content: "Starter Pack 2 (Nightfall: Kingdom Frontier TD), payment was successful but the item has not been given to me",
            link: "https://drive.google.com/open?id=1UxNJsFl_LOTJRtZYfWT2HqX0Z4oxXU63",
            answer: "xin id hóa đơn và báo logout",
            status: 1
        }
    ]

    let url = "http://192.168.0.11:8080/getdata"

    apiService.callAPI(url).then(data => {
        $scope.cases = data
        $scope.$apply()
    })
}