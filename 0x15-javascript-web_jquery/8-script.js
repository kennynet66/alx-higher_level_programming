$.get("https://swapi-api.alx-tools.com/api/films/?format=json", (data) => {
    data.results.forEach((movie, i) => {
        $("#list_movies").append(`[${i + 1}]. ${movie.title} <br>`)
        // console.log(movie.title);
    })    
// console.log(data.results);
})