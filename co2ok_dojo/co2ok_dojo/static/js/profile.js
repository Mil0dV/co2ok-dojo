var hasExtension = false;

chrome.runtime.sendMessage('ebkngbljjoeelkacamjffdedkbbjlnii', { message: "version" },
  function (reply) {
    // alert(reply);
    if (reply) {
          if (reply.version) {
            // if (reply.version >= '1.0') {
                hasExtension = true;
            // }
        }
    }
    else {
      hasExtension = 'jhskjgjg';
    }
    // alert(hasExtension);
});
// alert(hasExtension);
window.addEventListener('load', function(){

   chrome.webstore.install()

})
