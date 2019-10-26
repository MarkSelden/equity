function dumpRatings(query) {
//insert mechanism for retrieving a products rating
	console.log("4")

  $('#product').append(companyName);
  $('#rating').append(companyRatings[companyName]);
}

var companyName = chrome.storage.local.get(['company'], function(result) {
          console.log('Value currently is ' + result.key);
        });
var companyRatings = chrome.storage.local.get(['ratings'], function(result) {
	console.log("success");
})

document.addEventListener('DOMContentLoaded', function () {
  dumpRatings();
});



