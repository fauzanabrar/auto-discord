function castSpell(times = 1, delay = 5500) {
    let count = 0;

    function runCycle() {
        if (count >= times) {
            console.log("✅ Done looping!");
            return;
        }

        const castBtn = [...document.querySelectorAll("button")].find(
            (btn) => btn.textContent.trim() === "Cast a Spell"
        );

        if (castBtn) {
            castBtn.click();
            console.log("Clicked Cast a Spell");

            setTimeout(() => {
                const dropdown = [
                    ...document.querySelectorAll('div[role="button"]'),
                ].find((div) => div.textContent.trim() === "Choose a spell...");

                if (!dropdown) {
                    console.warn("Dropdown not found. Stopping.");
                    return;
                }

                dropdown.click();

                setTimeout(() => {
                    let options = document.querySelectorAll('[role="option"]');

                    if (options.length === 0) {
                        console.warn("No options found.");
                        return;
                    }

                    const lastOption = options[options.length - 1];
                    lastOption.scrollIntoView({
                        behavior: "smooth",
                        block: "center",
                    });
                    lastOption.click();

                    count++;
                    console.log(
                        `Selected last spell [${count}/${times}]: ${lastOption.textContent.trim()}`
                    );

                    setTimeout(runCycle, delay); // Wait before next cycle
                }, 1300);
            }, 3000);
        } else {
            console.warn("Cast a Spell button not found.");
        }
    }

    runCycle();
}
