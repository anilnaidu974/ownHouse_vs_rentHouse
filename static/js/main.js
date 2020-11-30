
$(document).ready(function(){


    $('input').keypress(function(evt){
        return (/^[0-9]*\.?[0-9]*$/).test($(this).val()+evt.key);
    });

    // var $form = $('#myForm')
    // $("#myForm").validate();
    // $("#p_cost").rules("remove", "required");
    // $("#loan").rules("remove", "required");
    // $("#l_interest").rules("remove", "required");
    // $("#years").rules("remove", "required");
    // $("#rent").rules("remove", "required");
    // $("#savings").rules("remove", "required");
    // $("#s_interest").rules("remove", "required");

    $("#evaluate").click(function () {
        

        var p_cost = $("#p_cost").val()
        var loan = $("#loan").val()
        var l_interest = $("#l_interest").val()
        var years = $("#years").val()
        var rent = $("#rent").val()
        var savings = $("#savings").val()
        var s_interest = $("#s_interest").val()
        var houseType = $("#houseType").val()

        if (p_cost == '' || loan == '' || l_interest == '' || years == '' || rent == '' || savings == '' || s_interest == '' || houseType == null) {
            
            
            alert("Please fill All the Details")
        }
        else{

            $("#buffering").toggle('show');
            //form is valid
            // p_cost = parseInt(p_cost)
            // loan = parseInt(loan)
            // l_interest = parseFloat(l_interest)
            // years = parseInt(years)
            // rent  = parseInt(rent)
            // savings = parseInt(savings)
            // s_interest = parseFloat(s_interest)
            // houseType =parseInt( houseType)
            sendData(p_cost,loan,l_interest,years,rent,savings,s_interest,houseType)
        }
    });

    function sendData(p_cost,loan,l_interest,years,rent,savings,s_interest,houseType){


        $.ajax
        ({ 
            url: '/getPredictions',
            data: { 
                "p_cost" : p_cost,
                "loan" : loan,
                "l_interest" : l_interest,
                "years" : years,
                "houseType" : houseType,
                "rent" : rent,
                "savings" : savings,
                "s_interest" : s_interest
                
                },
            type: 'post',
            success: function(data)
            {
                $("#buffering").toggle('hide');

                status = data['status']
                result = data['result']

                
                if ( result == 0 )
                {   
                    $("#result").empty()
                    $("#result").text("Rent");
                    // alert("Rent is more profitable to you")
                }
                else{
                    $("#result").empty()
                    $("#result").text("Own");
                    // alert("Own is more profitable to you")
                }
                $("#myModal").toggle('show');
            }
        });
    }
    
    $("#modalok").click(function () {
        $("#myModal").toggle('hide');
    });

})

