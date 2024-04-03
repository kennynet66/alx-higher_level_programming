$.get("https://swapi-api.alx-tools.com/api/films/?format=json", (data) => {
    data.results.forEach(movie => {
        movie.characters.forEach((character, i)=> {
            console.log(character);
            $.get(character, (characterData) => {
                $("#character").append(`[${i + 1}]. ${characterData.name} <br>`)
            })
        })

    })
})