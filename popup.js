var supplier = "not yet found";
var score = "not yet found";


//Injects both proper values into the html
const setVals =  referee => {

	//access company name, all the work happens in callback function
	chrome.storage.local.get('company', result => {

		//sets suplier 
		supplier = result.company;
		//injects into product element
		$('#product').append(supplier);
		//calls the helper function, to set the score(referee lol). Callback hell is neccessary for the referee function to have the proper company key
		referee(supplier);



	});//end of promise callback function

};//end of the setComp declaration


//Helper function for setting the ethics score 
const setScore =  key => {

	//gets the ratings dictionary, more work in callback
	chrome.storage.local.get('ratings', data => {

		if (key in data.ratings){//checks to make we have data on the company 

			//sets score equal to the key(passed in) in the dictionary in data
			score = data.ratings[key];
			//injects score into rating element in Html
		  	$('#rating').append(score);  	

		  	var num = Number(score);

		  	if (num <= 5){
		  		document.getElementById("rating").style.backgroundColor = "Red";
		  	}else if (num <= 10){
		  		document.getElementById("rating").style.backgroundColor = "Orange";
		  	}else {
		  		document.getElementById("rating").style.backgroundColor = "#99ff99";
		  	}
	  
		}else{

			$('#rating').append("Idk *Shrug*"); 
	
		}

		

	});//storage.get rating
};//end of the setScire declaration

setVals(setScore);

