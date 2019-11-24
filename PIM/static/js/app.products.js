app.controller("controller.home.products", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {
  console.log('in product pageeeeeeeee');
  $scope.data = {
    tableData: [],
    productsTableData: []
  }
  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.homepage.productsTemplate.items.html'
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
    url: '/api/homepage/productTemplate/',
    views: views,
    itemsNumPerView: [20, 40, 60],
    filterSearch: true,
    searchField: 'name',
    deletable: true,
    multiselectOptions : multiselectOptions,
  };
  var pviews = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.homepage.products.items.html'
  }, ];
  $scope.productsConfig = {
    url: '/api/homepage/product/',
    views: pviews,
    itemsNumPerView: [24, 48, 96],
    filterSearch: true,
    searchField: 'itemNumber',
    deletable: true
  };


  $scope.tableAction = function(target, action, mode) {
    console.log( action);

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
    else{
      for (var i = 0; i < $scope.data.tableData.length; i++) {
        if ($scope.data.tableData[i].pk == parseInt(target)) {
          if (action == 'editTemplate') {
            var title = 'Edit Template : ';
            var appType = 'templateEditor';
          }
          if (action == 'viewTemplate') {
            var title = 'Template : ';
            var appType = 'templateview';
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
  $scope.productsTableAction = function(target, action, mode) {
    console.log(target, action, mode);

    for (var i = 0; i < $scope.data.productsTableData.length; i++) {
      if ($scope.data.productsTableData[i].pk == parseInt(target)) {
        if (action == 'viewProduct') {
          var title = 'Product : ';
          var appType = 'productExplore';
        }

        $scope.addTab({
          title: title + $scope.data.productsTableData[i].pk,
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

app.controller("controller.home.productsTemplate.explore", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {
  $scope.templateDetails = $scope.data.tableData[$scope.tab.data.index]
  $http({
    method: 'GET',
    url: '/api/homepage/productField/?template=' + $scope.templateDetails.pk,
  }).
  then(function(response) {
    $scope.tempFieldsData = response.data
  })

  $http({
    method: 'GET',
    url: '/api/homepage/product/?template=' + $scope.templateDetails.pk,
  }).
  then(function(response) {
    $scope.tempProductsData = response.data

  })

  $scope.generatePDF = function() {
    $http({
      method: 'GET',
      url: '/api/homepage/broucherpdf/?val=' + $scope.templateDetails.pk,

    }).
    then(function(response) {
      Flash.create('success', 'PDF Generated Successfully')
      $scope.templateDetails.pdfgenerated = true
    })
  }
})

app.controller("controller.home.products.explore", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {
  $scope.productDetails = $scope.data.productsTableData[$scope.tab.data.index]
  $scope.saveProduct = function() {
    if ($scope.productDetails.itemNumber == null && typeof $scope.productDetails.itemNumber != 'number') {
      Flash.create('danger', 'Please Mention Proper Item Number')
      return
    }
    var toSend = {
      itemNumber: $scope.productDetails.itemNumber
    }
    fieldaData = []
    for (var i = 0; i < $scope.productDetails.fieldValues.length; i++) {
      if ($scope.productDetails.fieldValues[i].field.required && $scope.productDetails.fieldValues[i].field.type == 'Char' && $scope.productDetails.fieldValues[i].field.value.length == 0) {
        Flash.create('danger', 'Please Fill All Required Fields')
        return
      }
      if ($scope.productDetails.fieldValues[i].field.type == 'Integer' && $scope.productDetails.fieldValues[i].field.value == null && typeof $scope.productDetails.fieldValues[i].field.value != 'number') {
        Flash.create('danger', 'Invalid Data Format')
        return
      }
      fieldaData.push({
        pk: $scope.productDetails.fieldValues[i].pk,
        typ: $scope.productDetails.fieldValues[i].field.type,
        value: $scope.productDetails.fieldValues[i].field.value
      })
    }
    toSend.fieldaData = fieldaData
    $http({
      method: 'PATCH',
      url: '/api/homepage/product/' + $scope.productDetails.pk + '/',
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



app.controller("controller.home.productsTemplate.form", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {

  if ($scope.tab == undefined) {
    $scope.productForm = {

    }
  } else {
    $scope.productForm = $scope.data.productsTableData[$scope.tab.data.index]
  }

  $scope.templateSearch = function(query) {
    return $http.get('/api/homepage/productTemplate/?limit=10&appname__icontains=' + query).
    then(function(response) {

      var arr = []
      var checkArr = []
      for (var i = 0; i < response.data.results.length; i++) {
        if (checkArr.indexOf(response.data.results[i].parent_name)==-1) {
          arr.push(response.data.results[i])
          checkArr.push(response.data.results[i].parent_name)
        }
      }
      console.log(arr);

      return arr;
    })
  };

  // $scope.fetchTempFields = function(tempPk) {
  //   $http({
  //     method: 'GET',
  //     url: '/api/homepage/productTemplate/?template=' + tempPk,
  //   }).
  //   then(function(response) {
  //     $scope.productFieldData = response.data
  //   })
  // }
  // $scope.$watch('productForm.parentname', function(newValue, oldValue) {
  //   if (newValue.pk) {
  //     $scope.fetchTempFields(newValue.pk)
  //   } else {
  //     $scope.productFieldData = []
  //   }
  // })

  // $uibModal.open({
  //   templateUrl: '/static/ngTemplates/app.homepage.productTemplates.modal.html',
  //   size: $scope.size,
  //   backdrop: true,
  //   windowClass: 'center-modal',
  //   resolve: {
  //     image: function() {
  //       return $scope.imgSrc;
  //       return $scope.name1;
  //       return $scope.name2;
  //       return $scope.name3;
  //     },
  //   },
  //   controller: function($scope, Flash, $uibModalInstance, image) {
  //     $scope.src = image
  //     $scope.closeModal = function() {
  //       $uibModalInstance.dismiss();
  //     }
  //   },
  // })

  $scope.resetTemplate = function() {
    $scope.tempFieldsData = []
    $scope.templateForm = {
      name: '',
      parent_name: '',
      description: '',
      rteData1_otl: '',
      rteData1_en: '',
      rteData2_otl: '',
      rteData2_en: '',
      keyword1_v:'',
      keyword1_u:'',
      keyword1_d:'',
      keyword2_v:'',
      keyword2_u:'',
      keyword2_d:'',
      keyword3_v:'',
      keyword3_u:'',
      keyword3_d:'',
      keyword4_v:'',
      keyword4_u:'',
      keyword4_d:'',
      disclaimer_otl:'',
      disclaimer_en:'',
      defaultImage: emptyFile,
      backgroundImage1: emptyFile,
      backgroundImage2: emptyFile,
      media: [],
      color : '',
      catalogBG1 : emptyFile,
      catalogBG2 :emptyFile,
      rteDescription :'',
      des_ch : '',
      des_de : '',
      rteData1_ch : '',
      rteData2_ch : '',
      disclaimer_ch : '',
      rteDescription_de : '',
      rteDescription_ch : ''
    }
    $scope.fieldForm = {
      name: '',
      type: 'Char',
      required: true,
      dimensions: '',
      inPdf: true,
      inUI: true,
      showForm: false
    }
  }
  $scope.fetchTempFields = function(baseName) {
    $http({
      method: 'GET',
      url: '/api/homepage/productField/?template=' + baseName,
    }).
    then(function(response) {
      $scope.tempFieldsData = response.data
    })
  }

  if ($scope.tab == undefined) {
    $scope.mode = 'new'
    $scope.resetTemplate()
    $scope.fetchTempFields()
  } else {
    $scope.mode = 'edit'
    $scope.templateForm = $scope.data.tableData[$scope.tab.data.index]
    console.log($scope.data.tableData[$scope.tab.data.index],'$scope.data.tableData[$scope.tab.data.index].keyword1');
    if ($scope.data.tableData[$scope.tab.data.index].keyword1) {
      var l1Data = JSON.parse($scope.data.tableData[$scope.tab.data.index].keyword1)
      // $scope.templateForm.keyword1_v = l1Data.value
      $scope.templateForm.keyword1_u = l1Data.value1
      $scope.templateForm.keyword1_d = l1Data.value2
    }
    if ($scope.data.tableData[$scope.tab.data.index].keyword2) {
      var l2Data = JSON.parse($scope.data.tableData[$scope.tab.data.index].keyword2)
      // $scope.templateForm.keyword2_v = l2Data.value
      $scope.templateForm.keyword2_u = l2Data.value1
      $scope.templateForm.keyword2_d = l2Data.value2
    }
    if ($scope.data.tableData[$scope.tab.data.index].keyword3) {
      var l3Data = JSON.parse($scope.data.tableData[$scope.tab.data.index].keyword3)
      // $scope.templateForm.keyword3_v = l3Data.value
      $scope.templateForm.keyword3_u = l3Data.value1
      $scope.templateForm.keyword3_d = l3Data.value2
    }
    if ($scope.data.tableData[$scope.tab.data.index].keyword4) {
      var l4Data = JSON.parse($scope.data.tableData[$scope.tab.data.index].keyword4)
      // $scope.templateForm.keyword4_v = l4Data.value
      $scope.templateForm.keyword4_u = l4Data.value1
      $scope.templateForm.keyword4_d = l4Data.value2
    }
    console.log($scope.templateForm, 'dtaaaa');
    // if ($scope.templateForm.parent_name) {
    //   $scope.templateForm.parent_name = {parent_name:$scope.templateForm.parent_name}
    // }
    $scope.fieldForm = {
      name: '',
      type: 'Char',
      required: true,
      dimensions: '',
      inPdf: true,
      inUI: true,
      showForm: false
    }
    $scope.fetchTempFields($scope.templateForm.pk)
  }

  $scope.addField = function() {
    $scope.fieldForm = {
      name: '',
      type: 'Char',
      required: true,
      dimensions: '',
      inPdf: true,
      inUI: true,
      showForm: true
    }
  }

  $scope.deleteField = function(idx) {
    $http({
      method: 'DELETE',
      url: '/api/homepage/productField/' + $scope.tempFieldsData[idx].pk + '/',
    }).
    then(function(response) {
      console.log(idx);
      Flash.create('success', 'Deleted Successfully')
      $scope.tempFieldsData.splice(idx, 1)
    })
  }

  $scope.editField = function(idx) {
    console.log($scope.tempFieldsData[idx]);
    $scope.fieldForm = $scope.tempFieldsData[idx]
    $scope.fieldForm.showForm = true
    $scope.tempFieldsData.splice(idx, 1)
  }

  $scope.saveTemplateField = function() {
    if (!$scope.templateForm.pk) {
      Flash.create('danger', 'Invalid Template')
      return
    }
    console.log('save field');
    if ($scope.fieldForm.name.length == 0) {
      Flash.create('danger', 'Please Mention Field Name')
      return
    }
    var tosend = {
      template: $scope.templateForm.pk,
      name: $scope.fieldForm.name,
      dimensions: $scope.fieldForm.dimensions,
      type: $scope.fieldForm.type,
      required: $scope.fieldForm.required,
      inPdf: $scope.fieldForm.inPdf,
      inUI: $scope.fieldForm.inUI
    }
    if ($scope.fieldForm.dimensions != null && $scope.fieldForm.dimensions.length > 0) {
      tosend.dimensions = $scope.fieldForm.dimensions
    }
    var method = 'POST'
    var url = '/api/homepage/productField/'
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

  $scope.saveTemplate = function() {

    var f = $scope.templateForm
    console.log(f);
    if (f.name.length == 0) {
      Flash.create('danger', 'Please Mention Template Name')
      return
    }
    if (typeof $scope.templateForm.parent_name != 'object' && $scope.templateForm.parent_name.length==0) {
      Flash.create('danger', 'Please Select Parent Name')
      return
    }
    if (f.description.length == 0) {
      Flash.create('danger', 'Please Write Some Description')
      return
    }

    if(typeof $scope.templateForm.parent_name == 'object'){
      $scope.parentname  = $scope.templateForm.parent_name.parent_name
    }else{
      $scope.parentname  = $scope.templateForm.parent_name
    }
    console.log($scope.mode,'objjjj');
    var fd = new FormData()
    fd.append('name', f.name)
    fd.append('parent_name', $scope.parentname)
    fd.append('description', f.description)
    if (f.des_ch != null && f.des_ch.length > 0) {
      fd.append('des_ch', f.des_ch)
    }
    if (f.des_de != null && f.des_de.length > 0) {
      fd.append('des_de', f.des_de)
    }
    if (f.rteData1_en != null && f.rteData1_en.length > 0) {
      fd.append('rteData1_en', f.rteData1_en)
    }
    if (f.rteData1_otl != null && f.rteData1_otl.length > 0) {
      fd.append('rteData1_otl', f.rteData1_otl)
    }
    if (f.rteData1_ch != null && f.rteData1_ch.length > 0) {
      fd.append('rteData1_ch', f.rteData1_ch)
    }
    if (f.rteData2_ch != null && f.rteData2_ch.length > 0) {
      fd.append('rteData2_ch', f.rteData2_ch)
    }
    if (f.rteData2_en != null && f.rteData2_en.length > 0) {
      fd.append('rteData2_en', f.rteData2_en)
    }
    if (f.rteData2_otl != null && f.rteData2_otl.length > 0) {
      fd.append('rteData2_otl', f.rteData2_otl)
    }
    if (f.rteDescription != null && f.rteDescription.length > 0) {
      fd.append('rteDescription', f.rteDescription)
    }
    if (f.rteDescription_ch != null && f.rteDescription_ch.length > 0) {
      fd.append('rteDescription_ch', f.rteDescription_ch)
    }
    if (f.rteDescription_de != null && f.rteDescription_de.length > 0) {
      fd.append('rteDescription_de', f.rteDescription_de)
    }

    if (f.defaultImage != null && f.defaultImage != emptyFile && typeof f.defaultImage != 'string') {
      fd.append('defaultImage', f.defaultImage)
    }
    else if($scope.mode=='new'){
      Flash.create('danger', 'Please Add Default Image')
      return
    }
    if (f.backgroundImage1 != null && f.backgroundImage1 != emptyFile && typeof f.backgroundImage1 != 'string') {
      fd.append('backgroundImage1', f.backgroundImage1)
    }else if($scope.mode=='new'){
      Flash.create('danger', 'Please Add First Page Background Image')
      return
    }
    if (f.backgroundImage2 != null && f.backgroundImage2 != emptyFile && typeof f.backgroundImage2 != 'string') {
      fd.append('backgroundImage2', f.backgroundImage2)
    }else if($scope.mode=='new'){
      Flash.create('danger', 'Please Add Second Page Background Image')
      return
    }
    if (f.catalogBG1 != null && f.catalogBG1 != emptyFile && typeof f.catalogBG1 != 'string') {
      fd.append('catalogBG1', f.catalogBG1)
    }

    if (f.catalogBG2 != null && f.catalogBG2 != emptyFile && typeof f.catalogBG2 != 'string') {
      fd.append('catalogBG1', f.catalogBG2)
    }

    if (f.productImage1 != null && f.productImage1 != emptyFile && typeof f.productImage1 != 'string') {
      fd.append('productImage1', f.productImage1)
    }
    if (f.productImage2 != null && f.productImage2 != emptyFile && typeof f.productImage2 != 'string') {
      fd.append('productImage2', f.productImage2)
    }

    if (f.disclaimer_en != null && f.disclaimer_en.length > 0) {
      fd.append('disclaimer_en', f.disclaimer_en)
    }
    if (f.disclaimer_otl != null && f.disclaimer_otl.length > 0) {
      fd.append('disclaimer_otl', f.disclaimer_otl)
    }
    if (f.disclaimer_ch != null && f.disclaimer_ch.length > 0) {
      fd.append('disclaimer_ch', f.disclaimer_ch)
    }    

    if (f.color != null && f.color.length > 0) {
      fd.append('color', f.color)
    }


    var k1Obj = {value1:f.keyword1_u,value2:f.keyword1_d}
    fd.append('keyword1', JSON.stringify(k1Obj))

    var k2Obj = {value1:f.keyword2_u,value2:f.keyword2_d}
    fd.append('keyword2', JSON.stringify(k2Obj))

    var k3Obj = {value1:f.keyword3_u,value2:f.keyword3_d}
    fd.append('keyword3', JSON.stringify(k3Obj))

    var k4Obj = {value1:f.keyword4_u,value2:f.keyword4_d}
    fd.append('keyword4', JSON.stringify(k4Obj))

    // var k4Obj = {value:f.keyword4_v,unit:f.keyword4_u,description:f.keyword4_d}
    // fd.append('keyword4', JSON.stringify(k4Obj))

    var pfObj = {description1:f.productfields_1,description2:f.productfields_2,description3:f.productfields_3,description4:f.productfields_4}
    fd.append('productfields', JSON.stringify(pfObj))


    var mediaPks = []
    for (var i = 0; i < f.media.length; i++) {
      mediaPks.push(f.media[i].pk)
    }
    if (mediaPks.length > 0) {
      fd.append('media', mediaPks)
    }

    // fd.append('ropes', f.ropes)
    // fd.append('elastic_elongation', f.elastic_elongation)
    // fd.append('permenant_elongation', f.permenant_elongation)
    // fd.append('lifting_height', f.lifting_height)

    var method = 'POST'
    var url = '/api/homepage/productTemplate/'
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
      Flash.create('success', 'Template Created Successfully')
      // $scope.templateForm = response.data
    }, function(error) {
      console.log('errrr');
      Flash.create('danger', error.status + ' : ' + error.statusText)
    })
  }
})
app.controller("controller.home.products.form", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {

  if ($scope.tab == undefined) {
    $scope.productForm = {
      itemNumber: 0,
      template: '',
    }
  } else {
    $scope.productForm = $scope.data.productsTableData[$scope.tab.data.index]
  }

  $scope.templateSearch = function(query) {
    return $http.get('/api/homepage/productTemplate/?limit=10&name__icontains=' + query).
    then(function(response) {
      return response.data.results;
    })
  };
  $scope.fetchTempFields = function(tempPk) {
    $http({
      method: 'GET',
      url: '/api/homepage/productField/?template=' + tempPk,
    }).
    then(function(response) {
      $scope.productFieldData = response.data
    })
  }
  $scope.$watch('productForm.template', function(newValue, oldValue) {
    if (newValue.pk) {
      $scope.fetchTempFields(newValue.pk)
    } else {
      $scope.productFieldData = []
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
      url: '/api/homepage/product/',
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
