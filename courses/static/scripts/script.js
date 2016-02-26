var menuButtons = document.getElementsByClassName('menu-button');

for(var i = 0; i < menuButtons.length; i ++){

menuButtons[i].onclick = function(){
	if(! event.target.classList.contains('arrow-below')){
		var hidden = document.getElementsByClassName('user-menu-elem');
		for(var i = 0; i < hidden.length; i++){
			hidden[i].classList.toggle('hidden');
		};
	}
};



}

/*var b = Math.min(window.innerHeight,document.getElementsByTagName('body')[0].offsetHeight);
document.getElementsByClassName('container')[0].style.height = b;
var m = document.getElementsByTagName('main')[0].offsetHeight;
var h = document.getElementsByTagName('header')[0].offsetHeight;
var f = document.getElementsByTagName('footer')[0].offsetHeight;
document.getElementsByTagName('footer')[0].style.margin = b-(m+f+h) + "px 0px 0px 0px";*/


