app.config(function($stateProvider) {

  $stateProvider
    .state('workforceManagement.payroll.salary', {
      url: "/salary",
      views: {
        "": {
          templateUrl: '/static/ngTemplates/app.payroll.salary.html',
          controller: 'workforceManagement.salary',
        }
      }
    })
});

app.controller("controller.warehouse.payroll.openReportInfo", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal, $uibModalInstance, usr) {

  $http({
    method: 'GET',
    url: '/api/HR/payroll/?user=' + usr
  }).then(function(response) {
    $scope.payroll = response.data[0];
    console.log($scope.payroll);
  })

})


app.controller("workforceManagement.salary.payroll.info", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {

  $scope.data = $scope.tab.data;

  $scope.joiningDate =new Date($scope.data.joiningDate);
  $scope.joiningDateYear = $scope.joiningDate.getFullYear();
  $scope.joiningMonth =  $scope.joiningDate.getMonth();

  $scope.currentDate = new Date()
  $scope.currentYear = new Date().getFullYear()
  $scope.currentMonth =  new Date().getMonth();

  if($scope.data.lastWorkingDate!=null){
    $scope.lastWorkingDate =new Date($scope.data.lastWorkingDate);
    $scope.lastWorkingYear = $scope.lastWorkingDate.getFullYear();
    $scope.lastWorkingMonth = $scope.lastWorkingDate.getMonth();
  }
  else{
    $scope.lastWorkingDate = $scope.currentDate
    $scope.lastWorkingYear = $scope.currentYear
    $scope.lastWorkingMonth = $scope.currentMonth
  }




  if ($scope.lastWorkingYear<$scope.currentYear) {
    $scope.currentYear = $scope.lastWorkingYear
    $scope.currentDate = $scope.lastWorkingDate
  }



  $scope.$watch('currentYear', function(newValue, oldValue) {

    console.log($scope.joiningMonth,$scope.lastWorkingMonth);
    $scope.monthsData =[]
    $scope.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if($scope.joiningDateYear==$scope.lastWorkingYear){;
      if($scope.joiningMonth==$scope.lastWorkingMonth){
        $scope.monthsData.push($scope.months[$scope.joiningMonth])
      }
      else{
        $scope.monthsData = $scope.months.splice($scope.joiningMonth,$scope.lastWorkingMonth-1)
      }
    }
    else if(newValue==$scope.joiningDateYear){
      $scope.monthsData = $scope.months.splice($scope.joiningMonth,$scope.months.length)
    }
    else if(newValue==$scope.lastWorkingYear){
      $scope.monthsData =  $scope.months.splice(0,$scope.lastWorkingMonth+1)
    }
    else{
      $scope.monthsData = $scope.months
    }
  })

  $scope.next = function() {
    $scope.currentYear += 1;
  }

  $scope.prev = function() {
    $scope.currentYear -= 1;
  }

})

app.controller("workforceManagement.salary.payslips.info", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {

  $scope.data = $scope.tab.data;


  $scope.months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobar", "November", "December"]
  $scope.pay={}
  $scope.updateReport = function(){
    if($scope.data.dateOfProcessing==undefined||$scope.data.dateOfProcessing==null){
      Flash.create('danger', 'Please select Date of Processing');
      return
    }
    else if (typeof $scope.data.dateOfProcessing == 'object') {
    $scope.data.dateOfProcessing =$scope.data.dateOfProcessing.toJSON().split('T')[0]
    } else {
      $scope.data.dateOfProcessing = $scope.data.dateOfProcessing
    }
    if($scope.pay.status==true){
      $scope.status = "approved"
    }
    else{
      $scope.status = "submitted"
    }
    $http({
      method: 'PATCH',
      url: '/api/payroll/report/' + $scope.data.pk + '/',
      data: {
        dateOfProcessing: $scope.data.dateOfProcessing,
        status : $scope.status
      }
    }).
    then(function(response) {
      $scope.data = response.data
    })

  }
  //
  //   $scope.reportData = [];
  //   $scope.total=0.0
  //   $scope.tds=0.0
  //   $http({
  //   method: 'GET',
  //   url: '/api/payroll/payslip/?month='+$scope.data.month
  // }).
  // then(function(response) {
  //   $scope.reportData = response.data;
  // })

})


