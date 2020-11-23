$(document).ready(function() {
        "use strict";
    
    $("body").delegate(".drop-menu", "click", function(event) {
        event.preventDefault();
        $(this).attr('tabindex', 1).focus();
        $(this).toggleClass('active');
        $(this).find('.dropeddown').slideToggle(300);
    });

    $("body").delegate(".drop-menu", "focusout", function(event) {
        $(this).removeAttr('tabindex', 1).focus();
        $(this).removeClass('active');
        $(this).find('.dropeddown').slideUp(300);
    });

    $("body").delegate(".grid.view-type", "click", function(event) {
        $('.list.view-type').removeClass('active')
        $(this).addClass('active');
        $('.listing__card').removeClass('list');
        $('.list_products .col-md-6').addClass('col-lg-3');
    });

    $("body").delegate(".list.view-type", "click", function(event) {
        $('.grid.view-type').removeClass('active')
        $(this).addClass('active');
        $('.listing__card').addClass('list');
        $('.list_products').addClass('list');
        $('.list_products .col-lg-3').removeClass('col-lg-3');
    });



    $('select[name=region] > option:first-child').text('All Regions');
    $('select[name=locality] > option:first-child').text('All Locality');
    $('select[name=category] > option:first-child').text('All categories');
    $('select[name=purpose] > option:first-child').text('Purpose');
    $('input[name=address] ').attr("placeholder", "Enter Address, City or State");
    $('input[name=title] ').attr("placeholder", "Enter Propert name or title");
    $('input[name=bed] ').attr("placeholder", "Beds").attr("min", '1');
    $('input[name=bath] ').attr("placeholder", "Baths").attr("min", '1');
    $('input[name=price__min] ').attr("placeholder", "From GH₵").attr("min", '1');
    $('input[name=price__max] ').attr("placeholder", "To GH₵").attr("min", '1');
    $('input[name=to_price] ').attr("placeholder", "To GH₵").attr("min", '1');
    $('input[name=from_price] ').attr("placeholder", "From GH₵").attr("min", '1');



    $("body").delegate(".close-menu", "click", function(event) {
        $('.navbar-collapse.collapse').removeClass('show')
    });
        
    $('.banner-carousel').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        infinite: true,
        speed: 300,
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
    });

    $('.testimony__carousel').slick({
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        // adaptiveHeight: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 754,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 554,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });


    $("body").delegate("#subscript-btn", "click", function(event) {
    var subcriptEmail = $('#subscript-email').val();
    if(subcriptEmail){
        event.preventDefault();
            $('#subscriptionModal').modal('toggle');
            $('.form_subscription #id_email').val(subcriptEmail)
        }
    });


    function alertFunc(msg) {
        var message = `<div class="alert alert-danger alert-dismissible fade show" role="alert">
            ${msg}
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>`;
        return message
    }
    $("#subForm").submit(function(event) {
        event.preventDefault();
        var form = $(this)
        if (form.valid()) {
            // $('#loading').addClass('loading');
            $.ajax({
                url: "/ajax_subscriptionform/",
                method: "POST",
                data: form.serialize(),
                // beforeSend: function() {
                //     $(".loading").show();
                // },
                // complete: function() {
                //     $(".loading").hide();
                // },
                success: function(data) {
                    if(data == 'ok'){
                        $('#subscriptionModal').modal('hide');
                        $('#completeSubscriptionModal').modal('toggle');
                    }else{
                        $("#signup_error").html(alertFunc(data));
                    }
                }
            })
        }else{
            $("#signup_error").html(alertFunc('Please fill all the forms'));
        }
    });

});

