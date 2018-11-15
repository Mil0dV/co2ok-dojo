// function chgBrowserLogo()
//   {
   
//      var buttonIcon = document.querySelectorAll('.button-icon');
//     for (var i = 0; i < buttonIcon.length; i++) {
     
//        if(navigator.userAgent.indexOf("Chrome")!=-1)
//     {
     
//        buttonIcon[i].className = 'button-icon fa fa-chrome'
      
//     }else if(navigator.userAgent.indexOf("Firefox")!=-1){
      
//        buttonIcon[i].className = 'button-icon fa fa-firefox';
      
//     }else{
//       console.log('unkwon');
//     }
      
//     }
    
//   }
//   chgBrowserLogo(); 
  
function installNinjaButton()
  {
    var button = jQuery('.install-ninja-button');
    // if (/Edge/.test(navigator.userAgent)) {
       // button.attr('target', '_self');
       // button.attr('href','http://co2ok.eco/ninja/#ninja-without-extension-desktop');
    //}
     if(navigator.userAgent.indexOf("Chrome")>-1)
     {
       button.attr('href', 'https://chrome.google.com/webstore/detail/co2okninja/omlkdocjhkgbllabpihhdggplladfipe');
     }else if(navigator.userAgent.indexOf("Firefox")>-1)
     {
       button.attr('href', 'https://addons.mozilla.org/en-US/firefox/addon/co2ok-ninja/');
     }else if(navigator.userAgent.match(/iPad/i) != null)
     {       
       button.attr('target', '_self');
       button.attr('href','http://co2ok.eco/faq-co2ok-ninja-without-extension/#ninja-without-extension-desktop');   
      }else if(navigator.userAgent.match(/i(Phone|Pod)/i))
      {
        button.attr('target', '_self');
        button.attr('href','http://co2ok.eco/faq-co2ok-ninja-without-extension/#ninja-without-extension-desktop');
      }else {
     // alert('This browser isn\'t supported \r\n(only Chrome and FireFox are currently supported)');
        button.attr('target', '_self');
        button.attr('href','http://co2ok.eco/faq-co2ok-ninja-without-extension/#ninja-without-extension-desktop');
        button.href = 'http://co2ok.eco/faq-co2ok-ninja-without-extension/#ninja-without-extension-desktop';
     }    
    
  }

jQuery('.install-ninja-button').click(function(e){
    installNinjaButton();
});