app.controller("workforceManagement.salary.payroll.report", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {


  $scope.userSearch = function(query) {
    return $http.get('/api/HR/userSearch/?username__contains=' + query).
    then(function(response) {
      return response.data;
    })
  };

  var today = new Date();
  $scope.selectedYear = today.getFullYear();
  $scope.selectedMonth = today.getMonth() + 1 + '';


  // $scope.data = $scope.tab.data;



  $scope.data = []

  $scope.daysInMonth = new Date(parseInt($scope.selectedYear), parseInt($scope.selectedMonth), 0).getDate();
  $scope.addedData =[]
  $scope.initializeSheet = function() {
    $scope.addedData =[]
    var toDelete = [];
    for (var i = 0; i < $scope.report.payslips.length; i++) {
      toDelete.push($scope.report.payslips[i].payslipID);
    }

    for (var i = 0; i < toDelete.length; i++) {
      $http({
        method: 'DELETE',
        url: '/api/payroll/payslip/' + toDelete[i] + '/'
      }).
      then(function(response) {

      })
    }


    $http({
      method: 'GET',
      url: '/api/HR/payroll/'
    }).
    then(function(response) {
      $scope.report.payslips = [];
      for (var i = 0; i < response.data.length; i++) {
        response.data[i].adHoc = 0;
        response.data[i].reimbursement = 0;

        $http({method : 'GET' , url : '/api/payroll/getReimbursement/?user=' + response.data[i].user }).
        then((function(i) {
          return function(response) {
            $scope.report.payslips[i].reimbursement = response.data.amount;
          }
        })(i))


        // response.data[i].totalTDS = $scope.totalTDS;
        response.data[i].days = $scope.daysInMonth;
        response.data[i].saved = false;
        response.data[i].amount = ((response.data[i].hra + response.data[i].special + response.data[i].lta + response.data[i].basic + response.data[i].adHoc) / 12).toFixed(2);
        response.data[i].tds = (((( response.data[i].special + response.data[i].basic + response.data[i].adHoc) / 12) + response.data[i].adHoc) * (response.data[i].taxSlab)/100).toFixed(2);
        response.data[i].totalPayable = (((((response.data[i].hra + response.data[i].special + response.data[i].lta + response.data[i].basic + response.data[i].adHoc) / 12) + response.data[i].adHoc) * 0.9) + response.data[i].reimbursement).toFixed(2);

        $scope.report.payslips.push(response.data[i]);
      }
    })
  }


  $scope.openReportInfo = function(idx) {
    $uibModal.open({
      templateUrl: '/static/ngTemplates/app.salary.payroll.openReportInfo.html',
      size: 'md',
      backdrop: true,
      resolve: {
        usr: function() {
          if (idx == undefined || idx == null) {
            return {};
          } else {
            return $scope.report.payslips[idx].user;
          }
        }
      },
      controller: "controller.warehouse.payroll.openReportInfo",
    }).result.then(function() {

    }, function() {
      // $rootScope.$broadcast('forceRefetch' , {});
    });



  }

  $scope.deffer = function(indx) {
    $scope.report.payslips[indx].deffered = true;
    if ($scope.report.payslips[indx].payslipID != undefined) {
      $http({
        method: 'PATCH',
        url: '/api/payroll/payslip/' + $scope.report.payslips[indx].payslipID + '/',
        data: {
          deffered: true
        }
      }).
      then(function(response) {

      })
    }
  }



  $scope.saveIndividualPayslip = function(id, indx) {
    var url = '/api/payroll/payslip/'
    if (id == undefined) {
      method = 'POST';
    } else {
      method = 'PATCH';
      url += id + '/'
    }

    var toSend = {
      tds: $scope.report.payslips[indx].tds,
      adHoc: $scope.report.payslips[indx].adHoc,
      days: $scope.report.payslips[indx].days,
      report: $scope.report.pk,
      user: $scope.report.payslips[indx].user,
      month: $scope.selectedMonth,
      year: $scope.selectedYear,
      amount: $scope.report.payslips[indx].amount,
      totalPayable: $scope.report.payslips[indx].totalPayable,
      reimbursement: $scope.report.payslips[indx].reimbursement,
    }

    $http({
      method: method,
      url: url,
      data: toSend
    }).
    then((function(indx) {
      return function(response) {
        $scope.report.payslips[indx].payslipID = response.data.pk;

        if (method = 'POST') {

          $scope.addedData.push(response.data)
        }
        else{
          $scope.addedData[indx] = response.data
        }
      }
    })(indx))
  }



  $scope.fetchOrCreate = function() {
    $http({
      method: 'GET',
      url: '/api/payroll/report/?month=' + $scope.selectedMonth + '&year=' + $scope.selectedYear
    }).
    then(function(response) {
      if (response.data.length == 0) {
        // the report was not created

        $http({
          method: 'POST',
          url: '/api/payroll/report/',
          data: {
            month: $scope.selectedMonth,
            year: $scope.selectedYear
          }
        }).
        then(function(response) {
          $scope.report = response.data;
          $scope.initializeSheet();
        })

      } else {
        $scope.report = response.data[0];
        for (var i = 0; i < $scope.report.payslips.length; i++) {
          $scope.report.payslips[i].payslipID = $scope.report.payslips[i].pk;
          $scope.addedData.push($scope.report.payslips[i])
        }


      }
    })
  }



  $scope.save = function(status) {
    // make a POST request with : total , totalTDS

    $scope.total =0.0
    $scope.totalTDS =0.0
    console.log($scope.addedData.payslips);
    if($scope.addedData.length>0){
      for (var i = 0; i <$scope.addedData.length; i++) {
        $scope.total+=  $scope.addedData[i].amount
        $scope.totalTDS +=  $scope.addedData[i].tds
      }
    }
    else{
      Flash.create('danger', 'Please select Employees');
      return
    }
    if(status=='save'){
      var toSend = {
        total:Math.round($scope.total),
        totalTDS: Math.round($scope.totalTDS),
        status:'created'
      }
    }
    else if(status=='submit'){
      var toSend = {
        total:Math.round($scope.total),
        totalTDS: Math.round($scope.totalTDS),
        status:'submitted'
      }
    }


    // if (submit) {
    //   toSend.status = 'submitted';
    // }
    $http({
      method: 'PATCH',
      url: '/api/payroll/report/' + $scope.report.pk + '/',
      data: toSend
    }).
    then(function() {

    })

  }

  $scope.submit = function() {
    $scope.save(true);
  }

  $scope.cancel = function(e) {
    $uibModalInstance.dismiss();
  };

  $scope.$watch('selectedYear', function() {
    $scope.addedData =[]
    $scope.fetchOrCreate();
  })

  $scope.$watch('selectedMonth', function() {
    $scope.addedData =[]
    $scope.fetchOrCreate();
  })


  $scope.years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]


  $scope.months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobar", "November", "December"]

  // $scope.reportData = [];
  // // if ($scope.report != undefined){
  // $http({
  //   method: 'GET',
  //   url: '/api/payroll/report/?month=' + $scope.months
  // }).
  // then(function(response) {
  //   $scope.reportData = response.data;

    // console.log('******************', response.data);
    // // $scope.reportData = response.data;
    // for (var i = 0; i < response.data.length; i++) {
    //   $scope.reportData.push(response.data[i]);
    // }



  // })


})

