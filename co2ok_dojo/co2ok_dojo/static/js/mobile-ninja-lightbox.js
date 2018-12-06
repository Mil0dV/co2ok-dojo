
$(function(){

    // display lightbox
    var tl = new TimelineMax();

    if(navigator.userAgent.match(/i(Phone|Pod|Pad)/i))
      {
        if($('.mobil_light_box').children().hasClass('lightboxActive'))
        {

        tl.to('.mobil_light_box', 0.5, {scale: 1, ease: Quad.easeInOut});

        // close lightbox
        $('.close_light_box').click(function(){

            tl.to('.mobil_light_box', 0.5, {scale: 0, ease: Quad.easeOut});

        })

        }else{
        console.log('lightbox is not active on this page...');
        }
    }

 })
