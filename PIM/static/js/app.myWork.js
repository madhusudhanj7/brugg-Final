app.controller("controller.home.myWork", function($scope, $state, $users,$aside, $stateParams, $http, Flash, $uibModal) {

  $scope.me = $users.get('mySelf');

  $scope.items = []

  $scope.selectDate = function(indx) {
    $scope.selectIndex = indx;
  }

  $scope.selectIndex = 7;

  $scope.next = function() {
    $scope.selectIndex < $scope.dates.length - 1 ? $scope.selectIndex++ : $scope.selectIndex = 0;

  }

  $scope.prev = function() {
    $scope.selectIndex > 0 ? $scope.selectIndex-- : $scope.selectIndex = $scope.dates.length - 1;
  }



  $scope.addTableRow = function() {
    $scope.items.push({
      project: '',
      duration: 0,
      comment: ''
    });
    console.log($scope.items);
  }

  $scope.totalTime = function() {

    if ($scope.items == undefined) {
      return 0;
    }


    var total = 0;
    for (var i = 0; i < $scope.items.length; i++) {
      if ($scope.items[i].duration != undefined) {
        total += $scope.items[i].duration;
      }
    }
    return total.toFixed(2);
    console.log('aaaaaa', total);
  }


  $scope.deleteTable = function(index) {
    if ($scope.items[index].pk != undefined) {
      $http({
        method: 'DELETE',
        url: '/api/performance/timeSheetItem/' + $scope.items[index].pk + '/'
      }).
      then((function(index) {
        return function(response) {
          $scope.items.splice(index, 1);
          Flash.create('success', 'Deleted');
        }
      })(index))

    } else {
      $scope.items.splice(index, 1);
    }
  };



  $scope.projectSearch = function(query) {
    return $http.get('/api/projects/project/?title__contains=' + query).
    then(function(response) {
      return response.data;
    })
  };

  var today = new Date();
  var day = 1000 * 3600 * 24;

  // $scope.dates = [new Date(today.getTime() - day * 2), new Date(today.getTime() - day), today, new Date(today.getTime() + day), new Date(today.getTime() + 2 * day)];
  $scope.dates = []
  for (var i = 10; i > 0; i--) {
    $scope.dates.push(new Date(today.getTime() - day * (i-3)))
  }

  console.log($scope.dates);


  $http({
    method: 'GET',
    url: '/api/projects/project/?member'
  }).
  then(function(response) {
    $scope.projects = response.data;
    console.log($scope.projects);
  })


  $scope.addProjects = function(idx) {

    for (var i = 0; i < $scope.items.length; i++) {
      if ($scope.items[i].project.pk == $scope.projects[idx].pk) {
        console.log($scope.items[i].project.pk);
        console.log($scope.projects[idx].pk);
        Flash.create('warning', 'Already added');
        return;
      }
    }

    $scope.items.push({
      project: $scope.projects[idx],
      duration: 0,
      comment: ''
    });

  }

  // function addZero(i) {
  //   if (i < 10) {
  //     i = "0" + i;
  //   }
  //   return i;
  // }

  $scope.checkin = function() {
    var d = new Date();
    console.log(d);
    $scope.checkinTime = d.getTime();
    console.log('aaaaaa', $scope.checkinTime,$scope.timeSheet);
    $http({
      method: 'PATCH',
      url: '/api/performance/timeSheet/'+ $scope.timeSheet.pk + '/',
      data: {
        checkInTime: 'checkin',
      }
    }).
    then(function(response) {
      $scope.btnTyp = response.data;

    })

  }

  $scope.checkout = function() {
    var d = new Date();
    $scope.checkoutTime = d.getTime() - $scope.checkinTime;
    console.log($scope.checkoutTime ,$scope.checkinTime);


    function msToTime(duration) {
        var milliseconds = parseInt((duration % 1000) / 100);
        var  seconds = parseInt((duration / 1000) % 60);
        var  minutes = parseInt((duration / (1000 * 60)) % 60);
        var  hours = parseInt((duration / (1000 * 60 * 60)) % 24);

        hours = (hours < 10) ? "0" + hours : hours;
        minutes = (minutes < 10) ? "0" + minutes : minutes;
        seconds = (seconds < 10) ? "0" + seconds : seconds;

        return hours + ":" + minutes + ":" + seconds + ":"+ milliseconds ;
      }
    $scope.totaltime = msToTime($scope.checkoutTime);
    console.log(typeof $scope.totaltime,'cccccccccccccc');
    console.log('bbbbbbbbbb', $scope.checkoutTime,$scope.timeSheet,$scope.totaltime,'vvvvvv');
    $http({
      method: 'PATCH',
      url: '/api/performance/timeSheet/'+ $scope.timeSheet.pk + '/',
      data: {
        checkOutTime: 'checkout',
        totaltime : $scope.totaltime,
      }
    }).
    then(function(response) {
      $scope.btnTyp = response.data;
      console.log("aaaaaaaaaaaaaaaaaaaaaaaa",$scope.btnTyp);
    })
  }

  $scope.$watch('selectIndex', function(newValue, oldValue) {
    var today = new Date()

    var dt = $scope.dates[newValue];
    if (dt > today ) {
      console.log('featureeeeeeee');
      $scope.Checkinshow = false
    }else {
      console.log('past or equallllllllll');
      $scope.Checkinshow = true
    }

    $http({
      method: 'GET',
      url: '/api/performance/timeSheet/?date=' + dt.toJSON().split('T')[0] + '&user=' + $scope.me.pk
    }).
    then(function(response) {
      if (response.data.length == 0) {

        $http({
          method: 'POST',
          url: '/api/performance/timeSheet/',
          data: {
            date: $scope.dates[newValue].toJSON().split('T')[0],
            // status: 'saved'
          }
        }).
        then(function(response) {
          $scope.timeSheet = response.data;
          $scope.items = $scope.timeSheet.items;
          console.log('dddddddddddd',$scope.timeSheet);
          if ($scope.timeSheet.checkIn == null && $scope.timeSheet.checkOut == null) {
            $scope.btnTyp = ''
          }else {
            $scope.btnTyp = $scope.timeSheet
          }
        })

      } else {
        $scope.timeSheet = response.data[0];
        $scope.items = $scope.timeSheet.items;
        console.log('dddddddddddd',$scope.timeSheet);
        if ($scope.timeSheet.checkIn == null && $scope.timeSheet.checkOut == null) {
          $scope.btnTyp = ''
        }else {
          $scope.btnTyp = $scope.timeSheet
        }
      }

    })


  })


  $scope.save = function() {

    for (var i = 0; i < $scope.items.length; i++) {
      var url = '/api/performance/timeSheetItem/'
      var method = 'POST';
      if ($scope.items[i].pk != undefined) {
        url += $scope.items[i].pk + '/'
        method = 'PATCH';
      }

      console.log('aaaaaaaaa', $scope.items[i].project.pk);



      var toSend = {
        project: $scope.items[i].project.pk,
        duration: $scope.items[i].duration,
        comment: $scope.items[i].comment,
        parent: $scope.timeSheet.pk,
      }
      console.log(toSend);

      $http({
        method: method,
        url: url,
        data: toSend
      }).
      then((function(i) {
        return function(response) {
          $scope.items[i].pk = response.data.pk;
          Flash.create('success', 'Saved');
        }
      })(i))

    }

  }
  $scope.Submit = function() {
    $http({
      method: 'PATCH',
      url: '/api/performance/timeSheet/' + $scope.timeSheet.pk + '/',
      data: {
        status: 'submitted'
      }
    }).
    then(function(response) {
      $scope.timeSheet = response.data;
      Flash.create('success', 'Submitted');
    })
  }



  //====================popup  calendar for employees

  $scope.openAttendance = function(){
    console.log('inside openAttendance functioin');
    $aside.open({
      templateUrl : '/static/ngTemplates/app.home.Attendance.html',
      placement: 'right',
      size: 'xl',
      backdrop : true,
      // resolve: {
      //   a : function() {
      //     return $scope.sai;
      //   },
      // },
      controller : 'ctrl.home.attendance.aside'
    })
 }


});

