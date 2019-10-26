


/* storage func 
chrome.storage.local.set({key: value}, function() {
          console.log('Value is set to ' + value);
        });


*/
function storeVal() {
	var name = document.getElementById("bylineInfo").text;
	chrome.storage.local.set({"company": name }, function() {
	          console.log('company is set to ' + name);
	        });


	alert(chrome.storage.local.get(['company'], function(result) {
	          console.log('Value currently is ' + result.key);
	        }));

}


document.addEventListener('DOMContentLoaded', function () {
  storeVal();
});

/* 


Manifest storage 
 "permissions": [
          "storage"
        ],

Manifest content.js

 "content_scripts": [
    {
      "matches": ["http://*.nytimes.com/*"],
     
      "js": ["contentScript.js"]
    }
  ],


  */