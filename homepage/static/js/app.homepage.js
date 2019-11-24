var app = angular.module('app', []);

app.config(function($httpProvider, $provide, $locationProvider) {

  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.withCredentials = true;
  $locationProvider.html5Mode(true);

});

app.controller('main', function($scope, $http, $timeout, $interval,$rootScope,$sce) {


  $scope.configs = [
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559800269_2__tsr.jpg' , productCode : 'TSR' , calculation : '125,000', caldeno: '18,129' , val1 : '0,124' , val2 : '0,50', min : 5 , max : 51,color:'rgb(84, 89, 96, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559224421_71__8x19_b-1.jpg' , productCode : '8X19' , calculation : '110,000', caldeno: '15,954' , val1 : '0,122' , val2 : '0,26', min : 5 , max : 61,color:'rgb(252, 252, 252, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559224338_29__dp9_b.jpg' , productCode : 'DP9' , calculation : '115,000', caldeno: '16,679' , val1 : '0,112' , val2 : '0,25', min : 40 , max : 72,color:'rgb(224, 217, 37, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559800269_2__tsr.jpg' , productCode : 'SC8' , calculation : '120,000', caldeno: '17,404' , val1 : '0,112' , val2 : '0,13', min : 50 , max : 80,color:'rgb(229, 184, 78, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559799874_01__scx9.jpg' , productCode : 'SCX9' , calculation : '120,000', caldeno: '17,404' , val1 : '0,112' , val2 : '0,16', min : 60 , max : 90,color:'rgb(152, 186, 211, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559224210_26__hrs_b.jpg' , productCode : 'HRS' , calculation : '125,000', caldeno: '18,129' , val1 : '0,104' , val2 : '0,13', min : 71 , max : 101,color:'rgb(81, 119, 165, 0.5)',url:''},
  ]

  $scope.doublepully = [
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559800269_2__tsr.jpg' , productCode : 'TSR' , calculation : '125,000', caldeno: '18,129' , val1 : '0,124' , val2 : '0,50', min : 5 , max : 31,color:'rgb(84, 89, 96, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559224421_71__8x19_b-1.jpg' , productCode : '8X19' , calculation : '110,000', caldeno: '15,954' , val1 : '0,122' , val2 : '0,26', min : 5 , max : 41,color:'rgb(252, 252, 252, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559799983_06__dp9.jpg' , productCode : 'DP9' , calculation : '115,000', caldeno: '16,679' , val1 : '0,112' , val2 : '0,25', min : 20 , max : 51,color:'rgb(224, 217, 37, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559800269_2__tsr.jpg' , productCode : 'SC8' , calculation : '120,000', caldeno: '17,404' , val1 : '0,112' , val2 : '0,13', min : 30 , max : 56,color:'rgb(229, 184, 78, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559799874_01__scx9.jpg' , productCode : 'SCX9' , calculation : '120,000', caldeno: '17,404' , val1 : '0,112' , val2 : '0,16', min : 40 , max : 61,color:'rgb(152, 186, 211, 0.5)',url:''},
    {image : 'https://brugg.cioc.in/media/homepage/images/productImage/1559224210_26__hrs_b.jpg' , productCode : 'HRS' , calculation : '125,000', caldeno: '18,129' , val1 : '0,104' , val2 : '0,13', min : 50 , max : 101,color:'rgb(81, 119, 165, 0.5)',url:''},
  ]

   $scope.pulleys={
     'pulley1':true,
     'pulley2':false
   }

  $scope.submitPulley=function(){
    console.log($scope.pulleys);
    if ($scope.pulleys == false){
      console.log("u ru pulley1");
    }
    else{
      console.log('pulley2');
    }

  }
  $scope.home = 'zoom';
  $scope.home1 = 'zoomout';
  $scope.submitSelect=function(pully){
    console.log($scope.sliderVal);
      $scope.pulleys = pully
      $scope.sliderVal = Number($scope.sliderVal)+1;
      console.log($scope.sliderVal);
      if($scope.pulleys  == true ){
        $scope.home = 'zoom';
        $scope.home1 = 'zoomout';
      }else{
        $scope.home = 'zoomout';
        $scope.home1 = 'zoom';
      }

  }
  $scope.sliderVal = 50;

  $scope.changeUrl = function(url){
    window.location.href= url
  }
  if (document.URL.split('/').slice(-1)[0]== 'rope-selection') {
    $http({method : 'GET' , url : '/api/homepage/productTemplate/'}).
    then(function(response) {
      $scope.productsData = response.data
      for (var i = 0; i < $scope.configs.length; i++) {
        for (var j = 0; j < $scope.productsData.length; j++) {
          if ($scope.configs[i].productCode.toLowerCase()==$scope.productsData[j].name.toLowerCase()) {
            $scope.configs[i].url = '/products/'+$scope.productsData[j].name+'_'+$scope.productsData[j].pk
          }
        }
      }
    })


      $scope.barLabelsCopy = ['TSR', '8x19', 'DP9', 'SC8', 'SCX9', 'HRS']
      $scope.barValCopy = [105, 101, 120, 115, 135, 138]
      $scope.barData = {labels:['TSR', '8x19', 'DP9', 'SC8', 'SCX9', 'HRS'],values:[105, 101, 120, 115, 135, 138]}

      $scope.bar2LabelsCopy = ['TSR', '8x19', 'DP9', 'SC8','SCX9', 'HRS']
      $scope.bar2ValCopy = [[0,10.65], [0,10.83], [0,11.60],[0,12.03],[0,0],[0,10]]
      $scope.bar2Data = {labels:['TSR', '8x19', 'DP9', 'SC8','SCX9', 'HRS'],values:[[0,10.65], [0,10.83], [0,11.60],[0,12.03],[0,0],[0,10]]}

      $scope.bar3LabelsCopy = ['TSR', '8x19', 'DP9', 'MCX9', 'SCX9', 'HRS']
      $scope.bar3ValCopy = [0.50, 0.26, 0.25, 0.30, 0.16, 0.125]
      $scope.bar3Data = {labels:['TSR', '8x19', 'DP9', 'SC8', 'SCX9', 'HRS'],values:[0.50, 0.26, 0.25, 0.30, 0.16, 0.125]}


    $scope.$watch('sliderVal', function(newValue, oldValue) {
      console.log($scope.pulleys,'hhhhhhh');
      var data=''
      if($scope.pulleys){
        data = $scope.configs
      }
      if(!$scope.pulleys){
        data = $scope.doublepully
      }
      $scope.dataPadding = (570-(newValue*5)) + 'px'
      for (var i = 0; i < $scope.barLabelsCopy.length; i++) {
        if (newValue>data[i].min && newValue<data[i].max) {
          $scope.barData.labels[i]=$scope.barLabelsCopy[i]
          $scope.barData.values[i]=$scope.barValCopy[i]

          $scope.bar2Data.labels[i]=$scope.bar2LabelsCopy[i]
          $scope.bar2Data.values[i]=$scope.bar2ValCopy[i]

          $scope.bar3Data.labels[i]=$scope.bar3LabelsCopy[i]
          $scope.bar3Data.values[i]=$scope.bar3ValCopy[i]
        }else {
          $scope.barData.labels[i]=''
          $scope.barData.values[i]=0

          $scope.bar2Data.labels[i]=''
          $scope.bar2Data.values[i]=[]

          $scope.bar3Data.labels[i]=''
          $scope.bar3Data.values[i]=0
        }
        myChart.update()
        // myChart2.update()
        myChart3.update()
        try {
          myChart2.clear()
        } catch (e) {

        }
        var ctx2 = document.getElementById('myChart2').getContext('2d');
        var myChart2 = new Chart(ctx2, {
          type: 'line',
          data: {
            labels: [0,0.13],
            datasets: [{
                data: $scope.bar2Data.values[0],
                label: $scope.bar2Data.labels[0],
                borderColor: "rgb(84, 89, 96, 1)",
                fill: false
              },{
                data: $scope.bar2Data.values[1],
                label: $scope.bar2Data.labels[1],
                borderColor: "rgb(252, 252, 252, 1)",
                fill: false
              }, {
                data: $scope.bar2Data.values[2],
                label: $scope.bar2Data.labels[2],
                borderColor: "rgb(224, 217, 37, 1)",
                fill: false
              }, {
                data: $scope.bar2Data.values[3],
                label: $scope.bar2Data.labels[3],
                borderColor: "rgb(229, 184, 78, 1)",
                fill: false
              }, {
                data: $scope.bar2Data.values[4],
                label: $scope.bar2Data.labels[4],
                borderColor: "rgb(152, 186, 211, 1)",
                fill: false
              }, {
                data: $scope.bar2Data.values[5],
                label: $scope.bar2Data.labels[5],
                borderColor: "rgb(81, 119, 165, 1)",
                fill: false
              }
            ]
          },
          options: {
            title: {
              display: true,
              text: 'Elastic elongation'
            },
            scales: {
              yAxes: [{
                  display: true,
                  ticks: {
                      beginAtZero: true,
                      max: 12
                  }
              }]
            }
          }
        })
      }
      // console.log($scope.bar3Data);
    })

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'horizontalBar',
      data: {
        labels: $scope.barData.labels,
        datasets: [{
          label: 'Minimum Breaking Load',
          data: $scope.barData.values,
          backgroundColor: [
            'rgb(84, 89, 96, 1)',
            'rgb(252, 252, 252, 1)',
            'rgb(224, 217, 37, 1)',
            'rgb(229, 184, 78, 1)',
            'rgb(152, 186, 211, 1)',
            'rgb(81, 119, 165, 1)'
          ],
          borderColor: [
            'rgba(84, 89, 96, 1)',
            'rgb(204, 206, 209,1)',
            'rgba(224, 217, 37, 1)',
            'rgba(229, 184, 78, 1)',
            'rgba(152, 186, 211, 1)',
            'rgba(81, 119, 165, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          xAxes: [{
            ticks: {
              beginAtZero: true
            },
          }],
          yAxes: [{
            gridLines: {
                color: "rgba(0, 0, 0, 0)",
            }
          }]
        },
      }
    });



    var ctx3 = document.getElementById('myChart3').getContext('2d');
    var myChart3 = new Chart(ctx3, {
      type: 'horizontalBar',
      data: {
        labels: $scope.bar3Data.labels,
        datasets: [{
          label: 'Permanent elongation',
          data: $scope.bar3Data.values,
          backgroundColor: [
            'rgb(84, 89, 96, 1)',
            'rgb(252, 252, 252, 1)',
            'rgb(224, 217, 37, 1)',
            'rgb(229, 184, 78, 1)',
            'rgb(152, 186, 211, 1)',
            'rgb(81, 119, 165, 1)'
          ],
          borderColor: [
            'rgba(84, 89, 96, 1)',
            'rgb(204, 206, 209,1)',
            'rgba(224, 217, 37, 1)',
            'rgba(229, 184, 78, 1)',
            'rgba(152, 186, 211, 1)',
            'rgba(81, 119, 165, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          xAxes: [{
            ticks: {
              beginAtZero: true
            },
          }],
          yAxes: [{
            gridLines: {
                color: "rgba(0, 0, 0, 0)",
            }
          }]
        },
      }
    });

  }


  $scope.test = "sdsad"

  $scope.hideheaderText = 'block'
  $scope.showBarSearch = 'none'
  $scope.stillShow = {val:false}
  $scope.imageDp =true

  $scope.showImage = function(){
    if ($scope.imageDp==true) {
      $scope.imageDp=false
    }
    else{
      $scope.imageDp=true
    }
  }
  $scope.showInput = function(){

    // $('.scroll-to-top').click()
    if ( window.screen.width>480) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    else {
      window.scrollTo({ top: 450, behavior: 'smooth' });
    }

    console.log('show searchhhh');
    $scope.hideheaderText = 'none'
    $scope.showBarSearch = 'block'
    // document.getElementById("searchInput").focus($scope.focusText());
    $timeout(function(){
      document.getElementById("searchInput").focus()
    },100)
  }

  $scope.blurText = function(event){
    if ($scope.stillShow.val) {
      $scope.showSearch = true
      $scope.querySearch=""
    }else {
      $scope.showBarSearch = 'none'
      $scope.hideheaderText = 'block'
      $scope.querySearch=""
    }
  }
  $scope.focusInput = function(){
      document.getElementById("searchInput").blur();
      $scope.showBarSearch = 'none'
      $scope.hideheaderText = 'block'
      $scope.querySearch=""
  }

  $scope.gotopage = function(product){
    console.log(product.url,'lllllllllllllllllllllllllllllllllllllllll');
    console.log(product,'kkk');
    $scope.showBarSearch = 'none'
    $scope.hideheaderText = 'block'
    $scope.querySearch = ""

    if (product.typ=='prodTemp') {
        window.location.href=product.url+product.name+"_"+product.pk
    }
    else if(product.typ=='accessories'){
      window.location.href=product.url+product.name+'/'
    }
    else if(product.typ=='blog'){
      window.location.href=product.url+product.name+'/'
    }
    else if(product.typ=='apptips'){
      window.location.href=product.url
    }
    else if(product.typ=='template'){
      window.location.href=product.url
    }
    else{
      window.location.href="/products/"+product.name+"-"+product.pk
    }

  }

  $scope.getQuery = function(){
    if ($scope.querySearch.length>0) {
      $http.get('/api/homepage/searchAll/?search='+ $scope.querySearch +'&limit='+5 ).
      then(function(response) {
        //  http://localhost:8000/media/homepage/images/productImage/1562588775_1__6x19_b.jpg
        var host = window.location.origin+'/media/'
        for (var i = 0; i < response.data.length; i++) {
          response.data[i].defaultImage = host + response.data[i].defaultImage
          console.log(response.data[i].defaultImage);
        }
        $scope.results = response.data
      })

    }
    else{
        $scope.results = []
    }
  }

  $rootScope.getCookie = function(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }


  $rootScope.setCookie = function(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }



  $scope.langOptions = [{
      flag: '/static/images/flags/USA-1.svg',
      code: 'en',
      lang: 'EN'
    },
    {
      flag: '/static/images/flags/Germany.svg',
      code: 'de',
      lang: 'DE'
    },
    {
      flag: '/static/images/flags/cn.png',
      code: 'zh',
      lang: 'CN'
    },
  ]

  $scope.data = {
    currentLang: $scope.langOptions[0]
  }

  $scope.changeLan = function(lang) {
    $scope.data.currentLang = lang;
    Cookies.set('lang', lang.code);
    location.reload();
  }

  if (Cookies.get('lang') != undefined) {
    for (var i = 0; i < $scope.langOptions.length; i++) {
      if ($scope.langOptions[i].code == Cookies.get('lang')) {
        $scope.data.currentLang = $scope.langOptions[i];
        break;
      }
    }
  }

  var cookieAccepted = $rootScope.getCookie("accepted");
  if (cookieAccepted != "") {
    cookieAccepted = JSON.parse(cookieAccepted)
    if (cookieAccepted.accepted) {
      $scope.show_cokie_agree = false;
    } else {
      $scope.show_cokie_agree = true;
    }
  } else {
    $scope.show_cokie_agree = true;
  }

  var visitorDetails = $rootScope.getCookie("visitorDetails");
  $rootScope.cookie = function(val) {
    $scope.show_cokie_agree = false;
    if (visitorDetails != "") {
      var uid = JSON.parse(visitorDetails).uid
      $rootScope.setCookie("accepted", JSON.stringify({
        'accepted': true,
        'uid': uid
      }), 365)
    }
  }

  $scope.changeLan = function(lang) {
    console.log('lang',lang);
    $scope.data.currentLang = lang;
    Cookies.set('lang', lang.code);
    location.reload();
  }

  if (Cookies.get('lang') != undefined) {
    for (var i = 0; i < $scope.langOptions.length; i++) {
      if ($scope.langOptions[i].code == Cookies.get('lang')) {
        $scope.data.currentLang = $scope.langOptions[i];
        break;
      }
    }
  }

  console.log('here');
  $scope.show = [false, false, false, false]
  $scope.keepshow = false;
  $scope.imagesList = ['static/images/about/sel1.jpg', '/static/images/about/sel2.jpg', '/static/images/about/sel3.jpg', '/static/images/about/sel4.jpg', '/static/images/about/sel5.jpg', '/static/images/about/sel6.jpg', '/static/images/about/sel7.jpg', '/static/images/about/sel8.jpg', '/static/images/about/sel9.jpg', '/static/images/about/sel10.jpg', '/static/images/about/sel11.jpg']
  $scope.showImage = function(value) {
     document.getElementById("SelImg").src = $scope.imagesList[value];
  }
  if (document.URL.split('/').slice(-1)[0]=='reference') {

    $scope.showImage(0)
  }




  var emptyFile = new File([""], "");
  $scope.resetForm = function(){
    $scope.form = {
      name: '',
      phone: '',
      email: '',
      cover_letter: '',
      cv_file: emptyFile
    }

  }
  $scope.loader = false
  $scope.resetForm()

  $scope.submit = function() {
    if ($scope.form.name =='') {
      $scope.error = "Add Your Name"
      return
    }
    if ($scope.form.email =='') {
      $scope.error = "Add Your Email"
      return
    }
    if ($scope.form.phone =='') {
      $scope.error = "Add Your Phone Number"
      return
    }
    if ($scope.form.cover_letter =='') {
      $scope.form.cover_letter = ' '
    }
    if ( typeof $scope.form.cv_file =='string' ) {
      $scope.error = "Add Resume of Proper Format"
      return
    }

    var cvfile = $('#cvfile')[0].files[0];
    if (cvfile.size ==0) {
      $scope.error = 'Please select your resume/CV'
      return;
    }

    var fd = new FormData();
    fd.append('name', $scope.form.name);
    fd.append('phone', $scope.form.phone);
    fd.append('email', $scope.form.email);
    fd.append('cover_letter', $scope.form.cover_letter);
    fd.append('cv_file', cvfile);

    console.log($scope.form.name, 'iiiiiii');
    $scope.loader = true
    $http({
      method: 'POST',
      url: 'api/homepage/emailSend/',
      data: fd,
      transformRequest: angular.identity,
      headers: {
        'Content-Type': undefined
      }
    }).then(function(response) {
      $scope.success = "Submitted Successfully!"
      $scope.loader = false
      $scope.resetForm()
      // $scope.careersmModals('newcareer')
      // $scope.cv_file = emptyFile;
      $scope.error = ""
      $timeout(function() {
          $scope.success = ""
      }, 2500);
    })


  }

});
