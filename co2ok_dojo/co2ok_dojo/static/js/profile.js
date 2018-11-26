// var hasExtension = false;
// chrome.runtime.sendMessage(extensionId, { message: "version" },
//   function (reply) {
//     if (reply) {
//         if (reply.version) {
//             if (reply.version >= requiredVersion) {
//                 hasExtension = true;
//             }
//         }
//     }
//     else {
//       hasExtension = false;
//     }
// });
// alert(hasExtension);


function ninjaAppInstallPNGswitch(){

  var choosedLang = document.querySelectorAll('.lang_choice');
  var ninjaAppInstall = document.querySelector('.ninja_app_install');
  for(i=0; i<=choosedLang.length; i++ ){

    choosedLang[i].addEventListener('click', function(e){
 
        var choosedLangVal = e.currentTarget.classList[1];
        window.localStorage.setItem('curLang',choosedLangVal);
        var curLang = window.localStorage.getItem('curLang');
        ninjaAppInstall.src = 'images/ninja_app_install_'+curLang+'.png';
        
    });

  }

}
ninjaAppInstallPNGswitch();
