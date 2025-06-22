<script src="{% static 'js/swiper.min.js' %}"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    new Swiper(".homeslider .swiper-container", {
      loop: true,
      effect: "fade",
      autoplay: {
        delay: 5000,  // ✅ 5 seconds
        disableOnInteraction: false
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true
      }
    });
  });
</script>
