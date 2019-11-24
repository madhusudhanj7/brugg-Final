app.controller('controller.home.accessories', function($scope, $http, Flash,$uibModal){
  $scope.data = {
    tableData: [],
    itemData : [],
  }
  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.home.accessories.item.html'
  }, ];

  var multiselectOptions = [{
      icon: 'fa fa-book',
      text: 'GenerateElevatorCatalog'
    },
    {
      icon: 'fa fa-book',
      text: 'GenerateCTPCatalog'
    },
  ];

  $scope.config = {
    url: '/api/homepage/accessories/',
    views: views,
    itemsNumPerView: [20, 40, 60],
    filterSearch: true,
    searchField: 'name',
    deletable: true,
    multiselectOptions : multiselectOptions,
  };

  var itemviews = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.home.accessories.item.item.html'
  }, ];

  $scope.itemconfig = {
    url: '/api/homepage/accessoriesData/',
    views: itemviews,
    itemsNumPerView: [20, 40, 60],
    filterSearch: true,
    searchField: 'itemNumber',
    deletable: true
  };



    $scope.tableAction = function(target, action, mode) {
      console.log(target, action, mode);

      if (action == 'GenerateElevatorCatalog') {

          $http({
            method: 'GET',
            url: '/api/homepage/generatebroucher/',

          }).
          then(function(response) {
            Flash.create('success', 'PDF Generated Successfully')
          })
      }
      else if (action == 'GenerateCTPCatalog') {

          $http({
            method: 'GET',
            url: '/api/homepage/ctpcatalog/',

          }).
          then(function(response) {
            Flash.create('success', 'PDF Generated Successfully')
          })
      }

      for (var i = 0; i < $scope.data.tableData.length; i++) {
        if ($scope.data.tableData[i].pk == parseInt(target)) {
          if (action == 'accessoriesEditor') {
            var title = 'Edit Accessories : ';
            var appType = 'accessoriesEditor';
          }
          if (action=='accessoriesDelete'){
             $scope.delete = function() {
              $http({
                method: 'DELETE',
                url: '/api/homepage/accessories/' + $scope.data.tableData[i].pk + '/',
              }).
              then(function(response) {
                Flash.create('success', 'Deleted Successfully')
                $scope.data.tableData.splice(i, 1)
              })
            }
            $scope.delete()
            return
          }
          if (action=='accessoriesPdf') {
            $uibModal.open({
              templateUrl: '/static/ngTemplates/app.home.accessories.download.modal.html',
              size: 'lg',
              backdrop: true,
              windowClass: 'center-modal',
              resolve: {
                val: function() {
                  return $scope.data.tableData[i].pk ;
                },
              },
              controller: function($scope, Flash, $uibModalInstance, val) {


                $scope.generatePdfAccessories = function(){
                  console.log($scope.form.accessories,'llllllllll');
                  $http({
                    method: 'GET',
                    url: '/api/homepage/generatePdfAccessories/?accessories='+$scope.form.accessories,

                  }).
                  then(function(response) {
                      Flash.create('success', 'PDF Generated Successfully')
                      return
                  })
                }
                $http({
                  method: 'GET',
                  url: '/api/homepage/accessoriesSection/?accessories='+val,

                }).
                then(function(response) {
                  console.log(response.data);
                  $scope.accessoriesList = []
                  for (var i = 0; i < response.data.length; i++) {
                    if (response.data[i].lang == 'en') {
                      $scope.accessoriesList.push(response.data[i].basicProductName)
                    }
                  }
                })

              }
            })
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

    $scope.itemAction = function(target, action, mode) {
      console.log(target, action, mode);

      for (var i = 0; i < $scope.data.itemData.length; i++) {
        if ($scope.data.itemData[i].pk == parseInt(target)) {
          if (action == 'itemExplore') {
            var title = 'Explore Item : ';
            var appType = 'itemExplore';
          }

          $scope.addTab({
            title: title + $scope.data.itemData[i].pk,
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


app.controller('controller.home.accessories.form', function($scope, $http, Flash,$uibModal){
$scope.refresh = function(){
  $scope.form = {
    name:'',
    mainImage:emptyFile,
    sectionImage:emptyFile,
  }
}


$scope.refreshSection = function(){
  $scope.section = {
    categoryName:'',
    basicProductName:'',
    productName:'',
    tagLine:'',
    title1:'',
    desc1:'',
    title2:'',
    desc2:'',
    lang:'en',
    bottomtext:'',
    image1:emptyFile,
    image2:emptyFile,
    backgroundImage1:emptyFile,
    backgroundImage2:emptyFile,
    catalogBG1 :emptyFile,
    catalogBG2 : emptyFile,
    media:[]
  }
}


$scope.refreshSection()

$scope.sectionDetails = []
if ($scope.tab == undefined) {
  $scope.mode='new'
  $scope.refresh();
} else {
  $scope.form = $scope.data.tableData[$scope.tab.data.index]
  $http({
    method: 'GET',
    url: '/api/homepage/accessoriesSection/?accessories='+ $scope.form.pk,
  }).
  then(function(response) {
    $scope.sectionDetails = response.data
  })
}




$scope.save=function(){
  var f = $scope.form;
  var fd = new FormData();
  fd.append('name', f.name)
  if (f.mainImage != null && f.mainImage != emptyFile && typeof f.mainImage != 'string'  ) {
      fd.append('mainImage', f.mainImage)
  }
  if (f.sectionImage != null && f.sectionImage != emptyFile && typeof f.sectionImage != 'string' ) {
      fd.append('sectionImage', f.sectionImage)
  }

  if (f.pk){
      var method ='PATCH'
      var url='/api/homepage/accessories/'+f.pk+'/'
  }
  else{
    var method ='POST'
    var url='/api/homepage/accessories/'
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
    $scope.form=response.data
    Flash.create('success', "Saved");

  })
}

$scope.languages = [
  'en',
  'de',
  'zh'
]

$scope.editSection = function(data,indx){
  $scope.section = data
  document.getElementById("englishName").disabled = true;
  $scope.sectionDetails.splice(indx ,1)
}

$scope.deleteSection = function(data,indx){
  $http({method : 'DELETE' , url : '/api/homepage/accessoriesSection/' + data.pk + '/'}).
    then(function(response) {
      $scope.sectionDetails.splice(indx ,1)
      Flash.create('success', response.status + ' : ' + response.statusText );
    })
}

$scope.saveSection = function(){
  if ($scope.section.categoryName == '') {
    Flash.create('warning', 'Add Category Name' )
    return
  }
  if ($scope.section.productName == '') {
    Flash.create('warning', 'Add Product Name' )
    return
  }
  var f = $scope.section;
  var fd = new FormData();
  fd.append('categoryName', f.categoryName)
  fd.append('productName', f.productName)
  fd.append('basicProductName', f.basicProductName)
  fd.append('tagLine', f.tagLine)
  fd.append('title1', f.title1)
  fd.append('desc1', f.desc1)
  fd.append('title2', f.title2)
  fd.append('desc2', f.desc2)
  fd.append('accessories', $scope.form.pk)
  fd.append('lang', f.lang)
  fd.append('bottomtext', f.bottomtext)

  var mediaPks = []
  for (var i = 0; i < f.media.length; i++) {
    mediaPks.push(f.media[i].pk)
  }
  if (mediaPks.length > 0) {
    fd.append('media', mediaPks)
  }

  if (f.image1 != null && f.image1 != emptyFile && typeof f.image1 != 'string'  ) {
      fd.append('image1', f.image1)
  }
  if (f.image2 != null && f.image2 != emptyFile && typeof f.image2 != 'string' ) {
      fd.append('image2', f.image2)
  }
  if (f.backgroundImage1 != null && f.backgroundImage1 != emptyFile && typeof f.backgroundImage1 != 'string'  ) {
      fd.append('backgroundImage1', f.backgroundImage1)
  }
  if (f.backgroundImage2 != null && f.backgroundImage2 != emptyFile && typeof f.backgroundImage2 != 'string' ) {
      fd.append('backgroundImage2', f.backgroundImage2)
  }
  if (f.catalogBG1 != null && f.catalogBG1 != emptyFile && typeof f.catalogBG1 != 'string'  ) {
      fd.append('catalogBG1', f.catalogBG1)
  }
  if (f.catalogBG2 != null && f.catalogBG2 != emptyFile && typeof f.catalogBG2 != 'string' ) {
      fd.append('catalogBG2', f.catalogBG2)
  }

  if (f.pk){
      var method ='PATCH'
      var url='/api/homepage/accessoriesSection/'+$scope.section.pk+'/'
  }
  else{
    var method ='POST'
    var url='/api/homepage/accessoriesSection/'
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
    Flash.create('success', "Saved");
    $scope.sectionDetails.push(response.data)
    $scope.refreshSection()
  })

}

$scope.reset = function(){
  $scope.refresh()
  $scope.refreshSection()
  $scope.sectionDetails = []
}

$scope.addField = function(val){
  $uibModal.open({
    templateUrl: '/static/ngTemplates/app.home.accessories.field.modal.html',
    size: 'lg',
    backdrop: true,
    windowClass: 'center-modal',
    resolve: {
      val: function() {
        return val;
      },
    },
    controller: function($scope, Flash, $uibModalInstance, val) {
      $scope.val = val

      $scope.fieldForm = {
        name: '',
        type: 'Char',
        required: true,
        dimensions: '',
        inPdf: true,
        inUI: true,
        showForm: true
      }

      $http({
        method: 'GET',
        url: '/api/homepage/accessoriesField/?productBaseName__iexact='+ val.basicProductName,
      }).
      then(function(response) {
        $scope.tempFieldsData = response.data
      })

      $scope.editField =  function(data,indx){
        $scope.tempFieldsData.splice(indx, 1)
        $scope.fieldForm = data
        document.getElementById("name").disabled = true;
      }

      $scope.saveTemplateField = function() {
        console.log('save field');
        if ($scope.fieldForm.name.length == 0) {
          Flash.create('danger', 'Please Mention Field Name')
          return
        }
        var tosend = {
          template: $scope.val.pk,
          name: $scope.fieldForm.name,
          dimensions: $scope.fieldForm.dimensions,
          type: $scope.fieldForm.type,
          required: $scope.fieldForm.required,
          inPdf: $scope.fieldForm.inPdf,
          inUI: $scope.fieldForm.inUI,
          productBaseName : $scope.val.basicProductName,
        }
        if ($scope.fieldForm.dimensions != null && $scope.fieldForm.dimensions.length > 0) {
          tosend.dimensions = $scope.fieldForm.dimensions
        }
        var method = 'POST'
        var url = '/api/homepage/accessoriesField/'
        if ($scope.fieldForm.pk) {
          method = 'PATCH'
          url += $scope.fieldForm.pk + '/'
        }
        $http({
          method: method,
          url: url,
          data: tosend,
        }).
        then(function(response) {
          Flash.create('success', 'Saved')
          $scope.tempFieldsData.push(response.data)
          $scope.fieldForm = {
            name: '',
            type: 'Char',
            required: true,
            dimensions: '',
            inPdf: true,
            inUI: true,
            showForm: false
          }

        }, function(error) {
          Flash.create('danger', 'Errors in the form')
        })
      }
    },
  })
}

$scope.viewProduct = function(val){
  $uibModal.open({
    templateUrl: '/static/ngTemplates/app.home.accessories.tableData.modal.html',
    size: 'lg',
    backdrop: true,
    windowClass: 'center-modal',
    resolve: {
      val: function() {
        return val;
      },
    },
    controller: function($scope, Flash, $uibModalInstance, val) {
      $scope.val = val



      $http({
        method: 'GET',
        url: '/api/homepage/accessories_table/?product='+ val.basicProductName,
      }).
      then(function(response) {
        $scope.heading = response.data.heading
        $scope.accessoriesData = response.data.data
      })

    }
  })
}


})

app.controller('controller.home.accessories.item.form', function($scope, $http, Flash,$uibModal){

  if ($scope.tab == undefined) {
    $scope.productForm = {
      itemNumber: 0,
      template: '',
    }
  } else {
    $scope.productForm = $scope.data.productsTableData[$scope.tab.data.index]
  }

  // $scope.accesstemplateSearch = function(query) {
  //   return $http.get('/api/homepage/accessoriesSection/?limit=10&basicProductName__icontains=' + query).
  //   then(function(response) {
  //       return response.data;
  //     var arr = []
  //     var checkArr = []
  //     for (var i = 0; i < response.data.results.length; i++) {
  //       if (checkArr.indexOf(response.data.results[i].parent_name)==-1) {
  //         arr.push(response.data.results[i])
  //         checkArr.push(response.data.results[i].parent_name)
  //       }
  //     }
  //     console.log(arr);
  //
  //     return arr;
  //   })
  // }

  $scope.accesstemplateSearch  = function(query) {
    return $http.get('/api/homepage/accessoriesSection/?limit=10&basicProductName_query=' + query).
    then(function(response) {
      console.log('@', response.data);
      return response.data.results;
    })
  };

  $scope.fetchTempFields = function(tempPk) {

    $http({
      method: 'GET',
      url: '/api/homepage/accessoriesField/?productBaseName=' + tempPk,
    }).
    then(function(response) {
      console.log(response.data,'kreeeeeeeeee');
      $scope.productFieldData = response.data
    })
  }

  $scope.$watch('productForm.template', function(newValue, oldValue) {
    if (newValue!=undefined) {
      if (newValue.pk) {
        $scope.fetchTempFields(newValue.basicProductName)
      } else {
        $scope.productFieldData = []
      }
    }
  })

  $scope.saveProduct = function() {
    console.log($scope.productFieldData);
    var f = $scope.productForm
    if (f.itemNumber == null && typeof f.itemNumber != 'number') {
      Flash.create('danger', 'Please Mention Proper Item Number')
      return
    }
    if (!f.template.pk) {
      Flash.create('danger', 'Please Select Proper Template')
      return
    }
    var toSend = {
      itemNumber: f.itemNumber,
      template: f.template.pk,
      productBaseName : f.template.basicProductName
    }
    fieldaData = []
    for (var i = 0; i < $scope.productFieldData.length; i++) {
      if ($scope.productFieldData[i].required && $scope.productFieldData[i].type == 'Char' && $scope.productFieldData[i].value.length == 0) {
        Flash.create('danger', 'Please Fill All Required Fields')
        return
      }
      if ($scope.productFieldData[i].type == 'Integer' && $scope.productFieldData[i].value == null && typeof $scope.productFieldData[i].value != 'number') {
        Flash.create('danger', 'Invalid Data Format')
        return
      }
      fieldaData.push({
        pk: $scope.productFieldData[i].pk,
        typ: $scope.productFieldData[i].type,
        value: $scope.productFieldData[i].value
      })
    }
    toSend.fieldaData = fieldaData

    $http({
      method: 'POST',
      url: '/api/homepage/accessoriesData/',
      data: toSend,
    }).
    then(function(response) {
      Flash.create('success', 'Product Created Successfully')
      $scope.productForm = {
        itemNumber: 0,
        template: ''
      }
    }, function(error) {
      Flash.create('danger', 'Errors in the form')
    })
  }

})

app.controller('controller.home.accessories.item.explore', function($scope, $http, Flash,$uibModal){
  $scope.productDetails = $scope.data.itemData[$scope.tab.data.index]

  $scope.saveProduct = function() {
    if ($scope.productDetails.itemNumber == null && typeof $scope.productDetails.itemNumber != 'number') {
      Flash.create('danger', 'Please Mention Proper Item Number')
      return
    }
    var toSend = {
      itemNumber: $scope.productDetails.itemNumber
    }
    fieldaData = []
    for (var i = 0; i < $scope.productDetails.accessoriesfieldValues.length; i++) {
      if ($scope.productDetails.accessoriesfieldValues[i].field.required && $scope.productDetails.accessoriesfieldValues[i].field.type == 'Char' && $scope.productDetails.accessoriesfieldValues[i].field.value.length == 0) {
        Flash.create('danger', 'Please Fill All Required Fields')
        return
      }
      if ($scope.productDetails.accessoriesfieldValues[i].field.type == 'Integer' && $scope.productDetails.accessoriesfieldValues[i].field.value == null && typeof $scope.productDetails.accessoriesfieldValues[i].field.value != 'number') {
        Flash.create('danger', 'Invalid Data Format')
        return
      }
      fieldaData.push({
        pk: $scope.productDetails.accessoriesfieldValues[i].pk,
        typ: $scope.productDetails.accessoriesfieldValues[i].field.type,
        value: $scope.productDetails.accessoriesfieldValues[i].field.value
      })
    }
    toSend.fieldaData = fieldaData
    $http({
      method: 'PATCH',
      url: '/api/homepage/accessoriesData/' + $scope.productDetails.pk + '/',
      data: toSend,
    }).
    then(function(response) {
      Flash.create('success', 'Saved')
      $scope.productDetails = response.data
    }, function(error) {
      Flash.create('danger', 'Errors in the form')
    })
  }

})