app.controller('workforceManagement.salary.payroll.report.item', function($scope) {

  $scope.months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobar", "November", "December"]

});



app.controller("workforceManagement.salary", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal, $aside) {


  $scope.data = {
    tableData: [],
    allTableData: [],
    // reportTableData: []
  };

  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.payroll.salary.allitems.html',
  }, ];

  $scope.configAll = {
    views: views,
    url: '/api/HR/payroll/',
    searchField: 'user',
    itemsNumPerView: [8, 16, 24],
    // multiselectOptions: multiselectOptions,
  }


  $scope.tableActionAll = function(target, action, mode) {
    for (var i = 0; i < $scope.data.allTableData.length; i++) {
      if ($scope.data.allTableData[i].pk == parseInt(target)) {
        if (action == 'explore') {
          var title = 'payroll :';
          var appType = 'payrollExplorer';
        }


        console.log({
          title: title + $scope.data.allTableData[i],
          cancel: true,
          app: appType,
          data: {
            pk: target,
            index: i
          },
          active: true
        });


        $scope.addTab({

          title: title + $scope.data.allTableData[i].user,
          cancel: true,
          app: appType,
          data: $scope.data.allTableData[i],
          active: true
        })
      }
    }

  }


  var multiselectOptions = [{
    icon: 'fa fa-plus',
    text: 'new'
  }, ];

  var views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.payroll.salary.reportitems.html',
  }, ];
  var getParams = [{key : 'status!' , value :"created"}];
  $scope.config = {
    views: views,
    url: '/api/payroll/report',
    searchField: 'username',
    itemsNumPerView: [8, 16, 24],
    getParams : getParams,
    multiselectOptions: multiselectOptions,
  }



  $scope.tableAction = function(target, action, mode) {
    if (action == 'new') {
      $aside.open({
        templateUrl: '/static/ngTemplates/app.payroll.salary.report.html',
        placement: 'right',
        size: 'xl',
        backdrop: true,
        resolve: {

        },
        controller: 'workforceManagement.salary.payroll.report'
      })
    } else {
      for (var i = 0; i < $scope.data.tableData.length; i++) {
        if ($scope.data.tableData[i].pk == parseInt(target)) {
          if (action == 'details') {
            var title = 'Report :';
            var appType = 'reportExplorer';
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
// /api/finance/expenseSummary/?user=67

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

});
