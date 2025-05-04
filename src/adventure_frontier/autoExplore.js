function loopExploreLastPlace(times = 5, delay = 5500) {
    let count = 0;

    const interval = setInterval(() => {
        const dropdown = [...document.querySelectorAll('div[role="button"]')].find(div =>
            div.textContent.trim() === 'Choose a place...'
        );

        if (!dropdown) {
            console.warn('Dropdown not found. Stopping.');
            clearInterval(interval);
            return;
        }

        dropdown.click();

        setTimeout(() => {
            const container = document.querySelector('[data-list-id^=":"][data-list-id$=":"]');
            let options = [];
            if (container) {
                options = container.querySelectorAll('[data-list-item-id*="___choose-explore-"]');
            } else {
                console.warn("No matching container found.");
            }

            if (options.length === 0) {
                console.warn('No options found.');
                clearInterval(interval);
                return;
            }

            const lastOption = options[options.length - 1];
            lastOption.scrollIntoView({ behavior: 'smooth', block: 'center' });
            lastOption.click();

            console.log(`Selected last place [${count + 1}/${times}]: ${lastOption.textContent.trim()}`);

            // Wait a bit more and click the "Explore" button
            setTimeout(() => {
                const exploreBtn = [...document.querySelectorAll('button')].find(btn =>
                    btn.textContent.trim() === 'Explore'
                );

                if (exploreBtn) {
                    exploreBtn.click();
                    console.log('Clicked Explore');
                } else {
                    console.warn('Explore button not found.');
                }
            }, 1500); // Delay to allow selection to settle

        }, 1300); // Delay after opening dropdown

        count++;
        if (count >= times) {
            clearInterval(interval);
            console.log('✅ Done looping!');
        }
    }, delay); // Delay between each full cycle
}
