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

   $('.project-img').click(function(e){

      var currentCause = e.currentTarget.id;
      pickACause(currentCause);
      // ligthbox sluiten
      tl.to('.pick_cause_container', 0.5, {scale: 0, ease: Quad.easeOut});

   })

   function pickACause(causePicked)
   {


     $.ajax({

       type: "GET",
       url: '/picked_cause/',
       data: {
         causePicked: causePicked
         // csrfmiddlewaretoken: $('input[csrfmiddlewaretoken]').val()
       },
       success: function(data){

          $('.cause').html(data);

       },
       dataType: 'html'

     })

   }


   function co2compensated()
   {

     var co2compensated_num = document.querySelector('.co2compensated_num');
     setInterval(function(){

        co2compensated_num.innerHTML = Math.floor(Math.random() * 101)+" kgs";

     }, 5000);

   }
   co2compensated();

 })
