// window.addEventListener('load', function(){
//
//
//
// })


$(function(){

   // display lightbox
   var tl = new TimelineMax();
   tl.to('.light_box_container', 0.5, {scale: 1, ease: Quad.easeInOut});

   // close lightbox
   $('.close_light_box').click(function(){

     tl.to('.light_box_container', 0.5, {scale: 0, ease: Quad.easeOut});

   })

})