function filterMenu() {
    var input, filter, menuRows, boxes, dishName, i, j, txtValue;
    input = document.getElementById('searchBox');
    filter = input.value.toLowerCase();
    menuRows = document.getElementsByClassName("menu_row");

    for (j = 0; j < menuRows.length; j++) {
        boxes = menuRows[j].getElementsByClassName('box');
        for (i = 0; i < boxes.length; i++) {
            dishName = boxes[i].getElementsByClassName("dish-name")[0];
            txtValue = dishName.textContent || dishName.innerText;
            if (txtValue.toLowerCase().indexOf(filter) > -1) {
                boxes[i].style.display = "";
            } else {
                boxes[i].style.display = "none";
            }
        }
    }
}
