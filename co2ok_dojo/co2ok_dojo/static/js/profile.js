// var hasExtension = false;
//
// chrome.runtime.sendMessage('ebkngbljjoeelkacamjffdedkbbjlnii', { message: "version" },
//   function (reply) {
//     // alert(reply);
//     if (reply) {
//           if (reply.version) {
//             // if (reply.version >= '1.0') {
//                 hasExtension = true;
//             // }
//         }
//     }
//     else {
//       hasExtension = 'jhskjgjg';
//     }
//     // alert(hasExtension);
// });
// // alert(hasExtension);
// window.addEventListener('load', function(){
//
//    chrome.webstore.install()
//
// })

 $(function(){

   var pickCauseButt = document.querySelector('.pick_cause_butt');
   var pick_cause_container = document.querySelector('.pick_cause_container');
   var tl = new TimelineMax();
   pickCauseButt.addEventListener('click', function(){

     tl.to('.pick_cause_container', 0.5, {scale: 1, ease: Quad.easeInOut});

     // close lightbox
     $('.close_light_box').click(function(){

       tl.to('.pick_cause_container', 0.5, {scale: 0, ease: Quad.easeOut});

     })


   })

   $('.co2ok-featured-project-image').click(function(e){

      var currentCause = e.currentTarget.id;
      pickACause(currentCause);

   })

   function pickACause(causePicked)
   {


     $.ajax({

       type: "GET",
       url: '/accounts/profile/',
       data: {
         cause: causePicked
       },
       success: function(data){

          //return nothing

       },
       dataType: 'html'

     })

   }


 })
