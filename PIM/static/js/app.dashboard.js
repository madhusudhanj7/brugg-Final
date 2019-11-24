app.controller("controller.home", function($scope, $state, $http) {

  $scope.selectedUnit = ['Monthly','Weekly']

  $scope.selected = {
    toWatch:'Weekly'
  }

  $scope.$watch('selected.toWatch', function(newValue, oldValue) {
    console.log(newValue,'dddddddd');
    if (newValue!=='') {
      $scope.fetchGraphData(newValue)
    }
  })


$scope.fetchGraphData = function (typ) {
  $http({
    method: 'GET',
    url: '/api/ERP/graphData/?'+typ
  }).then(function(response) {
    console.log(response.data);
    $scope.labels = response.data.graphLabels;
    $scope.totalVisitors = response.data.totalVisitors
    $scope.totalApiGent = response.data.totalApiGent
    $scope.totalBlogSubs = response.data.totalBlogSubs
    $scope.totalContacts = response.data.totalContacts

    $scope.stat = [];
    $scope.stat1 = [];
    for (var j = 0; j < response.data.graphData.length; j++) {
      $scope.stat = [];
      for (let char in response.data.graphData[j]) {
        $scope.stat.push(response.data.graphData[j][char])
      }
      $scope.stat1.push($scope.stat)
    }
    $scope.mainArr = [];

    for (var i = 0; i < $scope.stat1[0].length; i++) {
      $scope.mainArr1 =  []
      for (var j = 0; j < $scope.stat1.length; j++) {
        $scope.mainArr1.push($scope.stat1[j][i])
      }
      $scope.mainArr.push($scope.mainArr1)
    }
    console.log($scope.mainArr);
    $scope.mainData = $scope.mainArr
    $scope.series = ['API Generated','Blog Subscribed','Demo Requested','Contacts'];
  })
}

$scope.fetchGraphData('Weekly')
})
