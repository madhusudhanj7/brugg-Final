var connection = new autobahn.Connection({url: 'ws://'+ '192.168.0.12'+':8080/ws', realm: 'default'});

// "onopen" handler will fire when WAMP session has been established ..
connection.onopen = function (session) {

   console.log("session established!");

   // our event handler we will subscribe on our topic
   //
  function chatResonse (args) {
    console.log(args);
    var status = args[0];
    var msg = args[1];
    var friend = args[2];
    var scope = angular.element(document.getElementById('chatWindow'+friend)).scope();
    console.log(scope);
    if (typeof scope !='undefined' ) {
      scope.$apply(function() {
        if (status =="T" && !scope.$$childHead.isTyping) {
          scope.$$childHead.isTyping = true;
          setTimeout( function(){
            var scope = angular.element(document.getElementById('chatWindow'+friend)).scope();
            scope.$apply(function() {
              scope.$$childHead.isTyping = false;
            });
          }, 1500 );
        }else if (status=="M") {
          scope.$$childHead.addMessage(msg , args[3])
        }else if (status=="MF") {
          console.log('attach file');
          scope.$$childHead.addMessage(msg , args[3])
        };
      });
    } else {
      if (status == 'T') {
        return;
      };
      var scope = angular.element(document.getElementById('main')).scope();
      scope.$apply(function() {
        scope.fetchAddIMWindow(args[3] , friend);
      });
    };
  };

  processNotification = function(args){
    var scope = angular.element(document.getElementById('main')).scope();
    scope.$apply(function() {
      scope.fetchNotifications(args[0]);
    });
  };

  processUpdates = function(args){
    var scope = angular.element(document.getElementById('aside')).scope();
    if (typeof scope != 'undefined') {
      scope.$apply(function() {
        scope.refreshAside(args[0]);
      });
    }
  };

  processDashboardUpdates = function(args) {
    console.log(args);
    var scope = angular.element(document.getElementById('dashboard')).scope();
    console.log(scope);

    if (typeof scope != 'undefined') {
      scope.$apply(function() {
        scope.refreshDashboard(args[0]);
      });
    }
  };

  supportChatResponse = function(args) {
      var scope = angular.element(document.getElementById('chatTab')).scope();
      console.log(scope);
      console.log(args);

      function userExist() {
        for (var i = 0; i < scope.newUsers.length; i++) {
          if (scope.newUsers[i].uid == args[0] ) {
            console.log('yes');
            if (args[1]=='M') {
              scope.newUsers[i].messages.push( {msg : args[2].msg, sentByMe:false , created: args[2].created })
              return true
            }else if (args[1]=='MF') {
              if (args[2].img) {
                console.log('img');
                scope.newUsers[i].messages.push( {msg:"", img : args[2].img, sentByMe:false , created:  args[3] })
              }else if (args[2].audio) {
                console.log('audiio');
                scope.newUsers[i].messages.push( {msg:"", audio : args[2].audio, sentByMe:false , created:  args[3] })
              }else if (args[2].video) {
                console.log('video');
                scope.newUsers[i].messages.push( {msg:"", video : args[2].video, sentByMe:false , created:  args[3] })
              }else if (args[2].doc) {
                console.log('doc');
                scope.newUsers[i].messages.push( {msg:"", doc : args[2].doc, sentByMe:false , created:  args[3] })
              }
            }
            return true
          }
        }
        for (var i = 0; i < scope.myUsers.length; i++) {
          if (scope.myUsers[i].uid == args[0] ) {
            console.log('yes');
            if(args[1]=='M') {
              scope.myUsers[i].messages.push( {msg : args[2].msg, sentByMe:false , created:  args[2].created })
            }else if (args[1]=='MF') {
              if (args[2].img) {
                console.log('img');
                scope.myUsers[i].messages.push( {msg:"", img : args[2].img, sentByMe:false , created:  args[3] })
              }else if (args[2].audio) {
                console.log('audiio');
                scope.myUsers[i].messages.push( {msg:"", audio : args[2].audio, sentByMe:false , created:  args[3] })
              }else if (args[2].video) {
                console.log('video');
                scope.myUsers[i].messages.push( {msg:"", video : args[2].video, sentByMe:false , created:  args[3] })
              }else if (args[2].doc) {
                console.log('doc');
                scope.myUsers[i].messages.push( {msg:"", doc : args[2].doc, sentByMe:false , created:  args[3] })
              }
            }
            return true
          }
        }
      }

      if (userExist()) {
        console.log('yes');
        // var s =  angular.element(document.getElementById('chatBox'+ args[0])).scope();
        // console.log(s);
      }else {
        console.log('no');
        console.log(args);
        if(args[1]=='M') {
          console.log(args,'argssssssssss');
          scope.newUsers.push( {name : 'Ashish', uid: args[0],  messages : [{msg : args[2].msg, sentByMe:false , created:  args[2].created }], isOnline:true }  )
        }else if (args[1]=='MF') {
          if (args[2].img) {
            scope.newUsers.push( {name : 'Ashish', uid: args[0],  messages : [{msg:"", img : args[2].img, sentByMe:false , created:  args[3] }], isOnline:true }  )
          }else if (args[2].audio) {
            scope.newUsers.push( {name : 'Ashish', uid: args[0],  messages : [{msg:"", audio : args[2].audio, sentByMe:false , created:  args[3] }], isOnline:true }  )
          }else if (args[2].video) {
            scope.newUsers.push( {name : 'Ashish', uid: args[0],  messages : [{msg:"", video : args[2].video, sentByMe:false , created:  args[3] }], isOnline:true }  )
          }else if (args[2].doc) {
            scope.newUsers.push( {name : 'Ashish', uid: args[0],  messages : [{msg:"", doc : args[2].doc, sentByMe:false , created:  args[3] }], isOnline:true }  )
          }
          return true
        }
      }

      if (args[1]=='O') {
        var uid = args[0];
        var status = 'O';
        connection.session.publish('service.support.chat.' + uid, [ status ], {}, {
          acknowledge: true
        }).
        then(function(publication) {
          console.log("Published");
        });
      }

  };

  session.subscribe('service.support.agent', supportChatResponse).then(
    function (sub) {
      console.log("subscribed to topic 'supportChatResponse'");
    },
    function (err) {
      console.log("failed to subscribed: " + err);
    }
  );


  session.subscribe('service.chat.'+wampBindName, chatResonse).then(
    function (sub) {
      console.log("subscribed to topic 'chatResonse'");
    },
    function (err) {
      console.log("failed to subscribed: " + err);
    }
  );
  session.subscribe('service.notification.'+wampBindName, processNotification).then(
    function (sub) {
      console.log("subscribed to topic 'notification'");
    },
    function (err) {
      console.log("failed to subscribed: " + err);
    }
  );
  session.subscribe('service.updates.'+wampBindName, processUpdates).then(
    function (sub) {
      console.log("subscribed to topic 'updates'");
    },
    function (err) {
      console.log("failed to subscribed: " + err);
    }
  );
  session.subscribe('service.dashboard.'+wampBindName, processDashboardUpdates).then(
    // for the various dashboard updates
    function (sub) {
      console.log("subscribed to topic 'dashboard'");
    },
    function (err) {
      console.log("failed to subscribed: " + err);
    }
  );

};


  // fired when connection was lost (or could not be established)
  //
connection.onclose = function (reason, details) {
   console.log("Connection lost: " + reason);
}
connection.open();
