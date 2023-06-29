function copyPassword(password) {
    var tempInput = document.createElement("input");
    tempInput.value = password;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);

    alert('Contrasenya copiada');
}

function filterWebpages() {
    var input = document.getElementById("web-input");
    var filter = input.value.toLowerCase();
    var table = document.getElementById("web-table");
    var rows = table.getElementsByTagName("tr");

    for (var i = 1; i < rows.length; i++) {
        var webColumn = rows[i].getElementsByTagName("td")[0];
        var webValue = webColumn.textContent || webColumn.innerText;
        if (webValue.toLowerCase().startsWith(filter)) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}
