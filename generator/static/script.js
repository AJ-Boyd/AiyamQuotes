
// limits the number of adjectives being selected to 3
function limitAdj() {
    const checkboxes = document.querySelectorAll('input[name="adjective"]:checked');
    
    if (checkboxes.length > 3) {
        event.preventDefault(); 
        return false;
    }
  }