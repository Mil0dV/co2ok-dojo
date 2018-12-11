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


  //categorie weergeven afhankelijk van de device van de gebruiker

  function categorieDisplay()
  {

    var categoryContainer_butt = document.querySelector('.categoryContainer');
    var categoryDropDown = document.querySelector('.categoryDropDown');

    if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent)
        || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4)))
    {

      categoryDropDown.style.display = 'none';
      categoryContainer_butt.style.display = 'flex';

    }else{

      categoryDropDown.style.display = 'flex';
      categoryContainer_butt.style.display = 'none';

    }

  }
  categorieDisplay();

  window.addEventListener('resize', categorieDisplay);


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
     tl.to('.categoryContainer', 0.4, {top: 100, ease: Quad.easeInOut}, 0.2);
     tl.to('.categoryDropDown', 0.4, {top: 130, ease: Quad.easeInOut}, 0.2);
     tl.to('.search_result', 0.4, {position: 'relative',top: 0, ease: Quad.easeInOut}, 0.2);

   }


   function enableMenu()
   {

     var tl = new TimelineMax();
     tl.to('.mobile_ninja_menu', 0.5, {height: 'auto', paddingBottom: 0, ease: Quad.easeInOut}, 0.2);
     tl.to('.neutral-ninja', 0.4, {scale: 1, display: 'flex', ease: Quad.easeInOut}, 0.2);
     tl.to('.categoryContainer', 0.3, {top: 220, ease: Quad.easeInOut}, 0.1);
     tl.to('.categoryDropDown', 0.3, {top: 240, ease: Quad.easeInOut}, 0.1);
     tl.to('.search_result', 0.3, {position: 'relative',top: 120, ease: Quad.easeInOut}, 0.1);

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

   var catSelect = document.querySelector('.categorySelect');

   $('.categorySelect').change(function(e){

     catVal = catSelect.options[catSelect.selectedIndex].value;
     filterByCategory(catVal);

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
