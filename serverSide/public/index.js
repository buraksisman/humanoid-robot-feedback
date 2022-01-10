const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('sum', {numbers:[1,2]})
});


sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on("sum_result", (data) => {
  console.log(data);
});

sio.on("feedback", (data) =>{
  console.log(data);
});

sio.on("feedbackResponse", (data) =>{
  console.log(data);
});

sio.on("feedbackResponseApp", (data) =>{
  console.log(data);
  console.log(data.responseFromRobot);
  var messageArray = new Uint8Array(data.responseFromRobot);
var string = new TextDecoder().decode(messageArray);
  $("#responsefromrobot").html(string);
});

function joinRoom(){
  sio.join('ut');
  sio.to('ut').emit('comment','ben geldim');
}

function requestFeedback(val){
  var response = ""
  if (val == 1)
    response = "Did you miss any concept?";
  else if(val == 2)
    response = "Is there a relationship between ...?";
  else if(val == 3)
    response = "Is X important in this elation?";
  
    sio.emit('receiveFeedback', {feedbackid:1, feedback:"" + response})
}
