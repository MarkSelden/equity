//var ratings = require('./result.json');

//when installed it needs to load the dictionary that we will access into storage, only needs to load once since it will always be the same score. 
chrome.runtime.onInstalled.addListener(function() {
    const ratings = {"Garnier": 15};
	chrome.storage.local.set({"ratings": ratings},  function() {
	          console.log('ratings is set to ' + ratings);
	        });
  });





