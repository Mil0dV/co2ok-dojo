window.addEventListener('load', function(){
//
//    var dropdownMenuButton = document.getElementById('dropdownMenuButton');
//    var lang_choice = document.querySelectorAll('.lang_choice');
//    var langArr = {
//
//       nl: 'Nederlands',
//       en: 'English',
//       es: 'España',
//       fr: 'Francias',
//       de: 'Deutschland'
//
//    };
//
//    dropdownMenuButton.textContent = localStorage.getItem(langArr.nl);
//
//    localStorage.setItem('nl','Nederlands');
//    localStorage.setItem('en','English');
//    localStorage.setItem('es','España');
//    localStorage.setItem('fr','Francias');
//    localStorage.setItem('de','Deutschland');
//
//    for (var i = 0; i < lang_choice.length; i++) {
//
//      lang_choice[i].addEventListener('click', function(e){
//
//        var landCode = e.currentTarget.classList[1];
//        dropdownMenuButton.textContent = localStorage.getItem(langArr.landCode);
//
//      })
//
//    }

var mobileMenu = document.querySelector('.hanburger-menu');
var mobileMenuStatus = false;
function showMobileMenu(){
  var tl = new TimelineMax();
  tl.to('.mobile-menu', 0.5, {marginTop: 0, ease: Quad.easeInOut});
}

function hideMobileMenu(){
  var tl = new TimelineMax();
  tl.to('.mobile-menu', 0.5, {marginTop: -200, ease: Quad.easeIn});
}

mobileMenu.addEventListener('click', function(){
   mobileMenuStatus = !mobileMenuStatus;
   if(mobileMenuStatus){
     showMobileMenu();
   }else{
     hideMobileMenu();
   }
})


})
