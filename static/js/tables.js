

   $(document).ready(function()
        {
          $('#list_table').DataTable();
        });
        $(document).ready(function()
        {
          $('#books_table').DataTable();
        });

        //preventing the link bottons to do their default work
        $("#av").click(
          function(e)
            {
              e.preventDefault();
            }   
     );
     $("#tkn").click(
      function(e)
        {
          e.preventDefault();
        }   
 );
 $('#all').click(
   function(e)
   {
     e.preventDefault();
   }
 )


     
       $(document).ready(

        function()
        {
            // making <tr> with id taken to note display
          $('#tkn').click(hide_available)
            // making <tr> with id available to note display
          $('#av').click(hide_taken)
             // making <tr> showing all the table
          $('#all').click(show_all)
        }
       )
// A variable that hides taken_id
       var hide_taken = function()
       { 
        var hav = $('tr#taken')
        var hav1 = $('tr#available')
        if (hav1.hasClass('hide_available')) {
          hav1.removeClass('hide_available')
        }
        hav.addClass('hide_taken')
       }
// A variable that hides available_id
       var hide_available= function()
       {
        var htk = $('tr#available')
        var htk1 = $('tr#taken')
        if (htk1.hasClass('hide_taken')) {
          htk1.removeClass('hide_taken')
        }
        htk.addClass('hide_available')   
       }

       var show_all = function()
       {
         var sa = $('tr#available')
         var st = $('tr#taken')
         if (sa.hasClass('hide_available')) {
           sa.removeClass('hide_available')
         }
         if (st.hasClass('hide_taken')) {
           st.removeClass('hide_taken')
         }

       }



