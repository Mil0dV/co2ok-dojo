$(function(){

   $('#serachInput').keyup(function(e){

      var searchInputVal = $('#serachInput').val();
      // ajaxRequest(searchInputVal);
      $.ajax({

        type: "GET",
        url: '/partner-stores-data/',
        data: {
          search_val: searchInputVal,
          csrfmiddlewaretoken: $('input[csrfmiddlewaretoken]').val()
        },
        success: function(data){

           $('.search_result').html(data);

        },
        dataType: 'html'

      })

   })


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
