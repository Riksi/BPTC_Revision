//When you mark an area as complete, JS sends this to the server
//Endpoint indicates whether topic is closed and also indicates progress level
//If closed, then collapse that section of the list
//Need EL to listen for click 
//Need function to send AJAX request
//Need function to collapse topic

//Function to show/hide answer

//Have generic show/hide function and create classes for each element to modify //appearance


//Also need to get the "progress" value from the server


/*var topics = document.getElementsByClassName('area-checkbox');

for(var i = 0; i < topics.length; i++){
	topics[i].addEventListener('click',markCompleted);
}

function markCompleted(e){
	var tar = e.target;
	if(tar.className == 'area-checkbox'){
		console.log(this);
	updateCompleted(tar.checked,tar.id,this.id);
}
}

function updateCompleted(checked,areaId,topicId){
	document.getElementById(topicId).click();
}*/



//If 






var above = document.getElementsByClassName('above');

for(var i = 0; i < above.length; i ++){
		above[i].addEventListener('click',showOrHide);
	}


var header = document.getElementsByTagName('header')[0];
var footer = document.getElementsByTagName('footer')[0];
var questions = document.getElementsByClassName('questions')[0];

document.getElementById('show-modules').addEventListener('click', function(){
	showMenu(false)
})

var elems = [header,footer,questions]
elems.forEach(function(el){
	el.addEventListener('click',function(){
	showMenu(true);
	
})
});



function showMenu(condition) {
	event.stopPropagation();
	var menu = document.getElementsByClassName('module-tabs')[0];
	console.log(menu.classList.contains('shown'));
	if(menu.classList.contains('shown')==condition){
		menu.classList.toggle('shown');
		
	}
}





document.addEventListener('click',function(){})

function showOrHide(){
		var id = getBelowId(this,'show');
		console.log(id);
		document.getElementById(id).classList.toggle('hidden');
		this.classList.toggle('below-hidden');
	};


function getBelowId(elem,prefix){	
	var classes = elem.classList;
	var numClasses = classes.length;
	for(var i = 0; i < numClasses; i++){
		var cl = classes[i];
		if(cl.startsWith(prefix)){//fix the find bit
			return cl.slice(prefix.length+1) //+1 to accommodate the '-'
		}
	}
}


document.getElementsByClassName('modules')[0].addEventListener('click', function(e){
	var clicked = e.target;
	console.log(clicked.tagName)
	if(clicked.tagName == 'INPUT'){
        someText = new XMLHttpRequest();
        someText.onreadystatechange = callBack;
        var url = clicked.id
        someText.open("GET", url, true);
        someText.send();
    }
})

function callBack(){
    if(someText.readyState==4 && someText.status==200){
       var module_data = JSON.parse(someText.responseText);
       console.log(module_data);
       if(module_data['module_completed']){
       		document.getElementById(module_data['module_id']).click();
       }
    }
};



function changeColour(el){
	el.classList.toggle('flag-hover');
}


	/*document.addEventListener('click',
		function(e){
			console.log(e.target.parentNode);
			if(e.target.className == 'flag'){
				console.log('clicked');
			postFunction(e.target);
		};
		})*/
	
	


	function postFunction(el) {
		  var xhttp = new XMLHttpRequest();
		  xhttp.onreadystatechange = function() {
		    if (xhttp.readyState == 4 && xhttp.status == 200) {
		      console.log(xhttp.responseText);
		      changeFlagClass(el.id);
		    }
		  };
		  xhttp.open("POST", '/testpost', true);
		  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		  var csrf = 'csrfmiddlewaretoken='+ document.getElementById('csrf').value;
		  var flagged = 'flagged=' + (el.className == 'flag'); 
		  el.classList.toggle('flag');
		  el.classList.toggle('unflag');
		  var question_id = 'question_id=' + el.id;
		  var user_id = 'user_id=' + document.getElementById('user_id').value;
		  xhttp.send([csrf,question_id,user_id,flagged].join('&'));
		}


var flagButton = document.getElementById('show-flagged');
if( flagButton){
document.getElementById('show-flagged').addEventListener('click',toggleFlagged)
}

function changeFlagClass(qid){
	document.getElementById('question-'+qid).classList.toggle('flagged');
}

function toggleFlagged(){
	this.classList.toggle('below-hidden');
	document.getElementById('question-list').classList.toggle('flagged-only');
}



/*var questions = document.getElementsByClassName('question-list-item');
var qn = document.getElementsByClassName('qn')
if(questions.length){

	var before = document.getElementById('previous');
	var after = document.getElementById('next');
	var present_position = 0;

	for(var i = 0; i < Math.min(questions.length,5); i++){
		questions[i].style.display = 'block';
		qn[i].innerHTML = i+1;
	};


if(questions.length > 5){after.style.display = 'block';}


	function showQuestions(move){
		var new_position = present_position + move*5;
		if (new_position+5 < questions.length && new_position > 0){
			after.style.display = 'block';
			before.style.display = 'block';
		}
		if (new_position+5 >= questions.length){
			after.style.display = 'none';
			before.style.display = 'block';
		}
		if (new_position == 0){
			before.style.display = 'none';
			if(questions.length > 5){after.style.display = 'block';}
		}



		if(move == -1){
			for(var i = present_position; i < Math.min(present_position+5,questions.length); i++){
				questions[i].style.display = 'none';
				qn[i].style.display = 'none';
			};

			for(var i = new_position; i <new_position+5; i++){
				questions[i].style.display = 'block';
				qn[i].style.display = 'inline';
				qn[i].innerHTML = i+1;
			};
		
		}
		if(move == 1){

			for(var i = present_position; i < present_position+5; i++){
					questions[i].style.display = 'none';
					qn[i].style.display = 'none';
			};

			for(var i = new_position; i < Math.min(new_position+5,questions.length); i++){
					questions[i].style.display = 'block';
					qn[i].style.display = 'inline';
					qn[i].innerHTML = i+1;
				};
		}


		present_position = new_position;

	}


var nextQ = function(){
	console.log('nextQ')
		showQuestions(1)
	}

var prevQ = function(){
	console.log('prevQ')
	showQuestions(-1)
}
	before.addEventListener('click', prevQ)

	after.addEventListener('click', nextQ)
}*/