//==========================Attendance controller open ====================

app.controller('ctrl.home.attendance.aside', function($scope, $state, $users, $stateParams, $http, Flash, $timeout,$uibModal) {
  // $scope.baseUrl = '/api/PIM/home/myWork/';
  console.log('vbdhsfhbfhsbhfsbjfdbjfdbsjfd');
  $scope.me = $users.get('mySelf'); //hit api and get user who is logged in
  $scope.userform = {
    user: $scope.me
  }
  $scope.getUserAttendance = function() {
    //http get request to hit the api and fetch user data. we send user pk and date for which we need data.
    $http({
      method: 'GET',
      url: '/api/employees/fetchAttendance/?user=' + $scope.userform.user.pk + '&date=' + $scope.dateDisp.toJSON().split('T')[0],
    }).
    then(function(response) {
      // console.log(response.data,'resssssssssssss');
      $scope.values = response.data.valList
      $scope.timeList = response.data.timeList
      $scope.leavetype = response.data.leavetype
    })
    // console.log($scope.dateDisp, '7777777777777777');
    // console.log($scope.userform);
  }

  $scope.listOfDays = [{
    "val": 1,
    "disp": "Sunday"
  }, {
    "val": 1,
    "disp": "Monday"
  }, {
    "val": 1,
    "disp": "Tuesday"
  }, {
    "val": 1,
    "disp": "Wednesday"
  }, {
    "val": 1,
    "disp": "Thursday"
  },
  {
    "val": 1,
    "disp": "Friday"
  }, {
    "val": 1,
    "disp": "Saturday"
  }
];

var calDate = new Date(); // the current date value known to the calendar, also the selected. For a random month its 1st day of that month.
var calMonth = calDate.getMonth(); // in MM format
var calYear = calDate.getFullYear(); // in YYYY format

$scope.itemInView = [];
datesMap = getDays(calMonth, calYear);
$scope.dates = datesMap.days;
$scope.dateFlags = datesMap.flags;
$scope.dateDisp = calDate;
$scope.dayDisp = $scope.listOfDays[calDate.getDay()].disp; // Find equivalent day name from the index
$scope.getUserAttendance()


$scope.gotoToday = function() {
  var calDate = new Date(); // current day
  calMonth = calDate.getMonth();
  calYear = calDate.getFullYear();
  $scope.dateDisp = calDate;
  $scope.dayDisp = $scope.listOfDays[calDate.getDay()].disp;
  datesMap = getDays(calMonth, calYear);
  $scope.dates = datesMap.days;
  $scope.dateFlags = datesMap.flags;
  $scope.getUserAttendance()
};
$scope.gotoNext = function() {
  calMonth += 1;
  calDate.setFullYear(calYear, calMonth, 1);
  datesMap = getDays(calMonth, calYear);
  $scope.dates = datesMap.days;
  $scope.dateFlags = datesMap.flags;
  $scope.dateDisp = calDate;
  $scope.dayDisp = $scope.listOfDays[calDate.getDay()].disp;
  $scope.getUserAttendance()
};
$scope.gotoPrev = function() {
  calMonth -= 1;
  calDate.setFullYear(calYear, calMonth, 1);
  datesMap = getDays(calMonth, calYear);
  $scope.dates = datesMap.days;
  $scope.dateFlags = datesMap.flags;
  $scope.dateDisp = calDate;
  $scope.dayDisp = $scope.listOfDays[calDate.getDay()].disp;
  $scope.getUserAttendance()
};

$scope.range = function(min, max, step) {
  step = step || 1;
  var input = [];
  for (var i = min; i <= max; i += step) input.push(i);
  return input;
};
$scope.userSearch = function(query) {
  //search for the user
  return $http.get('/api/HR/userSearch/?username__contains=' + query).
  then(function(response) {
    return response.data;
  })
};


$scope.getval = function(typ, dt) {
  if ($scope.values!=undefined) {
    if (typ == 'Cur') {
      if ($scope.values[dt - 1] >= 8) {
        return '#cff6c9'
        //for worked more then 8hrs
      } else if ($scope.values[dt - 1] > 0 && $scope.values[dt - 1] < 8) {
        return '#f7decd'
        //for absent
      } else if ($scope.values[dt - 1] == 0) {
        return '#d7e8f7'
        //for loggedin  or loggedout once
      }else if ($scope.values[dt - 1] == -2) {
        return '#dbdbdb'
        //for the leave request
      }
    } else {
      return ''
    }
  }
}

});


//============================================Attendance controller close ==============================
