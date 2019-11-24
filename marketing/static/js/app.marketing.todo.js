app.controller('businessManagement.marketing.todo', function($scope, $http){
  $scope.tasks = [];

  $http({method : 'GET' , url : '/api/marketing/todo/'}).
  then(function(response) {
    $scope.tasks = response.data;
  })


  $scope.add = function() {
    $http({
          method:'POST',
          url:'/api/marketing/todo/',
          data:{textarea:$scope.item,
            name:$scope.name,
            number:$scope.number,
            status:$scope.status,
            fValue:$scope.fValue,
            pic:$scope.pic,
            file:$scope.file,
            }
    }).
    then(function(response){
       $scope.tasks.push(response.data);
       $scope.item = "";
       $scope.msg ="Saved data successfully"
    })
  }
  $scope.remove = function(x){
       $scope.tasks.splice(x,1);
  };
})
