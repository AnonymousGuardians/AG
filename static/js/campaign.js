const arrows = document.querySelectorAll('button.slick-arrow');
    var arrowButtonCheck = true;
    arrows.forEach((arrow) => {
      arrow.addEventListener('click', function () {
        if (arrowButtonCheck) {
          arrowButtonCheck = false;
          clearInterval(slide);
          bannerWrap.style.transition = 'transform 0.5s';
          let arrowType = arrow.classList[1];
          if (arrowType == 'Pre') {
            count--;
            if (count == 0) {
              bannerWrap.style.transform = 'translate(-' + 1500 * count + 'px)';
              setTimeout(function () {
                bannerWrap.style.transition = 'transform 0s';
                bannerWrap.style.transform = 'translate(-12000px)';
              }, 500);
              count = 8;
            } else {
              bannerWrap.style.transform = 'translate(-' + 1500 * count + 'px)';
            }
          } else {
            count++;
            if (count == 9) {
              bannerWrap.style.transform = 'translate(-' + 1500 * count + 'px)';
              setTimeout(function () {
                bannerWrap.style.transition = 'transform 0s';
                bannerWrap.style.transform = 'translate(-1500px)';
              }, 500);
              count = 1;
            } else {
              bannerWrap.style.transform = 'translate(-' + 1500 * count + 'px)';
            }
          }
          // temp.style.backgroundColor = "#f0f0f0";
          // temp = buttons[count];
          // buttons[count].style.backgroundColor = "black";
          swiperCurrent.innerHTML = `${count}`;
          slide = setInterval(autoSlide, 5000);
          setTimeout(function () {
            arrowButtonCheck = true;
          }, 500);
        }
      });
    });