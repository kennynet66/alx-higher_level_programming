$("#toggle_header").bind("click", () => {
    if ($("header").hasClass("green")) {
        $("header").removeClass("green")
        $("header").addClass("red")
    }
    else if ($("header").hasClass("red")) {
        $("header").removeClass("red")
        $("header").addClass("green")
    }
})