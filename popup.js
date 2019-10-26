function dumpRatings(query) {
//insert mechanism for retrieving a products rating
  $('#product').append("retrieved_prduct");
  $('#rating').append("5");
}

document.addEventListener('DOMContentLoaded', function () {
  dumpRatings();
});

alert(chrome.storage.local.get(['company'], function(result) {
          console.log('Value currently is ' + result.key);
        }));


