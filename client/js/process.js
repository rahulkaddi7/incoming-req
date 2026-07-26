const submitBtn = document.getElementById("submitBtn");

submitBtn.addEventListener("click", async (e) => {

    e.preventDefault();

    console.log("========== CLICK ==========");

    const request = document
        .getElementById("request")
        .value
        .trim();

    console.log("Request:", request);

    if (!request) {
        alert("Please enter a request.");
        return;
    }

    console.log("Showing loader");

    document
        .getElementById("loader")
        .classList.remove("hidden");

    console.trace("Hiding result card");

    document
        .getElementById("resultCard")
        .classList.add("hidden");

    console.log(
        "Current class:",
        document.getElementById("resultCard").className
    );

    try {

        console.log("Calling API...");

        const result = await processRequest(request);

        console.log("API Response:", result);

        document.getElementById("classification").textContent =
            result.classification;

        document.getElementById("urgency").textContent =
            result.urgency;

        document.getElementById("assignedTeam").textContent =
            result.assigned_team;

        document.getElementById("status").textContent =
            result.status;

        document.getElementById("followUp").textContent =
            result.follow_up;

        document.getElementById("priority").textContent =
            result.highPriority ? "Yes" : "No";

        document.getElementById("response").textContent =
            result.response;

        console.log("Removing hidden class...");

        document
            .getElementById("resultCard")
            .classList.remove("hidden");

        console.log(
            "Immediately after remove:",
            document.getElementById("resultCard").className
        );

        setTimeout(() => {
            console.log(
                "After 1 second:",
                document.getElementById("resultCard").className
            );
        }, 1000);

        setTimeout(() => {
            console.log(
                "After 3 seconds:",
                document.getElementById("resultCard").className
            );
        }, 3000);

    }
    catch(err){

        console.error("ERROR:", err);

    }
    finally{

        console.log("Hiding loader");

        document
            .getElementById("loader")
            .classList.add("hidden");

        console.log(
            "Final result card class:",
            document.getElementById("resultCard").className
        );

        console.log("========== END ==========");

    }

});