/*var topics = [
{name: 'Topic 1', completed: 0.8},
{name: 'Topic 2', completed: 0.7},
{name: 'Topic 3', completed: 0.3},
{name: 'Topic 4', completed: 0.1},
{name: 'Topic 5', completed: 0.07}
]*/


	var someText;
    function helloWorld(){
        someText = new XMLHttpRequest();
        someText.onreadystatechange = callBack;
        var url = document.getElementById('url').innerHTML;
        someText.open("GET", url, true);
        someText.send();
    };

    // When information comes back from the server.
    function callBack(){
        if(someText.readyState==4 && someText.status==200){
           var data = JSON.parse(someText.responseText);
           //var topics = data['user_progress_data'];
           //console.log(topics);
           var mgr = new progressManager(data);
		   mgr.init();
        }
    };

    window.onload = helloWorld();

function progressManager(data){
	this.topics = data['user_progress_data'];
	this.overall = {"name": 'Overall', "progress": 0, 'test_url': data['root_url']}; //calling it 'module__name' just for now
	this.view = new progressView();
}

progressManager.prototype.getTopics = function(){
	//this.topics = topics;
	this.overall["progress"] = this.topics.reduce(function(a,b){
		return a + b["progress"] 
		console.log(b);
	},0)/this.topics.length;
	console.log(this.overall["progress"]);
};

progressManager.prototype.markProgress = function(){
	this.view.render(this.overall);
	mgr = this;
	this.topics.forEach(function(topic){
		/*var words = topic["section__module__name"].split(' ')
		if(words.length > 5){
			topic["section__module__name"] = words.slice(0,3).reduce(function(a,b){
						a+=(' '+b);
						return a;
			})
			console.log('called')
		}*/
		mgr.view.render(topic)
	});
}
progressManager.prototype.init = function(){
	this.getTopics();
	this.markProgress();
}

function progressView(){
	this.outer = document.getElementById('progress-container');
}

progressView.prototype.render = function(topic){
	var rowDiv = document.createElement('div');
	rowDiv.className = 'row';
	
	var nameDiv = document.createElement('div');
	num = topic["section__module__module_no"]; //'Overall' has no module no field
	nameDiv.innerHTML = (num? num + '. ' +topic["section__module__name"]: topic["name"] )
	nameDiv.className = 'topic-name col-4 col-m-4';
	
	var progressOuter = document.createElement('div');
	progressOuter.className = 'progress-bar-outer col-7 col-m-7';

	var progressRow = document.createElement('div');
	progressRow.className = 'progress-bar-container row'

	var progressInner = document.createElement('div');
	progressInner.className = 'progress-bar-inner';
	
	var progressDiv = document.createElement('div');
	progressDiv.className = 'topic-progress-bar';
	progressDiv.style.width = String(topic["progress"]*100) + '%';

	var percentDiv = document.createElement('div');
	percentDiv.className = 'percent'
	percentDiv.innerHTML = Math.floor(topic["progress"]*100) + '%' 

	var testLink = document.createElement('a');
	testLink.href = topic['test_url'];

	var testButton = document.createElement('button');
	testButton.innerHTML = 'Test';
	testButton.className = 'test-button'

	testLink.appendChild(testButton);

	progressInner.appendChild(progressDiv);
	progressRow.appendChild(progressInner);
	progressRow.appendChild(percentDiv);
	progressOuter.appendChild(progressRow)
	
	rowDiv.appendChild(nameDiv);
	rowDiv.appendChild(progressOuter);
	rowDiv.appendChild(testLink);
	
	this.outer.appendChild(rowDiv);
}


function makeElem(elem,attributes){
	var el = document.createElement(elem);
	for(attr in attributes){
		if(typeof(attributes[attr]) == 'object'){
			for(val in attributes[attr]){
				el[attr][val] = attributes[attr][val];
			};
		}
		else{
			el[attr] = attributes[attr];
		};
	};
  return el;
}

