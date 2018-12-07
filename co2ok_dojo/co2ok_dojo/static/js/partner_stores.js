$(function(){

  function allStore()
  {

    $.ajax({

      type: "GET",
      url: '/partner-stores-all/',
      data: {
        csrfmiddlewaretoken: $('input[csrfmiddlewaretoken]').val()
      },
      success: function(data){

         $('.search_result').html(data);

      },
      dataType: 'html'

    })

  }
  allStore();


   $('#serachInput').keyup(function(e){

      var searchInputVal = $('#serachInput').val();
      if(searchInputVal == "")
      {

        allStore();
        enableMenu();

      }else{

        disableMenu();

      }
      // ajaxRequest(searchInputVal);
      $.ajax({

        type: "GET",
        url: '/partner-stores-search/',
        data: {
          search_val: searchInputVal,
          // user_lang: window.localStorage.get('curLang'),
          csrfmiddlewaretoken: $('input[csrfmiddlewaretoken]').val()
        },
        success: function(data){

           $('.search_result').html(data);

        },
        dataType: 'html'

      })

   })


   function disableMenu()
   {

     var tl = new TimelineMax();
     tl.to('.mobile_ninja_menu', 0.5, {height: 'auto', paddingBottom: 10, ease: Quad.easeInOut}, 0.2);
     tl.to('.neutral-ninja', 0.3, {scale: 0, display: 'none', ease: Quad.easeInOut}, 0.1);
      tl.to('.ninja-partner-store-bg', 0.4, {marginTop: 60, ease: Quad.easeInOut}, 0.2);

   }


   function enableMenu()
   {

     var tl = new TimelineMax();
     tl.to('.mobile_ninja_menu', 0.5, {height: 'auto', paddingBottom: 0, ease: Quad.easeInOut}, 0.1);
     tl.to('.neutral-ninja', 0.3, {scale: 1, display: 'flex', ease: Quad.easeInOut}, 0.1);
      tl.to('.ninja-partner-store-bg', 0.4, {marginTop: 200, ease: Quad.easeInOut}, 0.2);

   }


   // function categorySpliter(category)
   // {
   //
   //   var categoryArr = category;
   //   if(category.indexOf('&') > -1)
   //   {
   //
   //     categoryArr = category.split('&');
   //
   //   }
   //   return categoryArr;
   //
   // }


   $('.btn-mobile-ninja-caroussel').click(function(e){

     var categoryVal = e.currentTarget.textContent;
     // var splitCategoryVal = categorySpliter(categoryVal);
      filterByCategory(categoryVal);

   })

   function filterByCategory(categoryVal)
   {

       $.ajax({

         type: "GET",
         url: '/partner-stores-category/',
         data: {
           category_val: categoryVal,
           csrfmiddlewaretoken: $('input[csrfmiddlewaretoken]').val()
         },
         success: function(data){

            $('.search_result').html(data);

         },
         dataType: 'html'

       })

   }


   function share()
   {

     var ninja_share = document.querySelector('.ninja_share');
      var shareContent = document.querySelector('.shareContent');
      var tl = new TimelineMax();
      ninja_share.addEventListener('click', function(){

          tl.to('.share_box_container', 0.5, {scale: 1, ease: Quad.easeInOut});

          // close lightbox
          $('.close_share_box').click(function(){

            tl.to('.share_box_container', 0.5, {scale: 0, ease: Quad.easeOut});

          })

      })

   }
   share();

   // function ajaxRequest(searchData)
   // {
   //
   //   let xhr;
   //
   //   if (window.XMLHttpRequest) {
   //       // code for IE7+, Firefox, Chrome, Opera, Safari
   //        xhr = new XMLHttpRequest();
   //      } else {
   //       // code for IE6, IE5
   //         xhr = new ActiveXObject("Microsoft.XMLHTTP");
   //     }
   //
   //     xhr.onreadystatechange = function(){
   //
   //      if(this.readyState ==  4 && this.status == 200)
   //      {
   //
   //          // notification.innerHTML = xhr.responseText;
   //          console.log(xhr.responseText);
   //
   //      }
   //
   //    }
   //
   //    var csrf = $('input[csrfmiddlewaretoken]').val();
   //
   //    xhr.open('GET',"/?search_data="+searchData+'&csrfmiddlewaretoken='+csrf,true);
   //    xhr.send();
   //
   // }


})
