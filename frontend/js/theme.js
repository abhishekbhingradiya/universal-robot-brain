function setTheme(theme) {

    localStorage.setItem(
        "urb-theme",
        theme
    );

    if (theme === "light") {

        document.body.classList.add(
            "light-theme"
        );

    } else {

        document.body.classList.remove(
            "light-theme"
        );
    }
}

function toggleTheme() {

    const isLight =
        document.body.classList.contains(
            "light-theme"
        );

    if (isLight) {

        setTheme("dark");

    } else {

        setTheme("light");
    }
}

function initializeTheme() {

    const savedTheme =
        localStorage.getItem(
            "urb-theme"
        );

    if (savedTheme === "light") {

        document.body.classList.add(
            "light-theme"
        );
    }
}

initializeTheme();