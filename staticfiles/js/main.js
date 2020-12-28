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

    $('.propetyList .listing__card').addClass('list');
    $("body").delegate(".grid.view-type", "click", function(e) {
        e.preventDefault()
        $('.list.view-type').removeClass('active')
        $(this).addClass('active');
        $('.listing__card').removeClass('list');
        $('.list_products .col-md-12').addClass('col-lg-4').removeClass('col-md-12');
    });

    $("body").delegate(".list.view-type", "click", function(e) {
        e.preventDefault()
        $('.grid.view-type').removeClass('active')
        $(this).addClass('active');
        $('.listing__card').addClass('list');
        $('.list_products').addClass('list');
        $('.list_products .col-lg-4').removeClass('col-lg-4').addClass('col-md-12');
        console.log('howdy')
    });

    $("body").delegate(".cars_grid .grid.view-type", "click", function(e) {
        e.preventDefault()
        $('.list.view-type').removeClass('active')
        $(this).addClass('active');
        $('.listing__card').removeClass('list');
        $('.list_products .col-md-6').addClass('col-lg-4');
    });

    $("body").delegate(".cars_grid .list.view-type", "click", function(e) {
        e.preventDefault()
        $('.grid.view-type').removeClass('active')
        $(this).addClass('active');
        $('.listing__card').addClass('list');
        $('.list_products').addClass('list');
        $('.list_products .col-lg-4').removeClass('col-lg-4');
    });



    $('.banner-carousel select[name=category] > option:first-child').text('All Categories');
    $('.banner-carousel select[name=brand] > option:first-child').text('All Brands');
    $('.banner-carousel select[name=car_state] > option:first-child').text('Condition');
    $('.banner-carousel select[name=purpose] > option:first-child').text('Purpose');
    $('.banner-carousel input[name=address] ').attr("placeholder", "Enter Address, City or State");
    $('.banner-carousel input[name=title] ').attr("placeholder", "Property name or title");
    $('.banner-carousel .banner-cars input[name=title] ').attr("placeholder", "Car name ot title");
    
    // FILTER
    $('.filter-sec select[name=brand] > option:first-child').text('All');
    $('.filter-sec select[name=car_state] > option:first-child').text('All');
    $('.filter-sec select[name=region] > option:first-child').text('All');

    $(function() {
        $(".filter-sec .form-control").change(function() {
          $(".filter-sec form").submit();
        });
    });
    $('select[name=region] > option:first-child').text('All Regions');
    $('select[name=locality] > option:first-child').text('All Locality');
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

