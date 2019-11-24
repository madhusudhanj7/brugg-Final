app.controller('controller.home.locations', function($scope, $http, Flash,$uibModal){
  $scope.data = {
    tableData: [],
  }
  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.home.locations.item.html'
  }, ];


$scope.config = {
  url: '/api/homepage/locations/',
  views: views,
  itemsNumPerView: [12, 24, 36],
  filterSearch: true,
  searchField:'name',
  deletable: true,
};




    $scope.tableAction = function(target, action, mode) {
      console.log(target, action, mode);

      for (var i = 0; i < $scope.data.tableData.length; i++) {
        if ($scope.data.tableData[i].pk == parseInt(target)) {
          if (action == 'editLocations') {
            var title = 'Edit Locations : ';
            var appType = 'LocationsEditor';
          }
          if (action == 'viewLocations') {
            var title = 'Locations : ';
            var appType = 'Locationsview';
          }
          if (action=='delete'){
             $scope.delete = function() {
              $http({
                method: 'DELETE',
                url: '/api/homepage/locations/' + $scope.data.tableData[i].pk + '/',
              }).
              then(function(response) {
                Flash.create('success', 'Deleted Successfully')
                $scope.data.tableData.splice(i, 1)
              })
            }
            $scope.delete()
            return
          }

          $scope.addTab({
            title: title + $scope.data.tableData[i].pk,
            cancel: true,
            app: appType,
            data: {
              pk: target,
              index: i
            },
            active: true
          })
        }
      }
    }

    $scope.tabs = []
    $scope.searchTabActive = true

    $scope.closeTab = function(index) {
      $scope.tabs.splice(index, 1)
    }

    $scope.addTab = function(input) {
      $scope.searchTabActive = false;
      alreadyOpen = false;
      for (var i = 0; i < $scope.tabs.length; i++) {

        if ($scope.tabs[i].data.pk == input.data.pk && $scope.tabs[i].app == input.app) {
          $scope.tabs[i].active = true;
          alreadyOpen = true;
        } else {
          $scope.tabs[i].active = false;
        }
      }
      if (!alreadyOpen) {
        $scope.tabs.push(input)
      }
    }

})
app.controller('controller.home.locations.form', function($scope, $http, Flash,$uibModal){



$scope.initial = function(){
  $scope.form = {
    name:'',
    lat:0,
    long:0,
    address_en:'',
    address_de:'',
    address_zh:'',
    representation:false,
    shortUrl:''
  }
}

if ($scope.tab == undefined) {
  $scope.mode='new'
  $scope.initial()
} else {
  $scope.form = $scope.data.tableData[$scope.tab.data.index]
}

$scope.save = function(){

  var sendData = {
    name:$scope.form.name,
    lat:$scope.form.lat,
    long:$scope.form.long,
    address_en:$scope.form.address_en,
    address_de:$scope.form.address_de,
    address_zh:$scope.form.address_zh,
    representation:$scope.form.representation,
    shortUrl:$scope.form.shortUrl
  }
  if($scope.mode == 'new'){
    var method = "POST"
    var url = "/api/homepage/locations/"
  }else{
    var method = "PATCH"
    var url = "/api/homepage/locations/"+$scope.form.pk+"/"
  }

  $http({
    method: method,
    url: url,
    data: sendData,
  }).
  then(function(response) {
    Flash.create('success','Created  Sucessfully.');
    if ($scope.mode == 'new') {
      $scope.initial()
    }
  }, function(error) {
    Flash.create('danger','Something went wrong.');
  })

  }
})
