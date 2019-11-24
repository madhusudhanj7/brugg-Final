app.controller("controller.home.profile", function($scope , $state , $users ,  $stateParams , $http , Flash,$uibModal) {

  // $scope.data = $scope.tab.data;

  $scope.me = $users.get("mySelf");

  console.log('aaaaaaaaaaaaaaaaaaaaaa', $scope.me.pk);
  $http({
    method: 'GET',
    url: '/api/HR/payroll/?user=' + $scope.me.pk
  }).
  then(function(response) {
    $scope.payroll = response.data[0];
    console.log($scope.payroll);
  })
  console.log('((((((((((((((()))))))))))))))', $scope.me.pk);
  $http({
    method: 'GET',
    url: '/api/HR/designation/?user=' + $scope.me.pk
  }).
  then(function(response) {
    console.log(response.data, '&&&&&&&&&&&&&&&&&&&&&&&7');
    $scope.designation = response.data[0];
    console.log($scope.designation);

    if (typeof $scope.designation.division == 'number') {
      $http({
        method: 'GET',
        url: '/api/organization/divisions/' + $scope.designation.division + '/'
      }).
      then(function(response) {
        $scope.designation.division = response.data;
      })
    }

    if (typeof $scope.designation.unit == 'number') {
      $http({
        method: 'GET',
        url: '/api/organization/unit/' + $scope.designation.unit + '/'
      }).
      then(function(response) {
        $scope.designation.unit = response.data;
      })

    }




  })

  $http({
    method: 'GET',
    url: '/api/HR/profileAdminMode/?user=' + $scope.me.pk
  }).
  then(function(response) {
    console.log(response.data, '&&&&&&&&&&&&&&&&&&&&&&&7');
    $scope.data = response.data[0];
    console.log($scope.data);
  })

  $scope.openModal = function(payroll) {
  $uibModal.open({
       templateUrl: '/static/ngTemplates/app.home.profile.modal.html',
       size: 'lg',
       controller: function($scope,$http, Flash,$uibModalInstance,$users){
         $scope.data = payroll;
         console.log($scope.data);

         // $scope.joiningDate =new Date($scope.data.joiningDate);
         // $scope.joiningDateYear = $scope.joiningDate.getFullYear();
         // $scope.joiningMonth =  $scope.joiningDate.getMonth();
         //
         // $scope.currentDate = new Date()
         // $scope.currentYear = new Date().getFullYear()
         // $scope.currentMonth =  new Date().getMonth();
         //
         // if($scope.data.lastWorkingDate!=null){
         //   $scope.lastWorkingDate =new Date($scope.data.lastWorkingDate);
         //   $scope.lastWorkingYear = $scope.lastWorkingDate.getFullYear();
         //   $scope.lastWorkingMonth = $scope.lastWorkingDate.getMonth();
         // }
         // else{
         //   $scope.lastWorkingDate = $scope.currentDate
         //   $scope.lastWorkingYear = $scope.currentYear
         //   $scope.lastWorkingMonth = $scope.currentMonth
         // }
         //
         //
         //
         //
         // if ($scope.lastWorkingYear<$scope.currentYear) {
         //   $scope.currentYear = $scope.lastWorkingYear
         //   $scope.currentDate = $scope.lastWorkingDate
         // }
         //
         //
         //
         // $scope.$watch('currentYear', function(newValue, oldValue) {
         //
         //   console.log($scope.joiningMonth,$scope.lastWorkingMonth);
         //   $scope.monthsData =[]
         //   $scope.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
         //   if($scope.joiningDateYear==$scope.lastWorkingYear){;
         //     if($scope.joiningMonth==$scope.lastWorkingMonth){
         //       $scope.monthsData.push($scope.months[$scope.joiningMonth])
         //     }
         //     else{
         //       $scope.monthsData = $scope.months.splice($scope.joiningMonth,$scope.lastWorkingMonth-1)
         //     }
         //   }
         //   else if(newValue==$scope.joiningDateYear){
         //     $scope.monthsData = $scope.months.splice($scope.joiningMonth,$scope.months.length)
         //   }
         //   else if(newValue==$scope.lastWorkingYear){
         //     $scope.monthsData =  $scope.months.splice(0,$scope.lastWorkingMonth+1)
         //   }
         //   else{
         //     $scope.monthsData = $scope.months
         //   }
         // })
         //
         // $scope.next = function() {
         //   if($scope.lastWorkingYear == $scope.currentYear ){
         //     return ;
         //   }
         //   else{
         //   $scope.currentYear += 1;
         //   }
         // }
         //
         // $scope.prev = function() {
         //   if($scope.joiningDateYear == $scope.currentYear ){
         //     return ;
         //   }
         //   else{
         //   $scope.currentYear -= 1;
         //   }
         // }


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


         $scope.monthsList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

         $scope.allData = function(currentYear) {
           $scope.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
           $scope.currentYear = currentYear
           $scope.monthsData =[]
           if($scope.joiningDateYear==$scope.lastWorkingYear){
             if($scope.joiningMonth==$scope.lastWorkingMonth){
               $scope.monthsData.push($scope.months[$scope.joiningMonth])
             }
             else{
               $scope.monthsData = $scope.months.splice($scope.joiningMonth,$scope.lastWorkingMonth)
             }
           }
           else if($scope.currentYear==$scope.joiningDateYear){
             $scope.monthsData = $scope.months.splice($scope.joiningMonth,$scope.months.length)
           }
           else if($scope.currentYear==$scope.lastWorkingYear){
             $scope.monthsData =  $scope.months.splice(0,$scope.lastWorkingMonth+1)
           }
           else{
             $scope.monthsData = $scope.months
           }
         }
         $scope.$watch('currentYear', function(newValue, oldValue) {

            $scope.allData(newValue)

           $http({
             method: 'GET',
             url: '/api/payroll/payslip/?user=' + $scope.data.user + '&year=' + newValue
           }).
           then(function(response) {
             $scope.monthsForWhichPayslipsExist = []
             $scope.paySlips= response.data;

             for (var i = 0; i < $scope.paySlips.length; i++) {
               $scope.monthsForWhichPayslipsExist.push($scope.monthsList[$scope.paySlips[i].month -1]);
             }

           })


           console.log($scope.joiningMonth,$scope.lastWorkingMonth);

         })

         $scope.next = function() {
           if($scope.lastWorkingYear == $scope.currentYear ){
             return ;
           }
           else{
           $scope.currentYear += 1;
           $scope.allData($scope.currentYear)
           $scope.attendance = false;
           }
         }

         $scope.prev = function() {
           if($scope.joiningDateYear == $scope.currentYear ){
             return ;
           }
           else{
           $scope.currentYear -= 1;
           $scope.allData($scope.currentYear)
           $scope.attendance = false;
           }
         }



           $scope.cancel = function () {
             $uibModalInstance.dismiss('cancel')
           }

           $scope.attendance = false;

           $scope.view = function(n){
               $scope.monthss = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
               $scope.currentMonth=n;
                function monthIndex(mon){
                  for(var i=0;i<=$scope.monthss.length;i++){
                  if($scope.monthss.includes(mon)){
                    return $scope.monthss.indexOf(mon)+1;
                  }
                }
              }
              function daysInMonth (month, year) {
                  return new Date(year, month, 0).getDate();
              }
              $scope.presentDays=0;
              $scope.hrs =0;
              $scope.mins =0;
              $scope.indexMonth = monthIndex(n);
              $scope.days = daysInMonth($scope.indexMonth,$scope.currentYear);
              console.log($scope.currentYear,$scope.indexMonth,'mmmmmmmmmmmm');
              function interval(count){
                return   count ;
                 };

              $http({
                method: 'GET',
                url: '/api/performance/timeSheet/?user='+ $scope.data.user
              }).
              then(function(response) {
                $scope.presentDays=0;
                for (var i = 0; i < response.data.length; i++) {
                       $scope.split = response.data[i].date.split("-");
                       if( $scope.split[0] == $scope.currentYear){
                         if($scope.split[1] == $scope.indexMonth){
                           if(response.data[i].totaltime == null || typeof response.data[i].totaltime === "undefined"  ){

                           }
                           else{

                             $scope.timedata = response.data[i].totaltime.split(':');

                             $scope.mins = Number($scope.timedata[1]);
                             $scope.hrs = Number($scope.timedata[0]);
                             $scope.time =parseFloat($scope.hrs + '.' + $scope.mins);
                             console.log( $scope.time,'nnnnnnnnnn');
                             $scope.countDays =Math.floor($scope.time/8.5);
                             $scope.remainingHour = $scope.time%8.5;
                             $scope.remainingHours = $scope.remainingHour/8.5;
                             console.log( $scope.remainingHours ,'oooooooo');
                            $scope.presentDays += Math.floor(interval($scope.countDays)+$scope.remainingHours);
                             // if($scope.time >= 8.30)
                             // {
                             //   $scope.presentDays++
                             // }
                             $scope.attendance = true;
                             }

                         }
                     }
                  }
                 $scope.attendance = true;
              })
              $scope.leaveDays=0;
              $http({
                method: 'GET',
                url: '/api/HR/leave/?user='+$scope.data.user + '&status=approved&fromDate__year='+ $scope.currentYear + '&fromDate__month='+ $scope.indexMonth,
              }).
              then(function(response) {
                console.log(response.data);
                for (var i = 0; i < response.data.length; i++) {

                  if (response.data[i].leavesCount != null && response.data[i].leavesCount != undefined) {
                    $scope.leaveDays +=  response.data[i].leavesCount;
                  }
                }


              })
           }

         },
       })
     }


});
