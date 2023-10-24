document.getElementById("searchBox").addEventListener("input", function() {
    let filter = this.value.toLowerCase();
    let persons = document.querySelectorAll("#missingPersonsList li");

    persons.forEach(function(person) {
        let name = person.getAttribute("data-name").toLowerCase();
        if (name.includes(filter)) {
            person.style.display = "";
        } else {
            person.style.display = "none";
        }
    });
});

document.getElementById("submitForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let fullName = document.getElementById("fullName").value;
    let missingSince = document.getElementById("missingSince").value;
    let details = document.getElementById("details").value;

    if (!fullName || !missingSince || !details) {
        document.getElementById("errorMsg").innerText = "Please fill in all the required fields.";
        return;
    }

    // If everything is valid, you can proceed to send the data to your server or handle it accordingly.
    // For now, we'll just alert a success message.
    alert("Information submitted successfully!");
    this.reset();
});

