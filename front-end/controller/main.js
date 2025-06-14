var app = angular.module("myApp", ['ngRoute'])

app.config(function ($routeProvider) {
    $routeProvider
        .when('/table', {
            templateUrl: 'view/table.html',
            controller: tableCtrl,
        })
        .otherwise({
            redirectTo: '/table',
        })
}
)

app.controller('myCtrl', function ($scope) { })