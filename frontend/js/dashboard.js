let skillsChart = null;

async function loadOverview() {

    const data =
        await getData(
            "/dashboard/overview"
        );

    document.getElementById(
        "robots-count"
    ).textContent =
        data.total_robots;

    document.getElementById(
        "skills-count"
    ).textContent =
        data.total_skills;

    document.getElementById(
        "experiences-count"
    ).textContent =
        data.total_experiences;

    document.getElementById(
        "federation-count"
    ).textContent =
        data.federation_nodes;

    document.getElementById(
        "network-status"
    ).textContent =
        data.network_status;
}

async function loadActivity() {

    const data =
        await getData(
            "/dashboard/activity"
        );

    const container =
        document.getElementById(
            "activity-feed"
        );

    if (!container) {
        return;
    }

    container.innerHTML = "";

    data.activities
        .slice(0, 10)
        .forEach(
            activity => {

                container.innerHTML += `

                <div class="activity-item">

                    <div>

                        <strong>
                            ${activity.event_type}
                        </strong>

                    </div>

                    <div class="text-slate-400">

                        ${activity.entity}

                    </div>

                </div>

                `;
            }
        );
}

async function loadSkillChart() {

    const data =
        await getData(
            "/dashboard/top-skills"
        );

    const canvas =
        document.getElementById(
            "skills-chart"
        );

    if (!canvas) {
        return;
    }

    const labels =
        data.skills.map(
            item => item.strategy
        );

    const values =
        data.skills.map(
            item => item.avg_reward
        );

    if (skillsChart) {
        skillsChart.destroy();
    }

    skillsChart =
        new Chart(
            canvas,
            {
                type: "bar",

                data: {

                    labels: labels,

                    datasets: [
                        {
                            label: "Skill Fitness",

                            data: values,

                            borderWidth: 1,

                            backgroundColor:
                                "#06b6d4"
                        }
                    ]
                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    plugins: {

                        legend: {

                            labels: {

                                color: "#ffffff"
                            }
                        }
                    },

                    scales: {

                        x: {

                            ticks: {
                                color: "#94a3b8"
                            }
                        },

                        y: {

                            ticks: {
                                color: "#94a3b8"
                            }
                        }
                    }
                }
            }
        );
}

function enableAutoRefresh() {

    setInterval(
        async () => {

            await loadOverview();

            await loadActivity();

        },
        30000
    );
}

async function initializeDashboard() {

    await loadOverview();

    await loadActivity();

    await loadSkillChart();

    enableAutoRefresh();
}

initializeDashboard();