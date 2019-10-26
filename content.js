

function storeVal() {
	console.log(2);
	var name = document.getElementById("bylineInfo").text;
	console.log(name)
	chrome.storage.local.set({"company": name }, function() {
	          console.log('company is set to ' + name);
	        });



}

console.log("1");


document.addEventListener('DOMContentLoaded', function() {
	console.log("2");
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