function keresKepet() {
    // Könyv cím beolvasása az input mezőből
    var konyvCime = document.getElementById("konyvCime").value;

    // Keresés a könyv cím alapján
    var keresesURL = "https://www.antikvarium.hu/kereses?SearchTerm=" + encodeURIComponent(konyvCime);

    // Megnyitja az oldalt, majd megnézi a képeket
    window.open(keresesURL, "_blank");

    // Üzenet küldése a konzolra a demonstráció céljából
    console.log("Kép keresése a következő cím alapján: " + keresesURL);
}
