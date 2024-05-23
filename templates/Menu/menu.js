function highlightItem(element) {
    element.style.transform = "scale(1.05)";
    element.style.boxShadow = "0 4px 8px rgba(0,0,0,0.2)";
}

function unhighlightItem(element) {
    element.style.transform = "scale(1)";
    element.style.boxShadow = "none";
}

function filterMenu() {
    var input = document.getElementById("searchBox");
    var filter = input.value.toUpperCase();
    var menu = document.getElementById("Menu");
    var boxes = menu.getElementsByClassName("box");
    for (var i = 0; i < boxes.length; i++) {
        var dishName = boxes[i].getElementsByClassName("dish-name")[0];
        if (dishName.innerHTML.toUpperCase().indexOf(filter) > -1) {
            boxes[i].style.display = "";
        } else {
            boxes[i].style.display = "none";
        }
    }
}
