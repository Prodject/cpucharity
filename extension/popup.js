document.addEventListener('DOMContentLoaded', function(){

    var toggle = document.getElementById('toggle-miner');
    var userinput = document.getElementById('username');
    var submitButton = document.getElementById('submit-button');
    // set the initial state of the checkbox
    chrome.storage.sync.get("toggle_miner", function(data){
        if (data["toggle_miner"]){
            toggle.checked = true;
        } else {
            toggle.checked = false;
        }
      });

    toggle.addEventListener("change", function(){
        chrome.storage.sync.set({"toggle_miner": toggle.checked});
    });
    submitButton.addEventListener("submit", function(){
        chrome.storage.sync.set({"username": userinput.value});
    });

});
