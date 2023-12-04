$(document).ready(function() {
    var slider = $('.slider');
    var sliderItems = $('.slider-item');
    var totalSlides = sliderItems.length;
    var currentSlide = 0;

    function updateSlider() {
      var translateValue = -currentSlide * (100 / 4) + '%';
      slider.css('transform', 'translateX(' + translateValue + ')');
      sliderItems.removeClass('active');
      sliderItems.slice(currentSlide, currentSlide + 4).addClass('active');
    }

    function nextSlide() {
      if (currentSlide < totalSlides - 4) {
        currentSlide++;
      } else {
        currentSlide = 0; // Перейти к первому слайду после последнего
      }
      updateSlider();
    }

    function prevSlide() {
      if (currentSlide > 0) {
        currentSlide--;
      } else {
        currentSlide = totalSlides - 4; // Перейти к последнему слайду перед первым
      }
      updateSlider();
    }

    // Добавление автоматического переключения каждые 3 секунды
    var autoSlideInterval = setInterval(nextSlide, 5000);

    // Приостановка автоматического переключения при наведении курсора на слайдер
    slider.hover(
      function() {
        clearInterval(autoSlideInterval);
      },
      function() {
        autoSlideInterval = setInterval(nextSlide, 5000);
      }
    );

    $('.next-btn').click(function() {
      nextSlide();
    });

    $('.prev-btn').click(function() {
      prevSlide();
    });
  });