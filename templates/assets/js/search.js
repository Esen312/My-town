document.addEventListener('DOMContentLoaded', function () {
    var searchContainer = document.querySelector('.search-container');
    var searchForm = document.querySelector('.search');

    searchContainer.addEventListener('click', function (event) {
        // Проверяем, был ли клик по иконке лупы
        if (event.target.classList.contains('fa-search')) {
            // Переключаем класс для отображения/скрытия формы поиска
            searchForm.classList.toggle('search-active');
        }
    });

    // Добавляем обработчик события для закрытия формы поиска при клике вне неё
    document.addEventListener('click', function (event) {
        if (!searchContainer.contains(event.target) && !searchForm.contains(event.target)) {
            searchForm.classList.remove('search-active');
        }
    });
});