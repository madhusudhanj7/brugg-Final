app.config(function($stateProvider ){

  $stateProvider
  .state('home', {
    url: "/home",
    views: {
      "": {
        templateUrl: '/static/ngTemplates/home.html',
        controller:'controller.home.main'
      },
      "@home": {
        templateUrl: '/static/ngTemplates/app.home.dashboard.html',
        controller : 'controller.home'
      }
    }
  })

  .state('home.manageUsers', {
    url: "/manageUsers",
    templateUrl: '/static/ngTemplates/app.HR.manage.users.html',
    controller: 'admin.manageUsers'
  })

  .state('home.mail', {
    url: "/mail",
    templateUrl: '/static/ngTemplates/app.mail.html',
    controller: 'controller.mail'
  })
  .state('home.social', {
    url: "/social/:id",
    templateUrl: '/static/ngTemplates/app.social.html',
    controller: 'controller.social'
  })
  .state('home.blog', {
    url: "/blog/:id?action",
    templateUrl: '/static/ngTemplates/app.home.blog.html',
    controller: 'controller.home.blog'
  })
  .state('home.calendar', {
    url: "/calendar",
    templateUrl: '/static/ngTemplates/app.home.calendar.html',
    controller: 'controller.home.calendar'
  })
  .state('home.notes', {
    url: "/notes",
    templateUrl: '/static/ngTemplates/app.home.notes.html',
    controller: 'controller.home.notes'
  })
  .state('home.profile', {
    url: "/profile",
    templateUrl: '/static/ngTemplates/app.home.profile.html',
    controller: 'controller.home.profile'
  })
  .state('home.myWork', {
    url: "/myWork",
    templateUrl: '/static/ngTemplates/app.home.myWork.html',
    controller: 'controller.home.myWork'
  })
  .state('home.products', {
    url: "/products",
    templateUrl: '/static/ngTemplates/app.home.products.html',
    controller: 'controller.home.products'
  })
  .state('home.pdf', {
    url: "/pdf",
    templateUrl: '/static/ngTemplates/app.home.pdf.html',
    controller: 'controller.home.pdf'
  })
  .state('home.careers', {
    url: "/careers",
    templateUrl: '/static/ngTemplates/app.homepage.careersForm.html',
    controller: 'controller.home.careers'
  })
  .state('home.apptips', {
    url: "/apptips",
    templateUrl: '/static/ngTemplates/app.home.apptips.html',
    controller: 'controller.home.apptips'
  })
  .state('home.accessories', {
    url: "/accessories",
    templateUrl: '/static/ngTemplates/app.home.accessories.html',
    controller: 'controller.home.accessories'
  })
  .state('home.album', {
    url: "/album",
    templateUrl: '/static/ngTemplates/app.home.album.html',
    controller: 'controller.home.album'
  })
  .state('home.locations', {
    url: "/locations",
    templateUrl: '/static/ngTemplates/app.home.locations.html',
    controller: 'controller.home.locations'
  })

});

app.controller("controller.home.main", function($scope , $state) {
  $scope.modules = $scope.$parent.$parent.modules;
  $scope.dashboardAccess = false;
  $scope.homeMenuAccess = false;
  for (var i = 0; i < $scope.modules.length; i++) {
    if ($scope.modules[i].name == 'home'){
      $scope.dashboardAccess = true;
    }
    if ($scope.modules[i].name.indexOf('home') != -1) {
      $scope.homeMenuAccess = true;
    }
  }
})


app.controller('controller.home.menu' , function($scope ,$state, $http, $permissions){
  $scope.apps = [];

  $scope.buildMenu = function(apps){
    for (var i = 0; i < apps.length; i++) {
      a = apps[i];
      if (a.module != 1) {
        continue;
      }

      parts = a.name.split('.');
      a.dispName = parts[parts.length-1];

      if (a.name == 'app.dashboard') {
        a.state = 'home';
      }else {
        a.state = a.name.replace('app' , 'home');
      }
      $scope.apps.push(a);
    }
  }

  as = $permissions.apps();
  if(typeof as.success == 'undefined'){
    $scope.buildMenu(as);
  } else {
    as.success(function(response){
      $scope.buildMenu(response);
    });
  };

})
