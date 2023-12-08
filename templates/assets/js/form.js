function resetFilter() {
      // Сбросить значения фильтра и отправить форму
      document.querySelectorAll('.filter-form form input, .filter-form form select').forEach((input) => {
        input.value = '';
      });
      document.querySelector('.filter-form form').submit();
    }