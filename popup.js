alert("popup.js is running");
var supplier = "not yet found";
console.log("console log works");

//sets up a promise so that it will assign the values and then afterwards we can call assignments
const setCompany =  () => {
	chrome.storage.local.get('company', (result) => {
		alert("callback is running");
		supplier = result.company;
		$('#product').append(supplier); 	

});//end of promise callback function
};//end of the setComp declaration

const setScore =  () => {
	chrome.storage.local.get('ratings', (result) => {
		alert("SetScore running");
		score = result.ratings[supplier];
	  	$('#rating').append(score);  	

});//end of promise callback function
};//end of the setComp declaration



setCompany();
setScore();

 	 
 

 





/*
'use strict';

let changeColor = document.getElementById('changeColor');

chrome.storage.sync.get('color', function(data) {
  changeColor.style.backgroundColor = data.color;
  changeColor.setAttribute('value', data.color);
});

changeColor.onclick = function(element) {
  let color = element.target.value;
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(
        tabs[0].id,
        {code: 'document.body.style.backgroundColor = "' + color + '";'});
  });
};
*/



