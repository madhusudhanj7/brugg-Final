



app.controller('controller.home.apptips', function($scope, $http, Flash){
  $scope.data = {
    tableData: [],
  }
  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.homepage.apptipsItems.html'
  }, ];

  $scope.config = {
    url: '/api/homepage/apptips/?filter_data=none',
    views: views,
    itemsNumPerView: [20, 40, 60],
    filterSearch: true,
    searchField: 'tipname',
    deletable: true
  };




    $scope.tableAction = function(target, action, mode) {
      console.log(target, action, mode);

      for (var i = 0; i < $scope.data.tableData.length; i++) {
        if ($scope.data.tableData[i].pk == parseInt(target)) {
          if (action == 'editApptips') {
            var title = 'Edit Apptips : ';
            var appType = 'ApptipsEditor';
          }
          if (action == 'viewApptips') {
            var title = 'Template : ';
            var appType = 'Apptipsview';
          }
          if (action=='delete'){
             $scope.delete = function() {
              $http({
                method: 'DELETE',
                url: '/api/homepage/apptips/' + $scope.data.tableData[i].pk + '/',
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
app.controller("controller.home.apptips.form", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal,$sce) {


  $scope.resetTemplate = function() {
    $scope.apptipsForm = {
      text: '',
      image1: emptyFile,
      tipname:'',
      heading:'',
      lang:''

    }

  }

  $scope.languages = [
    'en',
    'de',
    'zh'
  ]

  $scope.media = [
    'nomedia',
    'image',
    'video',
  ]

  $scope.apptipSearch = function(query) {
    return $http.get('/api/homepage/apptips/?limit=10&query_data=' + query).
    then(function(response) {
      return response.data.results;
    })
  };
  $scope.fetchTempFields = function(tempPk) {
    console.log($scope.fetchTempFields.pk)
    $http({
      method: 'GET',
      url: '/api/homepage/apptips/' + tempPk,
    }).
    then(function(response) {
      $scope.appTipsData = response.data
    })
  }

  if ($scope.tab == undefined) {
    $scope.mode = 'new'
    $scope.resetTemplate()
  } else {
    $scope.mode = 'edit'
    $scope.apptipsForm = $scope.data.tableData[$scope.tab.data.index]
  }
  $scope.save = function() {


    var f = $scope.apptipsForm;
    console.log(f.image1,'image111')
    var url = '/api/homepage/apptips/';
    var fd = new FormData();

    fd.append('text', f.text)
    if (f.image1 != null && f.image1 != emptyFile  && typeof f.image1 != 'string' ) {
        fd.append('image1', f.image1)
    }
    fd.append('mediaTyp', f.mediaTyp)
    fd.append('size', f.size)
    fd.append('tipname', f.tipname)
    fd.append('lang', f.lang)
    // if (f.heading.pk != null && f.heading.pk != '' ) {
    //     fd.append('heading', f.heading.pk)
    //
    // }
    var method = 'POST';
    if (f.pk) {
      method = 'PATCH'
      url += f.pk + '/'
    }

    $http({
      method: method,
      url: url,
      data: fd,
      transformRequest: angular.identity,
      headers: {
        'Content-Type': undefined
      }

    }).

    then(function(response) {
      Flash.create('success','Created  Sucessfully');
      if ($scope.mode == 'new') {
        $scope.resetTemplate()
      }

    }, function(error) {
      $scope.msg = 'Errors In The Form'
    })





  }

  $scope.deleteField = function(idx) {
    $http({
      method: 'DELETE',
      url: '/api/homepage/apptips/' + $scope.appTipsData[idx].pk + '/',
    }).
    then(function(response) {
      console.log(idx);
      Flash.create('success', 'Deleted Successfully')
      $scope.appTipsData.splice(idx, 1)
    })
  }

  $scope.templateForm = false
  $scope.addOredit = 'Add'
  $scope.saveChild = false
  $scope.addTemplate = function(){
    $scope.templateForm = true
    $scope.apptipsAddform = {
      text: '',
      image1: emptyFile,
      tipname:'',
      heading:''
    }
    $scope.addOredit = 'Add'
    $scope.saveChild = false
  }

  $scope.apptipsAddform = {
    text: '',
    image1: emptyFile,
  }
  $scope.appTipsdata = []
  $http({
    method: 'GET',
    url: '/api/homepage/apptips/?heading='+ $scope.apptipsForm.pk,
  }).
  then(function(response) {
    $scope.appTipsdata = response.data
    for (var i = 0; i < $scope.appTipsdata.length; i++) {
      $scope.appTipsdata[i].image1 = $sce.trustAsResourceUrl($scope.appTipsdata[i].image1)
    }
  })
  $scope.saveTemplate = function(){
    console.log($scope.appTipsdata,'lll');
    var f = $scope.apptipsAddform;
    var url = '/api/homepage/apptips/';
    var fd = new FormData();

    fd.append('text', f.text)
    if (f.image1 != null && f.image1 != emptyFile && typeof f.image1 != 'string') {
        fd.append('image1', f.image1)
    }
    fd.append('mediaTyp', f.mediaTyp)
    fd.append('heading', $scope.apptipsForm.pk)
    fd.append('size', f.size)
    fd.append('lang',  $scope.apptipsForm.lang)

    var method = 'POST';
    if ($scope.saveChild ) {
      method = 'PATCH'
      url += $scope.editChildData.pk + '/'
    }


    $http({
      method: method,
      url: url,
      data: fd,
      transformRequest: angular.identity,
      headers: {
        'Content-Type': undefined
      }
    }).then(function(response) {
      Flash.create('success','Created  Sucessfully');
      $scope.apptipsAddform = {
        text: '',
        image1: emptyFile,
        tipname:'',
        heading:''
      }
      if(method == 'POST'){
        $scope.appTipsdata.push(response.data)
      }
      if(method == 'PATCH'){
        $scope.appTipsdata.splice($scope.ChildDataIdx,1,response.data)
      }
      $scope.templateForm = false
    }, function(error) {
      $scope.msg = 'Errors In The Form'
    })
  }




  $scope.editField = function(idx,pk) {

    $http({
      method: 'GET',
      url: '/api/homepage/apptips/'+ pk +'/',
    }).
    then(function(response) {
      $scope.editChildData = response.data
      $scope.ChildDataIdx = idx
      $scope.templateForm = true
      $scope.addOredit = 'Save'
      $scope.saveChild = true
      $scope.apptipsAddform.text=$scope.editChildData.text
      $scope.apptipsAddform.mediaTyp=$scope.editChildData.mediaTyp
      $scope.apptipsAddform.image1=$scope.editChildData.image1
      $scope.apptipsAddform.size=$scope.editChildData.size
    })
  }
  $scope.deleteChild = function(idx,pk) {

    $http({
      method: 'DELETE',
      url: '/api/homepage/apptips/'+ pk +'/',
    }).
    then(function(response) {
      $scope.appTipsdata.splice(idx,1)
    })
  }




})
