var AddThisJSLoaded = false; 
var clickedOnShare = false; 


var AddThisPubID = "ra-6178751abfc8c78b";  //  profile id(SD)
var AddThisJS =
  "//s7.addthis.com/js/300/addthis_widget.js#pubid=" + AddThisPubID;

function share(button) {
  if (navigator.share) {
    //check if Web Share API is supported by the browser or not
    var url = document.location.href;
    var title = document.getElementsByTagName("title")[0].innerHTML;
    var description = document
      .querySelector("meta[name=description]")
      .getAttribute("content");

    navigator.share({
      title: title,
      text: description,
      url: url
    });
  } else {
    if (!AddThisJSLoaded && !clickedOnShare) {
      //when AddThis not loaded and share button isn't clicked
      clickedOnShare = true; 
      showLoading(button);
      shareByAddThis(button);
    } else {
      toggleAddThisButtons(button);
    }
  }
}

function shareByAddThis(button) {
  var script = document.createElement("script");
  script.async = true;
  script.src = AddThisJS;

  script.onload = function() {
    clickedOnShare = false; 
    addthis.user.ready(function(data) {
      AddThisJSLoaded = true; 
      hideLoading(button);
      showAddThisButtons(button);
    });
  };

  script.onerror = function() {
    clickedOnShare = false; 
    hideLoading(button);
  };

  document.body.appendChild(script);
}

function showLoading(button) {
  button.classList.add("loading");
}

function hideLoading(button) {
  button.classList.remove("loading");
}

function showAddThisButtons(button) {
  button.classList.add("showAddThisButtons");
}

function toggleAddThisButtons(button) {
  button.classList.toggle("showAddThisButtons");
}
