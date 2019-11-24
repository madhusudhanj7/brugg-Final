app.controller('controller.home.album', function($scope, $http, Flash,$uibModal){

    $scope.data = {
      tableData: [],
    };

  var multiselectOptions = [{
    icon: 'fa fa-plus',
    text: 'new'
  }, ];


  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.home.album.item.html',
  }, ];

  $scope.config = {
    url: '/api/homepage/albumImages/',
    views: views,
    // options: options,
    itemsNumPerView: [12, 24, 48],
    multiselectOptions: multiselectOptions,
    searchField: 'username',
  };


$scope.tableAction = function(target, action, mode) {
  if (action == 'new') {
    $uibModal.open({
      templateUrl: '/static/ngTemplates/app.home.album.add.html',
      size: 'sm',
      backdrop: true,
      resolve: {

      },
      controller: 'controller.home.album.add'
    })
  } else {
    for (var i = 0; i < $scope.data.tableData.length; i++) {
      if ($scope.data.tableData[i].pk == parseInt(target)) {
        if (action == 'delete') {
          $http({
            method: 'DELETE',
            url: '/api/homepage/albumImages/' + $scope.data.tableData[i].pk + '/',
          }).
          then(function(response) {
            Flash.create('success', 'Deleted Successfully')
            $scope.data.tableData.splice(i, 1)
            return
          })
        }
        console.log({
          title: title + $scope.data.tableData[i],
          cancel: true,
          app: appType,
          data: {
            pk: target,
            index: i
          },
          active: true
        });
        $scope.addTab({
          title: title + $scope.data.tableData[i].pk,
          cancel: true,
          app: appType,
          data: $scope.data.tableData[i],
          active: true
        })
      }
    }
  }

}


})

app.controller('controller.home.album.add', function($scope, $http, Flash,$uibModal){
$scope.form = {
  image:emptyFile
}


$scope.save = function(){
  var f = $scope.form;
  var fd = new FormData();
  if (f.image != null && f.image != emptyFile && typeof f.image != 'string'  ) {
      fd.append('image', f.image)
    }
    else{
      Flash.create('warning','Please Add Image')
      return
    }
    $http({
      method: 'POST',
      url: '/api/homepage/albumImages/',
      data: fd,
      transformRequest: angular.identity,
      headers: {
        'Content-Type': undefined
      }
    }).
    then(function(response) {
      $scope.form=response.data
      Flash.create('success', "Saved");

    })


}


})
