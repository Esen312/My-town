const dropdown = document.querySelector('.dropdown');

dropdown.addEventListener('click', () => {
    dropdown.classList.toggle('active');
});


document.addEventListener("DOMContentLoaded", function () {
    const searchIcon = document.getElementById("search-icon");
    const searchForm = document.querySelector(".search");

    searchIcon.addEventListener("click", function () {
        searchForm.classList.toggle("active");
        if (searchForm.classList.contains("active")) {
            searchIcon.innerHTML = '<i class="bx bx-x"></i>'; // Change to close icon
        } else {
            searchIcon.innerHTML = '<i class="bx bx-search"></i>'; // Change back to search icon
        }
    });
});