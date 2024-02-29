function toggleSubtopicStatus(id) {
    var item = document.getElementById("subtopic-" + id);
    var checkbox = item.getElementsByTagName("input")[0];
    if (checkbox.checked) {
        // Apply the color change to the entire item, affecting all contained text
        item.style.color = "green";
    } else {
        // Revert the color change for the entire item
        item.style.color = "";
    }
}