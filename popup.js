




//var companyRatings = chrome.storage.local.get(['ratings'], function(result) {
	//console.log("success");
//})
console.log("4");
document.addEventListener('DOMContentLoaded', function () {
	console.log("4");
	$('#product').append("jif");
  	$('#rating').append("5");
  	console.log("5");
  	alert(chrome.storage.local.get(["company"], function(result) {
  		console.log("6");
  		alert(result.key);
        }));

});



