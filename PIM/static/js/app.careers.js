app.config(function($httpProvider) {

  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.withCredentials = true;

});

app.controller("controller.home.careers", function($scope, $state, $users, $stateParams, $http, Flash) {
  $scope.data = {
    tableData: []
  };

  $scope.me = $users.get('mySelf');

  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.homepage.careersTemplates.items.html'
  }, ];

  $scope.config = {
    url: '/api/homepage/careers/',
    views: views,
    itemsNumPerView: [20, 40, 60],
    filterSearch: true,
    searchField: 'name',
    deletable: true
  };

  $scope.tableAction = function(target, action, mode) {
    for (var i = 0; i < $scope.data.tableData.length; i++) {
      if ($scope.data.tableData[i].pk == parseInt(target)) {
        if (action == 'delete') {
          $http({
            method: 'DELETE',
            url: '/api/homepage/careers/' + parseInt(target) + '/'
          }).
          then(function(response) {
            Flash.create('success', 'Deleted');
            $scope.$broadcast('forceRefetch', {})
          })
        } else {
          if (action == 'edit') {
            var title = 'Edit Carrers : ';
            var appType = 'CareersEdit';
          }
          if (action == 'viewTemplate') {
            var title = 'viewCareers : ';
            var appType = 'Careersview';
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
  }

  $scope.tabs = [];
  $scope.searchTabActive = true;


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


app.controller("controller.home.careers.form", function($scope, $state, $users, $stateParams, $http, Flash) {


  if ($scope.tab == undefined) {
    $scope.mode = 'new'
    $scope.form = {
      name: '',
      jobtype: '',
      skills: '',
      description: '',
      status: false,
      maxctc: 0
    }
  } else {
    $scope.mode = 'edit'
    $scope.form = $scope.data.tableData[$scope.tab.data.index]
  }

    $scope.add = function() {
    dataToSend = $scope.form
    console.log(dataToSend);
    var method = 'POST'
    var url = '/api/homepage/careers/'
    if ($scope.form.pk) {
      method = 'PATCH'
      url += $scope.form.pk + '/'
    }

    $http({
      method: method,
      url: url,
      data: dataToSend
    }).
    then(function(response) {
      Flash.create('success', 'Posted');
      $scope.projects = response.data;
      console.log($scope.projects);
    })
  }
})
