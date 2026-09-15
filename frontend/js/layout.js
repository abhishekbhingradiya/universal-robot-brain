function createSidebar(activePage) {

    let dashboardClass = "nav-link";
    let robotsClass = "nav-link";
    let skillsClass = "nav-link";
    let experiencesClass = "nav-link";
    let federationClass = "nav-link";
    let graphClass = "nav-link";

    if (activePage === "dashboard") {
        dashboardClass = "nav-link-active";
    }

    if (activePage === "robots") {
        robotsClass = "nav-link-active";
    }

    if (activePage === "skills") {
        skillsClass = "nav-link-active";
    }

    if (activePage === "experiences") {
        experiencesClass = "nav-link-active";
    }

    if (activePage === "federation") {
        federationClass = "nav-link-active";
    }

    if (activePage === "graph") {
        graphClass = "nav-link-active";
    }

    return `
        <aside class="sidebar">

            <div class="brand">

                <div class="brand-title">
                    URB
                </div>

                <div class="brand-subtitle">
                    Universal Robot Brain
                </div>

            </div>

            <nav class="nav">

                <a
                    href="index.html"
                    class="${dashboardClass}"
                >
                    Dashboard
                </a>

                robots.html
                    Robots
                </a>

                <a
                    href="skills.html"
                    class="${skillsClass}"
                >
                    Skills
                </a>

                <a
                    href="experiences.html"
                    class="${experiencesClass}"
                >
                    Experiences
                </a>

                federation.html
                    Federation
                </a>

                graph.html
                    Knowledge Graph
                </a>

                <button
                    id="theme-toggle"
                    onclick="toggleTheme()"
                    class="btn-primary"
                    style="
                        width:100%;
                        margin-top:20px;
                    "
                >
                    Toggle Theme
                </button>

            </nav>

        </aside>
    `;
}

function renderLayout(activePage) {

    const sidebarContainer =
        document.getElementById(
            "sidebar-container"
        );

    if (!sidebarContainer) {
        return;
    }

    sidebarContainer.innerHTML =
        createSidebar(
            activePage
        );
}