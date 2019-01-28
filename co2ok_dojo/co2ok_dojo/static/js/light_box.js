// window.addEventListener('load', function(){
//
//
//
// })


// $(function(){

   // display lightbox
   var tl = new TimelineMax();

   if($('.light_box_container').children().hasClass('lightboxActive'))
   {

     tl.to('.light_box_container', 0.5, {scale: 1, ease: Quad.easeInOut});

     // close lightbox
     $('.close_light_box').click(function(e){
       // lb staat voor lightbopx
       var currentLb = e.currentTarget.parentNode;
       tl.to(currentLb, 0.5, {scale: 0, ease: Quad.easeOut});

     })

   }else{
     console.log('lightbox is not active on this page...');
   }

// })
